books=[
    {"name":"coding" ,"price":1, "quantity":1},
    {"name":"calculus" ,"price":2 ,"quantity":2},
    {"name":"computers" ,"price":3, "quantity":2},
    {"name":"english" , "price":4 ,"quantity":2}
]

while True:
    print(f"輸入1:購買\n輸入2:刪除\n輸入3:更新書庫\n輸入4:顯示庫存\n輸入5:退出")

    click=input("輸入1.2.3.4.5")
    if click=="1":
        add_book={"書名":"","價格":"","庫存":""}
        add_book["書名"]=input("輸入名稱")
        add_book["價格"]=input("輸入價格")
        add_book["庫存"]=input("輸入數量")
        books.append(add_book)
        print(f"成功加入{add_book}")
        continue

    elif click=="2":
        delete=input("輸入欲刪除書籍")
        for book in books:
            if delete==book["name"]:
                books.remove(book)
                print(f"成功刪除{delete}")

    elif click=="3":
        renew=  input("輸入欲更新書籍")
        for book in books:
            if book["name"]==renew:
                number=int(input("更新後的數量"))
                book["quantity"]=number
                print(f"書籍{renew}庫存已經改成{number}本")

    elif click=="4":
        check=input("輸入欲查詢書籍")
        for book in books:
           
            if  book["name"]==check:
                print(f"名稱:{book['name']}",f"{book['price']}元",f"{book['quantity']}本")

    elif click =="5":
        print("結束")
        break
    else:
        print("error")
        continue
    

    
