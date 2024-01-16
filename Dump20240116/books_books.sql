-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: books
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `title` varchar(80) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL,
  `genre` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('The Hunger Games','Suzanne Collins','Fantasy'),('Harry Potter and the Order of the Phoenix','JK Rowling','Fantasy'),('To Kill a Mockingbird','Harper Lee','Classic'),('Pride and Prejudice','Jane Austen','Classic'),('Twilight','Stephenie Meyer','Fantasy'),('The Book Thief','Markus Zusak','Historical Fiction'),('Animal Farm','George Orwell','Classic'),('The Chronicles of Narnia','C.S. Lewis','Fantasy'),('The Lord of the Rings','J.R.R. Tolkien','Fantasy'),('Gone with the Wind','Margaret Mitchell','Historical Fiction'),('The Fault in Our Stars','John Green','Romance'),('The Hitchhikers Guide to the Galaxy','Douglas Adams','Science Fiction'),('The Giving Tree','Shel Silverstein','Fantasy'),('Wuthering Heights','Emily BrontÃ','Historical Fiction'),('The Da Vinci Code','Dan Brown','Thriller'),('Memoirs of a Geisha','Arthur Golden','Historical Fiction'),('The Picture of Dorian Gray','Oscar Wilde','Fantasy'),('Alice in Wonderland','Lewis Carrol','Fantasy'),('Jane Eyre','Charlotte BrontÃ','Classic'),('Fahrenheit 451','Ray Bradbury','Science Fiction');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-16  7:47:09
