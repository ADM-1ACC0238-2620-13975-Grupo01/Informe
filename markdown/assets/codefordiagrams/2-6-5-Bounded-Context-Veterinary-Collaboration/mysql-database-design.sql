-- AniTec | 2.6.5 Veterinary Collaboration
-- MySQL 8 DDL prepared for manual ERD import.
-- Comments containing 'target' identify design additions not present in the inherited backend.
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS `VETERINARIAN_CLIENTS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `veterinarian_id` INT NOT NULL,
  `rancher_id` INT NOT NULL,
  `status` VARCHAR(30) NOT NULL COMMENT 'required, max 30',
  `requested_at` DATETIME NOT NULL COMMENT 'required',
  `accepted_at` DATETIME NULL COMMENT 'nullable',
  `revoked_at` DATETIME NOT NULL COMMENT 'target addition',
  `authorization_scope` JSON NOT NULL COMMENT 'target addition',
  CONSTRAINT `fk_veterinarian_clients_veterinarian_id` FOREIGN KEY (`veterinarian_id`) REFERENCES `USERS` (`id`),
  CONSTRAINT `fk_veterinarian_clients_rancher_id` FOREIGN KEY (`rancher_id`) REFERENCES `USERS` (`id`),
  CONSTRAINT `uk_veterinarian_client` UNIQUE (`veterinarian_id`, `rancher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `USERS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
