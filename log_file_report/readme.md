# Log File Report

[LogFile_Report.py](https://github.com/Alejandro-ZZ/Automation-with-Python/blob/master/log_file_report/LogFile_Report.py) generates two CSV files as a report 
from a regular system log file. Example:

## INPUT

[System Log File](https://github.com/Alejandro-ZZ/Automation-with-Python/blob/master/log_file_report/syslog.txt)

![logfile](https://user-images.githubusercontent.com/71833624/182030966-18f538fe-9716-4a9c-a3b1-2c56159d0427.png)

## OUTPUT

- [**CSV error report**](https://github.com/Alejandro-ZZ/Automation-with-Python/blob/master/log_file_report/error_message.csv): All type of errors and the count of each.

![Error_report](https://user-images.githubusercontent.com/71833624/182031007-48e007d7-886b-40b8-bad0-399de4a1d88d.png)


- [**CSV user report**](https://github.com/Alejandro-ZZ/Automation-with-Python/blob/master/log_file_report/user_statistics.csv): All usernames and log count of type INFO and ERROR.

![User_report](https://user-images.githubusercontent.com/71833624/182031016-daa58164-2bcd-480e-b342-4fb0668ec620.png)
