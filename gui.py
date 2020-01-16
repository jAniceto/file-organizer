from tkinter import *
from tkinter import filedialog
import tkinter.font as font
import os
import file_organizer as fo


main_font = ('Segoe UI Light', 12)
code_font = ('Consolas', 12)

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title('File Organizer')  # Width height
        master.geometry('455x550')  # Set window size
        master.configure(background='white')
        self.create_widgets()  # Create widgets/grid
        self.working_dir = fo.Directory()
        self.target_dir = fo.Directory()
        
    def create_widgets(self):
        # Title
        self.title = Label(self.master, text='File Organizer', font=('Segoe UI Light', 20), bg='white', padx=10, pady=10)
        self.title.grid(row=0, column=0, sticky=W)

        # Working Directory
        self.working_lb = Label(self.master, text='1) Working directory:', font=main_font, bg='white', padx=10, pady=10)
        self.working_lb.grid(row=1, column=0, sticky=W)
        self.working_text = StringVar()
        self.working_entry = Entry(self.master, textvariable=self.working_text, font=code_font, width=40, relief='flat', state='readonly')
        self.working_entry.grid(row=2, column=0, padx=10, ipady=5)
        self.select_btn = Button(self.master, text='Browse', font=main_font, relief='flat', command=self.select_working_dir)
        self.select_btn.grid(row=2, column=1)

        # Subdirectory selection list (sudirectories to merge)
        self.subdirs_list_lb = Label(self.master, text='2) Select directories to merge:', font=main_font, bg='white', padx=10, pady=10)
        self.subdirs_list_lb.grid(row=3, column=0, sticky=W)
        self.subdirs_listbox = Listbox(self.master, selectmode='multiple', width=40, font=code_font, relief='flat')
        self.subdirs_listbox.grid(row=4, column=0, sticky=W, padx=10)

        # Target directory
        self.target_lb = Label(self.master, text='3) Target directory for content:', font=main_font, bg='white', padx=10, pady=10)
        self.target_lb.grid(row=5, column=0, sticky=W)
        self.target_text = StringVar()
        self.target_entry = Entry(self.master, textvariable=self.target_text, width=40, font=code_font, relief='flat', state='readonly')
        self.target_entry.grid(row=6, column=0, sticky=W, padx=10, ipady=5)
        self.select_btn = Button(self.master, text='Browse', font=main_font, relief='flat', command=self.select_target_dir)
        self.select_btn.grid(row=6, column=1, sticky=N)

        # Merge files button
        self.merge_btn = Button(self.master, text='Merge content!', font=main_font, relief='flat', command=self.merge_content)
        self.merge_btn.grid(row=7, column=0, sticky=W, padx=10, pady=20)

    def select_target_dir(self):
        # Get directory
        dir_selected = filedialog.askdirectory()
        self.target_text.set(dir_selected)
        self.target_dir.path = dir_selected

    def select_working_dir(self):
        # Get directory
        dir_selected = filedialog.askdirectory()
        self.working_text.set(dir_selected)
        self.working_dir.path = dir_selected
        # Get working directory subdirectories
        self.working_dir.get_subdirs()
        # Clear listbox
        self.subdirs_listbox.delete(0, END)
        # Add subdirectories to listbox
        for item in self.working_dir.subdirs:
            self.subdirs_listbox.insert(END, item)

    def merge_content(self):
        # Get selected subdirectories
        selected_subdirs = [self.subdirs_listbox.get(idx) for idx in self.subdirs_listbox.curselection()]
        selected_subdirs_full_path = [os.path.join(self.working_dir.path, x) for x in selected_subdirs]
        # Move contents
        fo.merge_folders(selected_subdirs_full_path, self.target_dir.path)


root = Tk()
app = Application(master=root)
app.mainloop()
