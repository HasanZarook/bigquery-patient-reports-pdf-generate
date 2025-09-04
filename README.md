
# 🏥 Medicare Renal Failure Patient Report with BigQuery & ReportLab

This project uses **Google BigQuery** and **Python** to analyze Medicare datasets (2011–2014) and generate a **PDF report** with patient and payment details related to **renal failure**.

---

## 📂 Project Structure

```
.
├── renal_failure_report.py           # Main Python script
├── json id                           # GCP service account key (keep private)
├── DBLab7_PatientInfo_2021_CE_58.pdf # Generated PDF report
├── requirements.txt                  # Dependencies
└── README.md                         # Documentation
```

---

## ⚙️ Features

* Connects to **Google BigQuery** using a service account.
* Queries inpatient and outpatient datasets (`2011–2014`).
* Extracts:

  * Total number of inpatients with renal failure.
  * Total number of outpatients (all cases).
  * Average payment for inpatients.
  * Average payment for outpatients.
* Generates a **PDF report** (`DBLab7_PatientInfo_2021_CE_58.pdf`) with neatly formatted text.

---

## 📦 Requirements

Install dependencies before running:

```bash
pip install google-cloud-bigquery google-auth reportlab pandas
```

---

## ▶️ How to Run

1. Set up a **Google Cloud Service Account** and download its JSON key.
   Place it in your project folder.

2. Update the script to use your key:

   ```python
   credentials = service_account.Credentials.from_service_account_file(
       "your-key.json"
   )
   ```

3. Run the script:

   ```bash
   python renal_failure_report.py
   ```

4. Output:

   * A PDF file named **`DBLab7_PatientInfo_2021_CE_58.pdf`** will be created.
   * The report opens automatically in your default PDF viewer.

---

## 📊 Example Output in PDF

```
Payment Details for Patients with Renal Failure

Total number of in-patients in all medical centers     XXXX
Total number of outpatients in all medical centers     YYYY
Total avg amount paid to inpatient                     ZZZZ
Total avg amount paid to outpatient                    AAAA
```



## 👤 Author

**A.G. Hasan Zarook**
📍 University of Engineering and Technology, Lahore

