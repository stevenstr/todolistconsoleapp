"""ToDo list.

Create Client_ToDo instance to use method to manage to-do list.

Typical usage example:
    client = Client_ToDo()
"""

import requests
import json


class BadPriorityError(Exception):
    """Task priority has wrong value.

    Attributes::
        head: Text with type of error.
        message: Text with error message.
    """

    def __init__(self, head="ToDoPriorityError", message="Bad priority."):
        """Initializes the BadPriorityError instance.

        Args:
            head: Text with type of error. Default value: "ToDoPriorityError".
            message: Ntxt with error message. Default value: "Bad priority.".

        Inherited from Exception class.
        """
        super().__init__(message)
        self.head = head
        self.message = message


class BadIdError(Exception):
    """ID has wrong value.

    Attributes::
        head: Text with type of error.
        message: Text with error message.
    """

    def __init__(self, head="ToDoTaskIDError", message="Bad task ID."):
        """Initializes the BadIdError instance.

        Args:
            head: Text with type of error. Default value: "ToDoTaskIDError".
            message: Ntxt with error message. Default value: "Bad task ID.".

        Inherited from Exception class.
        """
        super().__init__(message)
        self.head = head
        self.message = message


class BadNameError(Exception):
    """Task Name has wrong value.

    Attributes::
        head: Text with type of error.
        message: Text with error message.
    """

    def __init__(self, head="ToDoTaskNameError", message="Bad task name."):
        """Initializes the BadIdError instance.

        Args:
            head: Text with type of error. Default value: "ToDoTaskNameError".
            message: Ntxt with error message. Default value: "BBad task name.".

        Inherited from Exception class.
        """
        super().__init__(message)
        self.head = head
        self.message = message


