CREATE VIEW if not exists view_1 AS 
SELECT * FROM frequency 
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

select A.docid, B.docid, sum(A.count * B.count) as similarity 
from view_1  A, view_1 B on A.term = B.term  
where A.docid = 'q' and B.docid != 'q'
group by A.docid, B.docid
order by similarity desc limit 10;
