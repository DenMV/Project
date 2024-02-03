#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Сортировка последовательности")

entry_label = tk.Label(root, text="Введите последовательность целых чисел через запятую:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

combo = ttk.Combobox(root, values=['Пузырьком', 'Пирамидальная', 'Быстрая'])
combo.current(0)
combo.pack(pady=10)

def sort_sequence():
    try:
        sequence = entry.get()
        validate_input(sequence)
        
        numbers = [int(num) for num in sequence.split(',')]
        
        sort_type = combo.get()
        
        start_time = time.time()
        
        if sort_type == 'Пузырьком':
            numbers = bubble_sort(numbers)
        elif sort_type == 'Пирамидальная':
            numbers = heap_sort(numbers)
        elif sort_type == 'Быстрая':
            numbers = quick_sort(numbers)
        
        end_time = time.time()
        
        output_text.delete('1.0', tk.END)  
        for num in numbers:
            output_text.insert(tk.END, f"{num}\n")
        output_text.insert(tk.END, f"Время сортировки: {end_time - start_time:.5f} секунд\n")
    except ValueError as ve:
        output_text.delete('1.0', tk.END)  
        output_text.insert(tk.END, f"Ошибка: {ve}\n")
    except Exception as e:
        output_text.delete('1.0', tk.END)  
        output_text.insert(tk.END, f"Ошибка: {str(e)}\n")

start_button = tk.Button(root, text="Start", command=sort_sequence)
start_button.pack(pady=10)

output_text = tk.Text(root, height=20, width=50)
output_text.pack(pady=10)

def validate_input(sequence):
    if not all(char.isdigit() or char in [','] for char in sequence):
        raise ValueError("В последовательности допускаются только числа и запятая.")
    if ';' in sequence:
        raise ValueError("Числа должны быть разделены запятыми, а не точками с запятой.")

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def heapify(numbers, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and numbers[i] < numbers[left]:
        largest = left

    if right < n and numbers[largest] < numbers[right]:
        largest = right

    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, n, largest)

def heap_sort(numbers):
    n = len(numbers)
    for i in range(n, -1, -1):
        heapify(numbers, n, i)
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)
    return numbers

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers.pop()
        items_greater = []
        items_lower = []
        for item in numbers:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

def test_sorting():
    numbers = [5, 1, 4, 2, 8]
    expected_output = [1, 2, 4, 5, 8]
    assert bubble_sort(numbers.copy()) == expected_output, "Тест пузырьковой сортировки не пройден"

    numbers = [5, 1, 4, 2, 8]
    expected_output = [1, 2, 4, 5, 8]
    assert heap_sort(numbers.copy()) == expected_output, "Тест пирамидальной сортировки не пройден"

    numbers = [5, 1, 4, 2, 8]
    expected_output = [1, 2, 4, 5, 8]
    assert quick_sort(numbers.copy()) == expected_output, "Тест быстрой сортировки не пройден"

root.mainloop()

test_sorting()


# In[ ]:




