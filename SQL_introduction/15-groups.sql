-- script that list the number of the records with the same score in the table second_table of the database hbtn_0c_0
SELECT score , count(*) AS number
FROM second_table
GROUP BY score
HAVING COUNT(*)
ORDER BY score DESC
