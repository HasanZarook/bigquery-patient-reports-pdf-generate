from google.cloud import bigquery
from reportlab.pdfgen import canvas
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
'your json id')

project_id = 'your json id'
client = bigquery.Client(credentials= credentials, project=project_id)

query_job = client.query("""
with `i_1` as (
    Select 	Sum(total_discharges)as a1 from `bigquery-public-data.medicare.inpatient_charges_2011`
    where drg_definition like '%RENAL%'
), 
`i_2` as (
    Select 	Sum(total_discharges)as a2 from `bigquery-public-data.medicare.inpatient_charges_2012`
    where drg_definition like '%RENAL%'
), 
`i_3` as (
    Select 	Sum(total_discharges)as a3 from `bigquery-public-data.medicare.inpatient_charges_2013`
    where drg_definition like '%RENAL%'
), 
`i_4` as (
    Select 	Sum(total_discharges)as a4 from `bigquery-public-data.medicare.inpatient_charges_2014`
    where drg_definition like '%RENAL%'
)
Select a1+a2+a3+a4 as Total_in from i_1, i_2, i_3, i_4 """)

query_job_2 = client.query("""
with `i_1` as (
    Select 	Sum(outpatient_services)as a1 from `bigquery-public-data.medicare.outpatient_charges_2011`
), 
`i_2` as (
    Select 	Sum(outpatient_services)as a2 from `bigquery-public-data.medicare.outpatient_charges_2012`
), 
`i_3` as (
    Select 	Sum(outpatient_services)as a3 from `bigquery-public-data.medicare.outpatient_charges_2013`
), 
`i_4` as (
    Select 	Sum(outpatient_services)as a4 from `bigquery-public-data.medicare.outpatient_charges_2014`
)


Select a1+a2+a3+a4 as Total_in from i_1, i_2, i_3, i_4
 """)


query_job_4 = client.query("""
with `i_1` as (
    Select 	AVg(average_total_payments)as a1 from `bigquery-public-data.medicare.outpatient_charges_2011`
), 
`i_2` as (
    Select 	AVg(average_total_payments)as a2 from `bigquery-public-data.medicare.outpatient_charges_2012`
), 
`i_3` as (
    Select 	AVg(average_total_payments)as a3 from `bigquery-public-data.medicare.outpatient_charges_2013`
), 
`i_4` as (
    Select 	AVg(average_total_payments)as a4 from `bigquery-public-data.medicare.outpatient_charges_2014`
)


Select Round(AVG(a1+a2+a3+a4), 3) as Total_in from i_1, i_2, i_3, i_4 
 """)



query_job_3 = client.query("""
with `i_1` as (
    Select 	AVg(average_total_payments)as a1 from `bigquery-public-data.medicare.inpatient_charges_2011`
), 
`i_2` as (
    Select 	AVg(average_total_payments)as a2 from `bigquery-public-data.medicare.inpatient_charges_2012`
), 
`i_3` as (
    Select 	AVg(average_total_payments)as a3 from `bigquery-public-data.medicare.inpatient_charges_2013`
), 
`i_4` as (
    Select 	AVg(average_total_payments)as a4 from `bigquery-public-data.medicare.inpatient_charges_2014`
)


Select Round(AVG(a1+a2+a3+a4), 3) as Total_in from i_1, i_2, i_3, i_4 
 """)

results = query_job.result()
results_2 = query_job_2.result()
results_3 = query_job_3.result()
results_4 = query_job_4.result()
a=results.to_dataframe()
a1 = results_2.to_dataframe()
a2 = results_3.to_dataframe()
a3 = results_4.to_dataframe()

b = str(a['Total_in'][0])
b1 = str(a1['Total_in'][0])
b2 = str(a2['Total_in'][0])
b3 = str(a3['Total_in'][0])


c = canvas.Canvas("DBLab7_PatientInfo_2021_CE_58.pdf")
c.setTitle("Patient Info")
c.setFont('Times-Bold', 27)
c.drawString(40, 750, "Payment Details for Patients with Renal Failure")
c.setFont('Times-Roman', 14)
c.drawString(40, 700, "Total number of in-patients in all medical centers")
c.drawString(400, 700, b)
c.drawString(40, 650, "Total number of outpatients in all medical centers")
c.drawString(400, 650, b1)
c.drawString(40, 600, "Total avg amount paid to inpatient")
c.drawString(400, 600, b2)
c.drawString(40, 550, "Total avg amount paid to outpatient")
c.drawString(400, 550, b3)

c.save()

import webbrowser

webbrowser.open("DBLab7_PatientInfo_2021_CE_58.pdf")

print("done")
