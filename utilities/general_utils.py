import uuid
import bcrypt


def generate_id():
    return str(uuid.uuid4())


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


class AuthenticationService:
    def __init__(self, users):
        self.current_user = None  # Track the currently signed-in user
        self.users = users  # A list of user dictionaries

    def signup(self, first_name, last_name, username, password, age):
        # Check if username already exists
        for user in self.users:
            if user['username'] == username:
                print("Username already exists.")
                return False
        
        # Create new user with a hashed password
        new_user = {
            'id': generate_id(),
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'password': hash_password(password),  # Hash the password
            'age': age,
            'role': 'user',  # Assign a default role
            'is_loggedin': False  # Initially not logged in
        }
        
        self.users.append(new_user)
        print("Signup successful.")
        return True
    

    def signin(self, username, password):
        for user in self.users:
            if user['username'] == username:
                if verify_password(password, user['password']):
                    user['is_loggedin'] = True
                    self.current_user = user
                    print("Signin successful.")
                    return True
                else:
                    print("Invalid password.")
                    return False
        
        print("Username not found.")
        return False
    

    def signout(self):
        if self.current_user:
            self.current_user['is_loggedin'] = False
            print(f"User {self.current_user['username']} signed out.")
            self.current_user = None
            return True
        else:
            print("No user is currently signed in.")
            return False


