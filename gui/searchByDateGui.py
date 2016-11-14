import Tkinter as tk

def createWindow():
    win = tk.Toplevel()
    win.title("Search By Date")
    win.geometry("300x200")
    itemName = tk.Label(win, text = "Enter Date:")
    itemName.grid(row=10, column = 2)
    itemNameEntry = tk.Entry(win)
    barcodeEntry.grid(row=10, column = 4, columnspan=3)
    searchButton = tk.Button(win, text="SEARCH")
    saveButton.grid(row = 15, column =4, columnspan=2)