# Fundamentals-of-Data-Engineering
## 📌 Project Overview
This project demonstrates an **ETL (Extract, Transform, Load)** pipeline for healthcare data.  
It integrates **patients, doctors, and feedback data** to generate insights on revenue, patient feedback, and doctor performance.

The project also includes **data analysis & visualizations** to help hospital management make data-driven decisions.

---

## 🔹 Data Sources
- **doctors_info.csv** → Doctor details (ID, name, specialty).  
- **patients_data_with_doctor.csv** → Patient treatment details, costs, and assigned doctors.  
- **patient_feedback.json** → Patient feedback scores and review dates.  

---

## 🔹 ETL Process
1. **Extract**  
   - Data loaded from CSV & JSON files.

2. **Transform**  
   - Converted treatment dates & review dates to datetime.  
   - Standardized treatment cost & room cost.  
   - Calculated **total treatment revenue**.  
   - Categorized patient feedback into **Poor, Average, Good, Excellent**.  

3. **Load**  
   - Final processed dataset stored in `data_warehouse/processed_healthcare_data.csv`.

---

## 🔹 Data Analysis Tasks
- 📊 **Top 5 Doctors by Revenue**  
- 📊 **Revenue by Specialty**  
- 📊 **Monthly Revenue Trends**  
- 📊 **Top 10 Doctors by Patient Feedback Distribution**  

---

## 🔹 Visualizations
- **Bar Chart** → Top 5 doctors by revenue  
- **Line Chart** → Monthly revenue trend  
- **Stacked Bar Chart** → Feedback distribution (Top 10 doctors)  

---

## 🚀 Tech Stack
- **Python** (Pandas, Matplotlib)  
- **Jupyter Notebook / .py scripts**  
- **GitHub** (for version control & sharing)  

---

## 📂 Repository Structure
