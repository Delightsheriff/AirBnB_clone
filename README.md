# HBNB Command-Line Interface

## Description

HBNB is a command-line interface (CLI) application for managing objects related to an AirBnB-like service. It allows users to create, view, update, delete, and list various objects such as Users, States, Cities, Places, Amenities, and Reviews. The application persists these objects to a JSON file (`file.json`), allowing data to be stored and retrieved across sessions.

## Installation

1.  Ensure you have Python 3 installed on your system.
2.  Clone the repository (if applicable) or download the project files.
3.  The console can be run directly from the command line. Make sure `console.py` is executable:
    ```bash
    chmod +x console.py
    ```

## Usage

To start the HBNB console, navigate to the project directory and run:

```bash
./console.py
```

You will see the `(hbnb)` prompt, where you can enter commands.

### Available Commands

The console supports the following commands:

*   **`create <ClassName>`**: Creates a new instance of `ClassName`, saves it to the JSON file, and prints its ID.
    *   Example: `create User`
*   **`show <ClassName> <id>`**: Prints the string representation of an instance based on its `ClassName` and `id`.
    *   Example: `show User 1234-abcd-5678-efgh`
*   **`destroy <ClassName> <id>`**: Deletes an instance based on its `ClassName` and `id`. The change is saved to the JSON file.
    *   Example: `destroy User 1234-abcd-5678-efgh`
*   **`all [ClassName]`**: Prints string representations of all instances. If `ClassName` is provided, it lists instances only of that class.
    *   Example: `all`
    *   Example: `all User`
*   **`update <ClassName> <id> <attribute_name> "<attribute_value>"`**: Updates an instance based on its `ClassName` and `id` by adding or updating an attribute. The change is saved to the JSON file.
    *   Example: `update User 1234-abcd-5678-efgh email "new_email@example.com"`
    *   **Note:** `id`, `created_at`, and `updated_at` attributes cannot be updated.
*   **`count <ClassName>`**: Prints the number of instances of a specific `ClassName`.
    *   Example: `count User`
*   **`quit`**: Exits the console.
*   **`EOF`**: Exits the console (can be triggered by Ctrl+D).
*   **`help [command]`**: Displays help information for commands.

### Alternative Command Syntax

The console also supports an alternative syntax for some commands:

*   **`<ClassName>.all()`**: Equivalent to `all <ClassName>`.
    *   Example: `User.all()`
*   **`<ClassName>.count()`**: Equivalent to `count <ClassName>`.
    *   Example: `User.count()`
*   **`<ClassName>.show(<id>)`**: Equivalent to `show <ClassName> <id>`.
    *   Example: `User.show("1234-abcd-5678-efgh")`
*   **`<ClassName>.destroy(<id>)`**: Equivalent to `destroy <ClassName> <id>`.
    *   Example: `User.destroy("1234-abcd-5678-efgh")`
*   **`<ClassName>.update(<id>, <attribute_name>, <attribute_value>)`**: Equivalent to `update <ClassName> <id> <attribute_name> "<attribute_value>"`.
    *   Example: `User.update("1234-abcd-5678-efgh", "first_name", "John")`
*   **`<ClassName>.update(<id>, <dictionary>)`**: Updates an instance with multiple attributes provided as a dictionary.
    *   Example: `User.update("1234-abcd-5678-efgh", {"first_name": "John", "age": 30})`

## Examples

Here are a few examples of how to use the HBNB console:

1.  **Create a new User:**
    ```
    (hbnb) create User
    f9e2b9c1-1a18-4f5a-823c-0d0fd898c479
    ```

2.  **Show the created User:**
    ```
    (hbnb) show User f9e2b9c1-1a18-4f5a-823c-0d0fd898c479
    [User] (f9e2b9c1-1a18-4f5a-823c-0d0fd898c479) {'id': 'f9e2b9c1-1a18-4f5a-823c-0d0fd898c479', 'created_at': datetime.datetime(2023, 10, 27, 10, 0, 0, 123456), 'updated_at': datetime.datetime(2023, 10, 27, 10, 0, 0, 123456)}
    ```

3.  **Update the User's name:**
    ```
    (hbnb) update User f9e2b9c1-1a18-4f5a-823c-0d0fd898c479 first_name "Betty"
    ```
    Or using the alternative syntax:
    ```
    (hbnb) User.update("f9e2b9c1-1a18-4f5a-823c-0d0fd898c479", "first_name", "Betty")
    ```

4.  **List all User objects:**
    ```
    (hbnb) all User
    ["[User] (f9e2b9c1-1a18-4f5a-823c-0d0fd898c479) {'id': 'f9e2b9c1-1a18-4f5a-823c-0d0fd898c479', 'created_at': datetime.datetime(2023, 10, 27, 10, 0, 0, 123456), 'updated_at': datetime.datetime(2023, 10, 27, 10, 5, 0, 654321), 'first_name': 'Betty'}"]
    ```

5.  **Count the number of User objects:**
    ```
    (hbnb) User.count()
    1
    ```

## Features

*   Command-line interface for interactive object management.
*   Supports multiple object types (Models).
*   Data persistence using JSON file storage.
*   Dynamic creation, retrieval, updating, and deletion of objects.
*   Alternative dot-notation for commands (e.g., `User.all()`).

## Models

The following models are available for management through the console:

*   `BaseModel` (Serves as the base for other models)
*   `User`
*   `State`
*   `City`
*   `Amenity`
*   `Place`
*   `Review`
