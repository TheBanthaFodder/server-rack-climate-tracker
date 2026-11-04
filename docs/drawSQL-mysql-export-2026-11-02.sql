CREATE TABLE `Temperature and Humidity`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `sensor-id` VARCHAR(50) NOT NULL,
    `recorded-at` TIMESTAMP NOT NULL,
    `tempc` FLOAT(53) NOT NULL,
    `humidity` FLOAT(53) NOT NULL,
    `status` VARCHAR(50) NOT NULL
);
ALTER TABLE
    `Temperature and Humidity` ADD INDEX `temperature and humidity_recorded_at_index`(`recorded-at`);