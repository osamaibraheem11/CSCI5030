import sys
import csv
from logic import SQL_log

read_csv = csv.reader(open("tests/sql_log_test.csv",encoding = "utf8" ))
for row in read_csv: 
   test_value, answer = row
   logic.SQL_log(test_value)
