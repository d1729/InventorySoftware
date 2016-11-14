import Tkinter as tk

def createWindow():
    win = tk.Toplevel()
    win.title("Search By Brand Name")
    win.geometry("300x100")
    brandName = tk.Label(win, text = "Brand Name:")
    brandName.grid(row=10, column = 2)
    brandNameEntry = tk.Entry(win)
    brandNameEntry.grid(row=10, column = 4, columnspan=3)
    searchButton = tk.Button(win, text="SEARCH")
    searchButton.grid(row = 15, column =4, columnspan=2)