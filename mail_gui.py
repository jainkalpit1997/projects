import xlwt
import time
import xlutils
from xlutils.copy import copy
import xlrd
import smtplib
import datetime
import random,time
import tkinter,datetime
from tkinter import *
def sign_up():
    global root1,e1,e2,e3,e4,e5,e6,e7
    root1=Tk()
    root1.grid()
    root1.geometry("1200x650+0+0")
    root1.title("sign_up page")
    head=Label(root1,text="SIGN UP",fg="black",bg="white",font='Arial 20 bold',anchor=E).place(x=600,y=50)
    head1=Label(root1,text="NAME",fg="black",bg="white",font='Arial 15',anchor=E).place(x=350,y=100)
    head2=Label(root1,text="gmail id",fg="black",bg="white",font='Arial 15',anchor=E).place(x=350,y=150)
    head3=Label(root1,text="10 digit mobile no.",fg="black",bg="white",font='Arial 15',anchor=E).place(x=350,y=200)
    head4=Label(root1,text="date of birth(DD/MM/YY)",fg="black",bg="white",font='Arial 15',anchor=E).place(x=350,y=250)
    head5=Label(root1,text="user name",fg="black",bg="white",font='Arial 15',anchor=E).place(x=350,y=300)
    head6=Label(root1,text="set password",fg="black",bg="white",font='Arial 15',anchor=E).place(x=350,y=350)
    head7=Label(root1,text="retype password",fg="black",bg="white",font='Arial 15',anchor=E).place(x=350,y=400)
    e1=Entry(root1)
    e1.place(x=700,y=100)
    e2=Entry(root1)
    e2.place(x=700,y=150)
    e3=Entry(root1)
    e3.place(x=700,y=200)
    e4=Entry(root1)
    e4.place(x=700,y=250)
    e5=Entry(root1)
    e5.place(x=700,y=300)
    e6=Entry(root1)
    e6.place(x=700,y=350)
    e7=Entry(root1)
    e7.place(x=700,y=400)
    read=Button(root1,text="SUBMIT",fg="black",bg="white",font='Arial 20 bold',bd=5,command=submit).place(x=600,y=500)   
    root1.mainloop()

def submit():
    global h1,h2,h3,h4,h5,h6,h7,c1,c2,c3,c4,c5,c6,c7
    name=e1.get()
    if(name!=""):
       try:
             h1
       except NameError:
             c1=1
             pass
             
       else:
             h1.destroy()
             c1=1
             
    else: 
          try:
              h1
          except NameError:
                h1=Label(root1,text="enter a name",fg="red",bg="white",font='Arial 10',anchor=E)
                h1.place(x=900,y=100)
                c1=0
          else:                                                                                      #for continuous two wrong input
                h1.destroy()   
                h1=Label(root1,text="enter a name",fg="red",bg="white",font='Arial 10',anchor=E)
                h1.place(x=900,y=100)
                c1=0
                
    
    email=e2.get()
    if(email.endswith('@gmail.com')): 
          try:
             h2
          except NameError:
             pass
             c2=1
          else:
             h2.destroy()
             c2=1
           
    else:
          try:
              h2
          except NameError:
              h2=Label(root1,text="please mention right name of id ",fg="red",bg="white",font='Arial 10',anchor=E)
              h2.place(x=900,y=150)
              c2=0        
          else:
              h2.destroy()    
              h2=Label(root1,text="please mention right name of id ",fg="red",bg="white",font='Arial 10',anchor=E)
              h2.place(x=900,y=150)
              c2=0

             
    phone=e3.get()
    if(len(str(phone))==10):
          try:
             h3
          except NameError:
             pass
             c3=1
          else:
             h3.destroy()
             c3=1
    else:
          try: 
             h3
          except NameError:
             h3=Label(root1,text="wrong mobile no. ",fg="red",bg="white",font='Arial 10',anchor=E)
             h3.place(x=900,y=200)
             c3=0   
            
          else:
             h3.destroy()
             h3=Label(root1,text="wrong mobile no. ",fg="red",bg="white",font='Arial 10',anchor=E)
             h3.place(x=900,y=200)       
             c3=0
             
    dob=e4.get()
    try :
         day,month,year = dob.split('/')
         datetime.datetime(int(year),int(month),int(day))
         try:
             h4
         except NameError:
             pass 
             c4=1
         else:
             h4.destroy()
             c4=1
         
    except ValueError :
             try:
                 h4
             except NameError:
                 h4=Label(root1,text="invalid date of birth ",fg="red",bg="white",font='Arial 10',anchor=E)
                 h4.place(x=900,y=250)
                 c4=0       
             else:
                 h4.destroy()
                 h4=Label(root1,text="invalid date of birth ",fg="red",bg="white",font='Arial 10',anchor=E)
                 h4.place(x=900,y=250) 
                 c4=0
    uname=e5.get()
    var=0
    for i in range(0,sheets[0].nrows):
        if(wbr1.cell_value(i,4)==uname):
            try:
                 h5
            except NameError:
                 h5=Label(root1,text="already exist user name",fg="red",bg="white",font='Arial 10',anchor=E)
                 h5.place(x=900,y=300)
                 var=1
                 c5=0       
            else:
                 h5.destroy()
                 h5=Label(root1,text="already exist user name",fg="red",bg="white",font='Arial 10',anchor=E)
                 h5.place(x=900,y=300)
                 var=1
                 c5=0
    if(var==0):
         try: 
             h5
         except NameError:
             pass
             c5=1
         else:
             h5.destroy() 
             c5=1
              

    password=e6.get()
    j=0
    k=0
    l=0
    if(len(password)>6):
        for i in password:
              if(i.islower()):
                       j=1
        for i in password:
              if(i.isupper()):
                       k=1
        for i in password:
              if(i=='#'or i=='@' or i=='$' or i=='&' or i=='*'):
                       l=1
    if(j==1 and k==1 and l==1):
         try:
             h6
         except NameError:
             c6=1
             pass
         else:
             c6=1
             h6.destroy() 
    else:
          try:
              h6
          except NameError:
              c6=0
              h6=Label(root1,text="use strong password:min. seven letter 1 upper 1 lower 1 special char",fg="red",bg="white",font='Arial 10',anchor=E)
              h6.place(x=900,y=350)  
          else:
              c6=0
              h6.destroy()
              h6=Label(root1,text="use strong password:min. seven letter 1 upper 1 lower 1 special char",fg="red",bg="white",font='Arial 10',anchor=E)
              h6.place(x=900,y=350)  
               

    repass=e7.get()
    if(repass==password):
             
               try:
                   h7
               except NameError:
                   c7=1
                   pass
               else:
                   h7.destroy()
                   c7=1
    else:
         try:
              h7
         except NameError:
              c7=0
              h7=Label(root1,text="retype again",fg="red",bg="white",font='Arial 10',anchor=E)
              h7.place(x=900,y=400)     
         else:
              h7.destroy()   
              h7=Label(root1,text="retype again",fg="red",bg="white",font='Arial 10',anchor=E)
              h7.place(x=900,y=400)
              c7=0


    if(c1==1 and c2==1 and c3==1 and c4==1 and c5==1 and c6==1 and c7==1):
         h8=Label(root1,text="account successfully created",fg="green",font='Arial 20 bold')
         h8.place(x=600,y=600)
         ws1.write(sheets[0].nrows,0,name)
         ws1.write(sheets[0].nrows,1,email)
         ws1.write(sheets[0].nrows,2,phone)
         ws1.write(sheets[0].nrows,3,dob)
         ws1.write(sheets[0].nrows,4,uname) 
         ws1.write(sheets[0].nrows,5,repass) 
         wb.save("maildata.xls")

