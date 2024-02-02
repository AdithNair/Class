from tkinter import *

root = Tk()
root.geometry("900x600")
root.title("Classes")

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
    def createNewElement(self):
        label = Label(root,text ="A new label had been created using class", fg="red")
        label.pack()
        btn = Button(root, text =" Button ", command = self.message)
        btn.pack(padx=20, pady = 10)
        
    def message(self):
        message.box.showinfo("showinfo", "You clicked the button created using class")
        
        
obj_of_CreateElements = CreateElements()

btn = Button(root, text ="Click to create label and button element", command = obj_of_CreateElements.createNewElement)
btn.pack(padx=20, pady = 10)

root.mainloop()