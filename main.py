import tkinter as tk

def callback():
    print("click!")

class start_window(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        tk.Frame.pack(self)
        tk.Label(self, text = 'Test Window', width=30).pack()
        b = tk.Button(root, text="Test Button", command=callback)
        b.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("CalcBucket")
    start_window(root)
    root.mainloop()