book=[
    {"name":"book1","price":100},
    {"name":"book2","price":200},
    {"name":"book3","price":300},
    {"name":"book4","price":400}
]


order=[
    {"name":"book1","quantity":1},
    {"name":"book2","quantity":2},
    
]
price=0
for buy in order:
    for sale in book:
        
        if buy["name"]== sale["name"]:
            price=price+sale["price"]*buy["quantity"]
            
            if price>100:
                print(price*0.7)
            else:
                    print(price)
