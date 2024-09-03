import time
from tkinter import *

import pandas
import ttkthemes
from tkinter import ttk, messagebox,filedialog
import pymysql


import pandas
from tkinter import filedialog, messagebox

def iexit():
    result=messagebox.askokcancel('Quit', 'Do you want to quit?')
    if result:
        root.destroy()
    else:
        pass
def expor_data():
    # Prompt the user to select a file path to save the CSV
    url = filedialog.asksaveasfilename(defaultextension='.csv',
                                       filetypes=[("CSV files", "*.csv"),
                                                  ("All files", "*.*")])

    # Ensure that a file path was selected
    if url:
        indexing = studentTable.get_children()
        newlist = []
        for i in indexing:
            content = studentTable.item(i)  # Corrected method to fetch data
            datalist = content["values"]
            newlist.append(datalist)

        # Create a DataFrame and save it as a CSV file
        table = pandas.DataFrame(newlist,
                                 columns=["id", "name", "mobile", "email", "address", "dobs", "gender", "date", "time"])
        table.to_csv(url, index=False)

        # Show success message
        messagebox.showinfo("Successful", "Data exported successfully")
    else:
        # Handle case where no file was selected
        messagebox.showwarning("Warning", "No file selected. Data export canceled.")


def update_student():
    def update_data():
        query = "UPDATE student SET name=%s, email=%s, mobile=%s, address=%s, gender=%s, dobs=%s WHERE id=%s"
        mycursor.execute(query, (nameEntry.get(), emailEntry.get(), mobileEntry.get(), addressEntry.get(),
                                 genderEntry.get(), dobEntry.get(), idEntry.get()))
        con.commit()
        messagebox.showinfo("Updated Successfully", "Student Updated Successfully", parent=update_window)
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.title("Update Student")
    update_window.resizable(False, False)

    # Student ID
    idLabel = Label(update_window, text="Student ID", font=("Times New Roman", 20, "bold"))
    idLabel.grid(column=0, row=0, padx=30, pady=15)
    idEntry = Entry(update_window, font=("Roman", 15, "bold"))
    idEntry.grid(column=1, row=0, padx=20, pady=15)

    # Student Name
    nameLabel = Label(update_window, text="Student Name", font=("Times New Roman", 20, "bold"))
    nameLabel.grid(column=0, row=1, padx=30, pady=15)
    nameEntry = Entry(update_window, font=("Roman", 15, "bold"))
    nameEntry.grid(column=1, row=1, padx=20, pady=15)

    # Mobile Number
    mobileLabel = Label(update_window, text="Mobile Number", font=("Times New Roman", 20, "bold"))
    mobileLabel.grid(column=0, row=2, padx=30, pady=15)
    mobileEntry = Entry(update_window, font=("Roman", 15, "bold"))
    mobileEntry.grid(column=1, row=2, padx=20, pady=15)

    # Email
    emailLabel = Label(update_window, text="Email", font=("Times New Roman", 20, "bold"))
    emailLabel.grid(column=0, row=3, padx=30, pady=15)
    emailEntry = Entry(update_window, font=("Roman", 15, "bold"))
    emailEntry.grid(column=1, row=3, padx=20, pady=15)

    # Address
    addressLabel = Label(update_window, text="Address", font=("Times New Roman", 20, "bold"))
    addressLabel.grid(column=0, row=4, padx=30, pady=15)
    addressEntry = Entry(update_window, font=("Roman", 15, "bold"))
    addressEntry.grid(column=1, row=4, padx=20, pady=15)

    # Gender
    genderLabel = Label(update_window, text="Gender", font=("Times New Roman", 20, "bold"))
    genderLabel.grid(column=0, row=5, padx=30, pady=15)
    genderEntry = Entry(update_window, font=("Roman", 15, "bold"))
    genderEntry.grid(column=1, row=5, padx=20, pady=15)

    # Date of Birth (DOB)
    dobLabel = Label(update_window, text="Date of Birth", font=("Times New Roman", 20, "bold"))
    dobLabel.grid(column=0, row=6, padx=30, pady=15)
    dobEntry = Entry(update_window, font=("Roman", 15, "bold"))
    dobEntry.grid(column=1, row=6, padx=20, pady=15)

    # Update Button
    update_student_button = ttk.Button(update_window, text="Update Student", width=25, command=update_data)
    update_student_button.grid(column=1, row=7, padx=20, pady=15)


    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    listdata = content["values"]

    if len(listdata) >= 7:
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        mobileEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])
    else:
        print("Error: listdata does not contain enough elements.")


