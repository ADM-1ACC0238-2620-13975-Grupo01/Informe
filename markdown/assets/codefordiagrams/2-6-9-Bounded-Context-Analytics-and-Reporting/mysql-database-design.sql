-- AniTec | 2.6.9 Analytics and Reporting
-- MySQL 8 DDL prepared for manual ERD import.
-- Comments containing 'target' identify design additions not present in the inherited backend.
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS `DASHBOARD_PROJECTIONS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'target read model',
  `owner_id` INT NOT NULL,
  `audience` VARCHAR(255) NOT NULL,
  `period_from` DATE NOT NULL,
  `period_to` DATE NOT NULL,
  `generated_at` DATETIME NOT NULL,
  `owner_audience_period` VARCHAR(255) NOT NULL UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `REPORT_METRICS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `projection_id` INT NOT NULL COMMENT 'target addition',
  `label` VARCHAR(80) NOT NULL COMMENT 'required, max 80',
  `value` VARCHAR(40) NOT NULL COMMENT 'required, max 40',
  `trend` VARCHAR(80) NOT NULL COMMENT 'max 80',
  `source_context` VARCHAR(255) NOT NULL COMMENT 'target traceability',
  CONSTRAINT `fk_report_metrics_projection_id` FOREIGN KEY (`projection_id`) REFERENCES `DASHBOARD_PROJECTIONS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
