-- AniTec | 2.6.3 Livestock Management
-- Android Room SQLite DDL prepared for manual ERD import.
-- Dates and DateTimes use ISO-8601 TEXT values; booleans use INTEGER 0/1.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS `CACHED_HERDS` (
  `herd_id` INTEGER PRIMARY KEY,
  `farm_id` INTEGER NOT NULL,
  `name` TEXT NOT NULL,
  `location` TEXT NOT NULL,
  `main_type` TEXT NOT NULL,
  `updated_at` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `CACHED_ANIMALS` (
  `animal_id` INTEGER PRIMARY KEY,
  `herd_id` INTEGER NOT NULL,
  `tag` TEXT NOT NULL UNIQUE,
  `qr_identifier` TEXT NOT NULL UNIQUE,
  `name` TEXT NOT NULL,
  `species` TEXT NOT NULL,
  `status` TEXT NOT NULL,
  `updated_at` TEXT NOT NULL,
  CONSTRAINT `fk_cached_animals_herd_id` FOREIGN KEY (`herd_id`) REFERENCES `CACHED_HERDS` (`herd_id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `PENDING_OPERATIONS` (
  `operation_id` TEXT PRIMARY KEY,
  `aggregate_type` TEXT NOT NULL,
  `aggregate_id` TEXT NOT NULL,
  `operation_type` TEXT NOT NULL,
  `payload_json` TEXT NOT NULL,
  `created_at` TEXT NOT NULL,
  `retry_count` INTEGER NOT NULL DEFAULT 0,
  `status` TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS `ix_pending_operations_status_created_at`
  ON `PENDING_OPERATIONS` (`status`, `created_at`);
