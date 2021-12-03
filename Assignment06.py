# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoFile.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KLMartinez,12/1/21,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name = "ToDoFile.txt"  # The name of the data file
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #

class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to the list

        :param task: (string) task, to be entered by the user
        :param priority: (string) priority, to be entered by the user
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows, with the new task added to it
        """
        row = {"Task": task.strip(), "Priority": priority.strip()}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from the list

        :param task: (string) task, to be entered by the user
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows, without the indicated task
        """
        for row in list_of_rows:  # Search table by row for the task to delete
            if task.lower() in row["Task"].lower():
                list_of_rows.remove(row)  # Delete the indicated row
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes list to the file

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows which was written to the file
        """
        file = open(file_name, "w")
        for row in list_of_rows:  # For each dictionary row, write the values (comma separated)
            file.write(row["Task"] + ',' + row["Priority"] + "\n")
        file.close()
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionary rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """ Gets a new task and priority from the user

        :return: (tuple) new task and priority
        """
        print("Enter the task and priority (Low, Medium, High):")
        task = input("Task: ")  # User enters a task
        priority = input("Priority (Low, Medium, High): ")  # User enters a priority
        print()  # Add an extra line for looks
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Gets a task to remove from the user

        :param task: (string) task entered by the user
        :return: (tuple) new task and priority
        """
        task = input("Which task from the list above would you like to remove?: ")
        print()  # Add an extra line for looks
        return task

    @staticmethod
    def output_save_confirmation():
        """ Shows the user that the list was saved

        :return: nothing
        """
        print("ToDo list saved.")
        print()  # Add an extra line for looks

    @staticmethod
    def output_exit_confirmation():
        """ Says goodbye to the user

        :return: nothing
        """
        print("Goodbye!")
        print()  # Add an extra line for looks


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name, table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task_add, priority_add = IO.input_new_task_and_priority()  # Prompt for new task & priority, upnack tuple
        Processor.add_data_to_list(task_add, priority_add, table_lst)  # Use input values as arguments
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task_remove = IO.input_task_to_remove()  # Prompt for task to remove, save variable
        Processor.remove_data_from_list(task_remove, table_lst)  # Use input value as argument
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        Processor.write_data_to_file(file_name, table_lst)  # Run write to file function
        IO.output_save_confirmation()  # Print confirmation
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        IO.output_exit_confirmation()  # Print Goodbye message
        break  # and Exit
