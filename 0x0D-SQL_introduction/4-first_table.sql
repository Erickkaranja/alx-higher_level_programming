-- creates a table called first_table in the current database.
USE DATABASE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS `first_table` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(256)
);
