import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()

os.makedirs("Dimtables", exist_ok=True)
os.makedirs("Facttable", exist_ok=True)

df = pd.read_csv("Data/hospitalnew.csv")

df["VisitDate"] = pd.to_datetime(df["VisitDate"], errors="coerce")

df["Patient"] = df["Patient"].str.strip().str.title()
df["Doctor"] = df["Doctor"].str.strip().str.title()
df["Department"] = df["Department"].str.strip().str.title()

df = df.drop_duplicates()

dim_patient = (
    df[["Patient", "City"]]
    .drop_duplicates()
    .reset_index(drop=True)
)

dim_patient.insert(
    0,
    "PatientID",
    range(1, len(dim_patient) + 1)  
)
dim_patient.rename(columns={"Patient": "PatientName"},inplace=True)

dim_doctor = (df[["Doctor", "Department"]].
              drop_duplicates(). reset_index(drop=True))

dim_doctor.insert(0, "DoctorID", range(1, len(dim_doctor)+1))

dim_doctor.rename(columns = {"Doctor":"Doctorname"}, inplace = True)

dim_Department = (df[["Department"]].
              drop_duplicates(). reset_index(drop=True))

dim_Department.insert(0, "DeptID", range(1, len(dim_Department)+1))

dim_Date = (
    df[["VisitDate"]]
    .drop_duplicates()
    .reset_index(drop=True)
)

dim_Date.insert(
    0,
    "DateID",
    range(1, len(dim_Date) + 1)
)

dim_Date["VisitDate"] = pd.to_datetime(dim_Date["VisitDate"])

dim_Date["Day"] = dim_Date["VisitDate"].dt.day
dim_Date["Month"] = dim_Date["VisitDate"].dt.month
dim_Date["Year"] = dim_Date["VisitDate"].dt.year


fact = df.merge(
    dim_patient,
    left_on=["Patient", "City"],
    right_on=["PatientName", "City"],
    how="left"
)


fact  = fact.merge(
    dim_doctor, left_on =["Doctor", "Department"],
    right_on = ["Doctorname", "Department"], how = "left"
)

fact = fact.merge(
    dim_Department,
    left_on="Department",
    right_on="Department",
    how="left"
)

fact["VisitDate"] = pd.to_datetime(fact["VisitDate"])
fact = fact.merge(dim_Date, 
                  left_on = "VisitDate", right_on = "VisitDate", how = "left")

fact_visit = fact[
    [
        "VisitID",
        "DateID",
        "PatientID",
        "DoctorID",
        "DeptID",
        "VisitType",
        "Diagnosis",
        "TreatmentCost"
    ]
]

dim_patient.to_csv("Dimtables/DimPatient.csv", index=False)
dim_doctor.to_csv("Dimtables/DimDoctor.csv", index=False)
dim_Department.to_csv("Dimtables/DimDepartment.csv", index=False)
dim_Date.to_csv("Dimtables/DimDate.csv", index=False)
fact_visit.to_csv("facttable/FactVisit.csv", index=False)


engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}")

with engine.begin() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS Hospital"))

engine.dispose()

engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/Hospital"
)

dimensions = {
    "DimPatient": dim_patient,
    "DimDoctor": dim_doctor,
    "DimDepartment": dim_Department,
    "DimDate": dim_Date,
    "Factvisit": fact_visit
}

for table_name, data in dimensions.items():

    data.to_sql(
        table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"{table_name} loaded")