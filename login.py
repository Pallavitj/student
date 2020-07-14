import pymysql
import tkinter as tk

def validate():
    a2=str(v2.get())
    a5=str(v4.get())
    if a5=='':
         v6.set("password must be filled")
    else:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='aict')
        cur=conn.cursor()
        res=cur.execute("select * from admin where email='"+a2+"' and password='"+a5+"'")
        if res:
            #v6.set("valid")
            root.destroy()
            import profile
            for r1 in cur:
                disp(r1[1])
        else:
            v6.set("invalid password") 
        cur.close()
        conn.close()

root=tk.Tk()
root.title("Login Form")

root.minsize(300,300)

v2 = tk.StringVar()

v4= tk.StringVar()

v6 = tk.StringVar()


label2=tk.Label(root,text="Email:").grid(row=1,column=0)
entry2=tk.Entry(root,textvariable=v2).grid(row=1,column=1)

label5=tk.Label(root,text="Password:").grid(row=4,column=0)
entry5=tk.Entry(root,show="*",textvariable=v4).grid(row=4,column=1)



button1=tk.Button(root,text="Submit",command=validate).grid(row=6,column=1)


label7=tk.Label(root,text=" ",textvariable=v6).grid(row=7,column=1)
root.mainloop()

