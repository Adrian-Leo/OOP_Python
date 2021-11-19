import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "label 1")
label2 = tkinter.Label(main_window, text = "label 2")
button1 = tkinter.Button(main_window,text= " yes")
button2 = tkinter.Button(main_window,text= " no")

#method positioning

label1.pack()
label2.pack()
button1.pack()
button2.pack()

#method menampilkan GUI

main_window.mainloop()