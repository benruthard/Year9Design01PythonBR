import tkinter as tk


root = tk.Tk() #creates standard window



#Variables: Store data for my program




#1. Construct the Object
#2. Configure the Obj
#3. Pack the Object

output = tk.Text(root,height = 30, width = 45) #Parameters
output.config(state = "disable", background = "antiquewhite")
output.grid(row = 0, column = 0, rowspan = 3, columnspan = 2)

output = tk.Text(root,height = 30, width = 45) #Parameters
output.config(state = "disable", background = "lightgreen")
output.grid(row = 0, column = 3, rowspan = 3, columnspan = 2)



output = tk.Text(root,height = 1, width = 16, borderwidth = 1, relief = "solid")
output.config(state = "normal")
output.grid(row = 0, column = 1)

output = tk.Text(root,height = 1, width = 16, borderwidth = 1, relief = "solid")
output.config(state = "normal")
output.grid(row = 1, column = 1)

output = tk.Text(root,height = 1, width = 16, borderwidth = 1, relief = "solid")
output.config(state = "normal")
output.grid(row = 2, column = 1)



labInput1 = tk.Label(root, text = "How much Sugar? (g)")
labInput1.config(background = "black", foreground = "white")
labInput1.grid(row = 0, column = 0)


labInput2 = tk.Label(root, text = "What Food/Drink?")
labInput2.config(background = "black", foreground = "white")
labInput2.grid(row = 1, column = 0)

labInput3 = tk.Label(root, text = "What Food/Drink Product?")
labInput3.config(background = "black", foreground = "white")
labInput3.grid(row = 2, column = 0)


submitButton = tk.Button(root, text = "SUBMIT")
submitButton.grid(row = 3, column = 0, columnspan = 2, sticky = "NESW")

Button = tk.Button(root, text = "Show Me My Stats From The Past Month")
Button.grid(row = 0, column = 3, columnspan = 2, rowspan = 2)

Button = tk.Button(root, text = "Show Me My Stats From The Past Year")
Button.grid(row = 1, column = 3, columnspan = 2, rowspan = 2)

var1 = tk.IntVar()
var2 = tk.IntVar()







root.mainloop() #starts the program


