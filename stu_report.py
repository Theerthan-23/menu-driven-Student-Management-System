student={
    "Ajay" : [97,76,88],
    "Vikruth" : [69,79,87]
}
def add_stu(n):                                              #Adding a new student
    mark=[]
    name=input("Enter the name: ")
    for i in range(1,4):
        m=int(input(f"Enter {i}th subject mark: "))
        mark.append(m)
         
    n[name]=mark
    print("List got updated!!!")
    print(n)

def update_name(stu):                                        #Changing the name of a student
    n1=input("Enter the old name: ")
    if n1 in stu:
        n2=input("Enter the new name: ")
        stu[n2]=stu[n1]
        del stu[n1]
        print("Name is updated!!")
    else:
        print("Name",n1,"does not exist")


def update_marks(stu):                                        #Updating the marks of a student
    n1=input("Enter the student name: ")
    if n1 in stu:
        print(stu[n1])
        marked=stu[n1]
        sub=int(input("Which subjects mark should be updated whether 1,2 or 3: "))
        if 1 <= sub <=3:
            ma=int(input("Enter the marks: "))
            marked[sub-1]=ma
        else:
                      print("Enter the corrrect subject number")

    else: 
            print("Name",n1,"does not exist")

def report(abc):                                             #Report of every student
      lis=[]
      for key,value in abc.items():
         total=0
         for i in range(0,len(value)):
              total+=value[i]

         avg=total/len(value)
         if avg>=90:
              gr="A"
         elif avg>=80:
              gr="B"
         else:
              gr="C"

         rep=(key,total,avg,gr)
         lis.append(rep)
      lis.sort(key=lambda x:x[2],reverse=True)
      for j in lis:
           print("Name: ",j[0])
           print("Total: ",j[1])
           print("Average: ",j[2])
           print("Grade: ",j[3])
           print("\n")

def parti(xyz):                                             #Report of a particular student
    na=input("Enter the name: ")
    tot=0
    if na in xyz:
            m=xyz[na]
            for i in range(0,len(m)):
                tot+=m[i]
            av=tot/len(m)
            if av>=90:
                g="A"
            elif av>=80:
                g="B"
            else:
                g="C"

            print("Name: ",na)
            print("Total: ",tot)
            print("Average: ",av)
            print("Grade: ",g)
    else:
            print("Student",na,"does not exist....")           

while True: 
    print("Menu: \n1.Add a new student\n2.Changing the name of a student\n3.Updating the marks of a student\n4.Report of every student\n5.Report of a particular student\n6.Exit")
    inp=int(input("Enter your choice: "))
    match inp:
        case 1:
          add_stu(student)
        case 2:
          update_name(student)
        case 3:
          update_marks(student)
        case 4:
          report(student)
        case 5:
          parti(student)
        case 6:
          print("Exitinggg....")
          exit()
        case _:
          print("Invalid choice")