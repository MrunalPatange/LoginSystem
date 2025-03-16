from tkinter import*
from PIL import ImageTk
from tkinter import messagebox

class Login:
    def __init__(self ,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("600x600")
        self.root.resizable(False,False)




        #Background Image

        self.bg=ImageTk.PhotoImage(file="D:/Python/LoginSystem/Images/background.jpg")
        self.ng_image = Label(self.root , image = self.bg).place(x=0 , y = 0 , relwidth = 1 , relheight = 1)


        #LogIn frame
        Frame_login = Frame(self.root , bg = "White")
        Frame_login.place(x = 50 , y= 50 , width = 500 , height = 488)
                    
        
        #Title and subtitle 
        title = Label(Frame_login , text = "Login" , font = ("Impact" , 35 ,  "bold") , fg = "#6162FF" , bg = "White").place(x = 90 , y = 30)
        subttitle = Label(Frame_login , text = "Member Login " , font = ("Calibri" , 15 ,  "bold") , fg = "#1d1d1d" , bg = "White").place(x = 90 , y = 100)
        




        # User Name 
        lbl_User = Label(Frame_login , text = "Username " , font = ("Calibri" , 15 ,  "bold") , fg = "grey" , bg = "White").place(x = 90 , y = 140)
        self.username = Entry(Frame_login , font = ("Calibrid" , 15 ,  "bold") , fg = "grey" , bg = "#E7E6e6")
        self.username.place(x = 90 , y = 170 , width = 320  , height = 35)




        # Password 
        lbl_password = Label(Frame_login , text = "Password " , font = ("Calibri" , 15 ,  "bold") , fg = "grey" , bg = "White").place(x = 90 , y = 210)
        self.password = Entry(Frame_login , font = ("Calibri" , 15 ,  "bold") , fg = "grey" , bg = "#E7E6e6")
        self.password.place(x = 90 , y = 240 , width = 320  , height = 35)


        #Button
        forget = Button(Frame_login , text = "Forget Password " , bd = 0 , font = ("Calibri" , 12 ) , fg = "grey" , bg = "White").place(x = 90 , y = 280)

        #Submit/login
        submit = Button(Frame_login , command = self.check_function ,cursor = "hand2" , text = "Login " , bd = 0 , font = ("Calibri" , 15 ) , fg = "White" , bg = "#6162FF").place(x = 90 , y = 320 , width = 180, height=40 )






    def check_function(self):
            if self.username.get()  == "" or self.password.get() == "" :
                messagebox.showerror("Error" , "All fields are required"  , parent = self.root)
        
            elif self.username.get()  != "Admin" or self.password.get() != "Admin@1234" :
                messagebox.showerror("Error" , "Invalid Username or Password"  , parent = self.root)

            else :
                messagebox.showinfo("Welcome" , f"Welcome  {self.username.get()}")





root = Tk()
obj = Login(root)
root.mainloop()


