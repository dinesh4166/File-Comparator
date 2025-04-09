import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from itertools import zip_longest

class FileComparator:
    """
    A class for File comparison
    """
    def __init__(self, root):
        """
        The constructor for FileComparator class.
        It calls the grid_layout, create_menu, and create_widgets methods.
        """
        self.root = root
        self.root.title("File Comparator")
        self.grid_layout()
        self.create_menu()
        self.create_widgets()

    def grid_layout(self):
        """
        The function to configure layout
        """
        for val1 in range(2):
            self.root.rowconfigure(val1, weight=1)
        for val2 in range(6):
            self.root.columnconfigure(val2, weight=1)
        self.root.configure(bg="light blue")

    def create_menu(self):
        """
        The function to create the menu bar
        """
        self.my_menu = tk.Menu(self.root)
        self.root.config(menu=self.my_menu)

        file_menu = tk.Menu(self.my_menu)
        self.my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Choose File 1", command=self.choose_file_1)
        file_menu.add_separator()
        file_menu.add_command(label="Choose File 2", command=self.choose_file_2)

        self.my_menu.add_command(label="Compare", command=self.compare)
        self.my_menu.add_command(label="Exit", command=self.root.destroy)


    def create_widgets(self):
        """
        The function to create widgets
        """
        self.text_area1 = scrolledtext.ScrolledText(self.root, height=25, font=("Times New Roman", 15), state='disabled')
        self.text_area1.grid(row=1, column=0, columnspan=3, padx=10)
        

        self.text_area2 = scrolledtext.ScrolledText(self.root, height=25, font=("Times New Roman", 15), state='disabled')
        self.text_area2.grid(row=1, column=3, columnspan=3, padx=10)

        tk.Label(self.root, text="", relief="solid", height=2, width=103).grid(row=0, columnspan=2, padx=10)
        tk.Label(self.root, text="", relief="solid", height=2, width=103).grid(row=0, column=3, columnspan=2, padx=10)

        tk.Button(self.root, text="", width=3, height=1, bg="black", borderwidth=5, command=self.choose_file_1).grid(row=0, column=2, sticky="w", padx=(0, 10))
        tk.Button(self.root, text="", width=3, height=1, bg="yellow", borderwidth=5, command=self.choose_file_2).grid(row=0, column=5, sticky="w", padx=(0, 10))
        tk.Button(self.root, text="Compare", width=40, bg="lightgreen", borderwidth=8, command=self.compare).grid(row=2, column=1, columnspan=3)
        tk.Label(self.root, text="differences", relief="solid", bg="brown", fg="white", width=10).grid(row=2, column=0)

    def remove_bom(self, filename, encoding='utf-8'):
        """
        Function to remove byte order mark (BOM) from a file
        """
        with open(filename, 'r', encoding=encoding, errors='replace') as file:
            decoded_content = file.readlines()
        return decoded_content
    
    def choose_file_1(self):
        """
        Function to choose the first file
        """
        file1_name = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("Csv files", "*.csv"), ("Json files", ".*json")))
        if not file1_name:
            return
        tk.Label(self.root, text=file1_name, relief="solid", height=2, width=103).grid(row=0, columnspan=2, padx=10)
        if ".csv" in file1_name:
            self.data1 = self.remove_bom(file1_name)
        else:
            with open(file1_name, "r", encoding="utf-8-sig") as file1:
                self.data1 = file1.readlines()
            
        self.text_area1.config(state='normal')
        self.text_area1.delete(1.0, tk.END)
        self.text_area1.insert(tk.END, ''.join(self.data1))
        self.text_area1.config(state='disabled')

    def choose_file_2(self):
        """
        Function to choose the another file
        """
        file2_name = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("Csv files", "*.csv"), ("Json files", ".*json")))
        if not file2_name:
            return
        tk.Label(self.root, text=file2_name, relief="solid", height=2, width=103).grid(row=0, column=3, columnspan=2, padx=10)
        if ".csv" in file2_name:
            self.data3 = self.remove_bom(file2_name)
        else:
            with open(file2_name, "r", encoding="utf-8-sig") as file2:
                self.data3 = file2.readlines()
                
        self.text_area2.config(state='normal')
        self.text_area2.delete(1.0, tk.END)
        self.text_area2.insert(tk.END, ''.join(self.data3))
        self.text_area2.config(state='disabled')

    def compare(self):
        """
        Function to compare the chosen files
        """
        try:
            self.data1
        except AttributeError:
            messagebox.showwarning(title="Ooops", message="Please choose file 1")
            return

        try:
            self.data3
        except AttributeError:
            messagebox.showwarning(title="Ooops", message="Please choose file 2")
            return
        difference_count = 0
        self.text_area1.config(state='normal')
        self.text_area1.delete(1.0, tk.END)
        self.text_area2.config(state='normal')
        self.text_area2.delete(1.0, tk.END)
        self.text_area1.tag_configure('magenta', background='magenta')
        self.text_area2.tag_configure('magenta', background='magenta')

        for val1, val2 in zip_longest(self.data1, self.data3, fillvalue=""):
            if val1.rstrip() == val2.rstrip():
                self.text_area1.insert(tk.END, val1)
                self.text_area2.insert(tk.END, val2)
            else:
                self.text_area1.insert(tk.END, val1, 'magenta')
                self.text_area2.insert(tk.END, val2, 'magenta')
                difference_count += 1

        tk.Label(self.root, text=f"differences = {difference_count}", relief="solid", bg="brown", fg="white", width=20).grid(row=2, column=0)
        self.text_area1.config(state='disabled')
        self.text_area2.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = FileComparator(root)
    root.mainloop()