def show_student():
    query = "select * from student "
    mycursor.execute(query)
    feched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())

    for i in feched_data:
        studentTable.insert("", END, values=i)


def delete_student():
    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    contentıd = content["values"][0]
    query = "delete from student where id=%s"
    mycursor.execute(query, contentıd)
    con.commit()
    messagebox.showinfo("delete", f"öge basarı ile silindi ID : {contentıd}")
    query = "select * from student "
    mycursor.execute(query)
    feched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in feched_data:
        studentTable.insert("", END, values=i)


def searchstudent():
    def search_data():
        query = "SELECT * FROM student WHERE id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dobs=%s "
        mycursor.execute(query, (
            idEntry.get(), nameEntry.get(), emailEntry.get(), mobileEntry.get(), addressEntry.get(), genderEntry.get(),
            dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_Data = mycursor.fetchall()
        for i in fetched_Data:
            studentTable.insert("", END, values=i)

    search_window = Toplevel()
    search_window.title("Search Student")
    search_window.resizable(False, False)

    # Student ID
    idLabel = Label(search_window, text="Student ID", font=("Times New Roman", 20, "bold"))
    idLabel.grid(column=0, row=0, padx=30, pady=15)
    idEntry = Entry(search_window, font=("Roman", 15, "bold"))
    idEntry.grid(column=1, row=0, padx=20, pady=15)

    # Student Name
    nameLabel = Label(search_window, text="Student Name", font=("Times New Roman", 20, "bold"))
    nameLabel.grid(column=0, row=1, padx=30, pady=15)
    nameEntry = Entry(search_window, font=("Roman", 15, "bold"))
    nameEntry.grid(column=1, row=1, padx=20, pady=15)

    # Mobile Number
    mobileLabel = Label(search_window, text="Mobile Number", font=("Times New Roman", 20, "bold"))
    mobileLabel.grid(column=0, row=2, padx=30, pady=15)
    mobileEntry = Entry(search_window, font=("Roman", 15, "bold"))
    mobileEntry.grid(column=1, row=2, padx=20, pady=15)

    # Email
    emailLabel = Label(search_window, text="Email", font=("Times New Roman", 20, "bold"))
    emailLabel.grid(column=0, row=3, padx=30, pady=15)
    emailEntry = Entry(search_window, font=("Roman", 15, "bold"))
    emailEntry.grid(column=1, row=3, padx=20, pady=15)

    # Address
    addressLabel = Label(search_window, text="Address", font=("Times New Roman", 20, "bold"))
    addressLabel.grid(column=0, row=4, padx=30, pady=15)
    addressEntry = Entry(search_window, font=("Roman", 15, "bold"))
    addressEntry.grid(column=1, row=4, padx=20, pady=15)

    # Gender
    genderLabel = Label(search_window, text="Gender", font=("Times New Roman", 20, "bold"))
    genderLabel.grid(column=0, row=5, padx=30, pady=15)
    genderEntry = Entry(search_window, font=("Roman", 15, "bold"))
    genderEntry.grid(column=1, row=5, padx=20, pady=15)

    # Date of Birth (DOB)
    dobLabel = Label(search_window, text="Date of Birth", font=("Times New Roman", 20, "bold"))
    dobLabel.grid(column=0, row=6, padx=30, pady=15)
    dobEntry = Entry(search_window, font=("Roman", 15, "bold"))
    dobEntry.grid(column=1, row=6, padx=20, pady=15)

    # Search Button
    search_student_button = ttk.Button(search_window, text="Search Student", width=25, command=search_data)
    search_student_button.grid(column=1, row=7, padx=20, pady=15)


def add_student():
    def add_data():
        if (idEntry.get() == "" or nameEntry.get() == "" or mobileEntry.get() == "" or
                emailEntry.get() == "" or addressEntry.get() == "" or dobEntry.get() == "" or
                genderEntry.get() == ""):
            messagebox.showinfo("Hata", "Lütfen tüm alanları doldurun", parent=add_window)
            return  # Eksik bilgi varsa, işlemi durdur

        currentdate = time.strftime('%d:%m:%Y')
        currenttime = time.strftime('%H:%M:%S')
        query = ("INSERT INTO student (id, name, mobile, email, address, dobs, gender, date, time) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

        try:
            mycursor.execute(query, (
                idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(),
                dobEntry.get(), genderEntry.get(), currentdate, currenttime))
            db.commit()  # Değişiklikleri veritabanına kaydet
            messagebox.showinfo("Başarı", "Veri başarıyla eklendi", parent=add_window)

            # Tabloyu temizle
            studentTable.delete(*studentTable.get_children())

            # Güncellenmiş verileri al ve göster
            query = "SELECT * FROM student"
            mycursor.execute(query)
            datalar = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for row in datalar:
                studentTable.insert("", END, values=row)

            add_window.destroy()  # Verileri ekledikten sonra pencereyi kapat
        except pymysql.MySQLError as err:
            messagebox.showerror("Hata", f"Bir şeyler yanlış gitti: {err}", parent=add_window)
            db.rollback()  # Hata olursa değişiklikleri geri al
        finally:
            add_window.destroy()  # İşlem başarılı veya başarısız olsun pencereyi kapat

    add_window = Toplevel()
    add_window.title("Add Student")
    add_window.resizable(False, False)
    # Student ID
    idLabel = Label(add_window, text="Student ID", font=("times new roman", 20, "bold"))
    idLabel.grid(column=0, row=0, padx=30, pady=15)
    idEntry = Entry(add_window, font=("roman", 15, "bold"))
    idEntry.grid(column=1, row=0, padx=20, pady=15)

    # Student Name
    nameLabel = Label(add_window, text="Student Name", font=("times new roman", 20, "bold"))
    nameLabel.grid(column=0, row=1, padx=30, pady=15)
    nameEntry = Entry(add_window, font=("roman", 15, "bold"))
    nameEntry.grid(column=1, row=1, padx=20, pady=15)

    # Mobile Number
    mobileLabel = Label(add_window, text="Mobile Number", font=("times new roman", 20, "bold"))
    mobileLabel.grid(column=0, row=2, padx=30, pady=15)
    mobileEntry = Entry(add_window, font=("roman", 15, "bold"))
    mobileEntry.grid(column=1, row=2, padx=20, pady=15)

    # Email
    emailLabel = Label(add_window, text="Email", font=("times new roman", 20, "bold"))
    emailLabel.grid(column=0, row=3, padx=30, pady=15)
    emailEntry = Entry(add_window, font=("roman", 15, "bold"))
    emailEntry.grid(column=1, row=3, padx=20, pady=15)

    # Address
    addressLabel = Label(add_window, text="Address", font=("times new roman", 20, "bold"))
    addressLabel.grid(column=0, row=4, padx=30, pady=15)
    addressEntry = Entry(add_window, font=("roman", 15, "bold"))
    addressEntry.grid(column=1, row=4, padx=20, pady=15)

    # Gender
    genderLabel = Label(add_window, text="Gender", font=("times new roman", 20, "bold"))
    genderLabel.grid(column=0, row=5, padx=30, pady=15)
    genderEntry = Entry(add_window, font=("roman", 15, "bold"))
    genderEntry.grid(column=1, row=5, padx=20, pady=15)

    # Date of Birth (DOB)
    dobLabel = Label(add_window, text="Date of Birth", font=("times new roman", 20, "bold"))
    dobLabel.grid(column=0, row=6, padx=30, pady=15)
    dobEntry = Entry(add_window, font=("roman", 15, "bold"))
    dobEntry.grid(column=1, row=6, padx=20, pady=15)

    add_student_button = ttk.Button(add_window, text="Add Student", command=add_data)
    add_student_button.grid(column=1, row=7, padx=20, pady=15)


count = 0
text = ""
s = "Student Management System"

# Veritabanı bağlantısını oluşturun
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Kk230134",
    database="studentmangementsystem"
)
mycursor = db.cursor()


def connect_database():
    def connect():
        host = hostEntry.get()
        user = usernameEntry.get()
        password = passwordEntry.get()
        global con
        try:
            con = pymysql.connect(host=host, user=user, passwd=password)
            mycursor = con.cursor()
            query = "CREATE DATABASE IF NOT EXISTS studentmangementsystem"
            try:
                mycursor.execute(query)
            except pymysql.err.ProgrammingError as e:
                if e.args[0] == 1007:  # Error code for "Can't create database; database exists"
                    pass  # Database already exists, continue without error
                else:
                    raise  # Re-raise other programming errors
            con.select_db('studentmangementsystem')

            # SQL Sorgusu oluşturma
            query = (
                "CREATE TABLE IF NOT EXISTS student ("
                "id INT NOT NULL PRIMARY KEY, "
                "name VARCHAR(30), "
                "mobile VARCHAR(30), "
                "email VARCHAR(30), "
                "address VARCHAR(100), "
                "gender VARCHAR(30), "
                "dobs VARCHAR(30), "
                "date VARCHAR(30), "
                "time VARCHAR(50))"
            )
            mycursor.execute(query)
            messagebox.showinfo("Connect Successful", "Database Connection Successfully")
            connectWindow.destroy()
            addstudentButton.config(state=NORMAL)
            updatetudentButton.config(state=NORMAL)
            showstudentButton.config(state=NORMAL)
            exportstudentButton.config(state=NORMAL)
            deletestudentButton.config(state=NORMAL)
            searchstudentButton.config(state=NORMAL)
            exitButton.config(state=NORMAL)

        except pymysql.err.OperationalError as e:
            messagebox.showinfo("Connect Failed", f"Database Connection Failed: {e}")
        except Exception as e:
            messagebox.showinfo("Connect Failed", f"An error occurred: {e}")

    connectWindow = Toplevel()
    connectWindow.geometry("470x300+730+230")
    connectWindow.title("Connect Database")
    connectWindow.resizable(0, 0)

    hostnameLabel = Label(connectWindow, text="Host Name", font=("arial", 20, "bold"))
    hostnameLabel.grid(row=0, column=0, padx=20, pady=10)

    hostEntry = Entry(connectWindow, font=("roman", 20, "bold"), bd=2)
    hostEntry.grid(row=0, column=1, padx=40, pady=10)

    usernameLabel = Label(connectWindow, text="User Name", font=("arial", 20, "bold"))
    usernameLabel.grid(row=1, column=0, padx=20, pady=10)

    usernameEntry = Entry(connectWindow, font=("roman", 20, "bold"), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=10)

    passwordLabel = Label(connectWindow, text="Password", font=("arial", 20, "bold"))
    passwordLabel.grid(row=2, column=0, padx=20, pady=10)

    passwordEntry = Entry(connectWindow, font=("roman", 20, "bold"), bd=2, show="*")
    passwordEntry.grid(row=2, column=1, padx=40, pady=10)

    connectButton = Button(connectWindow, text="Connect", command=connect)
    connectButton.grid(row=3, column=0, columnspan=2, padx=20, pady=20)


def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ""
    text = text + s[count]
    sliderlabel.config(text=text)
    count += 1
    sliderlabel.after(500, slider)


def clock():
    date = time.strftime('%d:%m:%Y ')
    current_time = time.strftime('%H:%M:%S')
    datatimelabel.config(text=f"   Date: {date}\nTime:{current_time}")
    datatimelabel.after(1000, clock)


root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme("radiance")

root.geometry('1280x720')
root.resizable(0, 0)
root.title("Student Management System")

datatimelabel = Label(root, text="DATA TIME", font=("Times New Roman", 18, "bold"))
datatimelabel.place(x=5, y=5)
clock()

sliderlabel = Label(root, text="Student Management System", font=("arial", 28, "bold"), width=30)
sliderlabel.place(x=200, y=0)
slider()

connectButton = ttk.Button(root, text="Connect database", command=connect_database)
connectButton.place(x=1000, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image = PhotoImage(file="image/student (1).png")
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0)

addstudentButton = ttk.Button(leftFrame, text="Add Student", width=25, state="disabled", command=add_student)
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton = ttk.Button(leftFrame, text="Search Student", width=25, state="disabled", command=searchstudent)
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton = ttk.Button(leftFrame, text="Delete Student", width=25, state="disabled", command=delete_student)
deletestudentButton.grid(row=3, column=0, pady=20)

updatetudentButton = ttk.Button(leftFrame, text="Update Student", width=25, state="disabled",command=update_student)
updatetudentButton.grid(row=4, column=0, pady=20)

showstudentButton = ttk.Button(leftFrame, text="Show Student", width=25, state="disabled", command=show_student)
showstudentButton.grid(row=5, column=0, pady=20)

exportstudentButton = ttk.Button(leftFrame, text="Export data", width=25, state="disabled",command=expor_data)
exportstudentButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text="Exit", width=25, state="disabled",command=iexit)
exitButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root, bg="lightgrey")  # Arka plan rengini ekleyerek görünürlüğü artırabilirsiniz
rightFrame.place(x=350, y=82, width=820, height=600)

