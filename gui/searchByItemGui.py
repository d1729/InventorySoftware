import Tkinter as tk

def createWindow():
    win = tk.Toplevel()
    win.title("Search By Item Name")
    win.geometry("300x100")
    itemName = tk.Label(win, text = "Item Name:")
    itemName.grid(row=10, column = 2)
    itemNameEntry = tk.Entry(win)
    itemNameEntry.grid(row=10, column = 4, columnspan=3)
    searchButton = tk.Button(win, text="SEARCH")
    searchButton.grid(row = 15, column =4, columnspan=2)