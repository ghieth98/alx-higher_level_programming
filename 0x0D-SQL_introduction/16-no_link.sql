-- script that lists all records the table second_table of the database
SELECT `score`, `name` FROM `second_table` WHERE `name`  != ""
ORDER BY `score` DESC;