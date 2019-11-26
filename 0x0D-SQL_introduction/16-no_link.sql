-- lists all records of the table second_table
-- doesnt list rows without name value, displays score then name,
-- listed by descending score.
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;
