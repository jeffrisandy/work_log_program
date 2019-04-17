import datetime
import re
import csv


class Log:
    """
    Log Class : base class that connect to database (csv file), add, remove and update logs,
    and also have functions to search the log

    """

    def __init__(self):
        """ Initialization that read the csv database and convert it to dictionary """
        self.db = {}

        with open('data.csv', newline="") as File:
            reader = csv.reader(File)

            for i, row in enumerate(reader):
                if i == 0:
                    continue
                else:
                    row[0] = datetime.datetime.strptime(row[0], "%d/%m/%Y")
                    self.db[i] = row

    def add(self, dates, title, time_spent, notes):
        """
        This function is to add log to the database, db
        :param dates: datetime object
        :param title: string
        :param time_spent: int
        :param notes: string
        :return: None
        """
        index = len(self.db) + 1
        self.db[index] = [dates, title, time_spent, notes]

    def remove_by_index(self, index):
        """
        Remove log, based on given index
        :param index: int
        :return: None
        """
        del self.db[index]
        print("Log data deleted.")

    def find_by_exact(self, string):
        """
        Finding in log database that match the string
        :param string: string
        :return: list of log index (int) that match the string
        """
        result = []
        for i, data in self.db.items():
            if string in str(data[1:]):
                result.append(i)
        return result

    def find_by_regex(self, pattern):
        """
        Finding in log database that match regex pattern
        :param pattern: regex pattern
        :return: list of log index (int) that match the pattern
        """
        result = []
        for i, data in self.db.items():
            if re.search(pattern, str(data[1:])):
                result.append(i)
        return result

    def find_by_date(self, date):
        """
        Finding in log database that match the given date
        :param date: datetime object
        :return: list of log index (int) that match the date
        """
        result = []
        for i, data in self.db.items():
            if data[0] == date:
                result.append(i)
        return result

    def find_by_range_date(self, start_date, end_date):
        """

        :param start_date: datetime object
        :param end_date: datetime object
        :return: list of log index (int) within the start & end date
        """
        result = []
        for i, data in self.db.items():
            if (data[0] >= start_date) & (data[0] <= end_date):
                result.append(i)
        return result

    def get_log(self, index):
        """
        Get the log data given the log index
        :param index: int, log index
        :return: tuples of date, title, time_spent, notes
        """
        date, title, time_spent, notes = self.db[index]
        return date, title, time_spent, notes

    def update_log(self, index, date, title, time_spent, notes):
        """
        update the log database
        :param index: int
        :param date: datetime object
        :param title: string
        :param time_spent: int
        :param notes: string
        :return: None
        """
        self.db[index] = [date, title, time_spent, notes]

    def to_csv(self):
        """
        Write the database to csv. It is performed after quitting the program
        :return: None
        """
        data = [['date', 'title', 'time_spent', 'notes']]

        for k, v in self.db.items():
            v[0] = datetime.datetime.strftime(v[0], "%d/%m/%Y")
            data.append(v)

        with open('data.csv', 'w', newline="") as myFile:
            writer = csv.writer(myFile)
            writer.writerows(data)
