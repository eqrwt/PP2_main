-- Search by part of name, surname or phone
DROP FUNCTION IF EXISTS search_phonebook(TEXT);

CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook
    WHERE phonebook.username ILIKE '%' || pattern || '%'
       OR phonebook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- FUNCTION to query with pagination
CREATE OR REPLACE FUNCTION get_phonebook_paginated(limit_size INT, offset_count INT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR)
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
        DELETE FROM phonebook WHERE phonebook.username = u_name;
    ELSIF u_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = u_phone;
    END IF;
END;
$$;

-- PROCEDURE to insert a new user or update if exists
DROP PROCEDURE insert_or_update_user(TEXT,TEXT);

CREATE OR REPLACE PROCEDURE insert_or_update_user(new_username TEXT, userphone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE phonebook.username = new_username) THEN
        UPDATE phonebook SET phone = userphone WHERE phonebook.username = new_username;
    ELSE
        INSERT INTO phonebook(username, phone) VALUES (new_username, userphone);
    END IF;
END;
$$ LANGUAGE plpgsql;


