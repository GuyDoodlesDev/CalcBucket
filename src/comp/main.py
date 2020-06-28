from tkinter import *

def fLibrary():
    print("clicked \"Library\"!")
    
def fMarket():
    print("clicked \"Market\"!")

def fLeaderboard():
    print("clicked \"Leaderboard\"!")

def fConfig():
    print("clicked \"Config\"!")

root = Tk()
root.wm_title("CalcBucket")
galleryFrame = Frame(root).pack( side = LEFT)
menuFrame = Frame(root).pack( side = LEFT )
Scrollbar(galleryFrame, bg="green").pack(side = RIGHT, fill = Y )
bLibrary = Button(menuFrame, text="Library", width=17, command=fLibrary).pack(anchor='w')
bMarket = Button(menuFrame, text="Market", width=17, command=fMarket).pack(anchor='w')
bLeaderboard = Button(menuFrame, text="Leaderboard",  width=17, command=fLeaderboard).pack(anchor='w')
bConfig = Button(menuFrame, text="Config", width=17, command=fConfig).pack(anchor='w')
root.mainloop()
