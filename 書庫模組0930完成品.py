inventory = {}


def add_item(item_name, quantity, author, date):
    if item_name in inventory:
        inventory[item_name]['quantity'] += quantity
    else:
        inventory[item_name] = {
            'quantity': quantity,
            'author': author,
            'date': date,

        }


def remove_item(item_name, quantity):
    if item_name in inventory and 'quantity' in inventory[item_name]:
        if inventory[item_name]['quantity'] >= quantity:
            inventory[item_name]['quantity'] -= quantity
            if inventory[item_name]['quantity'] == 0:
                del inventory[item_name]
        else:
            print("庫存不足或物品不存在")
    else:
        print("物品不存在")


def view_inventory():
    if not inventory:
        print("NONE")
    else:
        for item_name, details in inventory.items():
            if item_name not in ["Author_", "Date_"]:
                quantity = details['quantity']
                author = details['author']
                date = details['date']
                print(f"書名: {item_name}, 作者: {author}, 出版日期: {date}, 剩餘庫存: {quantity}本")


def return_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name]['quantity'] += quantity
    else:
        print("找不到此書")

