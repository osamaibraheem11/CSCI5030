import sys
import csv
import logic

read_csv = csv.reader(open("sql_log_test.csv",encoding = "utf8" ))
for row in read_csv: 
   test_statement, answer_statement, test_status, answer_status, test_type, answer_type = row
   