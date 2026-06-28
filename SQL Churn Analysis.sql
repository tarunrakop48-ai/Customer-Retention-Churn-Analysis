create database Customer_Churn_DB;

use customer_churn_db;

create table customer_churn(CustomerID varchar(50), Gender varchar(20), SeniorCitizen int, Partner varchar(10), Dependents varchar(10), Tenure int, Phoeservices varchar(10), InternetService varchar(50), Contract varchar(50), PaymentMethod varchar(100), MonthkyCharges decimal(10,2), TotalCharges decimal(10,2), Chrun varchar(10));

select * from customer_churn limit 10;

select count(*) from customer_churn;

describe customer_churn;

select distinct churn from customer_churn;

select distinct contract from customer_churn;

select distinct internetservice from customer_churn;

select count(*) as total_cutomers from customer_churn;

select count(*) as Churned_cutomers from customer_churn where churn="yes";

select count(*) as Active_cutomers from customer_churn where churn="no";

select round(sum( case when churn="yes" then 1 else 0 end)*100.0/count(*),2) as churn_rate from customer_churn;

select round(avg(monthlycharges),2) as AVG_Monthly_charges from customer_churn;

select round(sum(monthlycharges),2) as revenue_lost from customer_churn where churn="yes";

select contract, count(*)as cutomers, sum(case when churn='YES' then 1 else 0 end) as churned,
round(sum(case when churn='yes' then 1 else 0 end)*100.0/count(*),2) as churn_rate from customer_churn group by contract order by churn_rate desc;

select internetservice, count(*)as cutomers, sum(case when churn='YES' then 1 else 0 end) as churned,
round(sum(case when churn='yes' then 1 else 0 end)*100.0/count(*),2) as churn_rate from customer_churn group by internetservice order by churn_rate desc;

select paymentmethod, count(*)as cutomers, sum(case when churn='YES' then 1 else 0 end) as churned,
round(sum(case when churn='yes' then 1 else 0 end)*100.0/count(*),2) as churn_rate from customer_churn group by Paymentmethod order by churn_rate desc;

select seniorcitizen, count(*)as cutomers, sum(case when churn='YES' then 1 else 0 end) as churned,
round(sum(case when churn='yes' then 1 else 0 end)*100.0/count(*),2) as churn_rate from customer_churn group by seniorcitizen;