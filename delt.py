import pymysql
import tkinter as tk


def validate():
        a2=str(v2.get())
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='aict')
        cur=conn.cursor()
        res=cur.execute("select * from student where email='"+a2+"'")
        if res:
           cur.execute("delete  from student where email='"+a2+"'")
           v6.set("deleted successfully")
        else:
            v6.set("invalid password") 
        cur.close()
        conn.close()
        
root=tk.Tk()
root.title("details")

root.minsize(300,300)
v2= tk.StringVar()
v6= tk.StringVar()
label2=tk.Label(root,text="Email:").grid(row=1,column=0)
entry2=tk.Entry(root,textvariable=v2).grid(row=1,column=1)
button1=tk.Button(root,text="Submit",command=validate).grid(row=6,column=1)

btn = tk.Button(root, text="go back", command=lambda: openFrame(root)).grid(row=8,column=1)



label7=tk.Label(root,text=" ",textvariable=v6).grid(row=7,column=1)
def openFrame(root):
        """   """
        root.destroy()
        import profile
