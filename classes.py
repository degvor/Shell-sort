import random


class Massiv:
    def __init__(self, size, min_value, max_value):
        self.size = size
        self.min_value = min_value
        self.max_value = max_value

    def generation_massiv(self):
        massiv = [random.randint(self.min_value, self.max_value) for i in range(self.size)]
        return massiv


class Sort:
    def __init__(self, massiv):
        self.massiv = massiv

    def classic_shell_sort(self):
        comparisons = 0
        transposition = 0
        step = len(self.massiv) // 2
        while step > 0:
            for i in range(step, len(self.massiv)):
                current_value = self.massiv[i]
                position = i
                comparisons += 1

                while position >= step and self.massiv[position - step] > current_value:
                    self.massiv[position] = self.massiv[position - step]
                    transposition += 1
                    position -= step
                    self.massiv[position] = current_value
            step //= 2
        return self.massiv, comparisons, transposition

    def sedgewick_shell_sort(self):
        comparisons = 0
        transposition = 0
        sorting_number = []

        for i in range(0, len(self.massiv)):
            if i % 2 == 0:
                step = int(9 * 2 ** i - 9 * 2 ** (i / 2) + 1)
                sorting_number.append(step)
            else:
                step = int(8 * 2 ** i - 6 * 2 ** ((i + 1) / 2) + 1)
                sorting_number.append(step)
            if sorting_number[i] * 3 > len(self.massiv):
                break

        sorting_number.reverse()
        sorting_number = sorting_number[1:]

        last_index = len(self.massiv)

        for step in sorting_number:
            for i in range(step, last_index, 1):
                j = i
                delta = j - step

                while delta >= 0 and self.massiv[delta] > self.massiv[j]:
                    self.massiv[delta], self.massiv[j] = self.massiv[j], self.massiv[delta]
                    j = delta
                    delta = j - step
                    comparisons += 1
                    transposition += 1
                if delta >= 0:
                    comparisons += 1

        return self.massiv, comparisons, transposition

    def fibonachi_shell_sort(self):
        comparisons = 0
        transposition = 0

        Fibo_numbers = [0 for i in range(0, len(self.massiv))]
        for i in range(0, len(self.massiv)):
            if i == 0:
                Fibo_numbers[i] = 0
            elif i == 1:
                Fibo_numbers[i] = 1
            elif i >= 2:
                Fibo_numbers[i] = Fibo_numbers[i - 2] + Fibo_numbers[i - 1]
        Fibo_numbers.reverse()
        Fibo_numbers = Fibo_numbers[1:]

        last_index = len(self.massiv)

        for step in Fibo_numbers:
            for i in range(step, last_index, 1):
                j = i
                delta = j - step
                while delta >= 0 and self.massiv[delta] > self.massiv[j]:
                    self.massiv[delta], self.massiv[j] = self.massiv[j], self.massiv[delta]
                    j = delta
                    delta = j - step
                    transposition += 1
                    comparisons += 1
                if delta >= 0:
                    comparisons += 1

        return self.massiv, comparisons, transposition

    def tokuda_shell_sort(self):
        comparisons = 0
        transposition = 0
        sorting_number = []
        for i in range(0, 13):
            step = int(1 / 5 * (9 * (9 / 4) ** (i - 1) - 4))
            sorting_number.append(step)

        sorting_number.reverse()
        sorting_number = sorting_number[1:]
        last_index = len(self.massiv)

        for step in sorting_number:
            for i in range(step, last_index, 1):
                j = i
                delta = j - step
                while delta >= 0 and self.massiv[delta] > self.massiv[j]:
                    self.massiv[delta], self.massiv[j] = self.massiv[j], self.massiv[delta]
                    j = delta
                    delta = j - step
                    transposition += 1
                    comparisons += 1
                if delta >= 0:
                    comparisons += 1

        return self.massiv, comparisons, transposition
