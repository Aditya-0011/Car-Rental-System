# Car Rental System using Python and SQLite

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
     <a href = "#Libraries-required">Libraries required</li>
     <ul>
     <li>Colorama</li>
     <li>Sqlite3</li>
     <li>Difflib</li>
     <li>Datetime</li>
     <li>OS</li>
     </ul>
    </li>
    <li>
      <a href="#Steps-to-install-libraries">Steps to install libraries</a>
    </li>
    <li>
    <a href="#Steps-to-create-database">Steps to create database</a>
    </li>
  </ol>
</details>

## Libraries required
 ### __Colorama__  
   1. To print colored text in terminal window.  
   2. Install command:
      ```sh 
      pip install colorama
      ```      
  ### __SQLite3__  
   1. To connect database.  
   2. Comes pre-installed with Python. 
   
 ### __Difflib__  
   1. To get close match of any name(here it is car name).  
   2. Comes pre-installed with Python.  
    
    
 ### __Datetime__  
   1. To add date and time.  
   2. Comes pre-installed with Python.   
   
   
 ### __OS__  
   1. To interact with operating system.  
   2. Comes pre-installed with Python.  
    
   <p align="right">(<a href="#top">back to top</a>)</p>

## Steps to install libraries
  <ol type = "1">
  <li>Open command prompt.</li>  
  <li>Enter install commands to install that library.</li>
  </ol>
  
   <p align="right">(<a href="#top">back to top</a>)</p>
 
 ## Steps to create database
  <b>You need to create a database for first time in SQLite Studio</b>
  - <a href="https://github.com/pawelsalawa/sqlitestudio/releases/download/3.4.0/SQLiteStudio-3.4.0-windows-x64-installer.exe">Click to install SQLite Studio</a>
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
       
  <blockquote><b>If you change the names of columns in either of the tables make sure to do the same in <a href="https://github.com/Aditya-0011/Car-Rental-System/blob/main/CarRent.py">CarRent.py</a></b></blockquote>
 
 <p align="right">(<a href="#top">back to top</a>)</p>
