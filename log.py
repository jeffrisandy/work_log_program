import datetime
import re
import csv


class Log:
    def __init__(self):
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
        # return self.db.append([dates, title, time_spent, notes])
        index = len(self.db) + 1
        self.db[index] = [dates, title, time_spent, notes]

    def remove_by_index(self, index):
        del self.db[index]
        print("Log data deleted.")

    def find_by_exact(self, string):
        result = []
        for i, data in self.db.items():
            if string in " ".join(data[1:]):
                result.append(i)
        return result

    def find_by_regex(self, pattern):
        result = []
        for i, data in self.db.items():
            if re.search(pattern, " ".join(data[1:])):
                result.append(i)
        return result

    def find_by_date(self, date):
        result = []
        for i, data in self.db.items():
            if data[0] == date:
                result.append(i)
        return result

    def find_by_range_date(self, start_date, end_date):
        result = []
        for i, data in self.db.items():
            if (data[0] >= start_date) & (data[0] <= end_date):
                result.append(i)
        return result

    def get_log(self, index):
        date, title, time_spent, notes = self.db[index]
        return date, title, time_spent, notes

    def edit_log(self, index, date, title, time_spent, notes):
        self.db[index] = [date, title, time_spent, notes]

    def to_csv(self):

        data = [['date', 'title', 'time_spent', 'notes']]

        for k, v in self.db.items():
            v[0] = datetime.datetime.strftime(v[0], "%d/%m/%Y")
            data.append(v)

        with open('data.csv', 'w', newline="") as myFile:
            writer = csv.writer(myFile)
            writer.writerows(data)