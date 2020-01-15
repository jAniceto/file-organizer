from tkinter import *
from tkinter import filedialog
import os


class Directory:
    def __init__(self):
        self.path = None
        self.subdirs = None

    def get_subdirs(self):
        subdirs = []
        for item in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, item)):
                continue
            else:
                subdirs.append(item)
        self.subdirs = subdirs
        return subdirs

    def subdirs_full_path(self):
        return [os.path.join(self.path, x) for x in self.subdirs]


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title('File Organizer')  # Width height
        master.geometry("700x400")  # Set window size
        self.create_widgets()  # Create widgets/grid
        self.working_dir = Directory()
        self.target_dir = Directory()
        
    def create_widgets(self):
        # Working Directory
        self.working_lb = Label(self.master, text="1) Working directory:", padx=10, pady=10)
        self.working_lb.grid(row=0, column=0, sticky=W)
        self.working_text = StringVar()
        self.working_entry = Entry(self.master, textvariable=self.working_text, width=50)
        self.working_entry.grid(row=1, column=0, padx=10)
        self.select_btn = Button(self.master, text="Select directory", command=self.select_working_dir)
        self.select_btn.grid(row=1, column=1)

        # Subdirectory selection list (sudirectories to merge)
        self.subdirs_list_lb = Label(self.master, text="2) Select directories to merge:", padx=10, pady=10)
        self.subdirs_list_lb.grid(row=2, column=0, sticky=W)
        self.subdirs_listbox = Listbox(self.master, selectmode='multiple', width=50)
        self.subdirs_listbox.grid(row=3, column=0, sticky=W, padx=10)

        # Target directory
        self.target_lb = Label(self.master, text="3) Target directory for content:", padx=10, pady=10)
        self.target_lb.grid(row=4, column=0, sticky=W)
        self.target_text = StringVar()
        self.target_entry = Entry(self.master, textvariable=self.target_text, width=50)
        self.target_entry.grid(row=5, column=0, sticky=N, padx=10)
        self.select_btn = Button(self.master, text="Select directory", command=self.select_target_dir)
        self.select_btn.grid(row=5, column=1, sticky=N)

        # Merge files button
        self.merge_btn = Button(self.master, text="Merge content!", command=self.merge_content)
        self.merge_btn.grid(row=6, column=0, sticky=W, padx=10)

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
        # Add subdirectories to listbox
        for item in self.working_dir.subdirs:
            self.subdirs_listbox.insert(END, item)

    def merge_content(self):
        # Get selected subdirectories
        selected_subdirs = [self.subdirs_listbox.get(idx) for idx in self.subdirs_listbox.curselection()]
        selected_subdirs_full_path = [os.path.join(self.working_dir.path, x) for x in selected_subdirs]

        print(f"Copy\n{selected_subdirs_full_path}\nto\n{self.target_dir.path}")


def listbox_width(list_items):
    len_max = 0
    for item in list_items:
        if len(item) > len_max:
            len_max = len(item)

root = Tk()
app = Application(master=root)
app.mainloop()
