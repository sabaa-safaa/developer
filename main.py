from utilities.data_utils import load_data, save_data
from models.user import User
from models.meal import Meal
from models.bill import Bill
from services.auth_service import AuthenticationService
from services.user_service import UserService
from services.meal_service import MealService
from services.bill_service import BillService

def display_menu(options):
    print("\nMenu:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Choose an option: "))
    return choice

def handle_admin_menu(auth_service, user_service, meal_service, bill_service):
    options = ["List Users", "Add User", "Remove User", "Update User",
            "List Meals", "Add Meal", "Remove Meal", "Update Meal",
            "List Bills", "Logout"]
    choice = display_menu(options)

    if choice == 1:
        print(user_service.list_all())
    elif choice == 2:
        username = input("Username: ")
        password = input("Password: ")
        age = int(input("Age: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        user = User(username=username, password=password, is_loggedin=False, role='user', first_name=first_name, last_name=last_name)
        user_service.add(user)
    elif choice == 3:
        user_id = input("User ID to remove: ")
        user_service.remove(user_id)
    elif choice == 4:
        user_id = input("User ID to update: ")
        updated_info = {
            "username": input("New Username: "),
            "age": int(input("New Age: ")),
            "first_name": input("New First Name: "),
            "last_name": input("New Last Name: "),
            "role": input("New Role (admin/cashier/user): ")
        }
        user_service.update(user_id, updated_info)
    elif choice == 5:
        print(meal_service.list_all())
    elif choice == 6:
        name = input("Meal Name: ")
        price = float(input("Price: "))
        meal = Meal(name=name, price=price)
        meal_service.add(meal)
    elif choice == 7:
        meal_id = input("Meal ID to remove: ")
        meal_service.remove(meal_id)
    elif choice == 8:
        meal_id = input("Meal ID to update: ")
        updated_info = {
            "name": input("New Meal Name: "),
            "price": float(input("New Price: "))
        }
        meal_service.update(meal_id, updated_info)
    elif choice == 9:
        print(bill_service.list_all())
    elif choice == 10:
        return auth_service.signout(auth_service.current_user.id)

def handle_cashier_menu(bill_service):
    options = ["List Bills", "Mark Bill as Paid", "Logout"]
    choice = display_menu(options)

    if choice == 1:
        print(bill_service.list_all())
    elif choice == 2:
        bill_id = input("Bill ID to mark as paid: ")
        bill_service.update(bill_id, {"is_paid": True})
    elif choice == 3:
        return auth_service.signout(auth_service.current_user.id)

def handle_user_menu(meal_service, bill_service):
    options = ["List Meals", "Order Meal", "Logout"]
    choice = display_menu(options)

    if choice == 1:
        print(meal_service.list_all())
    elif choice == 2:
        meal_id = input("Meal ID: ")
        quantity = int(input("Quantity: "))
        bill = Bill(user_id=auth_service.current_user.id, meal_id=meal_id, quantity=quantity)
        bill_service.add(bill)
    elif choice == 3:
        return auth_service.signout(auth_service.current_user.id)

def main():
    users = load_data('users.txt', User)
    meals = load_data('meals.txt', Meal)
    bills = load_data('bills.txt', Bill)

    global auth_service
    auth_service = AuthenticationService(users)
    user_service = UserService(users)
    meal_service = MealService(meals)
    bill_service = BillService(bills)

    while True:
        if auth_service.current_user:
            role = auth_service.current_user.role
            if role == "admin":
                handle_admin_menu(auth_service, user_service, meal_service, bill_service)
            elif role == "cashier":
                handle_cashier_menu(bill_service)
            elif role == "user":
                handle_user_menu(meal_service, bill_service)
        else:
            options = ["Sign In", "Sign Up", "Exit"]
            choice = display_menu(options)

            if choice == 1:
                username = input("Username: ")
                password = input("Password: ")
                if auth_service.signin(username, password):
                    print("Signed in successfully!")
                else:
                    print("Invalid username or password.")
            elif choice == 2:
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                username = input("Username: ")
                password = input("Password: ")
                age = int(input("Age: "))
                new_user = auth_service.signup(first_name, last_name, username, password, age)
                print(f"User {new_user.username} signed up successfully!")
            elif choice == 3:
                print("Exiting...")
                break

        save_data('users.txt', users)
        save_data('meals.txt', meals)
        save_data('bills.txt', bills)

if __name__ == "__main__":
    main()
