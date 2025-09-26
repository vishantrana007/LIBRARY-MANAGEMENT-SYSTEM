-- ========================================
-- Library Management System Database Setup
-- Compatible with your app.py
-- ========================================

-- 1️⃣ Create database
CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

-- 2️⃣ Books table
CREATE TABLE IF NOT EXISTS books (
  book_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255),
  qty INT DEFAULT 1
);

-- 3️⃣ Members table
CREATE TABLE IF NOT EXISTS members (
  member_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  phone VARCHAR(20)
);

-- 4️⃣ Issue Books table
CREATE TABLE IF NOT EXISTS issue_books (
  issue_id INT AUTO_INCREMENT PRIMARY KEY,
  book_id INT NOT NULL,
  member_id INT NOT NULL,
  issue_date DATE NOT NULL,
  return_date DATE,
  FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- 5️⃣ Sample Data (Optional but recommended)
-- Sample Books
INSERT INTO books (title, author, qty) VALUES
('Python Basics', 'John Doe', 5),
('SQL for Beginners', 'Jane Smith', 3),
('Data Structures', 'Alice Johnson', 4);

-- Sample Members
INSERT INTO members (name, email, phone) VALUES
('Vishant Rana', 'vishant@example.com', '9876543210'),
('John Doe', 'john@example.com', '9123456780'),
('Alice Smith', 'alice@example.com', '9988776655');

-- Sample Issue Records (optional, can be empty)
INSERT INTO issue_books (book_id, member_id, issue_date, return_date) VALUES
(1, 1, CURDATE(), NULL),
(2, 2, CURDATE(), NULL);
