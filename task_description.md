### Task Description: Food Ordering System Implementation

#### **Project Overview**

You are tasked with implementing a food ordering system using object-oriented programming principles. The system will manage users, meals, and bills, and include authentication functionality. The project is structured into several key components, and your objective is to develop and integrate these components according to the provided file structure.

#### **File Structure and Descriptions**

1. **`services` Folder**

   - **`bill_service.py`**: Contains the `BillService` class responsible for managing bill-related operations. Implement methods for listing all bills, adding a new bill, removing an existing bill, and updating a bill.
   - **`user_service.py`**: Contains the `UserService` class responsible for managing user-related operations. Implement methods for listing all users, adding a new user, removing an existing user, and updating user information.
   - **`meal_service.py`**: Contains the `MealService` class responsible for managing meal-related operations. Implement methods for listing all meals, adding a new meal, removing an existing meal, and updating meal information.
   - **`auth_service.py`**: Contains the `AuthService` class responsible for handling authentication operations such as signing in, signing out, and hashing passwords.

2. **`database` Folder**

   - **`bills.txt`**: A text file containing bill data in CSV format. Each record has a UUID as its ID.
   - **`users.txt`**: A text file containing user data in CSV format. Each record has a UUID as its ID.
   - **`meals.txt`**: A text file containing meal data in CSV format. Each record has a UUID as its ID.

3. **`utilities` Folder**

   - **`base_service.py`**: Contains the `BaseService` abstract class, which provides a common interface for all services. This class will define abstract methods that must be implemented by concrete service classes.
   - **`utils.py`**: Contains utility functions such as `verify_password`, `hash_password`, and `generate_id`.
   - **`data_utils.py`**: Contains functions for data management, including `save_data` and `load_data`, which handle reading from and writing to the CSV files in the `database` folder.

4. **`models` Folder**

   - **`bill.py`**: Contains the `Bill` class with attributes for bill information. This class will define the structure of a bill object.
   - **`user.py`**: Contains the `User` class with attributes for user information. This class will define the structure of a user object.
   - **`meal.py`**: Contains the `Meal` class with attributes for meal information. This class will define the structure of a meal object.

5. **`main.py`**: The entry point of the application. This file will handle user interactions, display choices based on user roles, and invoke methods from the service classes to perform operations.

#### **Task Requirements**

1. **Implement Service Methods**:

   - **List All**: Implement a method to list all records (bills, users, meals) in each corresponding service class.
   - **Add**: Implement a method to add a new record to each corresponding service class.
   - **Remove**: Implement a method to remove an existing record from each corresponding service class.
   - **Update**: Implement a method to update an existing record in each corresponding service class.

2. **Implement Data Utilities**:
   - **`load_data`**: Implement the function to read data from text files in the `database` folder and return a list of dictionaries.
   - **`save_data`**: Implement the function to write data to text files in the `database` folder from a list of dictionaries.

3. **Implement Authentication Methods**:
   - **`signin`**: Implement the method for signing in a user, including password validation and session management.
   - **`signup`**: Implement the method for signing up a new user, including password hashing and default role assignment.
   - **`signout`**: Implement the method for signing out a user and handling session invalidation.
   - **Note**: You can use the implementation from the previous task as a reference for these methods.


#### **Hints**

- **Data Files**: You can use different file formats for data storage such as CSV or JSON. Choose the format that best fits your implementation and is easiest to handle with the `load_data` and `save_data` functions.
- **Handling Data**: Feel free to edit and adjust the code as necessary to meet the requirements. Ensure that your implementations for data reading and writing are robust and handle errors gracefully.
- **UUIDs**: Ensure that each record in your data files has a unique UUID as its ID. You can use the Python `uuid` module to generate these IDs.

#### **Deadline**

- **One week from today**: All tasks should be completed by August 30, 2024 12:00 AM.

#### **Bonus**

- Create a `testing` folder.
- Implement unit tests for each service class to ensure that all methods work correctly.
- Include tests for edge cases and invalid inputs.

#### **Submission**

- Please submit your completed project by sending the entire project folder to the assistant. Ensure that all files are included and that the project runs without errors. You can submit your task through the designated submission platform or method as instructed.

Feel free to reach out if you have any questions or need further clarifications. Good luck!

