from commodity import Commodity
from commodityBuy import CommodityBuy
import datetime

admin_username = "admin"
admin_password = "admin"

buyer_username = "1234"
buyer_password = "1234"

commodity_list = list()
commodity_list.append(Commodity("milk", "001", 100, 50, datetime.datetime(1401, 12, 2), 20000))
commodity_list.append(Commodity("sugar", "002", 80, 30, datetime.datetime(1401, 11, 23), 23000))
commodity_list.append(Commodity("book", "003", 34, 6, datetime.datetime(1401, 11, 12), 40000))
commodity_list.append(Commodity("rice", "004", 67, 23, datetime.datetime(1401, 10, 2), 78000))
commodity_list.append(Commodity("chips", "005", 53, 35, datetime.datetime(1402, 12, 6), 99000))
commodity_list.append(Commodity("salt", "006", 16, 10, datetime.datetime(1401, 8, 26), 82000))
commodity_list.append(Commodity("paper", "007", 86, 9, datetime.datetime(1401, 4, 13), 14000))
commodity_list.append(Commodity("fish", "008", 46, 5, datetime.datetime(1402, 7, 25), 45000))
commodity_list.append(Commodity("ice cream", "009", 24, 23, datetime.datetime(1401, 12, 2), 64000))
commodity_list.append(Commodity("meat", "011", 79, 9, datetime.datetime(1401, 12, 2), 67000))

def admin_page():

    while True:
        print("---------------")
        print("1- list of all commodity")
        print("2- define today date")
        print("3- search commodity by code")
        print("4- edit count of commodity")
        print("5- commodity list sort by price")
        print("6- exit")
        print("---------------")

        n = int(input("enter command: "))

        if n == 6:
            break

        elif n == 1:

            for item in commodity_list:
                print(item)

        elif n == 2:

            date = input("define today date")

        elif n == 3:

            code = input("enter code: ")
            for item in commodity_list:
                if item.code == code:
                    print(item)
                    break

        elif n == 4:

            code = input("enter code : ")
            count = int(input("enter count : "))
            for item in commodity_list:
                if item.code == code:
                    item.count = count
                    print("edited")
                    break

        elif n == 5:
            commodity_list.sort(key=lambda x: x.price)
            for item in commodity_list:
                print(item)

def buyer_page():

    basket_list = list()

    while True:
        print("wellcome to shop")
        print("1- show Commodity")
        print("2- add Commodity to invoice")
        print("3- show invoice")
        print("4- invoice verify")
        print("5- exit")
        print("-----------------")
        n = int(input("enter command: "))

        if n == 1:

            for item in commodity_list:
                print(item)

        elif n == 2:

            if len(basket_list) < 4:
                code = input("enter code : ")
                count = int(input("enter count : "))
                for item in commodity_list:
                    if item.code == code:
                        if item.expired_time < datetime.datetime.now():

                            commodity = CommodityBuy(item.name, code, count, (count * item.price))
                            basket_list.append(commodity)

                        else:
                            print("this Commodity is expired")
            else:
                print("your basket is full")

        elif n == 3:

            for item in basket_list:
                print(item)

        elif n == 4:

            print("your basket list : ")
            for item in basket_list:
                print(item)

            print("--------------")
            address = input("enter your address :")
            phone = input("enter your phone :")

            print("your buy is complete")

        elif n == 5:
            break




if __name__ == "__main__":

    while True:
        print("enter username : ")
        username = input()
        print("enter password : ")
        password = input()

        if username == admin_username and password == admin_password:
            admin_page()
        elif username == buyer_username and password == buyer_password:
            buyer_page()




