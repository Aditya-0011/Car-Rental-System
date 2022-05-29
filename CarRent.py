from difflib import get_close_matches
from colorama import Fore
from datetime import *
import time
from os import system
import sqlite3

def CarRent():

    conn = sqlite3.connect('Database.sqlite')
    cur = conn.cursor()

    try:
        def ShowServices(n): 
            try:
                print(Fore.GREEN + "\nSevices Available:-" + Fore.RESET)
                
                print(Fore.GREEN + '''
                1. Display Cars available.
                2. Rent a Car.
                3. Return Rented Car.
                4. Show Customer details.
                5. Exit.''' + Fore.RESET)

                s = int(input(Fore.YELLOW + "Enter Option to access the Services: " + Fore.RESET))
                return service(n,s)
            
            except ValueError:
                print(Fore.RED + "\nOptions entered should be integers" + Fore.RESET)
                return ShowServices(n)

        def service(n,s):

            if s == 1:
                return CurrentCar(n,k)
        
            elif s == 2:
                cur.execute('''Select * From Cars Where Available = 0''')
                row = cur.fetchone() 

                if row == None:
                    print(Fore.RED + "\nNo car is available to rent. Please check later." + Fore.RESET)
                    input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                    return ShowServices(n)
                
                cur.execute('''Select * From User Where Aadhar = ?''',(n,))
                row = cur.fetchone()

                if row[3] == "No Car rented":
                    w = int(input(Fore.YELLOW + "\nPlease Check Cars available if not. To dispaly cars available enter 0 else 1 to continue. Enter 2 to return to Services' menu: " + Fore.RESET))
                    return Rent(n, w)
                
                else:
                    print(Fore.RED + "\nOnly 1 car can be rented on each Aadhar Number." + Fore.RESET)
                    
                    input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                    return ShowServices(n)
        
            elif s == 3:
                cur.execute('''Select * From User Where Aadhar = ?''',(n,))
                row = cur.fetchone()
                
                if row[0]== "No Car rented":
                    print(Fore.RED + "\nService not Available." + Fore.RESET)
                    
                    input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                    return ShowServices(n)
                
                else:
                    rentedCar(n)
        
            elif s == 4:
                userDetails(n)

            elif s == 5:
                print(Fore.GREEN + '\nThanks for using our Services\n' + Fore.RESET)
                time.sleep(5)
                system('cls') 
                return CarRent()

            else:
                c = int(input(Fore.RED + "\nEnter correct Options: " + Fore.RESET))
                return service(n,c) 
            


        def CurrentCar(n, k):

            cur.execute('''Select * From Cars Where Available = 0''')
            row = cur.fetchone() 

            if row == None:
                print(Fore.RED + "\nNo car is available to rent. Please check later." + Fore.RESET)
                input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                return ShowServices(n)
            
            else:
                print("Cars available are: ")
                cur.execute("Select Name From Cars Where Available = 0")
                for car in cur:
                    print(Fore.CYAN + car[0])
                
                input(Fore.GREEN + "\nPress Enter to continue.\n" + Fore.RESET)
                
                if k == 1:
                    return Rent(n, 1)
                
                else:
                    return ShowServices(n)


        def Rent(n, w):
            try:
                if w == 0:
                    k = 1
                    return CurrentCar(n, k)
            
                elif w == 1:
                    car = input(Fore.YELLOW + "\nEnter Car Name to continue else 1 to return to Services' menu: " + Fore.RESET)
                    
                    if car == '1':
                        return ShowServices(n)
                    
                    else:    
                        return Pay(car, n)

                elif w == 2:
                    return ShowServices(n)
            
                else:
                    c = input(Fore.RED + "\nEnter correct Options: " + Fore.RESET)
                    return Rent(n, c)
                
            except ValueError:
                print(Fore.RED + "\nOptions entered should be integers\n" + Fore.RESET)
                w = int(input(Fore.RED + "\nPlease Check Cars available if not. To dispaly cars available enter 0 else 1 to continue. Enter 2 to return to Services' menu: " + Fore.RESET))
                return Rent(n, w)


        def Pay(car, n):
            cur.execute('''Select Name From Cars Where Available = 0''')
            find = []
            
            for cAr in cur: 
                find.append(cAr[0])
            
            if car in find:
                day = int(input(Fore.YELLOW + "\nEnter no. of days: " + Fore.RESET))
                returnDay = str(date.today() + timedelta(days=day))

                if day <= 15 and day >= 1:
                    bill = day*2000 + 2000
                    confirm = input(Fore.RED + "\nWrite 'CONFIRM' to confirm booking: \n" + Fore.RESET).upper()
                
                    if confirm == "CONFIRM":
                        print(Fore.RED + "\nBooking Confirmed. Bill:" + Fore.RESET, " ₹", bill, sep='')
                        print(Fore.RED + "\nDate to return Car:" + Fore.RESET, returnDay)
                        input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                
                    else:
                        return Pay(car, find, n)
                    return afterPay(car, n, returnDay)
                
                elif day > 15:
                    bill = day*1800 + 2000
                    confirm = input(Fore.RED + "\nWrite 'CONFIRM' to confirm booking: " + Fore.RESET).upper()
                
                    if confirm == "CONFIRM":
                        print(Fore.RED + "\nBooking Confirmed. Bill:" + Fore.RESET, " ₹", bill, sep='')
                        print(Fore.RED + "\nDate to return Car:" + Fore.RESET, returnDay)
                        input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                
                    else:
                        return Pay(car, find, n)
                    return afterPay(car, n, returnDay)
                
                else:
                    print(Fore.RED + "\nNo. of days should be greater than 0\n" + Fore.RESET) 
                    return Pay(car, find, n)
            else:
            
                close = (get_close_matches(car,find))
                
                if close == []:
                    print(Fore.RED + "\nCar doesn't not exist. Again enter car name" + Fore.RESET)
                    return CurrentCar(n,1)
                
                else:  
                    print(Fore.RED + "\nIs car name:" + Fore.RESET,close)
                    
                    c = input(Fore.YELLOW + "\nEnter Yes(Y) or No(N): " + Fore.RESET)
                    
                    if c == 'Y' or c == 'y':
                        car = car.join(close)
                        return Pay(car, n)
                    
                    elif c == 'N' or c == 'n':
                        print(Fore.RED + "\nAgain enter car name\n" + Fore.RESET)
                        return CurrentCar(n,1)
                    
                    else:
                        print(Fore.RED + "\nRespond with Y or N\n" + Fore.RESET)
                        return Pay(car, find, n)
            

        def afterPay(car, n, returnDay):    
            cur.execute('''Update Cars
                 Set Available = 1
                 Where Name = ?''', (car,))

            cur.execute('''Update User
                 Set Car = ?,
                     Date = ?
                 Where Aadhar = ?''', (car, returnDay, n))
            conn.commit()
            return ShowServices(n)


        def rentedCar(n):
            cur.execute('''Select * From User Where Aadhar = ?''',(n,))
            row = cur.fetchone()
            
            if row[3] == "No Car rented":
                print(Fore.RED + "Service not Available" + Fore.RESET )
                input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                return ShowServices(n)
            
            else:
                car = input(Fore.YELLOW + "\nEnter Rented Car Name: " + Fore.RESET)
                return returnCar(car, n)


        def returnCar(car, n):
            cur.execute('''Select Name From Cars Where Available = 1''')
            find = []
            
            for cAr in cur: 
                find.append(cAr[0])

            if car in find:
                cur.execute('''Select * From User Where Aadhar = ?''', (n,))
                row = cur.fetchone()
                chkDate = row[4]
                
                if str(date.today()) > chkDate:
                    print(Fore.RED + "\nCar returned past due date.\n" + Fore.RESET)
                
                if row[3] == car:
                    print(Fore.GREEN + "\nCar returned successfully. Your refund will be proceeded after inspection of car\n" + Fore.RESET)
                    cur.execute('''Update Cars
                        Set Available = 0
                        Where Name = ?''', (car,))

                    cur.execute('''Update User
                        Set Car = ?,
                            Date = ?
                        Where Aadhar = ?''', ("No Car rented", "No due date", n))
                    conn.commit()
                    return ShowServices(n)
                
                else:
                    print(Fore.RED + "\nEntered car is not rented by you. Please enter car name again.\n" + Fore.RESET)
                    return rentedCar(n)
            
            else:
                close = get_close_matches(car, find)
                
                print(Fore.RED + "\nIs car name: " + Fore.RESET,close)
                
                c = input(Fore.YELLOW + "\nEnter Yes(Y) or No(N): " + Fore.RESET)
            
                if c == 'Y' or c == 'y':
                    car = car.join(close)
                    return returnCar(car, n)
            
                elif c == 'N' or c == 'n':
                    print(Fore.RED + "\nAgain enter car name\n" + Fore.RESET)
                    return rentedCar(n)
            
                else:
                    print(Fore.RED + "\nRespond with Y or N\n" + Fore.RESET)
                    return returnCar(car, find, n)


        def userDetails(n):
            
            cur.execute('''Select * From User Where Aadhar = ?''',(n,))
            row = cur.fetchone()

            print(Fore.GREEN + "\nCustomer Details:-" + Fore.RESET)
            print(Fore.GREEN + "Name:" + Fore.RESET, row[0])
            print(Fore.GREEN + "Aadhar Number:" + Fore.RESET, row[1])
            print(Fore.GREEN + "Mobile Number:" + Fore.RESET, row[2])
            print(Fore.GREEN + "Car currently rented:" + Fore.RESET, row[3])
            print(Fore.GREEN + "Due Date:" + Fore.RESET, row[4])
    
            chkDate = row[4]
            
            if str(date.today()) > chkDate:
                print(Fore.RED + "\nReturn Date is past due date.\n" + Fore.RESET)
            
            input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
            return ShowServices(n)


        def RegisterUser():

            Name = input(Fore.YELLOW + "\nEnter Full Name: " + Fore.RESET)
            
            k = 0
            while k != 1:
                try:
                    mobile = int(input(Fore.YELLOW + "\nEnter Mobile Number: " + Fore.RESET))
                    if (len(str(mobile)) != 10):
                        print(Fore.RED + "\nMobile Number must be of 10 digits.")
                        time.sleep(5)
                        system('cls')
                        return CarRent()
                    
                    cur.execute('''Select * From User Where Mobile = ?''',(mobile,))
                    row = cur.fetchone()
                    if row != None:
                        print(Fore.RED + "\nCustomer already exist\n" + Fore.RESET)
                        input(Fore.CYAN + "Press Enter to continue.\n" + Fore.RESET)
                        time.sleep(5)
                        system('cls')
                        return CarRent()
                    
                    else:
                        k = 1

                
                except ValueError:
                    print(Fore.RED + "\nMobile Number must be of 10 digits and an integer\n" + Fore.RESET)
                    time.sleep(5)
                    system('cls')
                    return CarRent()
            
            k = 0
            while k != 1:
                try:
                    Ano = int(input(Fore.YELLOW + "\nEnter Aadhar Number: " + Fore.RESET))
                    
                    if (len(str(Ano)) != 12):
                        print(Fore.RED + "\nAadhar Number must be of 12 digit.")
                        time.sleep(5)
                        system('cls')
                        return CarRent()
                        
                    cur.execute('''Select * From User Where Aadhar = ?''',(Ano,))
                    row = cur.fetchone()
                    if row != None:
                        print(Fore.RED + "\nCustomer already exist\n" + Fore.RESET)
                        input(Fore.CYAN + "Press Enter to continue.\n" + Fore.RESET)
                        time.sleep(5)
                        system('cls')
                        return CarRent()
                    
                    else:
                        k = 1

                        
                except ValueError:
                    print(Fore.RED + "\nAadhar Number must be of 12 digits and an integer\n" + Fore.RESET)
                    time.sleep(5)
                    system('cls')
                    return CarRent()

            cur.execute('''Insert Into User (Name, Aadhar, Mobile, Car, Date)
                Values( ?, ?, ?, ?, ? )''', (Name, Ano, mobile, "No Car rented", "No due date"))
            
            print(Fore.RED + "\nCustomer Registered.\n" + Fore.RESET)
            print(Fore.GREEN + "\nCustomer Details:-" + Fore.RESET)
            print(Fore.GREEN + "Name:" + Fore.RESET,Name)
            print(Fore.GREEN + "Aadhar Number:" + Fore.RESET,Ano)
            print(Fore.GREEN + "Mobile Number:" + Fore.RESET,mobile)
            print(Fore.GREEN + "Car currently rented:" + Fore.RESET, "No Car rented")
            print(Fore.GREEN + "Due Date:" + Fore.RESET, "No due date")
            input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
            
            conn.commit()
            return Ano


        def RegisteredUser():
            try:
                Ano = int(input(Fore.YELLOW + "\nEnter Aadhar Number: " + Fore.RESET))

                cur.execute('''Select * From User Where Aadhar = ?''',(Ano,))
                row = cur.fetchone()
                if row != None:
                    print(Fore.GREEN + "\nCustomer Details:-" + Fore.RESET)
                    print(Fore.GREEN + "Name:" + Fore.RESET, row[0])
                    print(Fore.GREEN + "Aadhar Number:" + Fore.RESET, row[1])
                    print(Fore.GREEN + "Mobile Number:" + Fore.RESET, row[2])
                    print(Fore.GREEN + "Car currently rented:" + Fore.RESET, row[3])
                    print(Fore.GREEN + "Due Date:" + Fore.RESET, row[4])
            
                    chkDate = row[4]
                    
                    if str(date.today()) > chkDate:
                        print(Fore.RED + "\nReturn Date is past due date.\n" + Fore.RESET)
                    
                    input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)
                    return Ano
                
                else:
                    print(Fore.RED + "\nCustomer not found. Aadhar Number must be of 12 digits and an integer." + Fore.RESET)
                    input(Fore.CYAN + "\nPress Enter to continue.\n" + Fore.RESET)

                    system('cls')
                    return CarRent()


            except ValueError:
                print(Fore.RED + "\nAadhar Number must be an integer." + Fore.RESET)
                time.sleep(5)
                system('cls')
                return CarRent()

        print("\t"*5, Fore.RED + "-"*20,"Welcome to Car Rents Pvt Limited","-"*20 + Fore.RESET)

        print(Fore.GREEN + """
        Price:
        ₹2000 per day if car is booked for less than or equal to 15 days + ₹2000 Caution Money.
        ₹1800 per day if car is booked for more than 15 days + ₹2000 Caution Money.\n""" + Fore.RESET,
        Fore.LIGHTRED_EX + """
        1. Caution Money includes damages to vehicle and late return of vehicle and will be refunded after complete inspection of rented vehicle.
        2. Only 1 car can be rented on each Aadhar Number.
        3. Press Ctrl + C to exit at any moment.
        """ + Fore.RESET)

        input(Fore.CYAN + "Press Enter to continue." + Fore.RESET)

        Customer = input(Fore.YELLOW + "\nAre you registered customer?(Y/N): " + Fore.RESET)

        if (Customer == 'Y') or (Customer == 'y'):
            n = RegisteredUser()

        elif (Customer == 'N') or (Customer == 'n'):
            n = RegisterUser()

        else:
            print(Fore.RED +  "\nRespond with Y or N\n" + Fore.RESET)
            system('cls')
            return CarRent()

        k = 0
        ShowServices(n)
    
    except KeyboardInterrupt:
        exit()

system('cls')
CarRent()