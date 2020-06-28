from tkinter import *
import random
import string

def fLibrary():
    print("clicked \"Library\"!")
    
def fMarket():
    print("clicked \"Market\"!")

def fLeaderboard():
    print("clicked \"Leaderboard\"!")

def fConfig():
    print("clicked \"Config\"!")

def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

root = Tk()
root.geometry("1366x738")
root.wm_title("CalcBucket")
galleryFrame = Frame(root).pack(expand=0, fill=BOTH, side = RIGHT)
menuFrame = Frame(root).pack(fill=Y, side = LEFT )
scrollbar = Scrollbar(galleryFrame)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(galleryFrame, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, randomString(random.randint(27,69)))
listbox.pack(expand=1, fill=BOTH, side=RIGHT)
scrollbar.config(command=listbox.yview)
bLibrary = Button(menuFrame, text="Library", width=17, height=2, command=fLibrary).pack(anchor='w')
bMarket = Button(menuFrame, text="Market", width=17, height=2, command=fMarket).pack(anchor='w')
bLeaderboard = Button(menuFrame, text="Leaderboard",  width=17, height=2, command=fLeaderboard).pack(anchor='w')
bConfig = Button(menuFrame, text="Config", width=17, height=2, command=fConfig).pack(anchor='w')
root.mainloop()
