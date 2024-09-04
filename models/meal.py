from utilities.general_utils import generate_id
class Meal:
    def __init__(self, name, price):
        self.id = generate_id()
        self.name = name
        self.price = price
