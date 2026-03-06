"""
#STUDENT Management System

Student => (sid,sname,class,age)
Subject => (sid,sname,Hindi,English,Maths,Science,S.S.T,Sanskrit,Total,Percentage,Grades)

Add student records
View all students
Delete student
Update student detail
Student's Result
View all Student's Result
Search A student


"""
import pickle
import os
# A METHOD TO ADD A STUDENT
def addStudentRecords():

    file = open('Student.bin','ab')
    sid = input("\n\tEnter New Student ID :")
    sname = input("\tEnter Student Name : ")
    classs = input("\tEnter class : ")
    age = input("\tEnter Student AGE : ")
    pickle.dump(sid,file)
    pickle.dump(sname,file)
    pickle.dump(classs,file)
    pickle.dump(age,file)
    file.close()
    print("\n\tSTUDENT ADDED SUCCESSFULLY!")
    input("\tPRESS ENTER TO CONTINUE.....")


#A METHOD TO VIEW ALL STUDENTS   
def viewStudents():
    file = open('Student.bin','rb')
    try:
        print("SID\tSNAME\tClass\tAGE")
        while True:
            for x in range(4):
                data = pickle.load(file)
                print(data,end="\t")
            print()
    except:
        pass
    file.close()
    print("\n\tVIEW ALL STUDENTS SUCCESSFULLY!")
    input("\tPRESS ENTER TO CONTINUE....")



#A METHOD TO DELETE A STUDENT   
            
def deleteStudent():
    file = open('Student.bin','rb')
    file2 = open('tem.bin','ab')
    flag = 0
    sid = input("\n\tEnter Students ID TO DELETE : ")
    try:
        while True:
            data = pickle.load(file)
            if data==sid:
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
                flag =1
            else:
                pickle.dump(data,file2)
                
    except:
        pass
    file.close()
    file2.close()
    os.remove('Student.bin')
    os.rename('tem.bin','Student.bin')
    if flag==1:
        print("\n\tSTUDENT DELETE SUCCESSFULLY!")
    else:
        print("\n\tSTUDENT NOT FOUND!")
    input("\tPRESS ENTER TO CONTINUE....")
              


#A METHOD TO UPDATE STUDENT DETAIL                  
def updateStudentDetail():
    file = open('Student.bin','rb')
    file2 = open('temp.bin','ab')
    sid = input("\n\tEnter Students ID :")
    flag = 0
    try:
        while True:
            data = pickle.load(file)
            if sid==data:
                pickle.dump(data,(file2))
                name = pickle.load(file)
                print("\n\tName:",name)
                pickle.dump(name,file2)
                cls = pickle.load(file)
                print("\n\tClass:",cls)
                pickle.dump(cls,file2)
                print("\n\tAGE:",pickle.load(file))
                age = input("\n\tEnter New AGE :")
                pickle.dump(age,file2)
                flag = 1
            else:
                pickle.dump(data,file2)


    except:
        pass
    file.close()
    file2.close()
    os.remove('Student.bin')
    os.rename('temp.bin','Student.bin')
    if flag==1:
        print("\n\tAGE Updated successfully!")
    else:
        print("\n\tAGE Not Found!")
    input("\tPRESS ENTER TO CONTINUE....")


    

#A METHOD TO ADD STUDENT 'S RESULT

