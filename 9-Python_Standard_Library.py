# 9-2 Working with Paths
# from pathlib import Path

# path = Path("8-Modules/ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# path.name
# print('path.name: ', path.name)
# print('path.stem: ', path.stem)
# print('path.suffix: ', path.suffix)
# print('path.parent: ', path.parent)
# a = path.with_name("file.py")
# b = path.with_suffix(".txt")
# print('a: ', a)
# print('b: ', b)


# 9-3 Working with Directories
# from pathlib import Path
# path = Path("8-Modules/ecommerce/")
# # print('path: ', path)
# # # path.exists()
# # # path.mkdir()
# # # path.rmdir()
# # # path.rename("ecommerce2")

# # print('path.iterdir(): ', path.iterdir())
# # for p in path.iterdir():
# #     print(p)

# # paths = [p for p in path.iterdir() if p.is_dir()]
# # print('paths: ', paths)

# py_files = [p for p in path.rglob("*.py")]
# print('py_files: ', py_files)


# 9-4 Working with Files
# from pathlib import Path
# # from time import ctime
# import shutil


# # path = Path("8-Modules/ecommerce/__init__.py")

# # c_time = ctime(path.stat().st_ctime)
# # print('c_time: ', c_time)

# # text = print(path.read_text())
# # print('text: ', text)

# source = Path("8-Modules/ecommerce/__init__.py")
# target = Path() / "__init__.py"
# shutil.copy(source, target)


# 9-5 Working with Zip Files
# from pathlib import Path
# from zipfile import ZipFile

# # with ZipFile("file.zip", "w") as zip:
# #     for path in Path("8-Modules/ecommerce").rglob("*.*"):
# #         zip.write(path)

# with ZipFile("file.zip") as zip:
#     zip.namelist()
#     info = zip.getinfo('8-Modules/ecommerce/__init__.py')
#     print('info.file_size: ', info.file_size)
#     print('info.compress_size: ', info.compress_size)
#     zip.extractall("extract")


# 9-6 Working with CSV Files
# import csv

# # with open("data.csv", "w") as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["transaction_id", "product_id", "price"])
# #     writer.writerow([1000, 1, 5])
# #     writer.writerow([1001, 2, 15])

# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # list(reader)
#     # print('list(reader): ', list(reader))
#     for row in reader:
#         print('row: ', row)


# 9-7 Working with JSON Files
# import json
# from pathlib import Path

# # movie = [
# #     {"id": 1, "title": "Terminator", "year": 1989},
# #     {"id": 2, "title": "Kindergarten Cop", "year": 1990},
# # ]

# # data = json.dumps(movie)
# # Path("movies.json").write_text(data)


# data = Path("./movies.json").read_text()
# movies = json.loads(data)
# print('movies: ', movies)


# 9-8 Working with a SQLite Database
# import sqlite3
# import json
# from pathlib import Path

# # movies = json.loads(Path("movies.json").read_text())

# # with sqlite3.connect("db.sqlite3") as conn:
# #     command = "INSERT INTO Movies VALUES(?, ?, ?)"
# #     for movie in movies:
# #         conn.execute(command, tuple(movie.values()))

# #         conn.commit()

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "SELECT * FROM Movies"
#     cursor = conn.execute(command)
#     # for row in cursor:
#     #     print(row)
#     movies = cursor.fetchall()
#     print('movies: ', movies)


# 9-9 Working with Timestamps
# import time
# time.time()
# print('time.time(): ', time.time())


# def send_email():
#     for i in range(1000):
#         pass


# start = time.time()
# send_email()
# end = time.time()
# duration = end - start
# print('duration: ', duration)


# 9-10 Working with DateTimes
# from datetime import datetime
# import time

# dt1 = datetime(2018, 1, 1)
# dt2 = datetime.now()
# dt3 = datetime.strptime("2018/01/01", "%Y/%m/%d")  # <- datetime object
# dt3_strf = dt3.strftime("%Y/%m")  # <- String
# ct = dt3.ctime()
# dt4 = datetime.fromtimestamp(time.time())

