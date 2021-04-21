import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import csv
import logic


def write_2_log_test():
   read_csv = csv.reader(open("tests/sql_log_test.csv",encoding = "utf8" ))
   for row in read_csv: 
      test_statement, answer_statement, test_status, answer_status, test_purpose, answer_purpose = row
      logic.SQL_log(test_statement,test_status,test_purpose)
      rows_SQL_log = list(csv.reader(open("SQL-Scripts/sql_log.csv")))
      last_row = rows_SQL_log[-1]
      log_statement, log_time, log_status,log_purpose = last_row
      if log_statement == answer_statement and log_status == answer_status and log_purpose == answer_purpose:
         print('Pass')
      else:
         print('Fail')


write_2_log_test()