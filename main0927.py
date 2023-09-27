

import inventory_module as im

def main():
    while True:
        print("進銷貨系統"/n)
        print("1.新增物品")
        print("2.移除物品")
        print("3.查看庫存")
        print("4.退出")
        choice=input("請選擇操作")

        if choice=="1":
            item_name=input("請輸入物品名稱")
            quantity=int(input("請輸入數量"))
            im.add_item(item_name,quantity)

        elif choice=="2":
            item_name=input("請輸入物品名稱")
            quantity=int(input("請輸入數量"))
            im.remove_item(item_name,quantity)

        elif choice=="3":
            im.view_inventory()

        elif choice=="4":
            break
if __name__ == "__main__":
    main()