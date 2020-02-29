import csv
import io
from .models import User
import datetime


def csv_parser(file):
    data_set = file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    reader = csv.reader(io_string, delimiter=',', quotechar='|')
    users = []
    header = next(reader)
    print(header)
    for line in reader:
        user = User(name=line[0], surname=line[1], birth_date=datetime.datetime.strptime(line[2], "%Y-%m-%d").date(),
                    position=line[3])
        users.append(user)
    User.objects.bulk_create(users)
