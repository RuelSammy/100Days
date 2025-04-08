#Build a basic CRUD (Create, Read, Update, Delete) application.
# Simple CRUD app for managing users

users = []
next_id = 1

def create_user(name, email):
    global next_id
    user = {'id': next_id, 'name': name, 'email': email}
    users.append(user)
    next_id += 1
    print(f"User created: {user}")

def read_users():
    if not users:
        print("No users found.")
    else:
        for user in users:
            print(user)

def update_user(user_id, name=None, email=None):
    for user in users:
        if user['id'] == user_id:
            if name:
                user['name'] = name
            if email:
                user['email'] = email
            print(f"User updated: {user}")
            return
    print(f"No user found with id {user_id}")

def delete_user(user_id):
    global users
    for user in users:
        if user['id'] == user_id:
            users = [u for u in users if u['id'] != user_id]
            print(f"User deleted: {user}")
            return
    print(f"No user found with id {user_id}")

def menu():
    while True:
        print("\nCRUD Menu:")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            create_user(name, email)
        elif choice == '2':
            read_users()
        elif choice == '3':
            try:
                user_id = int(input("Enter user ID to update: "))
                name = input("Enter new name (leave blank to skip): ")
                email = input("Enter new email (leave blank to skip): ")
                update_user(user_id, name if name else None, email if email else None)
            except ValueError:
                print("Invalid input. ID must be a number.")
        elif choice == '4':
            try:
                user_id = int(input("Enter user ID to delete: "))
                delete_user(user_id)
            except ValueError:
                print("Invalid input. ID must be a number.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
