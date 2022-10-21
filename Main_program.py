from datetime import date, datetime
from random import randint
from typing import List

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Vikram-232",
    database="Accounts"
)
mycursor = db.cursor()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>Database Program<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# mycursor.execute("CREATE DATABASE Accounts")
# mycursor.execute("USE Accounts")
# mycursor.execute("INSERT INTO CHILDRENS VALUES (%s,%s)", (''))
# db.commit()
# mycursor.execute("SELECT * FROM CHILDRENS")
#
# for x in mycursor:
#     print(x)
# <<<<<<<<<<<<<<<<<<<<Database Ending>>>>>>>>>>>>>>>>>>>>>>>

# dates = date.datetime.now()

class transaction:
    trans=[]


class Logins:
    Parents: list[str] = ["Richard", "Maya"]
    children = ['Aron', 'James', 'Joe', 'Meghan', 'Niharika', 'Nile', 'Paula', 'Ruhan', 'Xi']


class Password:
    password = 123
password_obj = Password()


class Main_Bank_Account:
    main_bank: int = randint(80000000, 99999999)


class Wallet:
    wallet: int = randint(80000, 99999)



class Accounts:

    def Deposit():
        Password_Check = int(input("Enter the Password to deposit the Money : "))
        if (Password_Check == Password.password):
            k = int(input("Enter the Amount of money you want to deposit :"))
            Main_Bank_Account.main_bank = Main_Bank_Account.main_bank - k
            print(Main_Bank_Account.main_bank)
            Wallet.wallet = Wallet.wallet + k
            print(Wallet.wallet)
        else:
            print("You are not authorised to deposit the money")

    def Withdraw(store):
        Child_name = str(input("Enter your Name:"))
        withdraw_money = int(input("Enter the Amount of money you want to Withdraw :"))
        withdraw_reason = input("why do you want to withdraw money:")
        today = date.today()

        children = ['Aron', 'James', 'Joe', 'Meghan', 'Niharika', 'Nile', 'Paula', 'Ruhan', 'Xi']

        for c in children:
            if Child_name == c:
                flag = 1
                cursor = db.cursor()
                sql_select_query = """select * from Childrens"""
                cursor.execute(sql_select_query)
                record = cursor.fetchall()
                for row in record:
                    if (Child_name == row[0]):
                        if (flag != row[1]):
                            print("You are blocked to do transactions")
                        else:
                            if (withdraw_money > 50):
                                print("You are not allowed to withdraw money above 50$ ask for permission from maya")
                                Parent_name = input("Maya or Richard please provide your name: ")
                                for parents in Logins.Parents:
                                    if (Parent_name == parents):
                                        Password_Check = int(
                                            input("Enter the Password to allow the Money for withdraw :"))
                                        if (Password_Check == Password.password):
                                            print("please enter the Number according to the decision 1.Accept, 2.Transfer Request to dad, 3.Reject")
                                            request = int(input())
                                            if (request == 1):
                                                print("Proceding with the transcation")
                                                Wallet.wallet = Wallet.wallet - withdraw_money
                                                store.trans.append({
                                                    'Child_name': c,
                                                    'Money_withdrawn': withdraw_money,
                                                    'Discription of Money': withdraw_reason,
                                                    'Date_and_Time': today
                                                })
                                                print(Wallet.wallet)
                                            elif (request == 2):
                                                print("Request has been sent to dad")
                                            elif (request == 3):
                                                print("Your request has been rejected")
                                        else:
                                            print("You have entered wrong password")
                            else:
                                Wallet.wallet = Wallet.wallet - withdraw_money
                                store.trans.append({
                                    'Child_name':c,
                                    'Money_withdrawn':withdraw_money,
                                    'Discription of Money':withdraw_reason,
                                    'Date_and_Time':today
                                })
                                print(Wallet.wallet)
                        return True
        else:
            print("You are not a person from Richard and Maya Family")






    def Blocking():
        name = input("Enter the name of child you want to select:")
        flag = 0

        a = "select child from Childrens where child='{}'".format(name)
        mycursor.execute(a)

        data = mycursor.fetchall()

        for i in data:
            if (name != a):
                a1 = "update Childrens set Acc_status='{}' where Child='{}'".format(flag, name)
                mycursor.execute(a1)
                db.commit()
                print("The " + name + " successfully blocked.")
            else:
                print("you have enter the wronged name please try it again")


    def Unblocking():
        name = input("Enter the name of child you want to select:")
        flag = 1

        a = "select child from Childrens where child='{}'".format(name)
        mycursor.execute(a)

        data = mycursor.fetchall()

        for i in data:
            if (name != a):
                a1 = "update Childrens set Acc_status='{}' where Child='{}'".format(flag, name)
                mycursor.execute(a1)
                db.commit()
                print("The " + name + "  successfully unblocked.")
            else:
                print("you have enter the wronged name please try it again")

    def Transactions(store):
        for elem in store.trans:
            print(elem)


    def Parent_Withdraw(store):
        Parent_name = input("Enter your name")
        withdraw_money = int(input("Enter the Amount of money you want to Withdraw :"))
        withdraw_reason = input("why do you want to withdraw money:")
        Password_Check = int(input("Enter the Password to deposit the Money : "))
        if (Password_Check == Password.password):
            Wallet.wallet = Wallet.wallet - withdraw_money
            store.trans.append({
                'Child_name': c,
                'Money_withdrawn': withdraw_money,
                'Discription of Money': withdraw_reason,
                'Date_and_Time': today
            })
            print(Wallet.wallet)
        else:
            print("You are not authorised for transaction")





def mainmenu():
    """ Welcome To The Richard and Maya Family Wallet"""
    store=transaction
    if (Wallet.wallet <= 100):
        print("please add money into the wallet, amount in wallet is less than 100$")
    else:
        pass
    choice = -1
    while choice != 8:
        print('What Would you like to do')
        print('1. Deposit Amount')
        print('2. Child_Withdraw')
        print('3. Block Account')
        print('4. Unblock Account')
        print('5. Parent_withdraw')
        print('6. View Transactions')
        print('8. Exit')
        print()
        choice = int(input('Select Your Option(1-8) : '))

        if choice == 1:
            # clrscr()
            Accounts.Deposit()
        elif choice == 2:
            # clrscr()
            Accounts.Withdraw(store)

        elif choice == 3:
            # clrscr()
            Accounts.Blocking()
        elif choice == 4:
            Accounts.Unblocking()
        elif choice == 5:
            Accounts.Parent_Withdraw(store)
        elif choice == 6:
            Accounts.Transactions(store)

        elif choice == 8:
            pass
        else:
            print('Invalid Option !!!')
            print('Please Select A Valid Option')
            print()
            input('Press Enter To Continue...')

mainmenu()






