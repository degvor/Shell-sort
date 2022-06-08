import random
import tkinter as tk
from time import sleep
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
        # file_menu.add_command(label="Open")
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
        massiv_of_numbers = self.sorted_massiv[0]
        comparisons = str(self.sorted_massiv[1])
        transposition = str(self.sorted_massiv[2])

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

    def draw_graph(self, massiv, comparisons, transposition, pos=-1):
        self.canvas.delete("all")
        rev = massiv[::-1]
        for i in range(len(massiv)):
            self.canvas.create_line(self.position[i], 600, self.position[i], rev[i],
                                    fill="yellow" if i == pos else "red", width=4)
        self.label_comparisons.config(text=comparisons)
        self.label_transposition.config(text=transposition)
        self.update()
        sleep(0.2)

    def sort_graph_classic(self):
        self.canvas.delete("all")
        comparisons = 0
        transposition = 0
        massiv = self.height.copy()
        step = len(massiv) // 2
        while step > 0:
            for i in range(step, len(massiv)):
                current_value = massiv[i]
                position = i
                comparisons += 1

                while position >= step and massiv[position - step] > current_value:
                    massiv[position] = massiv[position - step]
                    transposition += 1
                    position -= step
                    massiv[position] = current_value

                    self.draw_graph(massiv, comparisons, transposition, position)

            step //= 2

    def sort_graph_sedgewick(self):
        self.canvas.delete("all")
        comparisons = 0
        transposition = 0
        sorting_number = []
        massiv = self.height.copy()

        for i in range(0, len(massiv)):
            if i % 2 == 0:
                step = int(9 * 2 ** i - 9 * 2 ** (i / 2) + 1)
                sorting_number.append(step)
            else:
                step = int(8 * 2 ** i - 6 * 2 ** ((i + 1) / 2) + 1)
                sorting_number.append(step)
            if sorting_number[i] * 3 > len(massiv):
                break

        sorting_number.reverse()
        sorting_number = sorting_number[1:]

        last_index = len(massiv)

        for step in sorting_number:
            for i in range(step, last_index, 1):
                j = i
                delta = j - step

                while delta >= 0 and massiv[delta] > massiv[j]:
                    massiv[delta], massiv[j] = massiv[j], massiv[delta]
                    j = delta
                    delta = j - step
                    comparisons += 1
                    transposition += 1
                    self.draw_graph(massiv, comparisons, transposition, delta)
                if delta >= 0:
                    comparisons += 1

    def sort_graph_fibo(self):
        self.canvas.delete("all")

        comparisons = 0
        transposition = 0
        massiv = self.height.copy()

        Fibo_numbers = [0 for i in range(0, len(massiv))]
        for i in range(0, len(massiv)):
            if i == 0:
                Fibo_numbers[i] = 0
            elif i == 1:
                Fibo_numbers[i] = 1
            elif i >= 2:
                Fibo_numbers[i] = Fibo_numbers[i - 2] + Fibo_numbers[i - 1]
        Fibo_numbers.reverse()
        Fibo_numbers = Fibo_numbers[1:]

        last_index = len(massiv)

        for step in Fibo_numbers:
            for i in range(step, last_index, 1):
                j = i
                delta = j - step
                while delta >= 0 and massiv[delta] > massiv[j]:
                    massiv[delta], massiv[j] = massiv[j], massiv[delta]
                    j = delta
                    delta = j - step
                    transposition += 1
                    comparisons += 1
                    self.draw_graph(massiv, comparisons, transposition, delta)
                if delta >= 0:
                    comparisons += 1

    def sort_graph_tokuda(self):
        self.canvas.delete("all")

        comparisons = 0
        transposition = 0
        sorting_number = []
        massiv = self.height.copy()

        for i in range(0, 13):
            step = int(1 / 5 * (9 * (9 / 4) ** (i - 1) - 4))
            sorting_number.append(step)

        sorting_number.reverse()
        sorting_number = sorting_number[1:]
        last_index = len(massiv)

        for step in sorting_number:
            for i in range(step, last_index, 1):
                j = i
                delta = j - step
                while delta >= 0 and massiv[delta] > massiv[j]:
                    massiv[delta], massiv[j] = massiv[j], massiv[delta]
                    j = delta
                    delta = j - step
                    transposition += 1
                    comparisons += 1
                    self.draw_graph(massiv, comparisons, transposition, delta)
                if delta >= 0:
                    comparisons += 1

    def dell_draw(self):
        self.label_comparisons.config(text="")
        self.label_transposition.config(text="")
        self.canvas.delete("all")


app = MainWindow()