class Client_ToDo:
    """Manage to-do list by http using json-server.

    Attributes:
        key_names: List of field names.
        key_widths: List of field widths.
    """

    def __init__(self):
        """Initializes the Client_ToDo instance."""
        self.key_names = ["id", "name", "priority"]
        self.key_widths = [3, 30, 9]

    def show_head(self):
        """Print head of tasks table for user."""
        print("\t\t", end="")
        for n, w in zip(self.key_names, self.key_widths):
            print(n.ljust(w), end="| ")
        print()

    def show_empty(self):
        """Print emty table for user when no tasks in to-do list."""
        print("\t\t", end="")
        for width in self.key_widths:
            print(" ".ljust(width), end="| ")
        print()

    def show_task(self, task: dict):
        """Print tasks table for user when to-do list has tasks.

        Args:
            task: Dictionary with single task from to_do list.
        """
        print("\t\t", end="")
        for field, width in zip(self.key_names, self.key_widths):
            print(str(task.get(field)).ljust(width), end="| ")
        print()

    def show(self, json):
        """Choice of what type of content print to the user.

        Args:
            json: Converted to json response body from the server.
        """
        self.show_head()
        if isinstance(json, list):
            for car in json:
                self.show_task(car)
        elif isinstance(json, dict):
            if json:
                self.show_task(json)
            else:
                self.show_empty()

    def get_tasks(self, query=""):
        """Http request to GET tasks from to-do list.

        Response is converted to JSON and passed to the show method when status code is OK.

        Args:
            query: Query parameter for URI. Default = empty string.
        """
        try:
            if query == "?_sort=priority":
                reply = requests.get(f"http://localhost:3000/tasks{query}")
            elif query == "?_sort=priority&_order=desc":
                reply = requests.get(f"http://localhost:3000/tasks{query}")
            else:
                reply = requests.get(f"http://localhost:3000/tasks")
        except requests.RequestException:
            print("Communication error")
        else:
            if reply.status_code == requests.codes.ok:
                self.show(reply.json())
            elif reply.status_code == requests.codes.not_found:
                print("Resource not found")
            else:
                print("Server error")

    def get_task_by_id(self):
        """Http request to GET task by ID from to-do list.

        ID gets from user's input and use like query for request.
        Response is converted to JSON and passed to the show method when status code is OK.

        Raises:
            BadIdError: Error occurred taking task ID from a user and converting ID to integer.
        """
        try:
            task_id = int(input("Task ID: "))
        except:
            raise BadIdError

        try:
            reply = requests.get(f"http://localhost:3000/tasks/{task_id}")
        except requests.RequestException:
            print("Communication error")
        else:
            if reply.status_code == requests.codes.ok:
                self.show(reply.json())
            elif reply.status_code == requests.codes.not_found:
                print("Resource not found")
            else:
                print("Server error")

    def add_task(self):
        """Http request to POST new task to to-do list.

        ID, NAME, PRIORITY get from user's input and converted to JSON for request body.
        Response is converted to JSON and passed to the show method when status code is OK.

        Raises:
            BadIdError: Error occurred taking task ID from a user and converting ID to integer.
            BadNameError: Error occurred taking task NAME from a user.
            BadPriorityError: Error occurred taking task PRIORITY from a user and converting PRIORITY to integer.
        """
        new_task = {}

        try:
            new_task["id"] = int(input("New task ID: "))
        except:
            raise BadIdError

        new_task["name"] = input("New task name: ")

        if len(new_task["name"]) <= 5:
            raise BadNameError(message="More than 5 characters!")

        try:
            new_task["priority"] = int(input("New task priority: "))
        except:
            raise BadPriorityError

        try:
            reply = requests.post(
                "http://localhost:3000/tasks/",
                headers={"Content-Type": "application/json"},
                data=json.dumps(new_task),
            )
        except requests.RequestException:
            print("Communication error")
        else:
            if reply.status_code == requests.codes.ok:
                self.show(reply.json())
            elif reply.status_code == requests.codes.not_found:
                print("Resource not found")
            else:
                print("Server error")

    def change_task(self):
        """Http request to PUT changes for task by ID.

        ID, NAME, PRIORITY get from user's input and converted to JSON for request body.
        Response is converted to JSON and passed to the show method when status code is OK.

        Raises:
            BadIdError: Error occurred taking task ID from a user and converting ID to integer.
            BadNameError: Error occurred taking task NAME from a user.
            BadPriorityError: Error occurred taking task PRIORITY from a user and converting PRIORITY to integer.
        """
        task_to_change = {}

        try:
            task_to_change["id"] = int(input("Task ID: "))
        except:
            raise BadIdError

        task_to_change["name"] = input("Task name: ")

        res = task_to_change.get("name")
        if res is not None:
            if len(res) <= 5:
                raise BadNameError(message="More than 5 characters!")
        else:
            raise BadNameError(message="Doesnt contain!")

        try:
            task_to_change["priority"] = int(input("Task priority: "))
        except:
            raise BadPriorityError

        try:
            reply = requests.put(
                f"http://localhost:3000/tasks/{task_to_change.get('id')}",
                headers={"Content-Type": "application/json"},
                data=json.dumps(task_to_change),
            )
        except requests.RequestException:
            print("Communication error")
        else:
            if reply.status_code == requests.codes.ok:
                self.show(reply.json())
            elif reply.status_code == requests.codes.not_found:
                print("Resource not found")
            else:
                print("Server error")

    def delete_task(self):
        """Http request to DELETE task by ID.

        ID gets from user's input and use like query for request.
        Response is converted to JSON and passed to the show method when status code is OK.

        Raises:
            BadIdError: Error occurred taking task ID from a user and converting ID to integer.
        """
        try:
            task_to_delete_id = int(input("Task ID: "))
        except:
            raise BadIdError

        try:
            reply = requests.delete(f"http://localhost:3000/tasks/{task_to_delete_id}")
            reply = requests.get("http://localhost:3000/tasks/")
        except requests.RequestException:
            print("Communication error")
        else:
            if reply.status_code == requests.codes.ok:
                self.show(reply.json())
            elif reply.status_code == requests.codes.not_found:
                print("Resource not found")
            else:
                print("Server error")

    def close_connection(self):
        """Close conection by HTTP request header and show info message for user aboit this."""
        try:
            reply = requests.head(
                "http://localhost:3000/tasks/",
                headers={"Connection": "Close"},
            )
        except requests.RequestException:
            print("Communication error")
        else:
            if (
                reply.status_code == requests.codes.ok
                and reply.headers["Connection"] == "close"
            ):
                print(f"Connection are closed successfully.")
            elif reply.status_code == requests.codes.not_found:
                print("Resource not found")
            else:
                print("Server error")


def show_menu():
    print(
        """
Show tasks
    1. Show all tasks
    2. Show all tasks sorted by priority
    3. Show all tasks sorted by priority desc
    4. Show single task by ID
5. Add new task
6. Change task by ID
7. Delete task by ID
8. Close connection and Exit
"""
    )


def main():
    """User menu."""

    client = Client_ToDo()

    show_menu()

    user_choice = input("Put what do you want: ")

    while user_choice != "8":
        if user_choice == "1":
            client.get_tasks()

        elif user_choice == "2":
            client.get_tasks("?_sort=priority")
        elif user_choice == "3":
            client.get_tasks("?_sort=priority&_order=desc")
        elif user_choice == "4":
            try:
                client.get_task_by_id()
            except BadIdError as e:
                print(e.message)
            except:
                print("\tSomesing goes wrong!")
        elif user_choice == "5":
            try:
                client.add_task()
            except (BadIdError, BadNameError, BadPriorityError) as e:
                print(e.message)
            except:
                print("\tSomesing goes wrong!")
        elif user_choice == "6":
            try:
                client.change_task()
            except (BadIdError, BadNameError, BadPriorityError) as e:
                print(e.message)
            except:
                print("\tSomesing goes wrong!")
        elif user_choice == "7":
            try:
                client.delete_task()
            except BadIdError as e:
                print(e.message)
            except:
                print("\tSomesing goes wrong!")

        show_menu()

        user_choice = input("Put what do you want: ")

    if user_choice == "8":
        client.close_connection()
        print("Good bye!")


if __name__ == "__main__":
    print("main.py - as independent module.\n")
    main()
else:
    print("main.py - as imported module.")
