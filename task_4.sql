-- SQL script to print the full description of the 'Books' table.
-- It queries the INFORMATION_SCHEMA.COLUMNS table to get column details.
-- The database name 'alx_book_store' will be passed as an argument to the mysql command.
-- No DESCRIBE or EXPLAIN statements are used, and all SQL keywords are in uppercase.

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books'