-- list all records where name is not empty
SELECT score, name
FROM second_table
WHERE name NOT NULL AND name != ""
ORDER BY score DESC;
