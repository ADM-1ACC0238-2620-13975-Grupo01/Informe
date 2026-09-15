-- AniTec | 2.6.2 Profile Management
-- MySQL 8 DDL prepared for manual ERD import.
-- Comments containing 'target' identify design additions not present in the inherited backend.
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS `USERS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `PROFILES` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT NOT NULL UNIQUE COMMENT 'target traceability',
  `first_name` VARCHAR(255) NOT NULL COMMENT 'required',
  `last_name` VARCHAR(255) NOT NULL COMMENT 'required',
  `email_address` VARCHAR(255) NOT NULL UNIQUE COMMENT 'required',
  `address_street` VARCHAR(255) NOT NULL,
  `address_number` VARCHAR(255) NOT NULL,
  `address_city` VARCHAR(255) NOT NULL,
  `address_postal_code` VARCHAR(255) NOT NULL,
  `address_country` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL COMMENT 'audit',
  `updated_at` DATETIME NOT NULL COMMENT 'audit',
  CONSTRAINT `fk_profiles_user_id` FOREIGN KEY (`user_id`) REFERENCES `USERS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
