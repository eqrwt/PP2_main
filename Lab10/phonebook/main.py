import update, delete, query, insert

if __name__ == "__main__":
    print("1. Insert from CSV")
    print("2. Insert from input")
    print("3. Update")
    print("4. Search")
    print("5. Delete")
    choice = input("Choose: ")

    if choice == '1':
        insert.insert_from_csv('contacts.csv')
    elif choice == '2':
        insert.insert_input()
    elif choice == '3':
        update.update_phone(2, new_username="Merey", new_phone="+7759949787")
    elif choice == '4':
        keyword = input("Search: ")
        query.search_phonebook(keyword)
    elif choice == '5':
        value = input("Delete by username or phone: ")
        delete.delete(value)