def sign_in():
    global root2,i2,i1
    root2=Tk()
    root2.grid()
    root2.geometry("1200x650+0+0")
    root2.title("sign_in page")
    head=Label(root2,text="SIGN IN",fg="black",bg="white",font='Arial 30 bold',anchor=E).place(x=600,y=50)
    head=Label(root2,text="USER NAME",fg="black",bg="white",font='Arial 20 bold',anchor=E).place(x=400,y=150)
    head1=Label(root2,text="PASSWORD",fg="black",bg="white",font='Arial 20 bold',anchor=E).place(x=400,y=250)         
    i1=Entry(root2)
    i1.place(x=700,y=150)
    i2=Entry(root2)
    i2.place(x=700,y=250)     
    read=Button(root2,text="SUBMIT",fg="black",bg="white",font='Arial 20 bold',bd=5,command=in_submit).place(x=600,y=300) 
    root2.mainloop()

def in_submit():
     global l1,k1
     k1=0    
     getuname=i1.get()
     getpass=i2.get()
     for i in range(0,sheets[0].nrows):
           if(wbr1.cell_value(i,4)==getuname and wbr1.cell_value(i,5)==getpass):
                try:
                    l1
                except NameError:
                    l1=Label(root2,text="successfully login",fg="green",font='Arial 20 bold')
                    l1.place(x=600,y=400)
                    k1=1
                else:
                    l1.destroy()
                    l1=Label(root2,text="successfully login",fg="green",font='Arial 20 bold')
                    l1.place(x=600,y=400)
                    k1=1
     if(k1==0):
         try:
             l1
         except NameError:
             l1=Label(root2,text=" wrong user name or password ",fg="green",font='Arial 20 bold')
             l1.place(x=600,y=400)
             k1=0      
         else:
             l1.destroy()
             l1=Label(root2,text=" wrong user name or password ",fg="green",font='Arial 20 bold')
             l1.place(x=600,y=400)
             k1=0      

def home():
    root=Tk()
    root.grid()
    root.geometry("1200x650+0+0")
    root.title("mail page")
    frame = tkinter.Frame(root, bg='red')
    frame.pack(fill='both',expand='yes')
    head=Label(text="MAIL",fg="black",bg="white",font='Arial 20 bold',anchor=E).place(x=600,y=150)
    button=Button(root,text="sign up",bd=5,relief='groove',command=sign_up).place(x=500,y=250)
    button=Button(root,text="sign in",bd=5,relief='groove',command=sign_in).place(x=700,y=250)
    root.mainloop()

global lrow
global wb
global ws1,sheets,lcol
wbr=xlrd.open_workbook("maildata.xls")
wbr1=wbr.sheet_by_index(0)
wb=xlutils.copy.copy(wbr)
ws1=wb.get_sheet("mail sheet")
wb.save("maildata.xls") 
sheets=wbr.sheets()
lrow=sheets[0].nrows
lcol=sheets[0].ncols
home()
 
