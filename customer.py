from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class CustWin:
    def __init__(self, root):
        self.root = root
        self.root.title("Village Management System")
        self.root.geometry("1120x550+230+200")

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", bg='black', fg='gold', font=('times new roman',15,'bold'), bd=2, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1120, height=40)

        # ==================LOGO=============================================
        # img1 = Image.open(r"C:\Users\Kizito\OneDrive - Millenium Information Systems\Desktop\camps\logo.jpg")
        # img1.resize((200, 40), Image.ANTIALIAS)
        # self.photoImg1 = ImageTk.PhotoImage(img1)

        # lblimg = Label(self.root, image=self.photoImg1, bd=0, relief=RIDGE)
        # lblimg.place(x=5, y=2, width=200, height=40)

        # ===========================LabelFrame Left =========================================================
        labelframeleft = LabelFrame(self.root, text='Customer Details', font=('times new roman',12,'bold'), bd=2, padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=400)

        # Customer Ref
        cust_ref_lbl = Label(labelframeleft, text='Customer Ref', font=('arial',10,'bold'), bd=2, padx=2, pady=6)
        cust_ref_lbl.grid(row=0, column=0, sticky=W)
        cust_ref_entry = ttk.Entry(labelframeleft, width=26, font=('arial',10,'bold'))
        cust_ref_entry.grid(row=0, column=1)

        # Names
        names_lbl = Label(labelframeleft, text='Full Names', font=('arial',10,'bold'), bd=2, padx=2, pady=6)
        names_lbl.grid(row=1, column=0, sticky=W)
        names_entry = ttk.Entry(labelframeleft, width=26, font=('arial',10,'bold'))
        names_entry.grid(row=1, column=1)

          # mobile number
        mobile_lbl = Label(labelframeleft, text='Mobile No', font=('arial',10,'bold'), bd=2, padx=2, pady=6)
        mobile_lbl.grid(row=2, column=0, sticky=W)
        mobile_entry = ttk.Entry(labelframeleft, width=26, font=('arial',10,'bold'))
        mobile_entry.grid(row=2, column=1)

          # gender
        gender_lbl = Label(labelframeleft, text='Gender', font=('arial',10,'bold'), bd=2, padx=2, pady=6)
        gender_lbl.grid(row=3, column=0, sticky=W)
        gender_combo = ttk.Combobox(labelframeleft, width=24, font=('arial',10,'bold'), state="readonly")
        gender_combo["value"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=1)

        # Employer
        employer_lbl = Label(labelframeleft, text='Employer', font=('arial',10,'bold'), bd=2, padx=2, pady=6)
        employer_lbl.grid(row=4, column=0, sticky=W)
        employer_entry = ttk.Entry(labelframeleft, width=26, font=('arial',10,'bold'))
        employer_entry.grid(row=4, column=1)

        # Nationality
        nationality_lbl = Label(labelframeleft, text='Nationality', font=('arial',10,'bold'), bd=2, padx=2, pady=6)
        nationality_lbl.grid(row=5, column=0, sticky=W)
        nationality_combo = ttk.Combobox(labelframeleft, width=24, font=('arial',10,'bold'), state="readonly")
        nationality_combo["value"] = ("Kenyan", "SA", "Other")
        nationality_combo.current(0)
        nationality_combo.grid(row=5, column=1)

        # id type
        id_type_lbl = Label(labelframeleft, text='ID type', font=('arial',10,'bold'), bd=2, padx=2, pady=6)
        id_type_lbl.grid(row=6, column=0, sticky=W)
        id_type_combo = ttk.Combobox(labelframeleft, width=24, font=('arial',10,'bold'), state="readonly")
        id_type_combo["value"] = ("National ID", "Passport", "Driving License")
        id_type_combo.current(0)
        id_type_combo.grid(row=6, column=1)

        # id number
        id_number_lbl = Label(labelframeleft, text='ID number', font=('arial',10,'bold'), bd=2, padx=2, pady=6)
        id_number_lbl.grid(row=7, column=0, sticky=W)
        id_number_entry = ttk.Entry(labelframeleft, width=26, font=('arial',10,'bold'))
        id_number_entry.grid(row=7, column=1)

        # ===========================BtnFrame Left =========================================================
        btnFrame = Frame(labelframeleft)
        btnFrame.place(x=0, y=300, width=420, height=30)

        # add
        add = Button(btnFrame, text="ADD",width=10, bg='black', fg='gold', font=('times new roman',10,'bold'), relief=RIDGE)
        add.grid(row=0, column=0, padx=2)

        # update
        update = Button(btnFrame, text="UPDATE",width=10, bg='black', fg='gold', font=('times new roman',10,'bold'), relief=RIDGE)
        update.grid(row=0, column=1, padx=2)

        # delete
        delete = Button(btnFrame, text="DELETE",width=10, bg='black', fg='gold', font=('times new roman',10,'bold'), relief=RIDGE)
        delete.grid(row=0, column=2, padx=2)

        # reset
        reset = Button(btnFrame, text="RESET",width=10, bg='black', fg='gold', font=('times new roman',10,'bold'), relief=RIDGE)
        reset.grid(row=0, column=3, padx=2)

        # ===========================  TableFrame  =========================================================
        table_frame = LabelFrame(self.root, text='Customer Details and Search System', font=('times new roman',12,'bold'), bd=2, padx=2)
        table_frame.place(x=430, y=50, width=650, height=500)

        # ===========================SearchFrame Left =========================================================
        searchFrame = Frame(table_frame)
        searchFrame.place(x=0, y=0, width=640, height=30)

        search_lbl = Label(searchFrame, text='Search By', font=('arial',10,'bold'), bd=2, bg='red', fg='blue')
        search_lbl.grid(row=0, column=0, padx=2)

        search_combo = ttk.Combobox(searchFrame, width=18, font=('arial',10,'bold'), state="readonly")
        search_combo["value"] = ("Cust Ref", "Employer", "Nationality")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2)

        search_txt = ttk.Entry(searchFrame, width=20, font=('arial',10,'bold'))
        search_txt.grid(row=0, column=2, padx=2)

        # reset
        reset = Button(searchFrame, text="Search",width=10, bg='black', fg='gold', font=('times new roman',10,'bold'), relief=RIDGE)
        reset.grid(row=0, column=3, padx=2)

        # reset
        reset = Button(searchFrame, text="Show All",width=10, bg='black', fg='gold', font=('times new roman',10,'bold'), relief=RIDGE)
        reset.grid(row=0, column=4, padx=2)

        # ===========================DetailsFrame Left =========================================================
        DetailsFrame = Frame(table_frame)
        DetailsFrame.place(x=0, y=50, width=640, height=350)

        scroll_x = ttk.Scrollbar(DetailsFrame ,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        self.cust_details_table = ttk.Treeview(DetailsFrame, columns=("ref", "name","mobile","gender","employer","nationality","idtype","idnumber"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading('ref', text="Customer Ref")
        self.cust_details_table.heading('name', text="Full Names")
        self.cust_details_table.heading('mobile', text="Mobile No")
        self.cust_details_table.heading('gender', text="Gender")
        self.cust_details_table.heading('employer', text="Employer")
        self.cust_details_table.heading('nationality', text="Nationality")
        self.cust_details_table.heading('idtype', text="ID Type")
        self.cust_details_table.heading('idnumber', text="ID Number")

        self.cust_details_table["show"] = "headings"

        self.cust_details_table.column('ref', width=100)
        self.cust_details_table.column('name', width=100)
        self.cust_details_table.column('mobile', width=100)
        self.cust_details_table.column('gender', width=100)
        self.cust_details_table.column('employer', width=100)
        self.cust_details_table.column('nationality', width=100)
        self.cust_details_table.column('idtype', width=100)
        self.cust_details_table.column('idnumber', width=100)

        self.cust_details_table.pack(fill=BOTH, expand=1)



if __name__ == '__main__':
    root = Tk()
    obj = CustWin(root)
    root.mainloop()