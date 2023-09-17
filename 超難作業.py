def circle_area_and_circle_perimeter(radius):
    return 3.14159*radius**2,radius*2*3.14159

def square_area_and_square_perimeter(length):
    return length**2,length*4

def triangle_area_and_triangle_perimeter(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**1/2,s*2
#不會用迴圈 還在研究
#我還沒領悟demain()的用法
enter=input("請輸入選項")
print(enter)
if enter=='1':
    r=float(input("輸入半徑"))
    print(circle_area_and_circle_perimeter(r))

elif enter=="2":
   len=float(input("輸入長度"))
   print(square_area_and_square_perimeter(len))

elif enter=="退出":
    print("感謝使用")

elif enter=="3":
    a=float(input("輸入第一邊"))
    b=float(input("輸入第二邊"))
    c=float(input("輸入第三邊"))
    list=[a,b,c] 
    list.sort()
    x=list[2]
    if a+b+c-2*x>0:#符合三角定理
        print (triangle_area_and_triangle_perimeter(a,b,c))
    else:
        print("這不是三角形") 

        
       

