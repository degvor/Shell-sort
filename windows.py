import random
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

import classes


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.size_massiv = tk.Entry(self)
        self.min_value = tk.Entry(self)
        self.max_value = tk.Entry(self)

        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0)

        file_menu.add_command(label="Graph Sort", command=self.show_window_graph)
        file_menu.add_command(label="Open", command=self.destroy)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Exit", command=self.destroy)

        menu.add_cascade(label="Menu", menu=file_menu)
        self.config(menu=menu)

        self.button_gen_massiv = tk.Button(self, text="Generate massiv",
                                           command=lambda: [self.show_size_massiv(),
                                                            self.generate_massiv(), self.show_generated_massiv()])
        self.button_classic_shell = tk.Button(self, text="Classic shell sort", command=self.show_classic_shell)
        self.button_sedgewick_sort = tk.Button(self, text="Sedgewick shell sort", command=self.show_sedgewick_sort)
        self.button_fibonachi_sort = tk.Button(self, text="Fibonachi shell sort", command=self.show_fibonachi_sort)
        self.button_tokuda_sort = tk.Button(self, text="Tokuda shell sort", command=self.show_tokuda_sort)

        self.label_text1 = tk.Label(text='Enter size of massiv: ')
        self.label_text2 = tk.Label(text='Enter min value: ')
        self.label_text3 = tk.Label(text='Enter max value: ')
        self.label_show_size = tk.Label(self, text="")
        self.label_show_massiv = tk.Label(self, text="", wraplength=1500)
        self.label_show_sorted = tk.Label(self, wraplength=1500)
        self.label_show_comparisons = tk.Label(self, text="")
        self.label_show_transposition = tk.Label(self, text="")
        self.text_show_massiv = tk.Text(self, height=90, width=90)
        self.text_show_massiv.place(x=0, y=0)
        self.text_show_sorted = tk.Text(self, height=90, width=90)
        self.text_show_sorted.place(x=800, y=0)

        self.massiv = []
        self.sorted_massiv = []

        self.label_text1.place(x=1600, y=25)
        self.size_massiv.place(x=1600, y=50)
        self.label_text2.place(x=1600, y=75)
        self.min_value.place(x=1600, y=100)
        self.label_text3.place(x=1600, y=125)
        self.max_value.place(x=1600, y=150)
        self.label_show_size.place(x=1600, y=175)
        self.label_show_massiv.place(x=0, y=0)
        self.label_show_sorted.place(x=0, y=450)
        self.label_show_comparisons.place(x=1600, y=200)
        self.label_show_transposition.place(x=1600, y=225)
        self.button_gen_massiv.place(x=1600, y=250)
        self.button_classic_shell.place(x=1600, y=275)
        self.button_sedgewick_sort.place(x=1600, y=300)
        self.button_fibonachi_sort.place(x=1600, y=325)
        self.button_tokuda_sort.place(x=1600, y=350)

    def show_size_massiv(self):
        value = self.size_massiv.get()
        text = "Size of generated massiv {}".format(value)
        self.label_show_size.config(text=text)

    def save_file(self):
        filepath = asksaveasfilename(
            defaultextension=".array",
            filetypes=[("Array files", "*.array"), ("All files", "*.*")],
        )
        if not filepath:
            return
        massiv_of_numbers = self.massiv[0]
        comparisons = str(self.massiv[1])
        transposition = str(self.massiv[2])

        for i, element in enumerate(massiv_of_numbers):
            massiv_of_numbers[i] = str(element)
        massiv_str = ';'.join(massiv_of_numbers)
        file = open(filepath, "w+")
        for i in range(len(massiv_str)):
            file.write(massiv_str[i])
            if i == len(massiv_str) - 1:
                file.write('\n')
        file.write('Comparisons: ' + comparisons + '\n')
        file.write('Transposition: ' + transposition + '\n')
        file.close()

    def generate_massiv(self):
        massiv = classes.Massiv(int(self.size_massiv.get()), int(self.min_value.get()),
                                int(self.max_value.get())).generation_massiv()
        self.massiv = massiv

    def show_generated_massiv(self):
        self.text_show_massiv.delete(1.0, tk.END)
        massiv = self.massiv
        text = str(massiv)
        self.text_show_massiv.insert(tk.END, text)

    def show_classic_shell(self):
        self.text_show_sorted.delete(1.0, tk.END)
        massiv = self.massiv.copy()
        sorted_massiv = classes.Sort(massiv).classic_shell_sort()
        comparisons = str(sorted_massiv[len(sorted_massiv) - 2])
        transposition = str(sorted_massiv[len(sorted_massiv) - 1])
        text = str(sorted_massiv[0])
        self.text_show_sorted.insert(tk.END, text)
        self.label_show_comparisons.config(text=comparisons)
        self.label_show_transposition.config(text=transposition)
        self.sorted_massiv = sorted_massiv

    def show_sedgewick_sort(self):
        self.text_show_sorted.delete(1.0, tk.END)
        massiv = self.massiv.copy()
        sorted_massiv = classes.Sort(massiv).sedgewick_shell_sort()
        comparisons = str(sorted_massiv[len(sorted_massiv) - 2])
        transposition = str(sorted_massiv[len(sorted_massiv) - 1])
        text = str(sorted_massiv[0])
        self.text_show_sorted.insert(tk.END, text)
        self.label_show_comparisons.config(text=comparisons)
        self.label_show_transposition.config(text=transposition)
        self.sorted_massiv = sorted_massiv

    def show_fibonachi_sort(self):
        self.text_show_sorted.delete(1.0, tk.END)
        massiv = self.massiv.copy()
        sorted_massiv = classes.Sort(massiv).fibonachi_shell_sort()
        comparisons = str(sorted_massiv[len(sorted_massiv) - 2])
        transposition = str(sorted_massiv[len(sorted_massiv) - 1])
        text = str(sorted_massiv[0])
        self.text_show_sorted.insert(tk.END, text)
        self.label_show_comparisons.config(text=comparisons)
        self.label_show_transposition.config(text=transposition)
        self.sorted_massiv = sorted_massiv

    def show_tokuda_sort(self):
        self.text_show_sorted.delete(1.0, tk.END)
        massiv = self.massiv.copy()
        sorted_massiv = classes.Sort(massiv).tokuda_shell_sort()
        comparisons = str(sorted_massiv[len(sorted_massiv) - 2])
        transposition = str(sorted_massiv[len(sorted_massiv) - 1])
        text = str(sorted_massiv[0])
        self.text_show_sorted.insert(tk.END, text)
        self.label_show_comparisons.config(text=comparisons)
        self.label_show_transposition.config(text=transposition)
        self.sorted_massiv = sorted_massiv

    def show_window_graph(self):
        app = GraphicSort()
        app.title("Graphic sort")
        app.mainloop()


