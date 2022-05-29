Libraries required:
  1. Colorama:
     >> To print colored text in terminal window.
     >> Install command: pip install colorama
   
  2. SQLite3:
     >> To handle database.
     >> Comes pre-installed with Python
  
  3. Difflib:
     >> To get close match of any name(here it is car name).
     >> Comes pre-installed with Python
  
  4. Datetime:
     >> To add date and time.
     >> Comes pre-installed with Python.
  
  5. OS:
     >> To interact with operating system.
     >> Comes pre-installed with Python.
  

Steps to install libraries:
  1. Open command prompt.
  2. Enter install commands to install that library.


Create a database in Sqlite Studio:
	Syntax: 
		>> Create Table Users(
		      	  Name Text,
			  Aadhar Integer Unique,
			  Mobile Integer Unique,
			  Car Text,
			  Date Blob
			  )

		>> Create Table Cars(
		          Name Text,
			  Available Integer Default 0
			  )
	
	>> If any change is made here make sure to the same in Code.
