-- AniTec | 2.6.1 Identity and Access Management
-- MySQL 8 DDL prepared for manual ERD import.
-- Comments containing 'target' identify design additions not present in the inherited backend.
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS `USERS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(80) NOT NULL COMMENT 'required, max 80; target unique',
  `password_hash` VARCHAR(255) NOT NULL COMMENT 'required',
  `full_name` VARCHAR(120) NOT NULL COMMENT 'required, max 120',
  `role` VARCHAR(40) NOT NULL COMMENT 'required, max 40',
  `created_at` DATETIME NOT NULL COMMENT 'audit',
  `updated_at` DATETIME NOT NULL COMMENT 'audit'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
