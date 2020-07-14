import pymysql
import tkinter as tk
class myapp:
    
   def validate(self,root):
    root.destroy()
    import newadmin
   def view(self,root):
       root.destroy()
       import view
   
   def add1(self,root):
    root.destroy()
    import add
   def delete(self,root):
      root.destroy()
      import delt
   def edit(self,root):
      root.destroy()
      import edit
      
   def disp(self,a2):
    root=tk.Tk()
    root.title("Profile Page")

    root.minsize(300,300)
    
    v2 = tk.StringVar()

    v4= tk.StringVar()

    v6 = tk.StringVar()
    v2.set(a2)

    label2=tk.Label(root,text="Welcome").grid(row=1,column=0)
    label3=tk.Label(root,text="",fg="blue",textvariable=v2).grid(row=1,column=1)
    button1=tk.Button(root,text="create new admin",command=lambda: self.validate(root)).grid(row=2,column=2)
    button2=tk.Button(root,text="add new record",command=lambda: self.add1(root)).grid(row=3,column=2)
    button3=tk.Button(root,text="view record",command=lambda: self.view(root)).grid(row=4,column=2)
    button4=tk.Button(root,text="delete record",command=lambda: self.delete(root)).grid(row=5,column=2)
    button5=tk.Button(root,text="edit record",command=lambda: self.edit(root)).grid(row=6,column=2)





    root.mainloop()

app=myapp();
app.disp("")

