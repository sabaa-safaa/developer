from models.user import User
from utilities.general_utils import verify_password, hash_password
from utilities.data_utils import save_data

class AuthenticationService:
    def __init__(self, users):
        self.current_user = None
        self.users = users

    def signin(self, username, password):
        for user in self.users:
            if user.username == username and verify_password(password, user.password):
                self.current_user = user
                user.is_loggedin = True  # Set the user as logged in
                return True
        return False

    def signup(self, first_name, last_name, username, password, age):
        hashed_password = hash_password(password)
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=hashed_password,
            is_loggedin=False,  # New users are not logged in by default
            role='user'  # Default role
        )
        self.users.append(new_user)
        save_data('users.txt', [user.to_dict() for user in self.users])
        return new_user

    def signout(self, user_id):
        for user in self.users:
            if user.id == user_id:
                user.is_loggedin = False
                if self.current_user == user:
                    self.current_user = None
                return True
        return False
