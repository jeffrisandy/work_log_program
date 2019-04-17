import menu
from log import Log


class WorkLog(Log):
    """
    The main class of this program.
    WorkLog class inheritance from Log class
    """

    def __init__(self):
        """ Initialization """
        super().__init__()

    def edit_log(self, index):
        """
        Edit the log data based on given log index
        :param index: int
        :return: Note
        """
        options = menu.show_edit_menu()
        date, title, time_spent, notes = self.get_log(index)

        if options == "e":
            date, title, time_spent, notes = menu.get_entries()
        elif options == "a":
            date = menu.get_entry_date()
        elif options == "b":
            title = menu.get_entry_title()
        elif options == "c":
            time_spent = menu.get_entry_time_spent()
        elif options == "d":
            notes = menu.get_entry_notes()

        self.update_log(index, date, title, time_spent, notes)

    def show_find_results(self, ids):
        """
        Display the search result of data in database
        :param ids: log index
        :return: None
        """
        i = 0

        # show msg if cannot find any result
        if len(ids) == 0:
            menu.clear_screen()
            menu.show_cannot_find()

        while i < len(ids):
            menu.clear_screen()
            logs = self.get_log(ids[i])
            menu.show_entry_log(*logs)

            print(f"\nResult of {i + 1} of {len(ids)}")

            log_options = "\n[N]ext, [P]revious, [E]dit, [D]elete, [R]eturn to search menu\n> "

            input_log_options = input(log_options).upper()

            if (input_log_options == "N") & (i != len(ids) - 1):
                i += 1
            elif (input_log_options == "P") & (i != 0):
                i -= 1
            elif input_log_options == "E":
                self.edit_log(ids[i])
            elif input_log_options == "D":
                self.remove_by_index(ids[i])
                ids.remove(ids[i])
            elif input_log_options == "R":
                menu.clear_screen()
                break
            else:
                menu.clear_screen()
                print("Please select actions.\n")

    def search_menu(self):
        """
        Search Menu & show search result
        :return: None
        """
        while True:
            menu.clear_screen()
            search_option = menu.get_search_by().lower()

            if search_option == "a":  # find by date
                date = menu.get_entry_date()
                ids = self.find_by_date(date)

            elif search_option == "b":  # find by date range
                start_date = menu.get_date("Start Date")
                end_date = menu.get_date("End Date")
                ids = self.find_by_range_date(start_date, end_date)

            elif search_option == 'c':  # find by exact word
                string_to_find = input("Type words to find : ")
                print("\n")
                ids = self.find_by_exact(string_to_find)

            elif search_option == 'd':  # find by regex
                regex = input("Type regex pattern to find : ")
                print("\n")
                ids = self.find_by_regex(regex)

            elif search_option == "e": # return to main menu
                menu.clear_screen()
                break

            self.show_find_results(ids)

    def entry_menu(self):
        """
        Entry new data menu and show search result
        :return: None
        """
        entries = menu.get_entries()
        self.add(*entries)
        menu.display_entry_added()

    def start(self):
        """
        Start the program
        :return: None
        """
        while True:
            menu.clear_screen()
            main_menu = menu.get_main_menu_option().lower()

            if main_menu == 'a': # add new entry
                self.entry_menu()

            elif main_menu == "b": # search menu
                self.search_menu()

            elif main_menu == "c": # quit
                menu.show_quit_msg()
                self.to_csv()
                break


if __name__ == "__main__":
    work_log = WorkLog()
    work_log.start()
