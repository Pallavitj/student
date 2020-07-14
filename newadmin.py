import pymysql
import tkinter as tk


########################################################################


class MyApp:
    def __init__(self):
        """Constructor"""
        root=tk.Tk()
        root.title("create new admin")

        root.geometry("400x300")
        self.v1 = tk.StringVar()
        self.v2 = tk.StringVar()
        self.v3 = tk.StringVar()
        self.v4 = tk.StringVar()
        self.v5 = tk.StringVar()
        self.v6 = tk.StringVar()

       # label1=tk.Label(root,text="Name:").grid(row=0,column=0)
        #entry1=tk.Entry(root,textvariable=self.v1).grid(row=0,column=1)

        label2=tk.Label(root,text="Email:").grid(row=0,column=0)
        entry2=tk.Entry(root,textvariable=self.v2).grid(row=0,column=1)

       # label3=tk.Label(root,text="Phone:").grid(row=2,column=0)
        #entry3=tk.Entry(root,textvariable=self.v3).grid(row=2,column=1)

        #self.g=tk.StringVar()

        #label4=tk.Label(root,text="Gender:").grid(row=3,column=0)
        #rb1=tk.Radiobutton(root,text="male",variable=self.g,value="male").grid(row=3,column=1)
        #rb2=tk.Radiobutton(root,text="female",variable=self.g,value="female").grid(row=3,column=2)

        label5=tk.Label(root,text="Password:").grid(row=1,column=0)
        entry5=tk.Entry(root,show="*",textvariable=self.v4).grid(row=1,column=1)

        label6=tk.Label(root,text="Cpassword:").grid(row=2,column=0)

        entry6=tk.Entry(root,show="*",textvariable=self.v5).grid(row=2,column=1)

        button1=tk.Button(root,text="Submit",command=lambda: self.validate()).grid(row=3,column=1)


        label7=tk.Label(root,text=" ",textvariable=self.v6).grid(row=4,column=1)
        
        btn = tk.Button(root, text="go back", command=lambda: self.openFrame(root)).grid(row=8,column=1)

            
    def openFrame(self,root):
        """   """
        root.destroy()
        import profile

 
        #btn = tk.Button(root, text="Already Have Acc?", command=lambda: self.openFrame(root)).grid(row=8,column=1)
    #----------------------------------------------------------------------
    def validate(self):
        # a1=str(self.v1.get())
        a2=str(self.v2.get())
       # a3=str(self.v3.get())
        #a4=str(self.g.get())
        a5=str(self.v4.get())
        a6=str(self.v5.get())
        if a5=='':
            self.v6.set("password must be filled")
        elif a5!=a6:
            self.v6.set("both password should be same")
        else:
            conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='aict')
            cur=conn.cursor()
            res=cur.execute("select * from admin where email='"+a2+"'")
            if res:
                self.v6.set("Email Already Exist")
            else:
                try:
                    cur.execute("insert into admin(email, password) VALUES('"+a2+"', '"+a5+"')")
                    conn.commit()
                    self.v6.set("Inserted Sucessfully")
                except:
                    conn.rollback()
            cur.close()
            conn.close()

    #----------------------------------------------------------------------
  #def openFrame(self,root):
   #     """   """
    #    root.destroy()
     #   app = LoginApp()
    #----------------------------------------------------------------------
    #def onCloseOtherFrame(self,otherFrame):
        """"""
     #   otherFrame.destroy()
      #  app=MyApp() """
 
#----------------------------------------------------------------------

app = MyApp()
