# sql vs mysql ?
# what ara datatypes in sql ? chr, varchr, int(10),bool, date, decimal,text
# char vs varchar ?

# varchar vs text 
# boolean True/False  true/false 0 r 1 :--where isActive = False
# float()
# decimal()

# date :-- "yyyy-mm-dd" :-- "2023-07-23"
# constraints :--
# used to perform conditions on columns while isnerting the data 
# enum()
# default
# check()
# pk :-- no allowing of duplicates and maintain value should not be null
# fk :-- 
# not null :-- 
# unique :-- 

# opeartors :-- 
# airtmatic 
# logical :-- and or not 
# compa  :-- 
# special :-- between , like, in (), not in() , is null 

# between :-- and

# select *
# from employees
# where city="hyd" or dept = "IT";


# select *
# from employees
# where city in ("hyd","IT");


# sql types :--
# autocommit =1
# safe updates=1


# # set 
# # autocimmit=0
# ddl :--  create, alter, drop, rename, truncate
# dml :--  insert, update, delete
# dql :-- select 


# autocommit=0
# delete 
# commit  # per save
# roolback





# agg :-- sum, min, max, count, avg


# clauses :-  gby,ha,oby,limit,offset

where :-- used to perform comidtions on originla column rows

# select count(*) as totalEmps
# from employees # 1
# where totalEmps>=5 #2

having :-- used to perform condition on virtual columns which being created at output table


select dept, count(*) as totalEmps
from employees # 1
group by dept
having totalEmps>7