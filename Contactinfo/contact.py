contact = {}

def display_contact():
    print("Name\t\tNumber\t\tEmail\t\tAddress")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
        
while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Update contact \n 5. Delete contact \n  6. Exit\n Enter Your Choice: "))
    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile nunber: ")
        mail =  input("Enetr the email: ")
        addr = input("Enetr the Address: ")
        contact[name] = {"Phone": phone, "Email": mail, "Address": addr}
    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(f"{search_name}'s Contact information:")
            print("Phone:", contact[search_name]["Phone"])
            print("Email:", contact[search_name]["Email"])
            print("Address:", contact[search_name]["Address"])
        else:
            print("Name is not found in contact list")
    elif choice == 3:
        if not contact:
            print("Empty")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact name to be editted: ")
        if edit_contact in contact:
            phone = input("Enter mobile number ")
            contact[edit_contact]["Phone"]=phone
            print("Contact Updated")
            display_contact()
        else:
            print("Name is not found in contact list")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted- ")
        if del_contact in contact:
            confirm = input("Are you sure you want to delete this contact? (y/n): ")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
            display_contact()
            print("Contact has been deleted successfully")
        else:
            print("Name is not found in contact list")         
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please enter a valid option.")