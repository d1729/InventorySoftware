from tkinter import *

class MainGui:

    def __init__(self,parent):
        self.parent =parent
        self.initGui()

    def initGui(self):
        mainMenu = Menu(self.parent)
        self.parent.title("Inventory Software")
        self.parent.config(menu=mainMenu)
        self.parent.geometry("900x600")
        FileMenu = Menu(mainMenu)
        mainMenu.add_cascade(label="File", menu=FileMenu)
        FileMenu.add_command(label="Add an item..")
        SearchMenu = Menu(mainMenu)
        SearchMenu.add_command(label="BY ITEM NAME")
        SearchMenu.add_command(label="BY BRAND NAME")
        SearchMenu.add_command(label="BY DATE")
        SearchMenu.add_command(label="BY PRICE")
        mainMenu.add_cascade(label="Search", menu=SearchMenu)
        DeleteMenu = Menu(mainMenu)
        mainMenu.add_cascade(label="Remove", menu=DeleteMenu)
        SellItemMenu = Menu(mainMenu)
        mainMenu.add_cascade(label="Payment", menu=SellItemMenu)


def main():
    root = Tk() 
    app=MainGui(root)
    root.mainloop()

if __name__ == '__main__':
    main()
