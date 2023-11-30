-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: marks
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add mark',1,'add_mark'),(2,'Can change mark',1,'change_mark'),(3,'Can delete mark',1,'delete_mark'),(4,'Can view mark',1,'view_mark'),(5,'Can add athlete',2,'add_athlete'),(6,'Can change athlete',2,'change_athlete'),(7,'Can delete athlete',2,'delete_athlete'),(8,'Can view athlete',2,'view_athlete'),(9,'Can add user',3,'add_user'),(10,'Can change user',3,'change_user'),(11,'Can delete user',3,'delete_user'),(12,'Can view user',3,'view_user'),(13,'Can add permission',4,'add_permission'),(14,'Can change permission',4,'change_permission'),(15,'Can delete permission',4,'delete_permission'),(16,'Can view permission',4,'view_permission'),(17,'Can add group',5,'add_group'),(18,'Can change group',5,'change_group'),(19,'Can delete group',5,'delete_group'),(20,'Can view group',5,'view_group'),(21,'Can add content type',6,'add_contenttype'),(22,'Can change content type',6,'change_contenttype'),(23,'Can delete content type',6,'delete_contenttype'),(24,'Can view content type',6,'view_contenttype'),(25,'Can add log entry',7,'add_logentry'),(26,'Can change log entry',7,'change_logentry'),(27,'Can delete log entry',7,'delete_logentry'),(28,'Can view log entry',7,'view_logentry'),(29,'Can add session',8,'add_session'),(30,'Can change session',8,'change_session'),(31,'Can delete session',8,'delete_session'),(32,'Can view session',8,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'admin','logentry'),(5,'auth','group'),(4,'auth','permission'),(6,'contenttypes','contenttype'),(2,'marks','athlete'),(1,'marks','mark'),(8,'sessions','session'),(3,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-07-01 22:44:39.286325'),(2,'contenttypes','0002_remove_content_type_name','2023-07-01 22:44:39.325193'),(3,'auth','0001_initial','2023-07-01 22:44:39.518735'),(4,'auth','0002_alter_permission_name_max_length','2023-07-01 22:44:39.551585'),(5,'auth','0003_alter_user_email_max_length','2023-07-01 22:44:39.559842'),(6,'auth','0004_alter_user_username_opts','2023-07-01 22:44:39.566915'),(7,'auth','0005_alter_user_last_login_null','2023-07-01 22:44:39.573255'),(8,'auth','0006_require_contenttypes_0002','2023-07-01 22:44:39.578267'),(9,'auth','0007_alter_validators_add_error_messages','2023-07-01 22:44:39.585334'),(10,'auth','0008_alter_user_username_max_length','2023-07-01 22:44:39.591781'),(11,'auth','0009_alter_user_last_name_max_length','2023-07-01 22:44:39.601891'),(12,'auth','0010_alter_group_name_max_length','2023-07-01 22:44:39.615404'),(13,'auth','0011_update_proxy_permissions','2023-07-01 22:44:39.622349'),(14,'auth','0012_alter_user_first_name_max_length','2023-07-01 22:44:39.630427'),(15,'users','0001_initial','2023-07-01 22:44:39.636446'),(16,'marks','0001_initial','2023-07-01 22:47:42.005466'),(17,'marks','0002_mark_points','2023-07-01 22:47:42.023223'),(18,'marks','0003_athlete','2023-07-01 22:47:42.041015'),(19,'marks','0004_mark_team','2023-07-01 22:47:42.061027'),(20,'marks','0005_athlete_team','2023-07-01 22:47:42.075774'),(21,'marks','0006_athlete_marks','2023-07-01 22:47:42.096820'),(22,'marks','0007_remove_athlete_marks_athlete_eight_athlete_four_and_more','2023-07-01 22:47:42.265240'),(23,'marks','0008_alter_athlete_eight_alter_athlete_four_and_more','2023-07-01 22:47:42.452789'),(24,'marks','0009_remove_athlete_eight_remove_athlete_four_and_more','2023-07-01 22:47:42.905819'),(25,'marks','0010_athlete_hj_mark_athlete_hj_points_athlete_lj_mark_and_more','2023-07-01 22:47:43.100853'),(26,'marks','0011_athlete_dt_mark_athlete_dt_points_athlete_sp_mark_and_more','2023-07-01 22:47:43.187087'),(27,'admin','0001_initial','2023-07-02 01:09:11.457144'),(28,'admin','0002_logentry_remove_auto_add','2023-07-02 01:09:11.469081'),(29,'admin','0003_logentry_add_action_flag_choices','2023-07-02 01:09:11.471080'),(30,'sessions','0001_initial','2023-07-02 01:09:11.473668'),(31,'marks','0012_athlete_user_mark_user','2023-07-02 21:16:05.731076'),(32,'users','0002_alter_user_username','2023-07-03 05:23:56.035272');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marks_athlete`
--

DROP TABLE IF EXISTS `marks_athlete`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marks_athlete` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `team` varchar(50) NOT NULL,
  `eight_mark` double NOT NULL,
  `eight_points` int NOT NULL,
  `four_h_mark` double NOT NULL,
  `four_h_points` int NOT NULL,
  `four_mark` double NOT NULL,
  `four_points` int NOT NULL,
  `four_r_mark` double NOT NULL,
  `four_r_points` int NOT NULL,
  `one_h_mark` double NOT NULL,
  `one_h_points` int NOT NULL,
  `one_mark` double NOT NULL,
  `one_points` int NOT NULL,
  `one_r_mark` double NOT NULL,
  `one_r_points` int NOT NULL,
  `sixteen_mark` double NOT NULL,
  `sixteen_points` int NOT NULL,
  `thirtytwo_mark` double NOT NULL,
  `thirtytwo_points` int NOT NULL,
  `two_mark` double NOT NULL,
  `two_points` int NOT NULL,
  `hj_mark` double NOT NULL,
  `hj_points` int NOT NULL,
  `lj_mark` double NOT NULL,
  `lj_points` int NOT NULL,
  `pv_mark` double NOT NULL,
  `pv_points` int NOT NULL,
  `tj_mark` double NOT NULL,
  `tj_points` int NOT NULL,
  `dt_mark` double NOT NULL,
  `dt_points` int NOT NULL,
  `sp_mark` double NOT NULL,
  `sp_points` int NOT NULL,
  `user` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marks_athlete`
--

LOCK TABLES `marks_athlete` WRITE;
/*!40000 ALTER TABLE `marks_athlete` DISABLE KEYS */;
INSERT INTO `marks_athlete` VALUES (14,'Geoffrey Agustin','men','Newark Memorial',0,0,0,0,0,0,0,0,0,0,11.5,745,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'admin'),(17,'Chance Tokubo','men','Newark Memorial ',0,0,0,0,0,0,0,0,0,0,0,0,0,0,270.39,734,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'admin');
/*!40000 ALTER TABLE `marks_athlete` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marks_mark`
--

DROP TABLE IF EXISTS `marks_mark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marks_mark` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `gender` varchar(5) NOT NULL,
  `event` varchar(10) NOT NULL,
  `mark` double NOT NULL,
  `points` int NOT NULL,
  `team` varchar(50) NOT NULL,
  `user` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marks_mark`
--

LOCK TABLES `marks_mark` WRITE;
/*!40000 ALTER TABLE `marks_mark` DISABLE KEYS */;
INSERT INTO `marks_mark` VALUES (10,'Geoffrey Agustin','men','100m',11.5,745,'Newark Memorial','admin'),(13,'Chance Tokubo','men','1600m',270.39,734,'Newark Memorial ','admin');
/*!40000 ALTER TABLE `marks_mark` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-30  1:27:19
