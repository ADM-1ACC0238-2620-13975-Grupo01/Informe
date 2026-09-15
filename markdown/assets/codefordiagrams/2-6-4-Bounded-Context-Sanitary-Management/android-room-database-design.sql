-- AniTec | 2.6.4 Sanitary Management
-- Android Room SQLite DDL prepared for manual ERD import.
-- Dates and DateTimes use ISO-8601 TEXT values; booleans use INTEGER 0/1.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS `CACHED_HEALTH_EVENTS` (
  `health_event_id` INTEGER PRIMARY KEY,
  `animal_id` INTEGER NOT NULL,
  `veterinarian_id` INTEGER NOT NULL,
  `type` TEXT NOT NULL,
  `event_date` TEXT NOT NULL,
  `clinical_data_json` TEXT NOT NULL,
  `next_due_date` TEXT NOT NULL,
  `updated_at` TEXT NOT NULL
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