# Scrollbars
scrollbarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollbarY = Scrollbar(rightFrame, orient=VERTICAL)
scrollbarX.pack(side=BOTTOM, fill=X)
scrollbarY.pack(side=RIGHT, fill=Y)

# Treeview
studentTable = ttk.Treeview(rightFrame, columns=("StudentID", "Name", "Mobile No", "Email", "Address", "Gender", "D.O.B", "Added Date", "Added Time"))
scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)
studentTable.config(xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set)

# Column başlıkları
studentTable.heading("StudentID", text="ID")
studentTable.heading("Name", text="Name")
studentTable.heading("Mobile No", text="Mobile No")
studentTable.heading("Email", text="Email")
studentTable.heading("Address", text="Address")
studentTable.heading("Gender", text="Gender")
studentTable.heading("D.O.B", text="Bird Day")
studentTable.heading("Added Date", text="Added Date")
studentTable.heading("Added Time", text="Added Time")

studentTable.column("StudentID", width=50, anchor=CENTER)
studentTable.column("Name", width=200, anchor=CENTER)
studentTable.column("Email", width=150, anchor=CENTER)
studentTable.column("Address", width=200, anchor=CENTER)
studentTable.column("Gender", width=100, anchor=CENTER)
studentTable.column("D.O.B", width=100, anchor=CENTER)
studentTable.column("Added Date", width=100, anchor=CENTER)
studentTable.column("Added Time", width=100, anchor=CENTER)
# Görüntülenmeyen başlıkları gizlemek için
studentTable.config(show="headings")
studentTable.pack(fill=BOTH, expand=True)

root.mainloop()
