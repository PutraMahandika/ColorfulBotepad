'''
CATATAN:
Sebelum menjalankan program, mohon ubah direktori terlebih dahulu untuk menghindari error.
ubah direktori di sekitar baris 15,30 dan 202
'''

from tkinter import *
from email import message
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import pickle

#ubah direktori di bawah, contoh: C:\\fileAnda\\notepad\\MainMenu
os.chdir("C:\\Users\\ASUS\\Desktop\\UltraSecret\\code\\python\\semester2\\notepad\\MainMenu")
def list():
    def cross_off_item():
        lb.itemconfig(
            lb.curselection(),
            fg="#dedede")
        lb.selection_clear(0, END)

    def uncross_item():
        lb.itemconfig(
            lb.curselection(),
            fg="#464646")
        lb.selection_clear(0, END)

    #ubah direktori di bawah, contoh: C:\\fileAnda\\notepad\\list
    os.chdir("C:\\Users\\ASUS\\Desktop\\UltraSecret\\code\\python\\semester2\\notepad\\list")
    def savefile():
        file_name = filedialog.asksaveasfilename(
            initialdir="C:/gui/data",
            title="Save File",
            filetypes=(
                ("Dat Files", "*.dat"), 
                ("All Files", "*.*"))
            )
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'
            stuff = lb.get(0, END)
            output_file = open(file_name, 'wb')
            pickle.dump(stuff, output_file)
            output_file.close()


    def openfile():
        file_name = filedialog.askopenfilename(
            initialdir="C:/gui/data",
            title="Open File",
            filetypes=(
                ("Dat Files", "*.dat"), 
                ("All Files", "*.*"))
            )

        if file_name:
            lb.delete(0, END)
            input_file = open(file_name, 'rb')
            stuff = pickle.load(input_file)
            input_file.close()
            for item in stuff:
                lb.insert(END, item)

    def newTask():
        task = my_entry.get()
        if task != "":
            lb.insert(END, task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("Peringatan", "Mohon masukkan input !")

    def deleteTask():
        lb.delete(ANCHOR)
        
    ws = Toplevel()
    ws.geometry('500x500')
    ws.title('Daftar catatan')
    ws.config(bg='#223441')
    ws.resizable(width=False, height=False)

    frame = Frame(ws)
    frame.pack(pady=10)

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb = Listbox(
        frame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#a6a6a6',
        activestyle="none",
        
    )
    lb.pack(side=TOP, fill=BOTH)

    sbb = Scrollbar(frame, orient="horizontal")
    sbb.pack(side=BOTTOM, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)
    lb.config(xscrollcommand=sbb.set)
    sbb.config(command=lb.xview)


    my_entry = Entry(
        ws,
        font=('times', 24)
        )

    my_entry.pack(pady=(20,5))

    button_frame = Frame(ws,bg='#223441')
    button_frame.pack(pady=20)

    button_frame2 = Frame(button_frame, bg='#c5f776')
    button_frame2.pack(side=BOTTOM, pady=5)

    addTask_btn = Button(
        button_frame,
        text='Tambah',
        font=('times 14'),
        bg='#c5f776',
        padx=20,
        pady=10,
        command=newTask
    )
    addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    delTask_btn = Button(
        button_frame,
        text='Hapus',
        font=('times 14'),
        bg='#ff8b61',
        padx=20,
        pady=10,
        command=deleteTask
    )
    delTask_btn.pack(fill=BOTH, expand=True, side=RIGHT)

    crossTask_btn = Button(
        button_frame2,
        text='Tandai',
        font=('times 14'),
        bg='#c5f776',
        padx=20,
        pady=10,
        command=cross_off_item
    )
    crossTask_btn.pack(side=LEFT)

    crossTask_btn = Button(
        button_frame2,
        text='Hapus Tanda',
        font=('times 14'),
        bg='#ff8b61',
        padx=1,
        pady=10,
        command=uncross_item
    )
    crossTask_btn.pack(side=RIGHT)

    open1 = PhotoImage(file=f"open.png")
    b0 = Button(
        ws,
        image=open1,
        borderwidth=0,
        highlightthickness=0,
        command=openfile,
        relief="flat")

    b0.place(
        x=0, y=0,
        width=70,
        height=32)

    save = PhotoImage(file=f"save.png")
    b8 = Button(
        ws,
        image=save,
        borderwidth=0,
        highlightthickness=0,
        command=savefile,
        relief="flat")

    b8.place(
        x=0, y=32,
        width=70,
        height=32)

    ws.mainloop()

def note():
    #ubah direktori di bawah, contoh: C:\\fileAnda\\notepad\\notepad
    os.chdir("C:\\Users\\ASUS\\Desktop\\UltraSecret\\code\\python\\semester2\\notepad\\notepad")
    def newfile():
        noteWindow.title("Colorful Notepad | Kelompok 12")
        file = None
        textarea.delete("1.0", "end")


    def openfile():
        file = filedialog.askopenfile(defaultextension="txt", filetypes=[
                                    ("All files", "*.*"), ("text Document", "*.txt")])
        file = file.name

        if file == "":
            file = None
        else:
            noteWindow.title(os.path.basename(file) + " - Colorful Notepad")
            textarea.delete("1.0", "end")
            file = open(file, "rb")
            textarea.insert(1.0, file.read())
            file.close()


    def savefile():
        global file
        if file == None:
            file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension="txt", filetypes=[
                ("All files", "*.*"), ("text Document", "*.txt")])
            if file == None:
                file = None
            else:
                file = open(file, "w")
                file.write(textarea.get("1.0", "end"))
                file.close()
                file = file.name
                noteWindow.title(os.path.basename(file) + " - Colorful Notepad")
        else:
            file = open(file, "w")
            file.write(textarea.get("1.0", "end"))
            file.close()


    def exitapp():
        noteWindow.destroy()


    def cutedit():
        textarea.event_generate("<<Cut>>")


    def copyedit():
        textarea.event_generate("<<Copy>>")


    def pasteedit():
        textarea.event_generate("<<Paste>>")


    def abouthelp():
        messagebox, messagebox.showinfo(
            "Notepad", "Aplikasi Notepad ini dibuat oleh kelompok 12 untuk memenuhi final project UAS AlgPro Semester 2")


    noteWindow = Toplevel()
    noteWindow.title("Colorful Notepad | Kelompok 12")
    global file
    file = None
    noteWindow.geometry("800x500")
    noteWindow.configure(bg="#ffffff")
    canvas = Canvas(
        noteWindow,
        bg="#ffffff",
        height=500,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"background.png")
    background = canvas.create_image(
        400.0, 251.0,
        image=background_img)

    textarea = Text(
        noteWindow,
        bd=10,
        padx=5,
        pady=5,
        bg="#d9d9d9",
        highlightthickness=0)

    textarea.place(
        x=0, y=32,
        width=800,
        height=466)

    open1 = PhotoImage(file=f"open.png")
    b0 = Button(
        noteWindow,
        image=open1,
        borderwidth=0,
        highlightthickness=0,
        command=openfile,
        relief="flat")

    b0.place(
        x=100, y=0,
        width=100,
        height=32)

    new = PhotoImage(file=f"new.png")
    b2 = Button(
        noteWindow,
        image=new,
        borderwidth=0,
        highlightthickness=0,
        command=newfile,
        relief="flat")

    b2.place(
        x=0, y=0,
        width=100,
        height=32)

    exit = PhotoImage(file=f"exit.png")
    b3 = Button(
        noteWindow,
        image=exit,
        borderwidth=0,
        highlightthickness=0,
        command=exitapp,
        relief="flat")

    b3.place(
        x=700, y=0,
        width=100,
        height=32)

    about = PhotoImage(file=f"about.png")
    b4 = Button(
        noteWindow,
        image=about,
        borderwidth=0,
        highlightthickness=0,
        command=abouthelp,
        relief="flat")

    b4.place(
        x=600, y=0,
        width=100,
        height=32)

    paste = PhotoImage(file=f"paste.png")
    b5 = Button(
        noteWindow,
        image=paste,
        borderwidth=0,
        highlightthickness=0,
        command=pasteedit,
        relief="flat")

    b5.place(
        x=500, y=0,
        width=100,
        height=32)

    copy = PhotoImage(file=f"copy.png")
    b6 = Button(
        noteWindow,
        image=copy,
        borderwidth=0,
        highlightthickness=0,
        command=copyedit,
        relief="flat")

    b6.place(
        x=400, y=0,
        width=100,
        height=32)

    cut = PhotoImage(file=f"cut.png")
    b7 = Button(
        noteWindow,
        image=cut,
        borderwidth=0,
        highlightthickness=0,
        command=cutedit,
        relief="flat")

    b7.place(
        x=300, y=0,
        width=100,
        height=32)

    save = PhotoImage(file=f"save.png")
    b8 = Button(
        noteWindow,
        image=save,
        borderwidth=0,
        highlightthickness=0,
        command=savefile,
        relief="flat")

    b8.place(
        x=200, y=0,
        width=100,
        height=32)

    noteWindow.resizable(False, False)
    noteWindow.mainloop()

def exitWindow():
    window.destroy()

window = Tk()

window.title("Colorful Notepad | Kelompok 12")
window.iconbitmap("note.ico")
window.geometry("800x600")
window.configure(bg = "#ebebeb")
canvas = Canvas(
    window,
    bg = "#ebebeb",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    535.5, 530.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    window,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = list,
    relief = "flat")

b0.place(
    x = 272, y = 380,
    width = 208,
    height = 46)

newNoteBtn = PhotoImage(file = f"img1.png")
b1 = Button(
    image = newNoteBtn,
    borderwidth = 0,
    highlightthickness = 0,
    command = note,
    relief = "flat")

b1.place(
    x = 272, y = 317,
    width = 208,
    height = 55)

exitBtn = PhotoImage(file = f"img2.png")
b2 = Button(
    image = exitBtn,
    borderwidth = 0,
    highlightthickness = 0,
    command = exitWindow,
    relief = "flat")

b2.place(
    x = 317, y = 443,
    width = 118,
    height = 46)

window.resizable(False, False)
window.mainloop()
