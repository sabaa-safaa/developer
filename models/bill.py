import datetime
from utilities.general_utils import generate_id

class Bill:
    def __init__(self, total_amount, user_id, meal_id):
        self.id = generate_id()
        self.meal_id = meal_id
        self.user_id = user_id
        self.total_amount = total_amount
        self.date = datetime.datetime.now()
        self.is_paid = False
        self.bills = []
               