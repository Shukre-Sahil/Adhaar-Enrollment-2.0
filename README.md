# Adhaar-Enrollment-2.0

### An interactive analytics dashboard built using Streamlit and PostgreSQL to analyze enrollment trends across states and districts in India.
### The dashboard provides dynamic filtering, KPI tracking, demographic distribution, and automated insights generation.


## 🚀 Features:

- 🌍 State-wise filtering
- 📈 Monthly enrollment trend analysis
- 📊 Month-over-Month (MoM) growth calculation
- 🏆 Top 5 districts by enrollment
- 👶 Age-group distribution analysis
- 🧠 Automated key insights display
- 📌 Dynamic KPI updates based on selected state


## 🗂 Dataset

The dataset contains:
- State & district-level enrollment data
- Monthly enrollment volumes
- Age group breakdown:
    - age_0_5
    - age_5_17
    - age_18_greater

#### *Source: The UIDAI Aadhaar enrollment dataset available via the `Open Government Data (OGD) Platform India`*

## 🛠 Tech Stack
- ![Python](https://img.shields.io/badge/Python-3.x-blue)
- ![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
- ![SQL](https://img.shields.io/badge/SQL-Database-red)
- ![Pandas](https://img.shields.io/badge/pandas-white)

## 📸 Screenshots

<img width="1909" height="928" alt="image" src="https://github.com/user-attachments/assets/42281b33-5496-4122-af63-5de89f20be3e" />

<img width="1904" height="929" alt="image" src="https://github.com/user-attachments/assets/62470c6d-1fe3-4894-bd1d-90c3a019b112" />

<img width="1908" height="911" alt="image" src="https://github.com/user-attachments/assets/ab7e049f-58ab-41bf-9164-81678c5f605b" />

<img width="1905" height="911" alt="image" src="https://github.com/user-attachments/assets/5aff8ea2-5e2e-4a20-9958-9f5a36497724" />


## ⚙️ How To Run Locally

### 1️⃣ Clone Repository

`https://github.com/Shukre-Sahil/Adhaar-Enrollment-2.0.git`

### 2️⃣ Install Requirements

`pip install -r requirements.txt`


### 3️⃣ Setup Database

- Create PostgreSQL database and then table.
  - `table_creation.sql`
- Import dataset.
  - `Merged_dataset.zip`   
- Update database connection credentials in your app file


### 4️⃣ Run Streamlit App
`streamlit run streamlit_app.py`

#### For making your own dashboard you can create views and index as per your work and then use them into your streamlit_app.py.
#### Refer `view_creation.sql` and `indexes.sql` for your reference.
## 👤 Author

**Your Name: Sahil Shukre**


