from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

class Notepad:
    root = Tk()
    root.iconbitmap(r'C:\Users\Lenovo\Downloads\np.ico')         # Notepad icon
    root.title("Untitled - Notepad")                             # Default title
    root.geometry("700x400")
    TextArea = Text(root, font=("Arial", 12))                    # Text area to type
    TextArea.pack(expand=True, fill=BOTH)                        # Resizing Text area

    # Creating a menubar
    menubar = Menu(root)
    FileMenu = Menu(menubar, tearoff=0)                          # File
    EditMenu = Menu(menubar, tearoff=0)                          # Edit
    HelpMenu = Menu(menubar, tearoff=0)                          # Help


    # using Scrollbar in the text area for scrolling
    Scrollbar = Scrollbar(TextArea)
    file = None

    # Initialization Method
    def __init__(self):

        # Creating the File menu
        self.FileMenu.add_command(label="New", command=self.newFile)             # New feature to open a new file
        self.FileMenu.add_command(label="Save", command=self.saveFile)           # Save feature to save a file
        self.FileMenu.add_command(label="Open", command=self.openFile)           # Open feature to open any existing file
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit", command=self.quitApp)            # Exit feature to exit the notepad
        self.menubar.add_cascade(label="File", menu=self.FileMenu)

        # Creating the Edit menu
        self.EditMenu.add_command(label="Select All     (Ctrl+A)", command=self.selectall())         # Select all feature with shortcut key
        self.EditMenu.add_command(label="Cut               (Ctrl+X)", command=self.cut)              # Cut feature with shortcut key
        self.EditMenu.add_command(label="Copy            (Ctrl+C)", command=self.copy)               # Copy feature with shortcut key
        self.EditMenu.add_command(label="Paste            (Ctrl+V)", command=self.paste)             # Paste feature with shortcut key
        self.EditMenu.add_command(label="Delete", command=self.delete)                               # Delete feature to delete a note
        self.menubar.add_cascade(label="Edit", menu=self.EditMenu)

        # Creating the Help menu
        self.HelpMenu.add_command(label="About Notepad", command=self.showAbout)
        self.menubar.add_cascade(label="Help", menu=self.HelpMenu)


        self.root.config(menu=self.menubar)                       # Configuring menu bar to the root


        self.Scrollbar.pack(side=RIGHT, fill=Y)                   # Packing the scrollbar to the right side of notepad
        self.Scrollbar.config(command=self.TextArea.yview)        # We can see the Scrollbar in the y-axis
        self.TextArea.config(yscrollcommand=self.Scrollbar.set)

    # Function to exit the Notepad
    def quitApp(self):
        self.root.destroy()

    # Function to open a file in the Notepad
    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes = [("All files", "*.*"),("Text document", ".txt")])

        # If the user does not give any name of the file then the file will not be saved.
        if self.file == "":
            self.file = None
        # If the user gives the name then the file will get saved.
        else:
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.TextArea.delete(1.0, END)
            file = open(self.file, "r")
            self.TextArea.insert(1.0, file.read())
            file.close()

     # Function to create a new file in the Notepad
    def newFile(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.TextArea.delete(1.0, END)

    # Function to save a file in the Notepad
    def saveFile(self):
        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All files", "*.*"),("text document", ".txt")])
            if self.file == "":
                self.file = None
            else:
                # Save as a new file
                file = open(self.file, "w")
                file.write(self.TextArea.get(1.0,END))
                file.close()

                self.root.title(os.path.basename(self.file) + " - Notepad")

        else:
            # Save the file
            file = open(self.file, "w")
            file.write(self.TextArea.get(1.0, END))
            file.close()


    # Function to display the about of the Notepad
    def showAbout(self):
        showinfo("Notepad", "Notepad - Version : 1.0")


    def cut(self):
        self.TextArea.event_generate("<<Cut>>")

    def copy(self):
        self.TextArea.event_generate("<<Copy>>")

    def selectall(self):
        self.TextArea.event_generate("<<SelectAll>>")

    def paste(self):
        self.TextArea.event_generate("<<Paste>>")

    def delete(self):
        f = open('.txt', 'w')
        self.TextArea.delete(1.0, END)

    def run(self):
        self.root.mainloop()

notepad = Notepad()
notepad.run()



















