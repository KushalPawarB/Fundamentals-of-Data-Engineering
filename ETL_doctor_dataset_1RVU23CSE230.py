# Importing Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Reading Data from CSV and JSON Files
doctors_info_df = pd.read_csv("F:/Sem-5/Fundamentals of Data Engineering/Labs/Lab-2/raw_data/doctors_info.csv")
patient_feedback_df = pd.read_json("F:/Sem-5/Fundamentals of Data Engineering/Labs/Lab-2/raw_data/patient_feedback.json")
patients_df = pd.read_csv("F:/Sem-5/Fundamentals of Data Engineering/Labs/Lab-2/raw_data/patients_data_with_doctor.csv")

# Converting Dates in String Format to Datetime
patients_df["treatment_date"] = pd.to_datetime(patients_df["treatment_date"])
patient_feedback_df["review_date"] = pd.to_datetime(patient_feedback_df["review_date"])

# Ensuring Cost is Numeric
patients_df["treatment_cost"] = patients_df["treatment_cost"].astype(float)
patients_df["room_cost"] = patients_df["room_cost"].astype(float)

# Total Revenue per Treatment
patients_df["total_cost"] = patients_df["treatment_cost"] + patients_df["room_cost"]

# Merging Doctors and Patients Data
merged_df = patients_df.merge(doctors_info_df, on="doctor_id", how="left")

# Merging Patient Feedback with Patients Data
final_df = merged_df.merge(patient_feedback_df, on="patient_id", how="left")

# Finally Uploading Processed Data to Data Warehouse
os.makedirs("data_warehouse", exist_ok=True)
final_df.to_csv("data_warehouse/processed_healthcare_data.csv", index=False)
print("Processed data saved successfully!")



