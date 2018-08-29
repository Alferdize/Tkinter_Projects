# ------------------------------------------------Packages------------------------------------------------

from tkinter import Tk, Menu, filedialog, END, messagebox, simpledialog
import tkinter.scrolledtext as ScrolledText
import pyautogui
import time
import os

# ------------------------------------------------Main------------------------------------------------

if __name__ == "__main__":
    root = Tk(className = " Untitled - AlfEditor")
    w, h = pyautogui.size()
# ------------------------------------------------Function------------------------------------------------



    def newFile():
        # There is content
        if len(textArea.get('1.0', END+'-1c')) > 0:
            out = messagebox.askyesnocancel("Save","Do you want to save the file?")
            if out == True:
                saveFile()
            elif out == False:
                textArea.delete('1.0', END)
            else:
                print(out)
            
            


        
    def openFile():
        file = filedialog.askopenfilename(parent = root,
                                      title = 'Select a text file',
                                          filetypes=(("Text file","*.txt"),
                                                 ("All files","*")))

        root.title(os.path.basename(file.name) + " - AlfEditor")
        if file != None:
            contents = file.read()
            textArea.insert('1.0', contents)
            file.close()

    def saveFile():
        file = filedialog.asksaveasfile(mode='w',defaultextension=".txt",
                                        filetypes = (("Text file","*.txt"),
                                                     ("HTML file","*.html,*.htm"),
                                                 ("All files","*.*")))
        root.title(os.path.basename(file.name) + " - AlfEditor")


        if file != None:
            # slice off the last character from  get, as an extra return (enter) is added
            data = textArea.get('1.0', END+'-1c')
            file.write(data)
            file.close()

    def date_time():
        n = len(textArea.get('1.0', END+'-1c'))
        if n > 0:
            textArea.insert(n, time.strftime('%I:%M %D'))
        else:
            textArea.insert('1.0', time.strftime('%I:%M %D'))


    def FindInFile():
        findString = simpledialog.askstring("Find..","Enter String to be find")
        textData = textArea.get('1.0', END+'-1c')
        n = textData.upper().count(findString.upper())
        if textData.upper().count(findString.upper()) > 0:
            label = messagebox.showinfo("Result",findString + " has multiple occurences." + str(n))
        else:
            label = messagebox.showinfo("Result","No match Found.")
            
        

    def exitEdt():
        if messagebox.askyesnocancel("Quit","Are you sure you want to quit?") == True:
            root.destroy()


    def About():
        label = messagebox.showinfo("About","Alferize alternative to Notepad")
        
    def new():
        pass


    def new1(evt):
        print("1")

# ------------------------------------------------Elements------------------------------------------------
    textArea = ScrolledText.ScrolledText(root, width=w, height=h,font=("Times",14))
    textArea.pack()

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff = 0)
    filemenu.add_command(label = "New          Ctrl+N", command = newFile)
    filemenu.add_command(label = "Open...      Ctrl+N", command = openFile)
    filemenu.add_command(label = "Save         Ctrl+N", command = saveFile)
    filemenu.add_command(label = "Save as...", command = new)
    filemenu.add_separator()
    filemenu.add_command(label = "Page Setup...", command = new)
    filemenu.add_command(label = "Print...     Ctrl+N", command = new)
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = exitEdt)
    menubar.add_cascade(label = "File", menu = filemenu)
    editmenu = Menu(menubar, tearoff = 0)
    editmenu.add_command(label = "Undo          Ctrl+N", command = new)
    editmenu.add_separator()
    editmenu.add_command(label = "Cut           Ctrl+N", command = new)
    editmenu.add_command(label = "Copy          Ctrl+N", command = new)
    editmenu.add_command(label = "Paste         Ctrl+N", command = new)
    editmenu.add_command(label = "Delete        Ctrl+N",command = new)
    editmenu.add_separator()
    editmenu.add_command(label = "Find...      Ctrl+N", command = FindInFile)
    editmenu.add_command(label = "Find Next    Ctrl+N", command = new)
    editmenu.add_command(label = "Replace...   Ctrl+N", command = new)
    editmenu.add_command(label = "Go To...     Ctrl+N", command = new)
    editmenu.add_separator()
    editmenu.add_command(label = "Select All   Ctrl+N", command = new)
    editmenu.add_command(label = "Time/Date    Ctrl+N", command = date_time)
    menubar.add_cascade(label = "Edit", menu = editmenu)
    formatmenu = Menu(menubar, tearoff = 0)
    formatmenu.add_command(label = "Word Wrap", command = new)
    formatmenu.add_command(label = "Font...", command = new)
    formatmenu.add_cascade(label = "Format", menu = formatmenu)
    viewmenu = Menu(menubar, tearoff = 0)
    viewmenu.add_command(label = "Status Bar", command = new)
    menubar.add_cascade(label = "View", menu = viewmenu)
    helpmenu = Menu(menubar, tearoff = 0)
    helpmenu.add_command(label = "View License", command = new)
    helpmenu.add_command(label = "About AlfEditor", command = About)
    menubar.add_cascade(label = "Help", menu = helpmenu)
    textArea.bind("<Control-N>",new1)
    root.config(menu=menubar)

    #Keep Window Open
    root.mainloop()


