# Hospital Data Engineering Project

## 1. Project Overview

The project starts with raw hospital data, cleans and transforms it using Python and Pandas, creates dimension and fact tables, loads the data into MySQL, establishes primary and foreign key relationships and performs SQL-based analysis.

## 2. Project Objective

The objective is to transform raw hospital visit data into a structured relational database using dimensional modelling and perform business analysis using SQL.


## 3. Project Workflow
```
Raw Hospital Data
       ↓
Python / Pandas Cleaning
       ↓
Dimension & Fact Table Creation
       ↓
CSV Export
       ↓
MySQL Data Loading
       ↓
Primary & Foreign Keys
       ↓
SQL Analysis
```

## 4. Project Structure

```
Hospital_Project/
│
├── Data/
│   └── hospitalnew.csv
│
├── Dimtables/
│   ├── DimPatient.csv
│   ├── DimDoctor.csv
│   ├── DimDepartment.csv
│   └── DimDate.csv
│
├── Facttable/
│   └── FactVisit.csv
│
├── python-sql-data-modelling.py
├── PK_FK_Altering.sql
├── Hospital_analysis.sql
├── .gitignore
├── requirements.txt
├── LICENSE
├── .env .exapmple
└── README.md
```

## 5. Data Cleaning

Python and Pandas are used to prepare the raw hospital data.

The cleaning process includes:

- Converting VisitDate into a date format
- Removing leading and trailing spaces
- Standardizing text using title case
- Removing duplicate records
- Preparing data for dimensional modelling


## 6. Database Design

The project uses a dimensional modelling approach consisting of dimension tables and a fact table.

  Dimension Tables
- DimPatient — Patient details and city
- DimDoctor — Doctor details and department
- DimDepartment — Department details
- DimDate — Visit date and date attributes

  Fact Table
- FactVisit — Hospital visit transactions containing visit type, diagnosis, and treatment cost.

## 7. MySQL Database

The transformed data is loaded into a MySQL database named:

**Hospital**

Python uses SQLAlchemy and PyMySQL to load the dimension and fact tables into MySQL.


## 8. SQL Analysis

The project contains queries for:

- Patient Visit & Cost
- Doctor Visit & Cost
- Diagnosis Analysis
- City-wise Analysis
- Daily Visit & Cost

The queries analyze patient visits, doctor performance, diagnosis costs, city-level activity, and daily visit trends.

## 9. SQL Concepts used

- CREATE DATABASE
- CREATE TABLE
- PRIMARY KEY
- FOREIGN KEY
- ALTER TABLE
-  INSERT
- JOIN
- GROUP BY
- ORDER BY
- COUNT()
- COUNT(DISTINCT)
- SUM()
- AVG()

## 10. Technologies Used

Programming & Libraries

- Python
- Pandas
- SQLAlchemy
- PyMySQL

Database & Tools

- MySQL
- MySQL Workbench
- VS Code
- Git
- GitHub

## 11. How to Run

Step 1 — 
```bash
pip install -r requirements.txt
```
Step 2 — Run the Python Script
```bash
python-sql-data-modelling.py
```
The script performs:

- Data cleaning
- Dimension table creation
- Fact table creation
- CSV export
- MySQL data loading

Step 3 — Create Primary & Foreign Keys

Open MySQL Workbench and run:

PK_FK_Altering.sql

Step 4 — Run Hospital_analysis

Run:

Hospital_analysis.sql to execute the hospital data analysis queries.

## 12. Project Outcome

```
The project demonstrates the complete flow:

Raw Data
   ↓
Python Cleaning
   ↓
Data Transformation
   ↓
Dimensional Modelling
   ↓
Fact & Dimension Tables
   ↓
MySQL
   ↓
Primary & Foreign Keys
   ↓
SQL Analysis
```

## Future Improvements 

- Implement incremental data loading
- Add automated pipeline scheduling
- Add advanced Power BI dashboard filtering and analytics
- Add database logging and error monitoring

## Author

**Akshay Gawand**