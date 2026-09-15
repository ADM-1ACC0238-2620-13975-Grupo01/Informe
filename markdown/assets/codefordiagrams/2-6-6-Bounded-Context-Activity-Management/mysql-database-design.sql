-- AniTec | 2.6.6 Activity Management
-- MySQL 8 DDL prepared for manual ERD import.
-- Comments containing 'target' identify design additions not present in the inherited backend.
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS `USERS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `ANIMALS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `FARM_ACTIVITIES` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `owner_id` INT NULL COMMENT 'nullable',
  `veterinarian_id` INT NULL COMMENT 'nullable',
  `animal_id` INT NULL COMMENT 'target addition, nullable',
  `title` VARCHAR(120) NOT NULL COMMENT 'required, max 120',
  `type` VARCHAR(40) NOT NULL COMMENT 'required, max 40',
  `scheduled_at` DATETIME NOT NULL COMMENT 'date in legacy model',
  `reminder_at` DATETIME NULL COMMENT 'target addition, nullable',
  `priority` VARCHAR(20) NOT NULL COMMENT 'required, max 20',
  `status` VARCHAR(30) NOT NULL COMMENT 'required, max 30',
  CONSTRAINT `fk_farm_activities_owner_id` FOREIGN KEY (`owner_id`) REFERENCES `USERS` (`id`),
  CONSTRAINT `fk_farm_activities_veterinarian_id` FOREIGN KEY (`veterinarian_id`) REFERENCES `USERS` (`id`),
  CONSTRAINT `fk_farm_activities_animal_id` FOREIGN KEY (`animal_id`) REFERENCES `ANIMALS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
