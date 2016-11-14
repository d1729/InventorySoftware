import Tkinter as tk
import additem 
import searchByItemGui, searchByBrandGui

TITLE_FONT = ("Helvetica", 18, "bold")

def getClasses(mods):
    classes = []
    for m in mods:
        for name, data in inspect.getmembers(m, inspect.isclass):
            classes.append(name)
    return classes

class MainGui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        '''container = tk.Frame(self) #creating the main window
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (additem.addItem, additem.addItem):
            page_name = F.__name__
            frame = F(self, container)
            self.frames[page_name] = frame
        def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()'''
        mainMenu = tk.Menu(self)
        self.title("Inventory Software")
        self.config(menu=mainMenu)
        self.geometry("900x600")
        FileMenu = tk.Menu(mainMenu)
        mainMenu.add_cascade(label="File", menu=FileMenu)
        FileMenu.add_command(label="Add an item..", command = additem.createWindow)
        SearchMenu = tk.Menu(mainMenu)
        SearchMenu.add_command(label="BY ITEM NAME", command = searchByItemGui.createWindow)
        SearchMenu.add_command(label="BY BRAND NAME", command = searchByBrandGui.createWindow)
        SearchMenu.add_command(label="BY DATE")
        SearchMenu.add_command(label="BY PRICE")
        mainMenu.add_cascade(label="Search", menu=SearchMenu)
        DeleteMenu = tk.Menu(mainMenu)
        DeleteMenu.add_command(label="BY ITEM NAME")
        DeleteMenu.add_command(label="BY BRAND NAME")
        mainMenu.add_cascade(label="Remove", menu=DeleteMenu)
        SellItemMenu = tk.Menu(mainMenu)
        mainMenu.add_cascade(label="Payment", menu=SellItemMenu)

        

def main():
    root = MainGui()
    root.mainloop()

if __name__ == '__main__':
    main()
