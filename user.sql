-- user mysql query migrations

CREATE TABLE
  `user` (
    `id` bigint unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(60) NOT NULL,
    `phoneNumber` varchar(25) NOT NULL,
    `age` int DEFAULT NULL,
    `password` text NOT NULL,
    PRIMARY KEY (`id`)
  ) ENGINE = InnoDB AUTO_INCREMENT = 11 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci