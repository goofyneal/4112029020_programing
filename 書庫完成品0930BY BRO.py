import 書庫模組0930完成品 as im


def main():
    while True:
        print("進銷貨系統")
        print("1.新增書籍: ")
        print("2.借閱書籍: ")
        print("3.查看庫存: ")
        print("4.還書: ")
        print("5.退出: ")
        choice = input("請選擇操作: ")

        if choice == "1":
            item_name = input("請輸入書名: ")
            quantity = int(input("請輸入加入書籍數量: "))
            author = input("請輸入作者: ")
            date = input("請輸入出版日期: ")
            
            im.add_item(item_name, quantity, author, date)

        elif choice == "2":
            item_name = input("請輸書籍名稱: ")
            quantity = int(input("請輸入借閱數量: "))
            im.remove_item(item_name, quantity)

        elif choice == "3":
            im.view_inventory()

        elif choice == "4":
            item_name = input("歸還書籍名稱: ")
            quantity = int(input("歸還書籍的數量: "))
            im.return_item(item_name, quantity)

        elif choice == "5":
            print('退出')
            break


if __name__ == "__main__":
    main()
