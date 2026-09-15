-- AniTec | 2.6.9 Analytics and Reporting
-- Android Room SQLite DDL prepared for manual ERD import.
-- Dates and DateTimes use ISO-8601 TEXT values; booleans use INTEGER 0/1.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS `CACHED_DASHBOARDS` (
  `dashboard_id` INTEGER PRIMARY KEY,
  `owner_id` INTEGER NOT NULL,
  `audience` TEXT NOT NULL,
  `period_from` TEXT NOT NULL,
  `period_to` TEXT NOT NULL,
  `generated_at` TEXT NOT NULL,
  `sync_state` TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `CACHED_REPORT_METRICS` (
  `metric_id` INTEGER PRIMARY KEY,
  `dashboard_id` INTEGER NOT NULL,
  `label` TEXT NOT NULL,
  `value` TEXT NOT NULL,
  `trend` TEXT NOT NULL,
  `source_context` TEXT NOT NULL,
  CONSTRAINT `fk_cached_report_metrics_dashboard_id` FOREIGN KEY (`dashboard_id`) REFERENCES `CACHED_DASHBOARDS` (`dashboard_id`) ON DELETE CASCADE
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
