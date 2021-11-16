from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage



class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Code Generator")
        self.root.resizable(False,False)

        title=Label(self.root,text="  Qr Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        "Subject details window"
        "Variables"
        self.var_sub_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_div=StringVar()


        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)

        emp_title=Label(emp_Frame,text="Subject Details",font=("goudy old style",20),bg='#043246',fg='white').place(x=0,y=0,relwidth=1)

        lbl_sub_code=Label(emp_Frame,text="Subject Code & Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_name=Label(emp_Frame,text="Teacher's Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_department=Label(emp_Frame,text="Department",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_div=Label(emp_Frame,text="Division",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)


        txt_sub_code=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_sub_code,bg='light yellow').place(x=240,y=60)
        txt_name=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_name,bg='light yellow').place(x=240,y=100)
        txt_department=Entry(emp_Frame,font=("times new roman",15,),textvariable=self.var_department,bg='light yellow').place(x=240,y=140)
        txt_div=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_div,bg='light yellow').place(x=240,y=180)



        btn_generate=Button(emp_Frame,text='Generate QR Code',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=200,height=30)
        btn_clear=Button(emp_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=300,y=250,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20,'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)


        "Subject QR Code window"
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        emp_title=Label(qr_Frame,text="Subject QR Code",font=("goudy old style",20),bg='#043246',fg='white').place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text='QR Code \nNot Available',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_sub_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_div.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
        

    def generate(self):
        if self.var_sub_code.get()==''or self.var_name.get()==''or self.var_department.get()==''or self.var_div.get()=='':
           self.msg='All Fields Are Required!!!'
           self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Subject Code & Name: {self.var_sub_code.get()}\nTeacher's Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\nDivision:{self.var_div.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            #qr_code=resizeimage.resize_cover(qr_code,[180,180])
            #qr_code.save("Subject_QR/Sub_"+str(self.var_sub_code.get())+'.png')
            "QR Code Image updatation"
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            "updating notification"
            self.msg='QR Code generated Successfully !!!!'
            self.lbl_msg.config(text=self.msg,fg='green')
        

        
root=Tk()
obj=Qr_Generator(root)
root.mainloop()
