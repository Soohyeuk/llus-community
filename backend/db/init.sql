CREATE DATABASE IF NOT EXISTS user CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE user;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(100) NOT NULL UNIQUE, /* 사용자 이름 */
    english_name VARCHAR(100) NOT NULL, /* 영어 이름 */
    us_phone_number VARCHAR(15) NOT NULL UNIQUE, /* 미국전화번호 */
    email VARCHAR(255) NOT NULL UNIQUE, /* 이메일 */
    gender ENUM('F', 'M') NOT NULL, /* 성별 */
    birth_date DATE NOT NULL, /* 생년월일 */
    school VARCHAR(255) NOT NULL, /* 학교 */
    grad_date INT NOT NULL, 
    role ENUM('user', 'admin') NOT NULL, /* 역할 */
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);