# print('dt1: ', dt1)
# print('dt2: ', dt2)
# print('dt3: ', dt3)
# print('ct: ', ct)
# print('dt4: ', dt4)
# print(f"{dt4.year}/{dt4.month}")
# print('dt3_strf: ', dt3_strf)
# print('dt2 > dt1: ', dt2 > dt1)


# 9-11 Working with Time Deltas
# from datetime import datetime, timedelta

# dt1 = datetime(2018, 1, 1)
# dt2 = datetime.now()
# dt3 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)

# duration = dt2 - dt1
# print('duration: ', duration)
# print('duration.days: ', duration.days)
# print('duration.seconds: ', duration.seconds)
# print('duration.total_seconds(): ', duration.total_seconds())

# print('dt1: ', dt1)
# print('dt3: ', dt3)


# 9-12 Generating Random Values
# import random
# import string

# random.random()
# print('random.random(): ', random.random())
# print('random.randint(1,10): ', random.randint(1, 10))
# print('random.choice([ 1, 2, 3, 4, 5 ]): ', random.choice([1, 2, 3, 4, 5]))
# print(
#     'random.choices([ 1, 2, 3, 4, 5 ], k=2): ',
#     random.choices([1, 2, 3, 4, 5], k=2)
# )

# print(
#     'random.choices("abcdefghijk", k=4): ',
#     random.choices("abcdefghijk", k=4)
# )
# print(
#     '"".join(random.choices("abcdefghijk", k=4)): ',
#     "".join(random.choices("abcdefghijk", k=4))
# )


# print('string.ascii_letters: ', string.ascii_letters)
# print('string.digits: ', string.digits)

# print(
#     '"".join(random.choices(string.ascii_letters + string.digits, k=4)): ',
#     "".join(random.choices(string.ascii_letters + string.digits, k=4))
# )

# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print('numbers: ', numbers)


# 9-13 Opening the Browser
# import webbrowser

# webbrowser.open("http://google.com")


# 9-14 Sending Emails, 9-15 Templates
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from pathlib import Path
# from email.mime.image import MIMEImage
# from email.mime.text import MIMEText
# from string import Template

# template = Template(Path('template.html').read_text())

# message = MIMEMultipart()
# message["from"] = "Mosh Hamedani"
# message["to"] = "s.hyodo@vegibus.co.jp"
# message["subject"] = "This is a test..."
# body = template.substitute({"name": "John"})
# message.attach(MIMEText(body, "html"))
# # message.attach(MIMEImage(Path("mosh.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo
#     smtp.starttls()
#     smtp.login (
#         "masamichi.kagaya.contact.form@gmail.com",
#         "masamimicontactform33333"
#     )
#     smtp.send_message(message)
#     print("Sent...")


# 9-16 Command-line Arguments
# import sys

# if len(sys.argv) == 1:
#     print("USAGE : python3 app.py <password>")

# else:
#     password = sys.argv[1]
#     print('Password: ', password)


# 9-17 Running External Programs
import subprocess

# compiled = subprocess.run(["ls", "-l"],
#                           capture_output=True,
#                           text=True)
# print('args: ', compiled.args)
# print('returncode: ', compiled.returncode)
# print('stderr: ', compiled.stderr)
# print('stdout: ', compiled.stdout)

# compiled = subprocess.run(["python3", "other.py"],
#                           capture_output=True,
#                           text=True)
# print('args: ', compiled.args)
# print('returncode: ', compiled.returncode)
# print('stderr: ', compiled.stderr)
# print('stdout: ', compiled.stdout)

try:
    compiled = subprocess.run(["false"],
                              capture_output=True,
                              text=True,
                              check=True)
    print('args: ', compiled.args)
    print('returncode: ', compiled.returncode)
    print('stderr: ', compiled.stderr)
    print('stdout: ', compiled.stdout)
except subprocess.CalledProcessError as ex:
    print('ex: ', ex)
