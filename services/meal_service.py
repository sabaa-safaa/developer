from utilities.base_service import BaseService
from utilities.data_utils import load_data, save_data
from models.meal import Meal


class MealService(BaseService):
    def list_all(self):
        # todo: implement this method
        meals = load_data('meals.txt')
        return [Meal(**meal_data) for meal_data in meals]
        pass

    def add(self):
        # todo: implement this method
        meals = load_data('meals.txt')
        meals.append(Meal.to_dict())
        save_data('meals.txt', meals)
        pass

    def remove(self, meal_id):
        # todo: implement this method
        meals = load_data('meals.txt')
        meals = [meal for meal in meals if meal['id'] != meal_id]
        save_data('meals.txt', meals)
        pass

    def update(self, meal_id, updated_info):
        # todo: implement this method
        meals = load_data('meals.txt')
        for meal in meals:
            if meal['id'] == meal_id:
                meal.update(updated_info)
                break
        save_data('meals.txt', meals)
        pass
