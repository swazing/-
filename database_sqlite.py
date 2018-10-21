import sqlite3,traceback
def create_table(db):
 try:
     conn=sqlite3.connect(db+'.db')
     print("Open database successfully")
     cur=conn.cursor()
     cur.execute('''
     CREATE TABLE COMPANY
     (ID INT PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     AGE INT NOT NULL,
     ADDRESS CHAR(50),
     SALARY REAL);
     ''')
     print("create table successfully")
     conn.commit()
     conn.close()
 except sqlite3.OperationalError:
     print('database:'+db+"  already exists")
def delete_database_table(db):
    conn=sqlite3.connect(db+'.db')
    print("Connecting database successfully! ")
    cur=conn.cursor()
    cur.execute('''
    DROP TABLE COMPANY;
    ''')
    print("succ")
    conn.commit()
    conn.close()

def insert_item(db):
 try:
     conn = sqlite3.connect(db + '.db')
     print("connecting database successfully!")
     cur=conn.cursor()
     id=int(input("ID:"))
     name=input('NAME:')
     age=int(input("AGE:"))
     address=input("ADDRESS:")
     salary=int(input("SALARY:"))
     info="INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES("+str(id)+','+"'"+name+"'"+','+str(age)+','+"'"+address+"'"+','+str(salary)+')'
     cur.execute(info)
     conn.commit()
     print("insert successfully!")
     conn.close()
 except sqlite3.IntegrityError:
     print("键值限制，已经存在了")
if __name__ == '__main__':
    name=input("the name of database:")
    #create_table(name)
    #delete_database(name)
    insert_item(name)