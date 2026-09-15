-- AniTec | 2.6.4 Sanitary Management
-- MySQL 8 DDL prepared for manual ERD import.
-- Comments containing 'target' identify design additions not present in the inherited backend.
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS `ANIMALS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `HEALTH_EVENTS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `animal_id` INT NOT NULL,
  `veterinarian_id` INT NULL COMMENT 'target traceability, nullable',
  `type` VARCHAR(40) NOT NULL COMMENT 'required, max 40',
  `event_date` DATE NOT NULL COMMENT 'required',
  `description` VARCHAR(500) NOT NULL COMMENT 'required, max 500',
  `veterinarian` VARCHAR(255) NOT NULL COMMENT 'legacy display field',
  `diagnosis` VARCHAR(255) NOT NULL,
  `treatment` VARCHAR(255) NOT NULL,
  `prescription` VARCHAR(255) NOT NULL,
  `follow_up` VARCHAR(255) NOT NULL,
  `next_due_date` DATE NULL COMMENT 'nullable',
  CONSTRAINT `fk_health_events_animal_id` FOREIGN KEY (`animal_id`) REFERENCES `ANIMALS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
