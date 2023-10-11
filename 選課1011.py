# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class course:
    def __init__(self,name,id,time,teacher):
        self.name=name
        self.id=id
        self.time=time
        self.teacher=teacher

   
    
def add_course():
      while True:
        x=input('請輸入要加入課程name or id:')
        if x=='c':
          print('結束123')
          break
        else:
          for i in range(len(courses)):
            if x==courses[i].name or x==str(courses[i].id):
              print(f"加入課程:{courses[i].name}  課程代碼:{courses[i].id}  課程時間:{courses[i].time}  老師:{courses[i].teacher}")
              print(courses[i].name) 
              schdule.append(courses[i].name)
              print(f"目前課程{schdule}") 
              
def remove():
    while True:
        r=input('請輸入要刪除課程name or id:')
        if r=='c':
          print('結束123')
          break
        else:
          for i in range(len(courses)):
            if r==courses[i].name or r==str(courses[i].id):              
             print(f"即將刪除課程:{courses[i].name}  課程代碼:{courses[i].id}  課程時間:{courses[i].time}  老師:{courses[i].teacher}")
             schdule.remove(courses[i].name)
             print(f"目前課程{schdule}")
             
schdule=[]        
courses=[]    
def view(self):
  for i in range(len(courses)):
    print(f"{i+1},{courses[i].name},{courses[i].id},{courses[i].time},{courses[i].teacher}")        

class student:
  def __init__(self,name,id):
    self.name=name
    self.id=id


students=[]    
def watch(self):
  for a in range(len(students)):
      print({a+1},{students[a].name},{students[a].id})









while True:
  n=input('課程name:')
  if n=='c':
    print('結束')
    break
  i=int(input('課程id:'))
  if i>10000:
    i=int(input('id只能輸入4碼,請再輸入一次'))
  t=input('上課時間time:')
  tc=input('授課老師teacher:')
  courses.append(course(n,i,t,tc))
  view(courses)

while True:
  sn=input('student name:')
  if sn=='c':
    print('結束')
    break
  sid=int(input('student id:'))
  if sid>10000000000:
    sid=int(input('學號不得超過十碼'))
  elif sid<1000000000:
    sid=int(input('學號需要十碼'))
  sn=sn.title()
  students.append(student(sn,sid))
  watch(students)
add_course()
remove()