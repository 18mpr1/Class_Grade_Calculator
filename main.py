# My first OOP program
from tkinter import *
import csv

# Root
root = Tk()
root.title("Grade Calculator")

# Labels
root.minsize(300, 300)
root.geometry("600x600")
root.config(bg="#5DADE2")

Title = Label(root, text="Grade Calculator", bg="#EC7063", height='1', font=("Georgia", 26, 'bold'))
Title.grid(column=1, row=0)

class Student:
    def __init__(self, first_name, last_name, number, age, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, Cname, max_students):
        self.Cname = Cname
        self.max_students = max_students
        self.students = []

    def add_student(self, Student):
        if len(self.students) <= self.max_students:
            self.students.append(Student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for Student in self.students:
            value += Student.get_grade()
        return value / len(self.students)


count = 0


def courseWindow():
    newWindow = Toplevel(root)
    newWindow.geometry('950x100')
    newWindow.config(bg='#D2FFFF')

    LabelA = Label(newWindow, text='Enter course name:', font=('Georgia', 17, 'bold'), bg='#D2FFFF', pady=10)
    LabelA.grid(row=0, column=0, sticky=E)
    entryA = Entry(newWindow, font=('Georgia', 17, 'bold'))
    entryA.grid(row=0, column=1)

    LabelB = Label(newWindow, text='Enter the maximum number of students:', font=('Georgia', 17, 'bold'), bg='#D2FFFF',
                   pady=10)
    LabelB.grid(row=1, column=0, sticky=E)
    entryB = Entry(newWindow, font=('Georgia', 17, 'bold'))
    entryB.grid(row=1, column=1)

    def submitInfo(*args):
        Course.Cname = entryA.get()
        Course.max_students = entryB.get()
        entryA.delete(0, END)
        entryB.delete(0, END)
        print(Course.max_students)
        return Course.max_students

    buttonSubmit = Button(newWindow, text="Submit", font=('Georgia', 17, 'bold'), bg='green', fg='white', width=5,
                          height=1, padx=10, command=submitInfo)
    buttonSubmit.grid(row=1, column=2)


def ClearData():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    filename1 = "data.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename1, "w+")
    f.close()
    filename2 = "data2.csv"
    g = open(filename2, "w+")
    g.close()


def AvgGrade(*args):
    aWindow = Toplevel(root)
    aWindow.geometry('500x50')
    aWindow.config(bg='#41062F')

    filename = 'data.csv'
    with open(filename) as f:
        s1 = f.read()
    # print(s)
    s1 = s1.split(",")
    #print(s1)
    s1 = s1[4::4]
    #print(s1)
    s2 = []  # Fresh list
    for i in s1:  # Declaring variable (i) as an item in the list (s1).
        s2.append(int(i))  # Look below for explanation
    print(s2)
    gradeSum = sum(s2)
    print(gradeSum)
    average = gradeSum / len(s2)
    rAverage = float("{:.2f}".format(average))
    print(rAverage)
    A = "The average grade is " + str(rAverage)
    # Convert to letter grades

    aLabel = Label(aWindow,bg="#41062F",fg="#21FE11",text=A,font=('Georgia',24,'bold'))
    aLabel.pack()



def onClick(*args):
    print("Button clicked")
    # print([entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get()])
    global count
    # CSV
    with open('data.csv', mode='a') as names_file:
        names_writer = csv.writer(names_file, delimiter=',', quotechar='"', lineterminator=',',
                                  quoting=csv.QUOTE_MINIMAL)
        names_writer.writerow([entry2.get(), entry1.get(), entry3.get(), entry4.get(), entry5.get()])
    with open('data2.csv', mode='a') as names_file:
        names_writer = csv.writer(names_file, delimiter=',', quotechar='"', lineterminator='\n',
                                  quoting=csv.QUOTE_MINIMAL)
        names_writer.writerow([entry2.get(), entry1.get(), entry3.get(), entry4.get(), entry5.get()])
    print(count)
    n = int(Course.max_students)
    if count < n-1:
        count = count + 1
    elif count >= n-1:
        button1["state"] = DISABLED
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


def DataWindow(*args):
    dWindow = Toplevel(root)
    dWindow.geometry('500x500')
    dWindow.config(bg='#1F1086')
    # Read csv file info and send it to the DataWindow
    # open file in read mode
    with open('data2.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(row)
            DataLabel = Label(dWindow, text=row, bg='#1F1086', fg="yellow", font=('Georgia', 12, 'bold'))
            DataLabel.pack()

def Instructions():
    iWindow = Toplevel(root)
    iWindow.geometry('1000x200')
    iWindow.config(bg='#C5BDEE')
    with open('HowToUseThis.txt', 'r') as file:
        data = file.read()
    iLabel = Label(iWindow,text=data,bg='#C5BDEE',fg='#0B350B',font=('Georgia',14,'bold'))
    iLabel.pack()

Label1 = Label(root, text="Enter first name:", height='1', width='18', font=("Georgia", 16, 'bold'), bg='#D2FFFF',
               anchor='e')
Label1.grid(column=0, row=2, pady=10)

entry1 = Entry(root, font=("Georgia", 17, 'bold'), width=20, bg='#D2FFFF', relief='flat')
entry1.grid(column=1, row=2)

Label2 = Label(root, text="Enter last name:", height='1', width='18', font=("Georgia", 16, 'bold'), bg='#D2FFFF',
               anchor='e')
Label2.grid(column=0, row=3, pady=10)

entry2 = Entry(root, font=("Georgia", 17, 'bold'), width=20, bg='#D2FFFF', relief='flat')
entry2.grid(column=1, row=3)

Label3 = Label(root, text="Enter student number:", height='1', width='18', font=("Georgia", 16, 'bold'), bg='#D2FFFF',
               anchor='e')
Label3.grid(column=0, row=4, pady=10)

entry3 = Entry(root, font=("Georgia", 17, 'bold'), width=20, bg='#D2FFFF', relief='flat')
entry3.grid(column=1, row=4)

Label4 = Label(root, text="Enter age:", height='1', width='18', font=("Georgia", 16, 'bold'), bg='#D2FFFF', anchor='e')
Label4.grid(column=0, row=5, pady=10)

entry4 = Entry(root, font=("Georgia", 17, 'bold'), width=20, bg='#D2FFFF', relief='flat')
entry4.grid(column=1, row=5)

Label5 = Label(root, text="Enter grade:", height='1', width='18', font=("Georgia", 16, 'bold'), bg='#D2FFFF',
               anchor='e')
Label5.grid(column=0, row=6, pady=10)

entry5 = Entry(root, font=("Georgia", 17, 'bold'), width=20, bg='#D2FFFF', relief='flat')
entry5.grid(column=1, row=6)

# Buttons
#C_Label = Button(root, text="Add course information", font=("Georgia", 10, 'bold'), height=1, fg='#6200A5',bg='#C5F2C4', command=courseWindow)
#C_Label.grid(column=0, row=1)

instructionsButton = Button(root,text="Instructions",font=('Georgia',10,'bold'),fg='#E56704',bg='#D2FFFF',command=Instructions)
instructionsButton.grid(column=0,row=0)

button1 = Button(root, text="Submit", font=("Georgia", 17, 'bold'), fg='#187D06', bg='#D2FFFF', command=onClick)
button1.grid(column=1, row=7, sticky=E)

button2 = Button(root, text="Clear data", font=("Georgia", 17, 'bold'), fg='#E30B0F', bg='#D2FFFF',command=ClearData)
button2.grid(column=1, row=8, sticky=E, pady=10)

button3 = Button(root, text="Get average grade", font=("Georgia", 17, 'bold'), height=1, fg='#77148D', bg='#D2FFFF',
                 command=AvgGrade)
button3.grid(column=0, row=8, sticky=S)

button3 = Button(root, text="Get maximum grade and student", font=("Georgia", 10, 'bold'), height=1, fg='#7C065C',
                 bg='#D2FFFF')
button3.grid(column=0, row=9, sticky=S, pady=10)

button4 = Button(root, text="See data", font=('Georgia', 10, 'bold'), command=DataWindow)
button4.grid(column=0, row=10)

# while in the range of max students, the button can only be clicked that many times before it is disabled
# use a value to check if button is pressed
courseWindow()

root.mainloop()
