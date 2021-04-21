from tkinter import *
from PIL import Image, ImageTk
from customer import CustWin

class VillageManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Village Management System")
        self.root.geometry("1350x750+0+0")

        img1 = Image.open(r"C:\Users\Kizito\OneDrive - Millenium Information Systems\Desktop\camps\hotel.jpeg")
        img1.resize((1350, 130), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoImg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1350, height=130)
        # ==================LOGO=============================================
        img2 = Image.open(r"C:\Users\Kizito\OneDrive - Millenium Information Systems\Desktop\camps\logo.jpg")
        img2.resize((230, 130), Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoImg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=130)
        # =================================TITLE=================================
        lbl_title = Label(self.root, text="VILLAGE MANAGEMENT SYSTEM", bg='black', fg='gold', font=('times new roman',40,'bold'), bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=130, width=1350, height=40)
        # ===================================MAIN FRAME=============================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=170, width=1350, height=550)

        # =================================MENU=================================
        lbl_menu = Label(main_frame, text="MENU", bg='black', fg='gold', font=('times new roman',16,'bold'), bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ===================================BTN FRAME=============================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=30, width=220, height=180)

        cust_btn = Button(btn_frame,command=self.cust_details, text="CUSTOMER",width=22, bg='black', fg='gold', font=('times new roman',12,'bold'), bd=0, cursor='hand1')
        cust_btn.grid(row=0, column=0, pady=1)

        room = Button(btn_frame, text="ROOM",width=22, bg='black', fg='gold', font=('times new roman',12,'bold'), bd=0, cursor='hand1')
        room.grid(row=1, column=0, pady=1)

        details = Button(btn_frame, text="DETAILS",width=22, bg='black', fg='gold', font=('times new roman',12,'bold'), bd=0, cursor='hand1')
        details.grid(row=2, column=0, pady=1)

        report = Button(btn_frame, text="REPORT",width=22, bg='black', fg='gold', font=('times new roman',12,'bold'), bd=0, cursor='hand1')
        report.grid(row=3, column=0, pady=1)

        logout = Button(btn_frame, text="LOGOUT",width=22, bg='black', fg='gold', font=('times new roman',12,'bold'), bd=0, cursor='hand1')
        logout.grid(row=4, column=0, pady=1)

        # ==================RIGHT SIDE IMAGE=============================================
        img3 = Image.open(r"C:\Users\Kizito\OneDrive - Millenium Information Systems\Desktop\camps\room1.jpg")
        img3.resize((1120, 550), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoImg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1120, height=550)

        # ==================BOTTOM IMAGES=============================================
        img4 = Image.open(r"C:\Users\Kizito\OneDrive - Millenium Information Systems\Desktop\camps\room.jpg")
        img4.resize((230, 180), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=190, width=230, height=180)

        img5 = Image.open(r"C:\Users\Kizito\OneDrive - Millenium Information Systems\Desktop\camps\room.jpg")
        img5.resize((1120, 560), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=380, width=230, height=180)

    def cust_details(self):
        self.new_win = Toplevel(self.root)
        self.app = CustWin(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = VillageManagementSystem(root)
    root.mainloop()