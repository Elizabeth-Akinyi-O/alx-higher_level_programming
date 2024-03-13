-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
--  Convert the following to UTF8:
--     Database hbtn_0c_0
--     Table first_table
--     Field name in first_table

USE `hbtn_0c_0`;
ALTER TABLE `first_table` MODIFY `name` VARCHAR(256) COLLATE utf8mb4_unicode_ci;
ALTER TABLE `first_table` COLLATE utf8mb4_unicode_ci;
