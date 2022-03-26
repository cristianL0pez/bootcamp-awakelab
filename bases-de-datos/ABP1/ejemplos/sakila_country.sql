-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: sakila
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `country_id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `country` varchar(50) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (1,'Afghanistan','2006-02-15 07:44:00'),(2,'Algeria','2006-02-15 07:44:00'),(3,'American Samoa','2006-02-15 07:44:00'),(4,'Angola','2006-02-15 07:44:00'),(5,'Anguilla','2006-02-15 07:44:00'),(6,'Argentina','2006-02-15 07:44:00'),(7,'Armenia','2006-02-15 07:44:00'),(8,'Australia','2006-02-15 07:44:00'),(9,'Austria','2006-02-15 07:44:00'),(10,'Azerbaijan','2006-02-15 07:44:00'),(11,'Bahrain','2006-02-15 07:44:00'),(12,'Bangladesh','2006-02-15 07:44:00'),(13,'Belarus','2006-02-15 07:44:00'),(14,'Bolivia','2006-02-15 07:44:00'),(15,'Brazil','2006-02-15 07:44:00'),(16,'Brunei','2006-02-15 07:44:00'),(17,'Bulgaria','2006-02-15 07:44:00'),(18,'Cambodia','2006-02-15 07:44:00'),(19,'Cameroon','2006-02-15 07:44:00'),(20,'Canada','2006-02-15 07:44:00'),(21,'Chad','2006-02-15 07:44:00'),(22,'Chile','2006-02-15 07:44:00'),(23,'China','2006-02-15 07:44:00'),(24,'Colombia','2006-02-15 07:44:00'),(25,'Congo, The Democratic Republic of the','2006-02-15 07:44:00'),(26,'Czech Republic','2006-02-15 07:44:00'),(27,'Dominican Republic','2006-02-15 07:44:00'),(28,'Ecuador','2006-02-15 07:44:00'),(29,'Egypt','2006-02-15 07:44:00'),(30,'Estonia','2006-02-15 07:44:00'),(31,'Ethiopia','2006-02-15 07:44:00'),(32,'Faroe Islands','2006-02-15 07:44:00'),(33,'Finland','2006-02-15 07:44:00'),(34,'France','2006-02-15 07:44:00'),(35,'French Guiana','2006-02-15 07:44:00'),(36,'French Polynesia','2006-02-15 07:44:00'),(37,'Gambia','2006-02-15 07:44:00'),(38,'Germany','2006-02-15 07:44:00'),(39,'Greece','2006-02-15 07:44:00'),(40,'Greenland','2006-02-15 07:44:00'),(41,'Holy See (Vatican City State)','2006-02-15 07:44:00'),(42,'Hong Kong','2006-02-15 07:44:00'),(43,'Hungary','2006-02-15 07:44:00'),(44,'India','2006-02-15 07:44:00'),(45,'Indonesia','2006-02-15 07:44:00'),(46,'Iran','2006-02-15 07:44:00'),(47,'Iraq','2006-02-15 07:44:00'),(48,'Israel','2006-02-15 07:44:00'),(49,'Italy','2006-02-15 07:44:00'),(50,'Japan','2006-02-15 07:44:00'),(51,'Kazakstan','2006-02-15 07:44:00'),(52,'Kenya','2006-02-15 07:44:00'),(53,'Kuwait','2006-02-15 07:44:00'),(54,'Latvia','2006-02-15 07:44:00'),(55,'Liechtenstein','2006-02-15 07:44:00'),(56,'Lithuania','2006-02-15 07:44:00'),(57,'Madagascar','2006-02-15 07:44:00'),(58,'Malawi','2006-02-15 07:44:00'),(59,'Malaysia','2006-02-15 07:44:00'),(60,'Mexico','2006-02-15 07:44:00'),(61,'Moldova','2006-02-15 07:44:00'),(62,'Morocco','2006-02-15 07:44:00'),(63,'Mozambique','2006-02-15 07:44:00'),(64,'Myanmar','2006-02-15 07:44:00'),(65,'Nauru','2006-02-15 07:44:00'),(66,'Nepal','2006-02-15 07:44:00'),(67,'Netherlands','2006-02-15 07:44:00'),(68,'New Zealand','2006-02-15 07:44:00'),(69,'Nigeria','2006-02-15 07:44:00'),(70,'North Korea','2006-02-15 07:44:00'),(71,'Oman','2006-02-15 07:44:00'),(72,'Pakistan','2006-02-15 07:44:00'),(73,'Paraguay','2006-02-15 07:44:00'),(74,'Peru','2006-02-15 07:44:00'),(75,'Philippines','2006-02-15 07:44:00'),(76,'Poland','2006-02-15 07:44:00'),(77,'Puerto Rico','2006-02-15 07:44:00'),(78,'Romania','2006-02-15 07:44:00'),(79,'Runion','2006-02-15 07:44:00'),(80,'Russian Federation','2006-02-15 07:44:00'),(81,'Saint Vincent and the Grenadines','2006-02-15 07:44:00'),(82,'Saudi Arabia','2006-02-15 07:44:00'),(83,'Senegal','2006-02-15 07:44:00'),(84,'Slovakia','2006-02-15 07:44:00'),(85,'South Africa','2006-02-15 07:44:00'),(86,'South Korea','2006-02-15 07:44:00'),(87,'Spain','2006-02-15 07:44:00'),(88,'Sri Lanka','2006-02-15 07:44:00'),(89,'Sudan','2006-02-15 07:44:00'),(90,'Sweden','2006-02-15 07:44:00'),(91,'Switzerland','2006-02-15 07:44:00'),(92,'Taiwan','2006-02-15 07:44:00'),(93,'Tanzania','2006-02-15 07:44:00'),(94,'Thailand','2006-02-15 07:44:00'),(95,'Tonga','2006-02-15 07:44:00'),(96,'Tunisia','2006-02-15 07:44:00'),(97,'Turkey','2006-02-15 07:44:00'),(98,'Turkmenistan','2006-02-15 07:44:00'),(99,'Tuvalu','2006-02-15 07:44:00'),(100,'Ukraine','2006-02-15 07:44:00'),(101,'United Arab Emirates','2006-02-15 07:44:00'),(102,'United Kingdom','2006-02-15 07:44:00'),(103,'United States','2006-02-15 07:44:00'),(104,'Venezuela','2006-02-15 07:44:00'),(105,'Vietnam','2006-02-15 07:44:00'),(106,'Virgin Islands, U.S.','2006-02-15 07:44:00'),(107,'Yemen','2006-02-15 07:44:00'),(108,'Yugoslavia','2006-02-15 07:44:00'),(109,'Zambia','2006-02-15 07:44:00');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-25 21:22:00
