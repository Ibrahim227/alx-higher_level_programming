-- prints the full description of the table first_table from the db hbtn_0c_0
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0';