def StudentsResult():
    file = open('StudentResult.bin','ab')
    sid = input("\n\tEnter New Student ID :")
    sname = input("\tEnter New Student Name :")
    hindi = float(input("\tEnter marks for hindi :" ))
    english = float(input("\tEnter marks for English  :" ))
    maths = float(input("\tEnter marks for maths:" ))
    science = float(input("\tEnter marks for science :" ))
    s_s_t = float(input("\tEnter marks for s_s_t :" ))
    sanskrit = float(input("\tEnter marks for snaskrit :" ))
    total = hindi+english+maths+sciense+s_s_t+sanskrit
    percentage = total/600*100
    if percentage>=90:
         grades = "A+"
    elif percentage>=80:
         grades = "A"
    elif percentage>=70:
         grades = "B+"
    elif percentage>=60:
          grades = "B"
    elif percentage>=50:
         grades = "C+"
    elif percentage>=45:
         grades = "C"
    else:
        grades = "D"
    pickle.dump(sid,file)
    pickle.dump(sname,file)
    pickle.dump(hindi,file)
    pickle.dump(english,file)
    pickle.dump(maths,file)
    pickle.dump(sciense,file)
    pickle.dump(s_s_t,file)
    pickle.dump(sanskrit,file)
    print("\n\tTotal Marks :", total)
    pickle.dump(total,file)
    print("\tPercentage :", percentage)
    pickle.dump(percentage,file)
    print("\tGrades :", grades)
    pickle.dump(grades,file)

    
    file.close()
    print("\n\tResult add Successfully! : ")
    input("\tPRESS ENTER TO CONTINUE... ")

    
#A METHOD TO VIEW ALL STUDENT RESULT

    
def viewstudentresult():
        file = open('StudentResult.bin','rb')
        try:
            print("SID\tSNAME\tHINDI\tENGLISH\tMATHS\tSCIENSE\tS_S_T\tSANSKRIT\tTOTAL\tPERCENTAGE\tGRADES")
            while True:
                for x in range(11):
                    data = pickle.load(file)
                    print(data,end="\t")
                print()
        except:
            pass
        file.close()
        print("\n\tVIEW STUDENTS RESULT SUCCESSFULLY!:")
        input("\tPRESS ENTER TO CONTINUE....")


#A METHOD TO GET STUDENT       
        
def getStudent(sid):
    st = []
    file = open('Student.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==sid:
                st.append(data)
                for x in range(3):
                    st.append(pickle.load(file))

    except:
        pass
    file.close()
    return st



def getStudentresult(sid):
    result = []
    file = open('StudentResult.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==sid:
                result.append(data)
                for z in range(11):
                    result.append(pickle.load(file))
    except:
        pass
    file.close()
    return result

#A METHOD TO SEARCH A STUDENT RESULT       
    
def searchAstudent():
    sid = input("\n\tEnter A Student ID : ")
    st = getStudent(sid)
    if len(st)!=0:
        file = open('StudentResult.bin','rb')
        try:
            print("\n\tHERE IS A STUDENT RESULT\n")
            while True:
                st = getStudent(pickle.load(file))
                result = getStudentresult(pickle.load(file))
                if len(st)!=0:
                    if st[0]==sid:
                        print("\n\tSID :",st[0])
                        print("\tSNAME :",st[1])
                        print("\tCLASS :",st[2])
                        print("\tAGE :",st[3])
                        print("\tHINDI :",result[1])
                        print("\tENGLISH :",result[2])
                        print("\tMATHS :",result[3])     
                        print("\tSCIENcE :",result[4])
                        print("\tS_S_T :",result[5])
                        print("\tSANSKRIT :",result[6])
                        print("\tTOTAL :",result[7])
                        print("\tPERCENTAGE :",result[8])
                        print("\tGRADES :",result[9])
                        print("\n-----------------------")
        except:
            pass
    else:
        print("\n\tSTUDENT NOT FOUND ON THIS ID:")
    file.close()
    input("\n\tPRESS ENTER TO CONTINUE....")
                      
                              
                              





print("\tSTUDENT MANAGEMENT SYSTEM")

while True:
    print("\t-------------------------")
    print("""      1-Add student records
      2- View all students
      3- Delete student
      4- Update student detail
      5- Student's Result
      6- View all Student result 
      7- Search a student
      0- Exit
    """)
    ch = int(input("Enter your choice :"))
    if ch==0:
       print("\n\tThank you ")
    elif ch==1:
        addStudentRecords()
    elif ch==2:
        viewStudents()
    elif ch==3:
        deleteStudent()
    elif ch==4:
        updateStudentDetail()
    elif ch==5:
        StudentsResult()
    elif ch==6:
        viewstudentresult()
    elif ch==7:
        searchAstudent()
    else:
        input("\n\tWRONG CHOICE\n\tTRY AGAIN!")
        
    
            
        



