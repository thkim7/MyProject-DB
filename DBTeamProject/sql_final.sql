-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: pos
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `b_id` int NOT NULL,
  `b_name` text NOT NULL,
  `b_emp` text NOT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch`
--

LOCK TABLES `branch` WRITE;
/*!40000 ALTER TABLE `branch` DISABLE KEYS */;
INSERT INTO `branch` VALUES (101,'서울','김철수'),(102,'인천','이덕배'),(103,'수원','최민식'),(104,'용인','김민수'),(105,'대구','최유리');
/*!40000 ALTER TABLE `branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `breadd`
--

DROP TABLE IF EXISTS `breadd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `breadd` (
  `p_id` int NOT NULL,
  `p_price` int NOT NULL,
  `p_name` text NOT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breadd`
--

LOCK TABLES `breadd` WRITE;
/*!40000 ALTER TABLE `breadd` DISABLE KEYS */;
INSERT INTO `breadd` VALUES (1001,2500,'단팥빵'),(1002,1500,'소보루빵'),(1003,2000,'크림빵'),(1004,4000,'피자빵'),(1005,6000,'식빵'),(1006,3000,'슈크림빵'),(1007,4000,'초코머핀'),(1008,5000,'바게트빵');
/*!40000 ALTER TABLE `breadd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iventory`
--

DROP TABLE IF EXISTS `iventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `iventory` (
  `i_date` int NOT NULL,
  `i_num` int DEFAULT NULL,
  `branch_b_id` int NOT NULL,
  `breadd_p_id` int NOT NULL,
  PRIMARY KEY (`i_date`,`branch_b_id`,`breadd_p_id`),
  KEY `fk_iventory_branch1_idx` (`branch_b_id`),
  KEY `fk_iventory_breadd1_idx` (`breadd_p_id`),
  CONSTRAINT `fk_iventory_branch1` FOREIGN KEY (`branch_b_id`) REFERENCES `branch` (`b_id`),
  CONSTRAINT `fk_iventory_breadd1` FOREIGN KEY (`breadd_p_id`) REFERENCES `breadd` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iventory`
--

LOCK TABLES `iventory` WRITE;
/*!40000 ALTER TABLE `iventory` DISABLE KEYS */;
INSERT INTO `iventory` VALUES (20221202,0,101,1001),(20221202,10,101,1002),(20221202,10,101,1003),(20221202,40,101,1004),(20221202,20,101,1005),(20221202,10,101,1006),(20221202,30,101,1007),(20221202,40,101,1008),(20221202,50,102,1001),(20221202,20,102,1002),(20221202,10,102,1003),(20221202,20,102,1004),(20221202,20,102,1005),(20221202,30,102,1006),(20221202,40,102,1007),(20221202,30,102,1008),(20221202,30,103,1001),(20221202,40,103,1002),(20221202,10,103,1003),(20221202,10,103,1004),(20221202,20,103,1005),(20221202,30,103,1006),(20221202,50,103,1007),(20221202,40,103,1008),(20221202,20,104,1001),(20221202,10,104,1002),(20221202,30,104,1003),(20221202,30,104,1004),(20221202,40,104,1005),(20221202,30,104,1006),(20221202,20,104,1007),(20221202,10,104,1008),(20221202,30,105,1001),(20221202,30,105,1002),(20221202,10,105,1003),(20221202,10,105,1004),(20221202,20,105,1005),(20221202,10,105,1006),(20221202,30,105,1007),(20221202,50,105,1008);
/*!40000 ALTER TABLE `iventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorder`
--

DROP TABLE IF EXISTS `sorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sorder` (
  `o_id` int NOT NULL,
  `branch_b_id` int NOT NULL,
  `breadd_p_id` int NOT NULL,
  `p_num` int NOT NULL,
  PRIMARY KEY (`o_id`,`branch_b_id`,`breadd_p_id`),
  KEY `fk_order_branch1_idx` (`branch_b_id`),
  KEY `fk_order_breadd1_idx` (`breadd_p_id`),
  CONSTRAINT `fk_order_branch1` FOREIGN KEY (`branch_b_id`) REFERENCES `branch` (`b_id`),
  CONSTRAINT `fk_order_breadd1` FOREIGN KEY (`breadd_p_id`) REFERENCES `breadd` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorder`
--

LOCK TABLES `sorder` WRITE;
/*!40000 ALTER TABLE `sorder` DISABLE KEYS */;
INSERT INTO `sorder` VALUES (1,101,1002,10),(2,105,1004,10),(3,101,1001,20),(4,101,1005,10),(5,105,1002,20);
/*!40000 ALTER TABLE `sorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spayment`
--

DROP TABLE IF EXISTS `spayment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spayment` (
  `s_id` int NOT NULL,
  `s_date` varchar(45) DEFAULT NULL,
  `s_amount` int NOT NULL,
  `order_o_id` int NOT NULL,
  PRIMARY KEY (`s_id`,`order_o_id`),
  KEY `fk_spayment_order1_idx` (`order_o_id`),
  CONSTRAINT `fk_spayment_order1` FOREIGN KEY (`order_o_id`) REFERENCES `sorder` (`o_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spayment`
--

LOCK TABLES `spayment` WRITE;
/*!40000 ALTER TABLE `spayment` DISABLE KEYS */;
INSERT INTO `spayment` VALUES (1,'2022-12-02 22:46:25',10,1),(2,'2022-12-02 22:46:29',10,2),(3,'2022-12-02 23:58:20',10,3),(4,'2022-12-03 13:08:34',10,4),(5,'2022-12-03 13:08:49',20,5);
/*!40000 ALTER TABLE `spayment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-07 11:37:43
