load data
into table tbw_hoge
append  
fields terminated by ';'
(cust_no DECIMAL EXTERNAL,
 cust_name char(40),
 memo char(10000)
)