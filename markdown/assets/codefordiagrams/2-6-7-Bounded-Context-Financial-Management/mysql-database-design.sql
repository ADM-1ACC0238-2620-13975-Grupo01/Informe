-- AniTec | 2.6.7 Financial Management
-- MySQL 8 DDL prepared for manual ERD import.
-- Comments containing 'target' identify design additions not present in the inherited backend.
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS `USERS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `FINANCIAL_RECORDS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `owner_id` INT NOT NULL,
  `type` VARCHAR(20) NOT NULL COMMENT 'required, max 20',
  `category` VARCHAR(80) NOT NULL COMMENT 'required, max 80',
  `amount` DECIMAL(10,2) NOT NULL COMMENT 'precision 10,2',
  `currency` VARCHAR(255) NOT NULL COMMENT 'target addition, default PEN',
  `record_date` DATE NOT NULL COMMENT 'required',
  `description` VARCHAR(255) NOT NULL,
  CONSTRAINT `fk_financial_records_owner_id` FOREIGN KEY (`owner_id`) REFERENCES `USERS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
