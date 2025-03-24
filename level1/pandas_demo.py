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


