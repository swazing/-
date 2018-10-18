import  sys,copy,ex1,re,time,fileinput,shelve,traceback
from random import *
from pprint import pprint
def store_person(db):
    """
    让用户输入数据并且存储到
    :param db:
    :return:
    """
    pid=input("enter unique ID number :")
    person={}
    person['name']=input("enter name:")
    person['age']=input("enter age:")
    person['phone']=input("enter phone number:")
    db[pid]=person
def lookiup_person(db):
    pid=input("enter ID number:")
    field=input("what u want to know(name,age,phone):")
    field=field.strip().lower()
    print(field.capitalize()+':',db[pid][field])

def findall_message(db):
    pid=input("enter ID:")
    c=db[pid]
    print('name:',db[pid]['name'])
    print('age',db[pid]['age'])
    print('phone',db[pid]['phone'])
def main():
    database=shelve.open('test.bat')
    while True:
     try:
      while True:
       c=input("你想干啥(1.store;2.check;3.check_all;4.quit)：")
       if c=='1':
        store_person(database)
       elif c=='2':
        lookiup_person(database)
       elif c=='3':
        findall_message(database)
       elif c=='4':
         return
     except KeyError:
        print('错了哦')
if __name__=="__main__":
    main()