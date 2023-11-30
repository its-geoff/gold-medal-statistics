-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: users
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
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add permission',10,'add_permission'),(38,'Can change permission',10,'change_permission'),(39,'Can delete permission',10,'delete_permission'),(40,'Can view permission',10,'view_permission'),(41,'Can add group',11,'add_group'),(42,'Can change group',11,'change_group'),(43,'Can delete group',11,'delete_group'),(44,'Can view group',11,'view_group'),(45,'Can add content type',12,'add_contenttype'),(46,'Can change content type',12,'change_contenttype'),(47,'Can delete content type',12,'delete_contenttype'),(48,'Can view content type',12,'view_contenttype'),(49,'Can add mark',13,'add_mark'),(50,'Can change mark',13,'change_mark'),(51,'Can delete mark',13,'delete_mark'),(52,'Can view mark',13,'view_mark'),(53,'Can add athlete',14,'add_athlete'),(54,'Can change athlete',14,'change_athlete'),(55,'Can delete athlete',14,'delete_athlete'),(56,'Can view athlete',14,'view_athlete'),(57,'Can add log entry',15,'add_logentry'),(58,'Can change log entry',15,'change_logentry'),(59,'Can delete log entry',15,'delete_logentry'),(60,'Can view log entry',15,'view_logentry'),(61,'Can add session',16,'add_session'),(62,'Can change session',16,'change_session'),(63,'Can delete session',16,'delete_session'),(64,'Can view session',16,'view_session');
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
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (2,'2023-07-02 01:35:34.147714','9','test, nmhs, 100m, 11.5, 745',3,'',13,2),(3,'2023-07-02 01:35:34.151598','8','test, nmhs, 100m, 11.5, 745',3,'',13,2),(4,'2023-07-02 01:35:34.153861','7','test, nmhs, 100m, 11.5, 745',3,'',13,2),(5,'2023-07-02 01:35:34.157028','6','test, nmsh, 100m, 11.5, 745',3,'',13,2),(6,'2023-07-02 01:35:34.159334','5','test, test, 100m, 11.5, 0',3,'',13,2),(7,'2023-07-02 01:35:34.161629','4','test, test, 100m, 11.5, 0',3,'',13,2),(8,'2023-07-02 01:35:34.164521','3','Geoffrey Agustin, Newark Memorial, 100m, 11.5, 0',3,'',13,2),(9,'2023-07-02 01:35:34.167898','2','Geoffrey Agustin, Newark Memorial, 100m, 11.5, 0',3,'',13,2),(10,'2023-07-02 01:35:34.170295','1','Geoffrey Agustin, Newark Memorial, 100m, 11.5, 0',3,'',13,2),(11,'2023-07-02 01:35:38.940850','13','test, nmhs',3,'',14,2),(12,'2023-07-02 01:35:38.943179','12','test, nmhs',3,'',14,2),(13,'2023-07-02 01:35:38.946391','11','test, nmhs',3,'',14,2),(14,'2023-07-02 01:35:38.952161','10','test, nmhs',3,'',14,2),(15,'2023-07-02 01:35:38.955307','9','test, nmhs',3,'',14,2),(16,'2023-07-02 01:35:38.957336','8','test, nmhs',3,'',14,2),(17,'2023-07-02 01:35:38.959707','7','test, nmsh',3,'',14,2),(18,'2023-07-02 01:35:38.962805','6','test, nmsh',3,'',14,2),(19,'2023-07-02 01:35:38.966222','5','test, test',3,'',14,2),(20,'2023-07-02 01:35:38.968656','4','test, test',3,'',14,2),(21,'2023-07-02 01:35:38.971317','3','Geoffrey Agustin, Newark Memorial',3,'',14,2),(22,'2023-07-02 01:35:38.974432','2','Geoffrey Agustin, Newark Memorial',3,'',14,2),(23,'2023-07-02 01:35:38.976444','1','Geoffrey Agustin, Newark Memorial',3,'',14,2),(24,'2023-07-02 19:28:41.727003','3','test0',2,'[]',9,2),(25,'2023-07-02 19:33:39.687013','3','test0',2,'[]',9,2),(26,'2023-07-02 21:34:36.674727','11','Chance Tokubo, Newark Memorial, 1600m, 270.29, 0',3,'',13,2),(27,'2023-07-02 21:34:40.752272','15','Chance Tokubo, Newark Memorial',3,'',14,2),(28,'2023-07-02 21:36:43.108651','12','Chance Tokubo, Newark Memorial, 1600m, 270.29, 0',3,'',13,2),(29,'2023-07-02 21:36:47.427702','16','Chance Tokubo, Newark Memorial',3,'',14,2),(30,'2023-07-02 23:14:00.424575','5','test',3,'',9,2),(31,'2023-07-02 23:30:35.336661','7','j',3,'',9,2),(32,'2023-07-02 23:34:22.880962','10','j',3,'',9,2),(33,'2023-07-02 23:35:41.002627','11','j',3,'',9,2),(34,'2023-07-02 23:36:05.978826','12','j',3,'',9,2),(35,'2023-07-03 04:30:26.489214','13','test1',3,'',9,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (15,'admin','logentry'),(11,'auth','group'),(10,'auth','permission'),(12,'contenttypes','contenttype'),(14,'marks','athlete'),(13,'marks','mark'),(16,'sessions','session'),(9,'users','user');
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
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-07-01 22:37:03.846788'),(2,'contenttypes','0002_remove_content_type_name','2023-07-01 22:37:03.877514'),(3,'auth','0001_initial','2023-07-01 22:37:03.978950'),(4,'auth','0002_alter_permission_name_max_length','2023-07-01 22:37:04.002903'),(5,'auth','0003_alter_user_email_max_length','2023-07-01 22:37:04.010492'),(6,'auth','0004_alter_user_username_opts','2023-07-01 22:37:04.017450'),(7,'auth','0005_alter_user_last_login_null','2023-07-01 22:37:04.024109'),(8,'auth','0006_require_contenttypes_0002','2023-07-01 22:37:04.028586'),(9,'auth','0007_alter_validators_add_error_messages','2023-07-01 22:37:04.034586'),(10,'auth','0008_alter_user_username_max_length','2023-07-01 22:37:04.041962'),(11,'auth','0009_alter_user_last_name_max_length','2023-07-01 22:37:04.047953'),(12,'auth','0010_alter_group_name_max_length','2023-07-01 22:37:04.061968'),(13,'auth','0011_update_proxy_permissions','2023-07-01 22:37:04.068405'),(14,'auth','0012_alter_user_first_name_max_length','2023-07-01 22:37:04.076407'),(31,'sessions','0001_initial','2023-07-01 22:45:50.524348'),(32,'users','0001_initial','2023-07-01 22:46:24.275720'),(33,'admin','0001_initial','2023-07-01 22:46:59.607415'),(34,'admin','0002_logentry_remove_auto_add','2023-07-01 22:46:59.622235'),(35,'admin','0003_logentry_add_action_flag_choices','2023-07-01 22:46:59.626236'),(47,'marks','0001_initial','2023-07-01 22:49:45.404350'),(48,'marks','0002_mark_points','2023-07-01 22:49:45.423721'),(49,'marks','0003_athlete','2023-07-01 22:49:45.440590'),(50,'marks','0004_mark_team','2023-07-01 22:49:45.453796'),(51,'marks','0005_athlete_team','2023-07-01 22:49:45.469961'),(52,'marks','0006_athlete_marks','2023-07-01 22:49:45.493588'),(53,'marks','0007_remove_athlete_marks_athlete_eight_athlete_four_and_more','2023-07-01 22:49:45.739762'),(54,'marks','0008_alter_athlete_eight_alter_athlete_four_and_more','2023-07-01 22:49:45.988559'),(55,'marks','0009_remove_athlete_eight_remove_athlete_four_and_more','2023-07-01 22:49:46.376002'),(56,'marks','0010_athlete_hj_mark_athlete_hj_points_athlete_lj_mark_and_more','2023-07-01 22:49:46.551155'),(57,'marks','0011_athlete_dt_mark_athlete_dt_points_athlete_sp_mark_and_more','2023-07-01 22:49:46.650826'),(58,'users','0002_alter_user_username','2023-07-02 21:16:22.545804'),(59,'marks','0012_athlete_user_mark_user','2023-07-02 21:16:32.604766'),(62,'users','0003_user_team','2023-11-04 06:11:09.976052');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9l15cg9wbsnbonnh6jn4t0zwe2axnvur','.eJxVjDsOwjAQBe_iGlk2_kJJnzNYu_YuDiBHipMKcXcSKQW0b2beWyRYl5rWTnMai7gKLU6_G0J-UttBeUC7TzJPbZlHlLsiD9rlMBV63Q7376BCr1tNziLqyKwhoDJMhHzxObNTKgIaBIqeLCGyskG54J22Z7ZmcwuaLD5fGBc44Q:1qFjNB:Oj8OSPDPBPVGydF1T9jm_u_K4x1mZJNLaIozg7h6EBw','2023-07-15 22:47:21.006622'),('b9lhgk6tz6clnlnvo6myr9pwg90mj14r','.eJxVjEEOwiAQRe_C2hBgBkpduvcMZIYBWzVtUtqV8e7apAvd_vfef6lE2zqkrZUljaLOyqnT78aUH2Xagdxpus06z9O6jKx3RR-06ess5Xk53L-DgdrwrTtmqshgjHMSCvYhkgRkCpQhSldtH9lbMAFA0KI1tSAa6zxABg_q_QHgQDb1:1qob3L:YNf8yV2-SXaD6oMKDhXwa9A3L_e2wrocYQ7rYiGJQ0Q','2023-10-20 02:58:59.113836'),('z27hcnh8z8dqrqvsxu95r7oz6ypwrdt6','.eJxVjMEOwiAQRP-FsyEtlIV69N5vILsslaqBpLQn479Lkx70NMm8N_MWHvct-b3G1S8srkKLy29HGJ4xH4AfmO9FhpK3dSF5KPKkVU6F4-t2un8HCWtq6zBYY8Ea0j0ECp1GhcrZOALOOkZWZkQC0jBjZ8kZcNwCoGm2DzyIzxfivDgK:1qGMZI:5zSU0JowUeFPKdbQnr3HO-yvj__PdBUN0lW77xv2s80','2023-07-17 16:38:28.969735');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marks_athlete`
--

LOCK TABLES `marks_athlete` WRITE;
/*!40000 ALTER TABLE `marks_athlete` DISABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marks_mark`
--

LOCK TABLES `marks_mark` WRITE;
/*!40000 ALTER TABLE `marks_mark` DISABLE KEYS */;
/*!40000 ALTER TABLE `marks_mark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(80) NOT NULL,
  `username` varchar(30) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `team` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (2,'pbkdf2_sha256$390000$FiiFbiNAYHuA2OcwZXEgnc$rkbtNTOD4MPI/tiamJ2FM1Lmp+DPFnasIqd07AV8cUc=','2023-11-30 07:45:24.697211','geoffreyyyagustin@gmail.com','admin',1,1,1,'admin'),(3,'pbkdf2_sha256$390000$SOc00oN41jWNjI2RPnrxuE$LQ0U/9Q7N8iCfeqL1OOmR53fiC1i55lzfvusMt3ap6g=','2023-07-03 16:38:28.920694','test@gmail.com','test0',1,0,0,'admin');
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-30  1:27:11
