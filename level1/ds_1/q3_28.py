# ~~~ This is a template for question 3  ~~~


# imports
from q1_28 import merge_sort_implementation
from q2_28 import insertion_sort_implementation
import pandas as pd
import matplotlib.pyplot as plt


# load data:
# Load the Excel file with multiple sheets:
excel_file = pd.ExcelFile("data.xlsx")

insertion_counts = []
merge_counts = []
sheet_numbers = []

# sort data and save results:
# For each sheet:
for idx, sheet_name in enumerate(excel_file.sheet_names):
    df = excel_file.parse(sheet_name)
    column = df.columns[0]
    data = df[column].dropna().tolist()

    # Run both sorting algorithms
    # insertion sort:
    insertion_sorted, insertion_ops = insertion_sort_implementation(data.copy())
    # merge_sort:
    merge_sorted, merge_ops = merge_sort_implementation(data.copy())

    # Collect the data
    sheet_numbers.append(idx + 1)
    insertion_counts.append(insertion_ops)
    merge_counts.append(merge_ops)


# plot figure:
plt.figure(figsize=(8, 6))
plt.plot(sheet_numbers, insertion_counts, label='Insertion Sort', color='orange')
plt.plot(sheet_numbers, merge_counts, label='Merge Sort', color='blue')

plt.xlabel("Sheet No.")
plt.ylabel("Count (Operations)")
plt.title("Question 3:")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
