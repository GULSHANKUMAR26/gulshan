contacts = {}

while True:
    print("contact book")
    print("1. Create contact")
    print("2. view contact")
    print("3. update contact")
    print("4. Delete contact")
    print("5. search contact")
    print("6. Count contact")
    print("7. Exit")

    choice = input("Enter your choice:")

    if choice =="1":
        name =input("Enter your name:")
        if name in contacts:
            print(f"contact name{name} already exists!") 
        else:
            age = input("Enter your age:")
            email = input("Enter your email:")
            mobile = input("Enter your mobile:")
            contacts[name] ={"age":int(age), "email":email, "mobile":mobile}
            print(f"Contact {name} created successfully!")

    elif choice == "2":
        name = input("Enter the name of the contact to view:")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}")
        else:
            print(f"Contact {name} does not exist!")

    elif choice =="3":
        name = input("Enter the name to update contact:")
        if name in contacts:
            age = input("Enter updated age =")
            email = input("Enter updated age =")
            mobile = input("Enter updated mobile number =")
            contacts[name] = {"age": int(age), "email":email, "monile":mobile}
        else:
            print("contact not found!")

        

    elif choice == "4":
        name = input("Enter contact name to delete =")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} does not exist!")

    elif choice == "5":  
        search_name = input("Enter the name to search:")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name {name} , Age:{age}, mobile Number:{mobile}, Email:{email}")
                found = True
                if not found:
                    print("No contacts found with that name")

    elif choice == "6":
        print(f"Total contacts in your book :{len(contacts)}")

    elif choice == "7":
        print("Good bye...Closing the program")
        break

    else:
        print("Invalid input")