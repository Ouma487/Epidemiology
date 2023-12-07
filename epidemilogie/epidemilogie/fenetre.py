from tkinter import *
def confinement():
    print('save it')
def run():
    print('loading')
def deconfinement():
    print('deconfinement')

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()
 
mainmenu = Menu(frame)
##premiere menu load
load = Menu(mainmenu, tearoff = 0)
load.add_command(   label='RUN',command=run)
load.add_command(label='Stop')
mainmenu.add_cascade(label='LOAD',menu=load)





## deuxieme menu options
options=Menu(mainmenu,tearoff=0)
options.add_command(label='confinement',command=confinement)
options.add_command(label='deconfinement',command=deconfinement)
mainmenu.add_cascade(label='OPTIONS',menu=options)



 
root.config(menu = mainmenu)
root.mainloop()
