-- script that lists all the cities of Calfornia that can be found in the database gbtn_0d_usa
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
