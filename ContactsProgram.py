contacts = []

def add_contact():

    contact = []
    print('---------------Adding--------------')
    name = input("Name: ")
    phone_number = input('Phone Number: ')
    email = input('Email: ')
    contact.append(name)
    contact.append((phone_number))
    contact.append(email)
    contacts.append(contact)

    print(f"\n----------------------------------------\n\n"
          f"Successfully added '{name}' to contacts\n")

def view_contact():
    print(f"----------------Viewing-----------------\n"
          f"Total Contacts: {len(contacts)}")

    for i, contact in enumerate(contacts):
        print(i+1, *contact)

def update_contact():

    try:
        print("-----------------Updating---------------------")

        for i, contact in enumerate(contacts):
            print(i + 1, contacts[i][0])

        update = int(input('\nUpdate which contact? '))

        if update > len(contacts):
            print("Out of Range")
        else:
            name = input('Name: ')
            phone_number = input('Phone Number: ')
            email = input('Email: ')

            contacts[update-1][0] = name
            contacts[update-1][1] = phone_number
            contacts[update-1][2] = email

            print(f"-------------------------------------\n"
                  f"Updated Contact {update}\n"
                  f"Name: {name}\n"
                  f"Phone Number: {phone_number}\n"
                  f"Email: {email}")
    except:
        print('Invalid Input.')

def delete_contact():

    try:
        print('---------------Deleting----------------')
        delete = int(input('Delete which contact? '))

        if 0 < delete < 6:
            print(f"Successfully deleted contact '{delete}'")
            del contacts[delete-1]
        else:
            print("Out of Range")
    except:
        print('Invalid Input')

while True:
    print(f'-----------Contact Operations-----------\n'
          f'1. Add Contact\n'
          f'2. View Contacts\n'
          f'3. Update Contact\n'
          f'4. Delete Contact\n'
          f'5. Exit')
    choice = input('Choice: ')

    if choice == '1':
        add_contact()

    elif choice == '2':
        view_contact()

    elif choice == '3':
        update_contact()

    elif choice == '4':
        delete_contact()

    elif choice == '5':
        break

    else:
        print('Enter a number with an assigned function')


print('You have exited the program.')