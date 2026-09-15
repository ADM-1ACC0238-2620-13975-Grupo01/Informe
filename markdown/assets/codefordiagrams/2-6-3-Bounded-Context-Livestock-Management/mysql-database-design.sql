-- AniTec | 2.6.3 Livestock Management
-- MySQL 8 DDL prepared for manual ERD import.
-- Comments containing 'target' identify design additions not present in the inherited backend.
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS `USERS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `FARMS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'target addition',
  `owner_id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL COMMENT 'required',
  `location` VARCHAR(255) NOT NULL COMMENT 'required',
  CONSTRAINT `fk_farms_owner_id` FOREIGN KEY (`owner_id`) REFERENCES `USERS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `HERDS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `farm_id` INT NOT NULL COMMENT 'target addition',
  `owner_id` INT NOT NULL,
  `veterinarian_id` INT NULL COMMENT 'nullable',
  `name` VARCHAR(80) NOT NULL COMMENT 'required, max 80',
  `location` VARCHAR(255) NOT NULL COMMENT 'legacy field',
  `owner` VARCHAR(255) NOT NULL COMMENT 'legacy display field',
  `main_type` VARCHAR(40) NOT NULL COMMENT 'required, max 40',
  CONSTRAINT `fk_herds_farm_id` FOREIGN KEY (`farm_id`) REFERENCES `FARMS` (`id`),
  CONSTRAINT `fk_herds_owner_id` FOREIGN KEY (`owner_id`) REFERENCES `USERS` (`id`),
  CONSTRAINT `fk_herds_veterinarian_id` FOREIGN KEY (`veterinarian_id`) REFERENCES `USERS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `ANIMALS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `herd_id` INT NOT NULL,
  `tag` VARCHAR(30) NOT NULL COMMENT 'required, max 30; target unique',
  `qr_identifier` VARCHAR(255) NOT NULL COMMENT 'target addition; target unique',
  `name` VARCHAR(80) NOT NULL COMMENT 'required, max 80',
  `species` VARCHAR(40) NOT NULL COMMENT 'required, max 40',
  `breed` VARCHAR(60) NOT NULL COMMENT 'required, max 60',
  `gender` VARCHAR(20) NOT NULL COMMENT 'required, max 20',
  `birth_date` DATE NULL COMMENT 'nullable',
  `weight` DECIMAL(10,2) NOT NULL COMMENT 'required',
  `status` VARCHAR(30) NOT NULL COMMENT 'required, max 30',
  CONSTRAINT `fk_animals_herd_id` FOREIGN KEY (`herd_id`) REFERENCES `HERDS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
