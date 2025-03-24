import pandas as pd

data = {
    "Patient_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [45, 63, 30, 25, 56, 70, 40, 35],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "Scan_Type": ["MRI", "CT", "X-ray", "MRI", "CT", "X-ray", "MRI", "CT"],
    "Diagnosis": ["Tumor", "Fracture", "Healthy", "Tumor", "Fracture", "Healthy", "Tumor", "Fracture"],
    "Scan_Cost": [1200, 800, 300, 1100, 750, 320, 1300, 900]
}

df = pd.DataFrame(data)

# task 1.1
print(df.head())
print()
# task 1.2
print(f'Mean Age: {df.Age.mean()} and Mean Scan_Cost: {df.Scan_Cost.mean()}')
print()
# task 1.3
scan_counts = df["Scan_Type"].value_counts()
print(scan_counts)
print()

# task 2.1
tumor_patients = df[df["Diagnosis"] == "Tumor"]
print(tumor_patients)
print()
# task 2.2
print(f'Mean Mri: {df[df["Scan_Type"] == 'MRI'].Scan_Cost.mean()} Mean CT: {df[df["Scan_Type"] == 'CT'].Scan_Cost.mean()} Mean X-ray: {df[df["Scan_Type"] == 'X-ray'].Scan_Cost.mean()}')
print()
# task 2.3
fracture_patients = df[df["Diagnosis"] == "Fracture"].groupby(["Gender"]).size()
print(fracture_patients)
print()

# task 3.1
# Define a function to categorize scan cost
def categorize_scan_cost(cost):
    if cost > 1000:
        return "High"
    elif 500 <= cost <= 1000:
        return "Medium"
    else:
        return "Low"

# Apply function to create new column
df["Scan_Cost_Category"] = df["Scan_Cost"].apply(categorize_scan_cost)

# Display the updated DataFrame
print(df)

# task 3.2
avg_scan_cost_by_gender = df.groupby("Gender")["Scan_Cost"].mean()
print(avg_scan_cost_by_gender)

# bonus task
import matplotlib.pyplot as plt

# Calculate the average scan cost per scan type
avg_scan_cost_by_type = df.groupby("Scan_Type")["Scan_Cost"].mean()

# Plot the bar chart
plt.figure(figsize=(8, 5))
avg_scan_cost_by_type.plot(kind="bar", color=["blue", "green", "orange"])

# Customize the plot
plt.xlabel("Scan Type")
plt.ylabel("Average Scan Cost")
plt.title("Average Scan Cost by Scan Type")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()



