CREATE DATABASE  IF NOT EXISTS `videokassety2` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `videokassety2`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: videokassety2
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Temporary view structure for view `my_view`
--

DROP TABLE IF EXISTS `my_view`;
/*!50001 DROP VIEW IF EXISTS `my_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `my_view` AS SELECT 
 1 AS `ФИО клиента`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `данные о выдачах`
--

DROP TABLE IF EXISTS `данные о выдачах`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `данные о выдачах` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Номер фильма` int DEFAULT NULL,
  `ФИО клиента` varchar(200) DEFAULT NULL,
  `Адрес клиента` varchar(200) DEFAULT NULL,
  `Дата выдачи` date DEFAULT NULL,
  `Дата возвращения` date DEFAULT NULL,
  `Залог` bigint DEFAULT NULL,
  `Оплата` bigint DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_Номер_фильма` (`Номер фильма`),
  CONSTRAINT `FK_Номер_фильма` FOREIGN KEY (`Номер фильма`) REFERENCES `сведения о фильме` (`Номер фильма`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=132 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `данные о выдачах`
--

LOCK TABLES `данные о выдачах` WRITE;
/*!40000 ALTER TABLE `данные о выдачах` DISABLE KEYS */;
INSERT INTO `данные о выдачах` VALUES (101,2,'Дьячков Ефрем Леонидович','Алматы, ул. Пушкина 15','2020-05-11','2020-05-14',500,1000),(102,2,'Ершов Борис Анатолиевич','Алматы, ул. Гоголя 20','2020-05-11','2020-05-14',500,1000),(103,2,'Темченко Йосеф Алексеевич','Алматы, ул. Кадырова 50','2020-05-11','2020-05-15',500,1000),(104,3,'Анисимов Устин Борисович','Алматы, ул. 138','2020-05-11','2020-05-16',500,1000),(105,3,'Андрейко Орландо Вадимович','Алматы, ул. Абая 23','2020-05-12','2020-05-17',500,1000),(106,5,'Кулагин Фёдор Вадимович','Алматы, ул. Азовская 5','2020-05-12','2020-05-17',500,1000),(107,5,'Носков Павел Анатолиевич','Алматы, ул. Айтбаева 10','2020-05-12','2020-05-17',500,1000),(108,7,'Кириленко Ираклий Виталиевич','Алматы, ул. Аксай-4','2020-05-12','2020-05-17',500,1000),(109,7,'Поляков Юлиан Петрович','Алматы, Алтынсарина 11','2020-05-13','2020-05-17',500,1000),(110,2,'Шилов Виктор Леонидович','Алматы, ул. Архангельская 100','2020-05-13','2020-05-18',500,1000),(111,2,'Лобанов Валериан Андреевич','Алматы, ул. Бабаева 32','2020-05-14','2020-05-19',500,1000),(112,8,'Кириленко Захар Александрович','Алматы, ул. Байканурова 1','2020-05-15','2020-05-20',500,1000),(113,10,'Давыдов Богдан Львович','Алматы, ул. Байсеитовой 5','2020-05-15','2020-05-21',500,1000),(114,3,'Третьяков Эдуард Владимирович','Алматы, ул. Бейсембаева 10','2020-05-15','2020-05-22',500,1000),(115,4,'Дорофеев Святослав Романович','Алматы, ул. Берсиева 4','2020-05-15','2020-05-23',500,1000),(116,2,'Капустин Иван Эдуардович','Алматы, ул. Весёлая 7','2020-05-15','2020-05-23',500,1000),(117,5,'Дубченко Чарльз Алексеевич','Алматы, ул. Глинки 9','2020-05-15','2020-05-23',500,1000),(118,11,'Попов Устин Богданович','Алматы, ул. Джалиля 95','2020-05-15','2020-05-23',500,1000),(119,6,'Дьячков Закир Романович','Алматы, ул. Добролюбова 1','2020-05-15','2020-05-23',500,1000),(120,2,'Зиновьев Устин Романович','Алматы, ул. Дулатова 77','2020-05-15','2020-05-23',500,1000),(124,5,'Валерий Прутков','г. Алматы, ул. Вишневского 48','2020-06-20','2020-06-21',1000,2000);
/*!40000 ALTER TABLE `данные о выдачах` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `компания производитель`
--

DROP TABLE IF EXISTS `компания производитель`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `компания производитель` (
  `ID Компании` int NOT NULL AUTO_INCREMENT,
  `Название компании` varchar(100) DEFAULT NULL,
  `Страна` varchar(100) DEFAULT NULL,
  `Город` varchar(100) DEFAULT NULL,
  `Год основания` int DEFAULT NULL,
  PRIMARY KEY (`ID Компании`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `компания производитель`
--

LOCK TABLES `компания производитель` WRITE;
/*!40000 ALTER TABLE `компания производитель` DISABLE KEYS */;
INSERT INTO `компания производитель` VALUES (10,'Marvel Studios','США','Бербанк',1993),(11,'Warner Bros. Pictures','США','Бербанк',1923),(12,'20th Century','США','Лос-Анджелес',1935),(13,'Lionsgate','США','Санта-Моника',1997),(14,'Miramax Films','США','Санта-Моника',1979),(15,'Paramount Pictures','США','Лос-Анджелес',1912),(16,'Pixar','США','Эмервиль',1979),(17,'The Walt Disney Company','США','Бербанк',1923),(20,'DreamWorks','США','Юниверсал-Сити',1994),(37,'Universal Pictures','США','Юниверсал-сити',1912);
/*!40000 ALTER TABLE `компания производитель` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `сведения о фильме`
--

DROP TABLE IF EXISTS `сведения о фильме`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `сведения о фильме` (
  `Номер фильма` int NOT NULL AUTO_INCREMENT,
  `Название фильма` varchar(200) DEFAULT NULL,
  `ID Компании` int DEFAULT NULL,
  `Год выпуска` int DEFAULT NULL,
  `Основные исполнители` varchar(200) DEFAULT NULL,
  `Характер фильма` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Номер фильма`),
  KEY `FK_Компания_производитель` (`ID Компании`),
  CONSTRAINT `FK_Компания_производитель` FOREIGN KEY (`ID Компании`) REFERENCES `компания производитель` (`ID Компании`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `сведения о фильме`
--

LOCK TABLES `сведения о фильме` WRITE;
/*!40000 ALTER TABLE `сведения о фильме` DISABLE KEYS */;
INSERT INTO `сведения о фильме` VALUES (1,'Железный человек 2',10,2010,'Джастин Теру, Роберт Дауни-мл., Гвинет Пэлтроу, Дон Чидл, Скарлетт Йоханссон, Микки Рурк','Фантастика'),(2,'Зеленая миля',11,1999,'Том Хэнкс, Дэвид Морс, Бонни Хант, Майкл Кларк Дункан, Джеймс Кромуэлл','фантастика, драма, криминал, детектив'),(3,'Престиж',11,2006,'Хью Джекман, Кристиан Бэйл, Майкл Кейн, Пайпер Перабо, Ребекка Холл, Скарлетт Йоханссон','фантастика, триллер, драма, детектив'),(4,'Один дома',12,1990,'Маколей Калкин, Джо Пеши, Дэниел Стерн, Кэтрин О’Хара, Джон Хёрд','комедия, семейный'),(5,'Чужие',12,1986,'Сигурни Уивер, Майкл Бин, Кэрри Хенн, Пол Райзер, Лэнс Хенриксен','ужасы, фантастика, боевик, триллер, приключения'),(6,'Достать ножи',13,2019,'Дэниэл Крэйг, Ана де Армас, Крис Эванс, Джейми Ли Кёртис, Майкл Шеннон','детектив, комедия, драма, криминал'),(7,'Три дня на побег',13,2010,'Рассел Кроу, Элизабет Бэнкс, Джейсон Бех, Аиша Хайндс, Оливия Уайлд','боевик, триллер, драма, мелодрама, криминал'),(8,'Криминальное чтиво',14,1994,'Джон Траволта, Сэмюэл Л. Джексон, Брюс Уиллис, Ума Турман, Винг Реймз','триллер, комедия, криминал'),(9,'Мальчик в полосатой пижаме',14,2008,'Эйса Баттерфилд, Джек Скэнлон, Дэвид Тьюлис, Вера Фармига, Эмбер Битти','драма, военный'),(10,'Форрест Гамп',15,1994,'Том Хэнкс, Робин Райт, Салли Филд, Гэри Синиз, Майкелти Уильямсон','драма, мелодрама, комедия, история, военный'),(11,'Крестный отец',15,1972,'Марлон Брандо, Аль Пачино, Джеймс Каан, Роберт Дювалл, Ричард С. Кастеллано','драма, криминал'),(12,'ВАЛЛИ',16,2008,'Бен Бертт, Элисса Найт, Джефф Гарлин, Фред Уиллард, Джон Ратценбергер','мультфильм, фантастика, приключения, семейный'),(13,'Корпорация монстров',16,2001,'Джон Гудман, Билли Кристал, Мэри Гиббс, Стив Бушеми, Джеймс Коберн','мультфильм, фэнтези, комедия, приключения, семейный'),(14,'Пираты Карибского моря: Проклятие Черной жемчужины',17,2003,'Джонни Депп, Джеффри Раш, Орландо Блум, Кира Найтли, Джек Девенпорт','фэнтези, боевик, приключения'),(15,'Зверополис',17,2016,'Джиннифер Гудвин, Джейсон Бейтман, Идрис Эльба, Дженни Слейт, Нейт Торренс','мультфильм, комедия, криминал, детектив'),(21,'Гладиатор',37,2000,'Рассел Кроу, Хоакин Феникс, Конни Нильсен','боевик');
/*!40000 ALTER TABLE `сведения о фильме` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `my_view`
--

/*!50001 DROP VIEW IF EXISTS `my_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `my_view` AS select `данные о выдачах`.`ФИО клиента` AS `ФИО клиента` from `данные о выдачах` where (`данные о выдачах`.`Номер фильма` in (1,2)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-02 14:14:28
