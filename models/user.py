from utilities.general_utils import generate_id

class User:
    def __init__(self, first_name, last_name, username, password, is_loggedin, role) -> None:
        self.id = generate_id()  # Automatically generate an ID
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.is_loggedin = is_loggedin
        self.role = role

    def to_dict(self):
        """Convert the User object to a dictionary."""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'password': self.password,
            'is_loggedin': self.is_loggedin,
            'role': self.role
        }
