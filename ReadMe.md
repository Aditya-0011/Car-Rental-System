Car Rental System using Python and SqLite
=========================================

Libraries required
-------------------
- __Colorama__  
   1. To print colored text in terminal window.  
   2. Install command:  ```pip install colorama``` 

- __SQLite3__  
   1. To handle database.  
   2. Comes pre-installed with Python.

- __Difflib__  
   1. To get close match of any name(here it is car name).  
   2. Comes pre-installed with Python.

- __Datetime__  
   1. To add date and time.  
   2. Comes pre-installed with Python. 

- __OS__  
   1. To interact with operating system.  
   2. Comes pre-installed with Python. 

Steps to install libraries
---------------------------
  ```
  1. Open command prompt.  
  2. Enter install commands to install that library.
  ```
You need to create a database for first time in SQLite Studio
--------------------------------------------------------------
  - [Click to install SQLite Studio](https://github.com/pawelsalawa/sqlitestudio/releases/download/3.4.0/SQLiteStudio-3.4.0-windows-x64-installer.exe)
  - SQLite syntax to create database
    - To create User table:
      ```
        Create Table Users(
                Name Text,
                Aadhar Integer Unique,
                Mobile Integer Unique,
                Car Text,
                Date Blob
                )
       ```
     - To create Car Availability table:
       ```
          Create Table Cars(
                  Name Text,
                  Available Integer Default 0
                  )
       ```
       
      > __If you change the names of columns in either of the tables make sure to do the same in [CarRent.py](https://github.com/Aditya-0011/Car-Rental-System/blob/main/CarRent.py)__
 
