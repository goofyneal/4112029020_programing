# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:47:00 2023

@author: User
"""
class purchaseable:
    def purchase(self,quantity,price):
        total_cost=quantity*price
        return total_cost


class spentable:
    def spent(self,purchase):
        total_spent=sum(purchase)
        return total_spent
    
    
class discount:
    def discount_price(self,price,discount_percent):
        discount_total=price*(1-discount_percent/100)
        return discount_total
    
    
class book(purchaseable,spentable,discount):
    def __init__(self,isbn,title,author,price,stock):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.price=price
        self.stock=stock
    def display_info(self):
        return f"Title:{self.title},Author:{self.author},PRICE:{self.price},Stock:{self.stock}"
    
    
book1=book(input("請輸入書籍編號"),input("請輸入書籍名稱"),input("請輸入書籍作者"),int(input("請輸入書籍價格)")),int(input("請輸入庫存")))



purchase_quantity=int(input("請輸入需購買數量"))
unit_price=book1.price
total_cost=book1.purchase(purchase_quantity,unit_price)

purchases=[total_cost]
total_spent=book1.spent(purchases)

discount_percent=int(input("請輸入折扣"))
discounted_price=book1.discount_price(book1.price,discount_percent)

book1.stock-=purchase_quantity

print("BOOK 1 INFO")
print(book1.display_info())

print(f"\nPurchase{purchase_quantity} copies of BOOK1 for {total_cost}.")
print(f"Total spent:{total_spent}.")

print(f"\nDiscounted price of BOOK1 after {discount_percent}% discount:{discounted_price}.")
print(f"庫存為{book1.stock}")