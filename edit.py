import pymysql
import tkinter as tk


########################################################################










def validate(root):
        a2=str(v2.get())
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='aict')
        cur=conn.cursor()
        res=cur.execute("select * from student where email='"+a2+"'")
        #print("Hiii")
        if res:
            #v6.set("valid")
             for r1 in cur:
                show(root,r1[0],r1[1],r1[2],r1[3],r1[5])
        
        cur.close()
        conn.close()
def update(v1,v2,v3,v4,v5):
        a1=str(v1.get())
        a2=str(v2.get())
        a3=str(v3.get())
        a4=str(v4.get())
        a5=str(v5.get())
        print(a1)
        if a5=='':
            self.v6.set("password must be filled")
        else:
            conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='aict')
            cur=conn.cursor()
            str1="update `student` set name='"+a1+"' where id='"+a5+"'"
            try:
                    cur.execute(str1)
                    conn.commit()
                    print("Updated Sucessfully")
                    
            except:
                    conn.rollback()
        cur.close()
        conn.close()        
root=tk.Tk()
root.title("details")

root.minsize(300,300)
v2= tk.StringVar()
v6= tk.StringVar()
label2=tk.Label(root,text="Email:").grid(row=1,column=0)
entry2=tk.Entry(root,textvariable=v2).grid(row=1,column=1)
button1=tk.Button(root,text="Submit",command=lambda: validate(root)).grid(row=2,column=0)

btn = tk.Button(root, text="go back", command=lambda: openFrame(root)).grid(row=2,column=1)



label7=tk.Label(root,text=" ",textvariable=v6).grid(row=3,column=1)
def openFrame(root):
        """   """
        root.destroy()
        import profile






def show(root,n0,n1,n2,n3,n4):
        
        v1 = tk.StringVar()
        v2 = tk.StringVar()
        v3 = tk.StringVar()
        v4 = tk.StringVar()
        v5 = tk.StringVar()
        v6 = tk.StringVar()
        v5.set(n0)
        v1.set(n1)
        v2.set(n2)
        v3.set(n3)
        v4.set(n4)
        
        label=tk.Label(root,text="Id:").grid(row=4,column=0)
        lab1=tk.Label(root,textvariable=v5).grid(row=4,column=1)
        
        label1=tk.Label(root,text="Name:").grid(row=5,column=0)
        entry1=tk.Entry(root,textvariable=v1).grid(row=5,column=1)

        label2=tk.Label(root,text="Email:").grid(row=6,column=0)
        entry2=tk.Entry(root,textvariable=v2).grid(row=6,column=1)

        label3=tk.Label(root,text="Phone:").grid(row=7,column=0)
        entry3=tk.Entry(root,textvariable=v3).grid(row=7,column=1)

        label5=tk.Label(root,text="Password:").grid(row=8,column=0)
        entry5=tk.Entry(root,show="*",textvariable=v4).grid(row=8,column=1)

        button7=tk.Button(root,text="Update",command=lambda: update(v1,v2,v3,v4,v5)).grid(row=10,column=1)


        label7=tk.Label(root,text=" ",textvariable=v6).grid(row=11,column=1)

 
       
    #----------------------------------------------------------------------
   

    #----------------------------------------------------------------------
  
    #----------------------------------------------------------------------
    
#----------------------------------------------------------------------



