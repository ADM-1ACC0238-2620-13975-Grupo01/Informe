-- AniTec | 2.6.8 Subscription Management
-- Flutter SQLite DDL prepared for manual ERD import.
-- Dates and DateTimes use ISO-8601 TEXT values; booleans use INTEGER 0/1.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS `CACHED_SUBSCRIPTION_PLANS` (
  `plan_id` INTEGER PRIMARY KEY,
  `name` TEXT NOT NULL,
  `price` REAL NOT NULL,
  `currency` TEXT NOT NULL,
  `max_animals` INTEGER NOT NULL,
  `is_active` INTEGER NOT NULL,
  `updated_at` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `CACHED_SUBSCRIPTIONS` (
  `subscription_id` INTEGER PRIMARY KEY,
  `user_id` INTEGER NOT NULL,
  `plan_id` INTEGER NOT NULL,
  `status` TEXT NOT NULL,
  `started_at` TEXT NOT NULL,
  `ends_at` TEXT NOT NULL,
  `updated_at` TEXT NOT NULL,
  CONSTRAINT `fk_cached_subscriptions_plan_id` FOREIGN KEY (`plan_id`) REFERENCES `CACHED_SUBSCRIPTION_PLANS` (`plan_id`) ON DELETE CASCADE
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
