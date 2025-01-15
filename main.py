import os
import time
import datetime
import json
import pickle


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
        if plate_id not in self.plates:
            self.plates.append(plate_id)
            print(f"Raqam {plate_id} foydalanuvchiga qo‘shildi.")
        else:
            print(f"Raqam {plate_id} allaqachon foydalanuvchiga tegishli.")
   
    def remove_plate(self, plate_id):
        self.plates.remove(plate_id)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, address: {self.address}, plates: {self.plates}"

class UserTable:
    def __init__(self):
        self.users = dict()

    def input(self, text):
        id = int(input(text))
        if id not in self.users:
            print("Bunday foydalanuvchi mavjud emas")
            return
        return id
   

    def find_holder(self,number_id):

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
        self.sell_number(number_id)
        self.users[user_id].add_plate(number_id)
    def add_number(self,user_id,number_id):
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

class Number:
    new_id=0
    AVAILABLE='Mavjud'
    SOLD='Sotilgan'
    @staticmethod
    def get_id():   
        Number.new_id+=1
        return Number.new_id
    def __init__(self,price):
        self.id=Number.get_id()
        self.numbers=dict()
        self.price=price
        self.holat=Number.AVAILABLE
    def __str__(self):
        return f"id: {self.id}, narx: {self.price}, holat: {self.holat}"
        
class NumberTable:
    def __init__(self):
        self.numbers=dict()
    def check_id(self, text):
        id = int(input(text))
        if id not in self.numbers:
            print(f"Bunday raqam id si {id} mavjud emas")
            return
        return id
    def add_number(self,number,price):
        number=Number(price)
        self.numbers[number.id]=number
        print(f"Raqam ID: {number.id} va narxi: {number.price} qo'shildi.")
        return number.id
    def get_numbers(self):
        return self.numbers
    def make_available(self,number_id):
        if number_id in self.numbers:
            if self.numbers[number_id].holat == Number.SOLD:
                self.numbers[number_id].holat = Number.AVAILABLE
                print(f"Raqam ID: {number_id} sotuvga qaytarildi.")
            else:
                print(f"Raqam ID: {number_id} sotuvga qo'yilmagan.")
        else:
            print(f"Raqam ID: {number_id} topilmadi.")
    def make_sold(self,number_id):
        if number_id in self.numbers:
             self.numbers[number_id].holat=Number.SOLD
             print(f"Raqam {number_id} sotildi.")
        else:
            print(f"Raqam ID: {number_id} topilmadi.")
    def change_price(self,number_id,new_price):
            
            if number_id in self.numbers:
                self.numbers[number_id].price=new_price
                print("Raqam narxi o'zgartirildi")
            else:
                print(f"Ushbu {number_id} dagi raqam topilmadi")
    def delete_number(self, number_id):
        if number_id in self.numbers:
            del self.numbers[number_id]
        else:
            print(f"Raqam {number_id} topilmadi")
number_table=NumberTable()


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
    user_id=user_table.input("User id si:")
    if user_id==None:
        return
    raqam=input("Sotib oladigon raqamingiz:")
    sales_table.add_sales(user_id,raqam)

def show_sales():
    sales=sales_table.get_sales()
    for sale in sales.values():
        print(f"\t {sale}")

def add_number():
    user_id=user_table.input("Foydalanuvchi id si :")
    if user_id==None:
        return
    number=input("Sotuvga quyadigon raqamingiz:")
    price=float(input("Raqamning narxini kiriting:"))
    number_id = number_table.add_number(number,price)
    user_table.add_number(user_id,number_id)
    print(f"Raqam {price} narx bilan sotuvga quyildi !")


def show_number():
    numbers=number_table.get_numbers()
    print("Sotuvdagi raqamlar: \n")
    for id, number in numbers.items():
        print(f"{number}")
def buy_number():
    user_id=user_table.input("Foydalanuvchi id sini kiriting:")
    if user_id==None:
        return
    number_id=number_table.check_id("Sotib olishni istagan raqamingiz id si:")
    if number_id==None:
        return
    if number_id in number_table.numbers:
        if number_table.numbers[number_id].holat==Number.AVAILABLE:
            sales_table.add_sales(number_id,user_id)
            number_table.make_sold(number_id)
            user_table.buy_number(user_id,number_id)
            print(f"Raqam ushbu id {number_id} foydalanuvchiga sotildi")
        else:
            print(f"Bu id {number_id} dagi raqam sotib olingan")
    else:
        print(f"Bu raqam id  {number_id} topilmadi")
def delete_number():
    number_id=number_table.check_id("O'chirmoqchi bulgan raqamingizni id raqami:")
    if number_id==None:
        return
    number_table.delete_number(number_id)
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
    print("1. Foydalanuvchini qo'shish")
    print("2. Foydalanuvchilar ro'yxatini ko'rish")
    print("3. Yangi raqamni sotuvga qo'yish")
    print("4. Sotuvdagi raqamlarni ko'rish")
    print("5. Raqam sotib olish")
    print("6. Raqam narxini o'zgartirish")
    print("7. Raqamni sotuvga qo'yish")
    print("8. Raqamni sotuvdan olish")
    print("9. Raqamni o'chirish")
    print("10. Sotuvlar tarixini ko'rish")

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
        add_number()
    elif operation == '4':
        show_number()
    elif operation == '5':
        buy_number()
    elif operation == '6':
        number_id=int(input("Narxni uzgartirmoqchi bulgan raqam id si:"))
        number_table.check_id("Narxni o'zgartirmoqchi bulgan raqamingiz id raqami:")
        if number_id==None:
            break
        new_price=int(input("Yangi narxni kiriting: "))
        number_table.change_price(number_id,new_price)
    elif operation == '7':
         number_id = int(input("Sotuvdan olishni istagan raqamning ID sini kiriting: "))
         number_table.make_available(number_id)
    elif operation == '8':
        pass
    elif operation == '9':
        delete_number()
    elif operation == '10':
        show_sales()
    else:
        print(f"Noto'g'ri amal tanlangan -> {operation}")

    print()
    wait()
    cont()
