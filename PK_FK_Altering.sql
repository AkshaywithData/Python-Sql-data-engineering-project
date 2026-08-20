create database hospital;
use hospital;
SELECT COUNT(*) FROM DimPatient;
SELECT COUNT(*) FROM DimDoctor;
SELECT COUNT(*) FROM DimDepartment;
SELECT COUNT(*) FROM DimDate;
SELECT COUNT(*) FROM factvisit;
    
DESC DimPatient;
DESC DimDoctor;
DESC DimDepartment;
DESC DimDate;
DESC FactVisit;

ALTER TABLE DimPatient
ADD PRIMARY KEY (PatientID);

ALTER TABLE DimDoctor
ADD PRIMARY KEY (DoctorID);
ALTER TABLE DimDepartment
ADD PRIMARY KEY (DeptID);

ALTER TABLE DimDate
ADD PRIMARY KEY (DateID);

ALTER TABLE FactVisit
ADD PRIMARY KEY (VisitID);

ALTER TABLE FactVisit
ADD CONSTRAINT fk_fact
FOREIGN KEY (PatientID)
REFERENCES DimPatient(PatientID);

alter table factvisit
add constraint fk_fact2
foreign key (doctorid) references dimdoctor(doctorid);

ALTER TABLE FactVisit
ADD CONSTRAINT fk_fact_department
FOREIGN KEY (DeptID)
REFERENCES DimDepartment(Deptid);

ALTER TABLE FactVisit
ADD CONSTRAINT fk_fact_date
FOREIGN KEY (DateID)
REFERENCES DimDate(DateID);

