from tkinter import *
from tkinter import messagebox

from PIL import ImageTk


def login():
    if usurnameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showinfo("Error", "Lütfen kullanıcı adınızı ve şifrenizi girin")
    elif usurnameEntry.get() == "ömer" and passwordEntry.get() == "1234":
        messagebox.showinfo("Success", "Hoş Geldin")
        window.destroy()
        import StudentManegementSystem
    else:
        messagebox.showinfo("Error", "Lütfen kullanıcı adınızı ve şifrenizi doğru girin")
window = Tk()
window.geometry('1280x720')
window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='image/bg.jpg')

label = Label(window, image=backgroundImage)
label.pack()

loginFrame = Frame(window, bg="white")
loginFrame.place(x=400, y=150)

loginImage = PhotoImage(file='image/logo.png')
loginLabel = Label(loginFrame, image=loginImage)
loginLabel.grid(row=0, column=0, columnspan=2, pady=10)

usurnameImage = PhotoImage(file='image/user.png')
usurnameLabel = Label(loginFrame, image=usurnameImage, text="Usurname", compound=LEFT,
                      font=("time new roman ", 20, "bold"), bg="white", )
usurnameLabel.grid(row=1, column=0, pady=10)

usurnameEntry = Entry(loginFrame, font=("time new roman ", 20, "bold"), bd=8, fg="royalblue")
usurnameEntry.grid(row=1, column=1)

passwordImage = PhotoImage(file='image/password.png')
passwordLabel = Label(loginFrame, image=passwordImage, text="Password", compound=LEFT,
                      font=("time new roman ", 20, "bold"), bg="white", )
passwordLabel.grid(row=2, column=0, pady=10)

passwordEntry = Entry(loginFrame, font=("time new roman ", 20, "bold"), bd=8, fg="royalblue")
passwordEntry.grid(row=2, column=1)

loginButton = Button(loginFrame, text="Login", font=("time new roman ", 14, "bold"), width=15, fg="white",
                     bg="cornflowerblue", activebackground="cornflowerblue", activeforeground="white", cursor="hand2",
                     command=login)
loginButton.grid(row=3, column=1, pady=10)

window.mainloop()
