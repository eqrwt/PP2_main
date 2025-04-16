-- Search by part of name, surname or phone
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, surname TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook
    WHERE name ILIKE '%' || pattern || '%' 
       OR surname ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- PROCEDURE to insert a new user or update if exists
CREATE OR REPLACE PROCEDURE insert_or_update_user(username TEXT, userphone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = username) THEN
        UPDATE phonebook SET phone = userphone WHERE name = username;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (username, userphone);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Insert many users
CREATE OR REPLACE PROCEDURE insert_many_users(users JSONB, OUT invalid_data JSONB)
LANGUAGE plpgsql
AS $$
DECLARE
    item JSONB;
    uname TEXT;
    uphone TEXT;
    errors JSONB := '[]'::JSONB;
BEGIN
    FOR item IN SELECT * FROM jsonb_array_elements(users)
    LOOP
        uname := item->>'name';
        uphone := item->>'phone';

        -- Simple phone check (e.g., 10 digits)
        IF uphone ~ '^\d{10}$' THEN
            CALL insert_or_update_user(uname, uphone);
        ELSE
            errors := errors || jsonb_build_object('name', uname, 'phone', uphone);
        END IF;
    END LOOP;
    invalid_data := errors;
END;
$$;

-- FUNCTION to query with pagination
CREATE OR REPLACE FUNCTION get_phonebook_paginated(limit_size INT, offset_count INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    ORDER BY id
    LIMIT limit_size OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;

-- Delete by username or phone 
CREATE OR REPLACE PROCEDURE delete_user(u_name TEXT DEFAULT NULL, u_phone TEXT DEFAULT NULL)
LANGUAGE plpgsql
AS $$
BEGIN
    IF u_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = u_name;
    ELSIF u_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = u_phone;
    END IF;
END;
$$;
