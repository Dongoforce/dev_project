import csv
from .models import User
import datetime
from errors import errors
import pandas as pd

CHUNK_SIZE = 1000


def header_finder(header, atr_name):
    if atr_name in header:
        return header.index(atr_name)
    else:
        return errors['MISSING ' + atr_name]


def csv_parser(file):
    header = file.readline().decode('UTF-8')[:-2]
    dialect = csv.Sniffer().sniff(header, [' ', ',', ';'])
    header = header.split(dialect.delimiter)
    normal_header = ['name', 'surname', 'birth_date', 'position']
    header_indexes = []

    for atr in normal_header:
        temp = header_finder(header, atr)
        if temp < 0:
            return temp
        else:
            header_indexes.append(temp)

    reader = pd.read_csv(file, chunksize=CHUNK_SIZE, encoding='utf-8', sep=dialect.delimiter, header=None)

    for df in reader:
        users = []
        for it, row in df.iterrows():
            row_list = list(row)
            try:
                birth_date_user = datetime.datetime.strptime(row_list[header_indexes[2]], "%Y-%m-%d").date()
            except:
                return errors['WRONG birth_data']

            name_user = row_list[header_indexes[0]]
            surname_user = row_list[header_indexes[1]]
            position_user = row_list[header_indexes[3]]

            if len(name_user) > 30:
                return errors['WRONG name LENGTH']
            if len(surname_user) > 60:
                return errors['WRONG surname LENGTH']
            if len(position_user) > 60:
                return errors['WRONG position LENGTH']

            user = User(name=name_user, surname=surname_user,
                        birth_date=birth_date_user,
                        position=position_user)
            users.append(user)
        User.objects.bulk_create(users)