class GraphicSort(tk.Tk):
    def __init__(self):
        super().__init__()
        menu = tk.Menu(self)
        menu.add_command(label="Exit", command=self.destroy)
        self.config(menu=menu)
        self.canvas = tk.Canvas(self, width=800, height=600, background="black")
        self.button_gen = tk.Button(self, text="Generate graphic columns", command=self.create_graph)
        self.button_classic = tk.Button(self, text="Sort by classic shell", command=self.sort_graph_classic)
        self.button_sedgewick = tk.Button(self, text="Sort by sedgewick", command=self.sort_graph_sedgewick)
        self.button_fibo = tk.Button(self, text="Sort by fibo", command=self.sort_graph_fibo)
        self.button_tokuda = tk.Button(self, text="Sort by tokuda", command=self.sort_graph_tokuda)
        self.button_dell = tk.Button(self, text="Clear", command=self.dell_draw)
        self.label_comparisons = tk.Label(self, text="")
        self.label_transposition = tk.Label(self, text="")
        self.canvas.pack()
        self.label_comparisons.pack()
        self.label_transposition.pack()
        self.button_gen.pack()
        self.button_classic.pack()
        self.button_sedgewick.pack()
        self.button_fibo.pack()
        self.button_tokuda.pack()
        self.button_dell.pack()

    def create_graph(self):
        self.canvas.delete("all")
        position = [0 for _ in range(0, 54)]
        height = [0 for _ in range(0, 54)]
        for i in range(0, 54):
            if i == 0:
                position[i] = 5
            else:
                position[i] = i * 15
        for i in range(0, 54):
            height[i] = random.randint(1, 600)

        for i in range(0, 54):
            self.canvas.create_line(position[i], 600, position[i], height[i], fill="green", width=4)
        self.height = height
        self.position = position

    def sort_graph_classic(self):
        self.canvas.delete("all")
        sorted_height = classes.Sort(self.height.copy()).classic_shell_sort()
        text = sorted_height[0]
        text_rev = text[::-1]
        comparisons = sorted_height[1]
        transposition = sorted_height[2]
        for i in range(len(text)):
            self.canvas.create_line(self.position[i], 600, self.position[i], text_rev[i], fill="red", width=4)
        self.label_comparisons.config(text=comparisons)
        self.label_transposition.config(text=transposition)

    def sort_graph_sedgewick(self):
        self.canvas.delete("all")
        sorted_height = classes.Sort(self.height.copy()).sedgewick_shell_sort()
        text = sorted_height[0]
        text_rev = text[::-1]
        comparisons = sorted_height[1]
        transposition = sorted_height[2]
        for i in range(len(text)):
            self.canvas.create_line(self.position[i], 600, self.position[i], text_rev[i], fill="red", width=4)
        self.label_comparisons.config(text=comparisons)
        self.label_transposition.config(text=transposition)

    def sort_graph_fibo(self):
        self.canvas.delete("all")
        sorted_height = classes.Sort(self.height.copy()).fibonachi_shell_sort()
        text = sorted_height[0]
        text_rev = text[::-1]
        comparisons = sorted_height[1]
        transposition = sorted_height[2]
        for i in range(len(text)):
            self.canvas.create_line(self.position[i], 600, self.position[i], text_rev[i], fill="red", width=4)
        self.label_comparisons.config(text=comparisons)
        self.label_transposition.config(text=transposition)

    def sort_graph_tokuda(self):
        self.canvas.delete("all")
        sorted_height = classes.Sort(self.height.copy()).tokuda_shell_sort()
        text = sorted_height[0]
        text_rev = text[::-1]
        comparisons = sorted_height[1]
        transposition = sorted_height[2]
        for i in range(len(text)):
            self.canvas.create_line(self.position[i], 600, self.position[i], text_rev[i], fill="red", width=4)
        self.label_comparisons.config(text=comparisons)
        self.label_transposition.config(text=transposition)

    # x0(position) y0(static)  x1(static) y1(height)

    def dell_draw(self):
        self.label_comparisons.config(text="")
        self.label_transposition.config(text="")
        self.canvas.delete("all")


app = MainWindow()
