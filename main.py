import os
import datetime
from log import Log


def get_main_menu_option():
    msg = "WORK LOG"
    msg += "\nWhat would you like to do ?"
    msg += "\na) Add new entry"
    msg += "\nb) Search in existing entry"
    msg += "\nc) Quit program"
    msg += "\n> "
    return input(msg)


def get_entry_date():
    msg = "Date of the task"
    date = get_date(msg)
    return date


def get_date(msg):
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
    msg = "Title : "
    input_msg = input(msg)
    while input_msg == "":
        print("Please input the title")
        input_msg = input(msg)
    return input_msg


def get_entry_time_spent():
    msg = "Time spent (rounded minutes): "
    while True:
        input_msg = input(msg)
        try:
            input_msg = round(float(input_msg))
        except ValueError:
            print("The value entered was not a number, try again.")
        else:
            return input_msg


def get_entry_notes():
    msg = "Notes (optional, you can leave this empty): "
    return input(msg)


def get_entries():
    date = get_entry_date()
    title = get_entry_title()
    time_spent = get_entry_time_spent()
    notes = get_entry_notes()
    return date, title, time_spent, notes


def display_entry_added():
    msg = "The entry has been add. Press enter to return to the menu"
    return input(msg)


def get_search_by():
    msg = "Do you want to search by: "
    msg += "\na) Exact date"
    msg += "\nb) Range of dates"
    msg += "\nc) Exact search"
    msg += "\nd) Search by Regex pattern"
    msg += "\ne) Return to menu"
    msg += "\n> "
    return input(msg)


def show_entry_log(date, title, time_spent, notes):
    msg = f"Date : {date},"
    msg += f"\nTitle: {title},"
    msg += f"\nTime spent: {time_spent},"
    msg += f"\nNotes : {notes}"
    print(msg)


def show_quit_msg():
    msg = "Thank you for using the Work Log program."
    msg += "\nCome again soon."
    print(msg)


def edit_log(index):
    msg = "What do you want to edit ?"
    msg += "\na) Date"
    msg += "\nb) Title"
    msg += "\nc) Time spent"
    msg += "\nd) Notes"
    msg += "\ne) All of above"
    msg += "\n> "
    options = input(msg).lower()
    date, title, time_spent, notes = work_log.get_log(index)

    if options == "e":
        date, title, time_spent, notes = get_entries()
    elif options == "a":
        date = get_entry_date()
    elif options == "b":
        title = get_entry_title()
    elif options == "c":
        time_spent = get_entry_time_spent()
    elif options == "d":
        notes = get_entry_notes()

    work_log.edit_log(index, date, title, time_spent, notes)


def show_find_results(ids):
    i = 0
    while i < len(ids):
        clear_screen()
        logs = work_log.get_log(ids[i])
        show_entry_log(*logs)

        print(f"\nResult of {i + 1} of {len(ids)}")

        log_options = "\n[N]ext, [P]revious, [E]dit, [D]elete, [R]eturn to search menu\n> "

        input_log_options = input(log_options).upper()

        if (input_log_options == "N") & (i != len(ids) - 1):
            i += 1
        elif (input_log_options == "P") & (i != 0):
            i -= 1
        elif input_log_options == "E":
            edit_log(ids[i])
        elif input_log_options == "D":
            work_log.remove_by_index(ids[i])
            ids.remove(ids[i])
        elif input_log_options == "R":
            clear_screen()
            break
        else:
            clear_screen()
            print("Please select actions.\n")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def start():
    while True:
        clear_screen()
        main_menu = get_main_menu_option().lower()

        if main_menu == 'a':
            entries = get_entries()
            work_log.add(*entries)
            display_entry_added()

        elif main_menu == "b":
            while True:
                clear_screen()
                search_option = get_search_by().lower()

                if search_option == "a":  # find by date
                    date = get_entry_date()
                    ids = work_log.find_by_date(date)
                    show_find_results(ids)
                elif search_option == "b":  # find by date range
                    start_date = get_date("Start Date")
                    end_date = get_date("End Date")
                    ids = work_log.find_by_range_date(start_date, end_date)
                    show_find_results(ids)

                elif search_option == 'c':  # find by exact word
                    string_to_find = input("Type words to find : ")
                    print("\n")
                    ids = work_log.find_by_exact(string_to_find)
                    show_find_results(ids)
                elif search_option == 'd':  # find by regex
                    regex = input("Type regex pattern to find : ")
                    print("\n")
                    ids = work_log.find_by_regex(regex)
                    show_find_results(ids)
                elif search_option == "e":
                    clear_screen()
                    break

        elif main_menu == "c":
            show_quit_msg()
            work_log.to_csv()
            break


if __name__ == "__main__":
    work_log = Log()
    start()
