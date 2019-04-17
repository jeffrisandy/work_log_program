import datetime
import os

"""
Helpers functions that show the menu options & logs, get data from user input
"""


def get_main_menu_option():
    """
    Display start menu option and get user input
    :return: string, user input
    """
    msg = "WORK LOG"
    msg += "\nWhat would you like to do ?"
    msg += "\na) Add new entry"
    msg += "\nb) Search in existing entry"
    msg += "\nc) Quit program"
    msg += "\n> "
    return input(msg)


def get_entry_date():
    """
    Get user input date during entry new data
    :return: datetime object
    """
    msg = "Date of the task"
    date = get_date(msg)
    return date


def get_date(msg):
    """
    Get user input date
    :param msg: string, additional msg to display to user
    :return: datetime object
    """
    msg += "\nPlease use DD/MM/YYYY format: "

    while True:
        input_date = input(msg)
        try:
            date = datetime.datetime.strptime(input_date, "%d/%m/%Y")
        except ValueError:
            print(f"{input_date} doesn't seem to be a valid date & time.")
        else:
            return date


def get_entry_title():
    """
    Get user input title of data
    :return: string, user input
    """
    msg = "Title : "
    input_msg = input(msg)
    while input_msg == "":
        print("Please input the title")
        input_msg = input(msg)
    return input_msg


def get_entry_time_spent():
    """
    Get user input time spent in rounded minues
    :return: int, user input
    """
    msg = "Time spent (rounded minutes): "
    while True:
        input_msg = input(msg)
        try:
            input_msg = int(input_msg)
        except ValueError:
            print("The value entered was not a number, try again.")
        else:
            return input_msg


def get_entry_notes():
    """
    Get user input notes
    :return: string
    """
    msg = "Notes (optional, you can leave this empty): "
    return input(msg)


def get_entries():
    """
    Display and get user input for adding new data
    :return: tupple of date (datetime object), title(str), time_spent(int), notes(str)
    """
    date = get_entry_date()
    title = get_entry_title()
    time_spent = get_entry_time_spent()
    notes = get_entry_notes()
    return date, title, time_spent, notes


def display_entry_added():
    """
    Displaying to user that the new data has been add
    :return: str, user input
    """
    msg = "The entry has been add. Press enter to return to the menu"
    return input(msg)


def get_search_by():
    """
    Displaying search menu options
    :return: str, user input
    """
    msg = "Do you want to search by: "
    msg += "\na) Exact date"
    msg += "\nb) Range of dates"
    msg += "\nc) Exact search"
    msg += "\nd) Search by Regex pattern"
    msg += "\ne) Return to menu"
    msg += "\n> "
    return input(msg)


def show_entry_log(date, title, time_spent, notes):
    """
    Displaying log data
    :param date: datetime object
    :param title: string
    :param time_spent: int
    :param notes: string
    :return: None
    """
    msg = f"Date : {date},"
    msg += f"\nTitle: {title},"
    msg += f"\nTime spent: {time_spent},"
    msg += f"\nNotes : {notes}"
    print(msg)


def show_quit_msg():
    """
    Displaying quit message
    :return: None
    """
    msg = "Thank you for using the Work Log program."
    msg += "\nCome again soon."
    print(msg)


def show_edit_menu():
    """
    Displaying log edit menu
    :return: string, user input
    """
    msg = "What do you want to edit ?"
    msg += "\na) Date"
    msg += "\nb) Title"
    msg += "\nc) Time spent"
    msg += "\nd) Notes"
    msg += "\ne) All of above"
    msg += "\n> "
    return input(msg).lower()


def clear_screen():
    """
    Clear screen
    :return: None"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_cannot_find():
    """
    Displaying msg that cannot find any in the database
    :return: None
    """
    clear_screen()
    print("Cannot find log.")
    input("Press enter to return to search menu ")