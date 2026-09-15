-- AniTec | 2.6.1 Identity and Access Management
-- Android Room SQLite DDL prepared for manual ERD import.
-- Dates and DateTimes use ISO-8601 TEXT values; booleans use INTEGER 0/1.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS `CACHED_IDENTITY` (
  `user_id` INTEGER PRIMARY KEY,
  `username` TEXT NOT NULL,
  `full_name` TEXT NOT NULL,
  `role` TEXT NOT NULL,
  `expires_at` TEXT NOT NULL,
  `sync_state` TEXT NOT NULL
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
