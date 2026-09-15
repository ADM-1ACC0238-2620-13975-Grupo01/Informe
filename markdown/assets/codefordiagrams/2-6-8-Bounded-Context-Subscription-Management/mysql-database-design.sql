-- AniTec | 2.6.8 Subscription Management
-- MySQL 8 DDL prepared for manual ERD import.
-- Comments containing 'target' identify design additions not present in the inherited backend.
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS `USERS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `SUBSCRIPTION_PLANS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(80) NOT NULL COMMENT 'required, max 80',
  `price` DECIMAL(10,2) NOT NULL COMMENT 'precision 10,2',
  `stripe_price_id` VARCHAR(120) NOT NULL COMMENT 'max 120',
  `max_animals` INT NOT NULL,
  `is_active` BOOLEAN NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `SUBSCRIPTIONS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT NOT NULL,
  `plan_id` INT NOT NULL,
  `stripe_customer_id` VARCHAR(120) NOT NULL COMMENT 'max 120',
  `stripe_subscription_id` VARCHAR(120) NOT NULL COMMENT 'max 120',
  `status` VARCHAR(40) NOT NULL COMMENT 'required, max 40',
  `started_at` DATE NOT NULL,
  `ends_at` DATE NULL COMMENT 'nullable',
  CONSTRAINT `fk_subscriptions_user_id` FOREIGN KEY (`user_id`) REFERENCES `USERS` (`id`),
  CONSTRAINT `fk_subscriptions_plan_id` FOREIGN KEY (`plan_id`) REFERENCES `SUBSCRIPTION_PLANS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `PAYMENTS` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT NOT NULL,
  `subscription_id` INT NOT NULL,
  `amount` DECIMAL(10,2) NOT NULL COMMENT 'precision 10,2',
  `currency` VARCHAR(10) NOT NULL COMMENT 'required, max 10',
  `provider` VARCHAR(40) NOT NULL COMMENT 'required, max 40',
  `provider_payment_id` VARCHAR(120) NOT NULL COMMENT 'required, max 120; target unique',
  `status` VARCHAR(40) NOT NULL COMMENT 'required, max 40',
  `paid_at` DATETIME NOT NULL,
  CONSTRAINT `fk_payments_user_id` FOREIGN KEY (`user_id`) REFERENCES `USERS` (`id`),
  CONSTRAINT `fk_payments_subscription_id` FOREIGN KEY (`subscription_id`) REFERENCES `SUBSCRIPTIONS` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
