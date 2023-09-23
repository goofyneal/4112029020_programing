book=[
    {"name":"1","price":100},
    {"name":"2","price":200},
    {"name":"3","price":300},
    {"name":"4","price":400}
]
order=[
    {"name":"1","quantity":0},
    {"name":"2","quantity":0},
    {"name":"3","quantity":0},
    {"name":"4","quantity":0}
]
stock=[
    {"name":"1","remain":10},
    {"name":"2","remain":20},
    {"name":"3","remain":30},
    {"name":"4","remain":40}
]
sum=0
while True :
    x=(input("請輸入你要購買書籍的編號:"))
    
    if x=="0":
       print(sum)
       break
    else:
        y=(input("請輸入你要購買書籍的數量:"))  
        
        for name in order:
            if x==name["name"]:
                name["quantity"]=int(y)
        for buy in book:
            for name in order:
                if buy["name"]==name["name"]:
                    total=buy["price"]*name["quantity"]
                    sum+=total
                                
                    
                    
print(f"你結束購買,總價為{sum}")

