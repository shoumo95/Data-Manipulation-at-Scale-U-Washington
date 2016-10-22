.open reuters.db
select count(*) from (select * from Frequency where docid = '10398_txt_earn');
select count(*) from (select term from Frequency where docid = '10398_txt_earn' and count = 1);
select count(*) from (select term from Frequency where docid = '10398_txt_earn' and count = 1 UNION select term from Frequency where docid = '925_txt_trade' and count = 1);
select count(*) from (select DISTINCT docid from Frequency where term = 'law' OR term = 'legal');
select count(*) from (select docid,count(distinct term) as c from Frequency group by docid having c>300);
select count(*) from (select docid from Frequency where term= 'transactions' INTERSECT select docid from Frequency where term= 'world');
