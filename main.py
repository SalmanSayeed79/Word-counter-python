#word counter
from tkinter import *
from PIL import Image
#normal mode
def normal_scan():
    file=open('text.txt')

    string=file.readline()
    words=string.split()
    count=0
    for i in words:
        count+=1
    label1 = Label(root, text='{}'.format(count))
    label1.pack(side=TOP)
#optimised mode
def optimised_scan():
    file = open('text.txt')
    commmon_words = ['a', 'of', 'the', 'and', 'to', 'with']
    string = file.readline()
    words = string.split()
    #print(words)
    count = 0
    for i in words:
        if i not in commmon_words:
            count += 1
    label2 = Label(root, text='{}'.format(count))
    label2.pack(side=TOP)


#taking input
file=open('text.txt')
#normal=normal_scan(file)
#optimised=optimised_scan(file)
#print(normal)
#print(optimised)

#creating the tkinter gui

root=Tk()
root.title('Word Counter')
root.geometry('500x500')
root.iconbitmap('logo.ico')
root.configure(bg='green')

#the welcome zone
#creating the entry field
label_empty=Label(root)
label_empty.pack(side=TOP)
entry1=Entry(root,width=100)
entry1.pack(side=TOP)
#creating the button
button1=Button(root,command=normal_scan,text='Normal Scan',padx=50,pady=8,font="Cambria",bg='red',fg='white',relief=RAISED,activebackground='blue')
button1.pack(side=TOP)
button2=Button(root,command=optimised_scan,text='Optimised Scan',padx=50,pady=8,font="Cambria")
button2.pack(side=TOP)



root.mainloop()