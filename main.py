import os
import time
import datetime

####################### BACKGROUND

class User:

    new_id = 0

    @staticmethod
    def get_id():
        User.new_id += 1
        return User.new_id

    def __init__(self, name, address):
        self.id = User.get_id()
        self.name = name
        self.address = address
        self.plates = []

    def add_plate(self, plate_id):
        self.plates.append(plate_id)

    def remove_plate(self, plate_id):
        self.plates.remove(plate_id)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, address: {self.address}, plates: {self.plates}"

class UserTable:
    def __init__(self):
        self.users = dict()

    def find_number(self,number_id):

        for id,user in self.users.items():
            if number_id  in user.plates:
                return id

    def add_user(self, name, address):
        user = User(name, address)
        id = user.id
        self.users[id] = user
    def sell_number(self,raqam_id):
        id = self.find_holder(raqam_id)
        self.users[id].remove_plate(raqam_id)

    def buy_number(self,user_id,number_id):
        self.users[user_id].add_plate(number_id)

    def get_users(self):
        return self.users

user_table = UserTable()

class Sales:
    new_id=0
    @staticmethod
    def get_id():
        Sales.new_id+=1
        return Sales.new_id
    def __init__(self,raqam,foy_id):
        self.id=Sales.get_id()
        self.raqam=raqam
        self.foy_id=foy_id
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')       
    def __str__(self):
          return f"id: {self.id}, raqam: {self.raqam}, foydalanuvchi id si: {self.foy_id}, sanasi: {self.date}"
        
class SalesTable:
    def __init__(self):
        self.sales=dict()
    def add_sales(self,raqam,foy_id):
        sale=Sales(raqam,foy_id)
        id=sale.id
        self.sales[id]=sale
    def get_sales(self):
        return self.sales
sales_table=SalesTable()
class NumberTable:
    @staticmethod
    def get_id():   
        Sales.new_id+=1
        return Sales.new_id
    def __init__(self):
        self.numbers=dict()
        
    def add_number(self,number):
        self.numbers[number.id]=number
    def get_numbers(self):
        return self.numbers

# number va number tablelarni yaratib olish, status = available
# make_available va make_sold funksiyalarini yozish, change_price

###########################  LINKER
def chiqish():
    exit()

def add_user():
    name = input("Ismingizni kiriting: ")
    address = input("Manzilingizni kiriting: ")
    user_table.add_user(name, address)
    print(f"{name} muvafaqqiyatli qo'shildi")

def show_users():
    users = user_table.get_users()

    print("Userlar:")
    for id, user in users.items():
        print(f"\t{user}")

def add_sales():
    user_id=input("User id si:")
    raqam=input("Sotib oladigon raqamingiz:")



    sales_table.add_sales(user_id,raqam)

def show_sales():
    sales=sales_table.get_sales()
    for sale in sales.values():
        print(f"\t {sale}")


###########################  INTERFACE

def clear():
    os.system('cls')

def wait():
    time.sleep(1.1)

def cont():
    input("Davom etish uchun enter bosing...")

while True:

    clear()

    print("0. Exit")
    print("1. Foydalanuchini qushish")
    print("2. Foydalanavchilar ro'yxatini ko'rish")
    print("3. Yangi raqam ni sotuvga quyish")
    print("4. Sotuvdagi raqamlarni ko'rish")
    print("5. Raqam sotib olish")
    print("6. Raqamni narxini o'zgartirish")
    print("7. Raqamni sotuvga quyish")
    print("8. Raqamni sotuvdan olish")
    print("9. Raqamni o'chirish")
    print("10.Sotuvlar tarixini ko'rish")

    print()

    operation = input("Amalni tanlang: ")

    print()

    if operation == '0':
        chiqish()
    elif operation == '1':
        add_user()
    elif operation == '2':
        show_users()
    elif operation == '3':
        add_sales()
    elif operation == '4':
        pass
    elif operation == '5':
        pass
    elif operation == '6':
        pass
    elif operation == '7':
        pass
    elif operation == '8':
        pass
    elif operation == '9':
        pass
    elif operation == '10':
        show_sales()
    else:
        print(f"Noto'g'ri amal tanlangan -> {operation}")

    print()
    wait()
    cont()
