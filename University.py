from ast import Break, Pass
from cv2 import bilateralFilter
import mysql.connector

class University:
    def __init__(self,name,country) :
        self.name=name
        self.country=country
        self.status=True
        self.connectDatabase()

    def run(self):
        self.menu()
        self.status=False
        choice= self.choice()

        if choice ==1:
            self.addStudent()
        if choice ==2:
            self.deleteStudent()
        if choice ==3:
            self.updateStudent()
        if choice ==4:
            self.showAllStudent()
        if choice ==5:
            pass

    def menu(self):
        print("******* EMİR UNIVERSITY *******".format(self.name))  
        print("\n1)Add Student\n2)Delete Student\n3)Update Student\n4)Show All  Students\n5)EXIT")

    def choice(self):
        while True:
            try:
                process=int(input("Select: "))
                if process<1 or process>5:
                    print("Operation number must be between 1-5 !!")
                    continue
                break
            except ValueError:
                print("Operation is must be integer number!!")    
        return process

    def addStudent(self):
        print("****Student Information****")
        name=input("Student's Name: ").lower().capitalize()        
        faculty=input("Student's Faculty: ").lower().capitalize()
        department=input("Student's Department: ").lower().capitalize()
        stid=input("Student's ID: ")

        while True:
            try:
                typ=int(input("Student's Education Type: "))
                if typ<1 or typ>2:
                    print("Student's Education type must be 1 or 2.")
                    continue
                break
            except ValueError:
                print("Type must be integer\n")  
        status="Active"
        sql = "INSERT INTO students (name,faculty,department,stid,typ,status) VALUES(%s, %s, %s, %s, %s, %s)"
        val = [name,faculty,department,stid,typ,status]
        self.cursor.execute(sql,val)
        self.connect.commit() 
        print("The student named {} succesfully added.".format(name))       
        
        

        
    def deleteStudent(self):
        self.cursor.execute("SELECT * FROM students")
        allStudents=self.cursor.fetchall()

        convertallString=lambda x:[str(y) for y in x]

        for i,j in enumerate(allStudents,1):
            print("{}){}".format(i," ".join(convertallString(j))))

        while True:   
            try: 
                select=int(input("Select the student to be deleted(Stid): "))
                break
            except ValueError:
                print("Please write correct type(int)")

        self.cursor.execute("DELETE FROM students WHERE stid={}".format(select))
        self.connect.commit()
        print("\n Student succesfully deleted.")

    def updateStudent(self):
        self.cursor.execute("SELECT * FROM students")
        allStudents=self.cursor.fetchall()

        convertallString=lambda x:[str(y) for y in x]

        for i,j in enumerate(allStudents,1):
            print("{}){}".format(i," ".join(convertallString(j))))

        while True:   
            try: 
                select=int(input("Select the student to be updated(Stid): "))
                break
            except ValueError:
                print("Please write correct type(int)")

        while True:
            update_select=input("\n1)Name\n2)Faculty\n3)Department\n4)Student ID\n5)Education\n6)Status\n").lower()    

            if update_select=="typ":
                while True:
                    try:
                        newValue=input("Enter the value: ")
                        if newValue not in (1,2):
                            continue
                        break

                    except ValueError:
                        print("It must be integer.")     
                self.cursor.execute("UPDATE students SET typ='{}' where stid='{}'".format(update_select,select))
            else:
                newValue=input("Enter the value:")
                self.cursor.execute("UPDATE students SET {}='{}' WHERE stid='{}'".format(update_select,newValue,select))

            self.connect.commit()    
            print("Update Success")
            break
                
                 
    def showAllStudent(self):
            student=input("Please write the student you want to see:")

            # self.cursor.execute("SELECT * FROM students")
            # allStudents=self.cursor.fetchall()

            # convertallString=lambda x:[str(y) for y in x]

            # for i,j in enumerate(allStudents,1):
            #     print("{}){}".format(i," ".join(convertallString(j))))

            self.cursor.execute("SELECT * FROM students WHERE name='{}'".format(student))
            pstudent=self.cursor.fetchall()
            print(pstudent)
                
        

    def systemExit(self):
        self.status=False

    def connectDatabase(self):
        self.connect=mysql.connector.connect(
            host="localhost" ,
            user="root",
            password="1234",
            database="university"
        )
        self.cursor=self.connect.cursor()
        self.cursor.execute("CREATE TABLE if not exists students(name VARCHAR(255),faculty VARCHAR(255),department VARCHAR(255),stid VARCHAR(255),typ INT,status VARCHAR(255))")
        self.connect.commit()
        

    

UNI=University("EMİR UNIVERSITY","TÜRKİYE")    

while UNI.status:
    UNI.run()