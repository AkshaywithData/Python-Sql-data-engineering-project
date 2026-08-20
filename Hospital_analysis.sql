use hospital

#1 Patient Visit & Cost
select p.patientname, p.city, count(f.visittype), sum(f.treatmentcost)
from dimpatient p 
join factvisit f
on p.patientid = f.patientid
group by p.patientname, p.city

#2  Doctor Visit & Cost
select d.doctorname, count(f.visittype), sum(f.treatmentcost) as total, avg(f.treatmentcost) as averagecost
from dimdoctor d
join factvisit f
on d.doctorid = f.doctorid
group by d.doctorname

#3  Diagnosis Analysis
select diagnosis, count(visittype), sum(treatmentcost) 
from factvisit
group by diagnosis
order by sum(treatmentcost) desc

#4 City-wise Analysis
select  p.city, count(p.patientname),  count(f.visittype), sum(f.treatmentcost)
from dimpatient p 
join factvisit f
on p.patientid = f.patientid
group by p.city

#5 Daily Visit & Cost
select d.visitdate, count(d.visitdate), sum(f.treatmentcost)
from dimdate d
join factvisit f
on d.dateid = f.dateid
group by d.visitdate
order by d.visitdate





