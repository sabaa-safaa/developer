from utilities.base_service import BaseService
from utilities.data_utils import load_data, save_data
from models.user import User


class UserService(BaseService):
    def list_all(self):
        # todo: implement this method
        users = load_data('users.txt')
        return [User(**user_data) for user_data in users]
        pass

    def add(self, user):
        # todo: implement this method
        users = load_data('users.txt')
        users.append(user.to_dict())
        save_data('users.txt', users)
        pass

    def remove(self, user_id):
        # todo: implement this method
        users = load_data('users.txt')
        users = [user for user in users if user['id'] != user_id]
        save_data('users.txt', users)
        pass

    def update(self, user_id, updated_info):
        # todo: implement this method
        users = load_data('users.txt')
        for user in users:
            if user['id'] == user_id:
                user.update(updated_info)
            break
        save_data('users.txt', users)
        pass

