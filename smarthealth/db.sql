/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.32 : Database - smarthealth
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`smarthealth` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `smarthealth`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

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

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add foodcalories',7,'add_foodcalories'),
(26,'Can change foodcalories',7,'change_foodcalories'),
(27,'Can delete foodcalories',7,'delete_foodcalories'),
(28,'Can view foodcalories',7,'view_foodcalories'),
(29,'Can add healthblog',8,'add_healthblog'),
(30,'Can change healthblog',8,'change_healthblog'),
(31,'Can delete healthblog',8,'delete_healthblog'),
(32,'Can view healthblog',8,'view_healthblog'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add notification',10,'add_notification'),
(38,'Can change notification',10,'change_notification'),
(39,'Can delete notification',10,'delete_notification'),
(40,'Can view notification',10,'view_notification'),
(41,'Can add nutritionist',11,'add_nutritionist'),
(42,'Can change nutritionist',11,'change_nutritionist'),
(43,'Can delete nutritionist',11,'delete_nutritionist'),
(44,'Can view nutritionist',11,'view_nutritionist'),
(45,'Can add user',12,'add_user'),
(46,'Can change user',12,'change_user'),
(47,'Can delete user',12,'delete_user'),
(48,'Can view user',12,'view_user'),
(49,'Can add reminder',13,'add_reminder'),
(50,'Can change reminder',13,'change_reminder'),
(51,'Can delete reminder',13,'delete_reminder'),
(52,'Can view reminder',13,'view_reminder'),
(53,'Can add medicalcondition',14,'add_medicalcondition'),
(54,'Can change medicalcondition',14,'change_medicalcondition'),
(55,'Can delete medicalcondition',14,'delete_medicalcondition'),
(56,'Can view medicalcondition',14,'view_medicalcondition'),
(57,'Can add healthdetails',15,'add_healthdetails'),
(58,'Can change healthdetails',15,'change_healthdetails'),
(59,'Can delete healthdetails',15,'delete_healthdetails'),
(60,'Can view healthdetails',15,'view_healthdetails'),
(61,'Can add feedback',16,'add_feedback'),
(62,'Can change feedback',16,'change_feedback'),
(63,'Can delete feedback',16,'delete_feedback'),
(64,'Can view feedback',16,'view_feedback'),
(65,'Can add doseinfo',17,'add_doseinfo'),
(66,'Can change doseinfo',17,'change_doseinfo'),
(67,'Can delete doseinfo',17,'delete_doseinfo'),
(68,'Can view doseinfo',17,'view_doseinfo'),
(69,'Can add calories',18,'add_calories'),
(70,'Can change calories',18,'change_calories'),
(71,'Can delete calories',18,'delete_calories'),
(72,'Can view calories',18,'view_calories'),
(73,'Can add reviewrating',19,'add_reviewrating'),
(74,'Can change reviewrating',19,'change_reviewrating'),
(75,'Can delete reviewrating',19,'delete_reviewrating'),
(76,'Can view reviewrating',19,'view_reviewrating'),
(77,'Can add chat',20,'add_chat'),
(78,'Can change chat',20,'change_chat'),
(79,'Can delete chat',20,'delete_chat'),
(80,'Can view chat',20,'view_chat');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(18,'health','calories'),
(20,'health','chat'),
(17,'health','doseinfo'),
(16,'health','feedback'),
(7,'health','foodcalories'),
(8,'health','healthblog'),
(15,'health','healthdetails'),
(9,'health','login'),
(14,'health','medicalcondition'),
(10,'health','notification'),
(11,'health','nutritionist'),
(13,'health','reminder'),
(19,'health','reviewrating'),
(12,'health','user'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-03-30 10:54:02.861180'),
(2,'auth','0001_initial','2023-03-30 10:54:04.282987'),
(3,'admin','0001_initial','2023-03-30 10:54:04.485866'),
(4,'admin','0002_logentry_remove_auto_add','2023-03-30 10:54:04.501518'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-03-30 10:54:04.517108'),
(6,'contenttypes','0002_remove_content_type_name','2023-03-30 10:54:04.626703'),
(7,'auth','0002_alter_permission_name_max_length','2023-03-30 10:54:04.704564'),
(8,'auth','0003_alter_user_email_max_length','2023-03-30 10:54:04.751460'),
(9,'auth','0004_alter_user_username_opts','2023-03-30 10:54:04.767081'),
(10,'auth','0005_alter_user_last_login_null','2023-03-30 10:54:04.845440'),
(11,'auth','0006_require_contenttypes_0002','2023-03-30 10:54:04.860778'),
(12,'auth','0007_alter_validators_add_error_messages','2023-03-30 10:54:04.876430'),
(13,'auth','0008_alter_user_username_max_length','2023-03-30 10:54:04.954504'),
(14,'auth','0009_alter_user_last_name_max_length','2023-03-30 10:54:05.048232'),
(15,'auth','0010_alter_group_name_max_length','2023-03-30 10:54:05.079758'),
(16,'auth','0011_update_proxy_permissions','2023-03-30 10:54:05.095381'),
(17,'auth','0012_alter_user_first_name_max_length','2023-03-30 10:54:05.188825'),
(18,'health','0001_initial','2023-03-30 10:54:06.110788'),
(19,'sessions','0001_initial','2023-03-30 10:54:06.172969'),
(20,'health','0002_alter_notification_time','2023-04-01 07:09:12.906684'),
(21,'health','0003_alter_doseinfo_time','2023-04-06 05:12:02.817317'),
(22,'health','0004_auto_20230411_1439','2023-04-11 09:10:02.138056'),
(23,'health','0005_medicalcondition_hd','2023-04-11 09:39:32.602147'),
(24,'health','0006_auto_20230411_1512','2023-04-11 09:43:02.406524'),
(25,'health','0007_auto_20230411_1540','2023-04-11 10:10:41.727672'),
(26,'health','0008_remove_healthdetails_gweight','2023-04-11 10:19:00.072525'),
(27,'health','0009_reviewrating','2023-04-11 11:15:03.702607'),
(28,'health','0010_reviewrating_nid','2023-04-17 09:31:10.605394'),
(29,'health','0011_auto_20230420_2038','2023-04-20 15:11:11.648141'),
(30,'health','0012_remove_healthdetails_hd','2023-04-20 16:40:26.234146'),
(31,'health','0013_nutritionist_lid','2023-04-28 06:07:34.208379'),
(32,'health','0014_auto_20230428_1713','2023-04-28 11:44:06.076647'),
(33,'health','0015_feedback_type','2023-05-04 10:23:46.543422');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('ftmbeljjplivtqd72674y4ctxeooo6ea','eyJmaWQiOjksImxpZCI6MTZ9:1puWPd:5VOkxbICguw6N-khdYPIqcCLNjCuXYXuPGxf-mt4JMo','2023-05-18 10:42:13.430133'),
('perc2feohehup5qr4lkjdr6e5wl0syxj','.eJyrVsrITFGyMtFRSgPRRjpKeSDaVEcpB0QbmukolYAYxrUA9_8LcQ:1puVyW:YdoVsFjTkrcHUxD6uMAdno7PE3sO7a3yoCke3MPIpdc','2023-05-18 10:14:12.795088');

/*Table structure for table `health_chat` */

DROP TABLE IF EXISTS `health_chat`;

CREATE TABLE `health_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `msg` longtext NOT NULL,
  `date` date NOT NULL,
  `fromid_id` bigint NOT NULL,
  `toid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_chat_fromid_id_b232f7a9_fk_health_login_id` (`fromid_id`),
  KEY `health_chat_toid_id_3ecfa67b_fk_health_login_id` (`toid_id`),
  CONSTRAINT `health_chat_fromid_id_b232f7a9_fk_health_login_id` FOREIGN KEY (`fromid_id`) REFERENCES `health_login` (`id`),
  CONSTRAINT `health_chat_toid_id_3ecfa67b_fk_health_login_id` FOREIGN KEY (`toid_id`) REFERENCES `health_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_chat` */

insert  into `health_chat`(`id`,`msg`,`date`,`fromid_id`,`toid_id`) values 
(1,'hiiii','2023-04-28',3,16),
(2,'rycg','2023-05-04',3,16),
(3,'hiiiii','2023-05-04',16,3),
(4,'rfd','2023-05-04',3,16),
(5,'heyyyyyyy','2023-05-04',16,3),
(6,'haai','2023-05-04',3,17),
(8,'okkk','2023-05-04',17,3),
(9,'hyyy','2023-05-04',17,3),
(10,'hello','2023-05-04',17,3),
(11,'aaaaaaaaaaaaaaaaa','2023-05-04',16,3),
(12,'okk','2023-05-04',3,17),
(13,'hy','2023-05-04',3,17),
(14,'joo','2023-05-04',3,17),
(15,'hooo','2023-05-04',3,17),
(16,'fhhh','2023-05-04',3,17),
(17,'hjk','2023-05-04',3,17),
(18,'hhj','2023-05-04',3,17);

/*Table structure for table `health_doseinfo` */

DROP TABLE IF EXISTS `health_doseinfo`;

CREATE TABLE `health_doseinfo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `time` varchar(200) NOT NULL,
  `mid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_doseinfo_mid_id_4bcd63a1_fk_health_reminder_id` (`mid_id`),
  CONSTRAINT `health_doseinfo_mid_id_4bcd63a1_fk_health_reminder_id` FOREIGN KEY (`mid_id`) REFERENCES `health_reminder` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_doseinfo` */

insert  into `health_doseinfo`(`id`,`time`,`mid_id`) values 
(1,'09:00:00',63),
(2,'13:00:00',63),
(3,'17:00:00',63),
(4,'09:00:00',64),
(5,'15:00:00',64),
(6,'21:00:00',66);

/*Table structure for table `health_feedback` */

DROP TABLE IF EXISTS `health_feedback`;

CREATE TABLE `health_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(30) NOT NULL,
  `uid_id` bigint NOT NULL,
  `type` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_feedback_uid_id_5a61f679_fk_health_user_id` (`uid_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_feedback` */

insert  into `health_feedback`(`id`,`feedback`,`date`,`reply`,`uid_id`,`type`) values 
(7,'good','2023-05-04','okkk',3,'user'),
(9,'Very Good','2023-05-04','aaaaaaaaaaaaaaaaaaaaaaa',16,'nutritionist');

/*Table structure for table `health_foodcalories` */

DROP TABLE IF EXISTS `health_foodcalories`;

CREATE TABLE `health_foodcalories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `food` varchar(30) NOT NULL,
  `image` varchar(100) NOT NULL,
  `quantity` varchar(30) NOT NULL,
  `calories` int NOT NULL,
  `carbs` double NOT NULL,
  `fats` double NOT NULL,
  `fiber` double NOT NULL,
  `proteins` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_foodcalories` */

insert  into `health_foodcalories`(`id`,`food`,`image`,`quantity`,`calories`,`carbs`,`fats`,`fiber`,`proteins`) values 
(1,'Apple','apple_BftdW7S.jpg','regular',45,0.7,0.6,0.4,0.5),
(2,'Rice','rice_i51LmRl.jpg','Cup',132,3.8,0.9,0.6,0.3),
(3,'Orange','orange_CkYo6Pl.jpg','regular',57,0.6,0.3,0.5,2.8),
(4,'Oats','oats_fFOjTO0.jpg','Cup',120,8.9,0.5,0.6,0.6);

/*Table structure for table `health_healthblog` */

DROP TABLE IF EXISTS `health_healthblog`;

CREATE TABLE `health_healthblog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `caption` varchar(50) NOT NULL,
  `blog` varchar(500) NOT NULL,
  `image` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_healthblog` */

insert  into `health_healthblog`(`id`,`caption`,`blog`,`image`,`date`) values 
(1,'Daily Fitness','Physical fitness is a state of health and well-being and, more specifically, the ability to perform aspects of sports, occupations and daily activities. Physical fitness is generally achieved through proper nutrition, moderate-vigorous physical exercise, and sufficient rest along with a formal recovery plan. Before the Industrial Revolution, fitness was defined as the capacity to carry out the day\'s activities without undue fatigue or lethargy. However, with automation and changes in l','h1_u3o7gqV.jpg','2023-03-31'),
(2,'Protein Diet','Proteins are essential nutrients for the human body. They are one of the building blocks of body tissue and can also serve as a fuel source. As a fuel, proteins provide as much energy density as carbohydrates: 4 kcal (17 kJ) per gram; in contrast, lipids provide 9 kcal (37 kJ) per gram. The most important aspect and defining characteristic of protein from a nutritional standpoint is its amino acid composition.  Proteins are polymer chains made of amino acids linked together by peptide bond','h3_1H5ya0K.jpg','2023-03-31'),
(3,'Importance of Yoga','Yoga is a group of physical, mental, and spiritual practices or disciplines which originated in ancient India and aim to control (yoke) and still the mind, recognizing a detached witness-consciousness untouched by the mind (Chitta) and mundane suffering (Duḥkha). There is a wide variety of schools of yoga, practices, and goals in Hinduism, Buddhism, and Jainism, and traditional and modern yoga is practic','h2_wsX5upC.jpg','2023-03-31');

/*Table structure for table `health_healthdetails` */

DROP TABLE IF EXISTS `health_healthdetails`;

CREATE TABLE `health_healthdetails` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dob` date NOT NULL,
  `height` int NOT NULL,
  `cweight` int NOT NULL,
  `bmi` int NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_healthdetails_lid_id_9d5a69f3_fk_health_login_id` (`lid_id`),
  CONSTRAINT `health_healthdetails_lid_id_9d5a69f3_fk_health_login_id` FOREIGN KEY (`lid_id`) REFERENCES `health_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_healthdetails` */

insert  into `health_healthdetails`(`id`,`dob`,`height`,`cweight`,`bmi`,`lid_id`) values 
(1,'2007-03-31',150,45,20,3),
(16,'2000-12-18',175,50,16,11),
(17,'2000-03-10',150,56,24,12),
(18,'2000-02-11',150,59,26,13),
(19,'2001-04-05',155,56,23,18);

/*Table structure for table `health_login` */

DROP TABLE IF EXISTS `health_login`;

CREATE TABLE `health_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `usertype` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_login` */

insert  into `health_login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','123','admin'),
(3,'aneetha','anu','user'),
(11,'sanan','sanu','user'),
(12,'amii','amee','user'),
(13,'rani','rano','user'),
(16,'anuaneetha2000@gmail.com','8848644022','nutritionist'),
(17,'shajinik75@gmail.com','9400979650','nutritionist'),
(18,'sham','shamna','user');

/*Table structure for table `health_medicalcondition` */

DROP TABLE IF EXISTS `health_medicalcondition`;

CREATE TABLE `health_medicalcondition` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `diabetes` varchar(10) NOT NULL,
  `cholestrol` varchar(10) NOT NULL,
  `pressure` varchar(10) NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_medicalcondition_lid_id_678800e4_fk_health_login_id` (`lid_id`),
  CONSTRAINT `health_medicalcondition_lid_id_678800e4_fk_health_login_id` FOREIGN KEY (`lid_id`) REFERENCES `health_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_medicalcondition` */

insert  into `health_medicalcondition`(`id`,`date`,`diabetes`,`cholestrol`,`pressure`,`lid_id`) values 
(2,'2023-01-30','10','20','30',3),
(6,'2023-04-13','30','40','140',3),
(7,'2023-04-13','10','10','10',11),
(8,'2023-04-13','10','100','10',3),
(9,'2023-04-13','10','100','30',3),
(10,'2023-04-13','10','100','300',3),
(16,'2023-03-13','0','0','0',12),
(17,'2023-04-13','0','0','0',13),
(19,'2023-04-18','0','0','200',3),
(20,'2023-04-28','0','0','200',12),
(21,'2023-04-28','0','120','0',18),
(23,'2023-04-28','0','150','200',18);

/*Table structure for table `health_notification` */

DROP TABLE IF EXISTS `health_notification`;

CREATE TABLE `health_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notification` varchar(50) NOT NULL,
  `time` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_notification` */

insert  into `health_notification`(`id`,`notification`,`time`) values 
(1,'Morning breakfast','13:07'),
(2,'Lunch','13:10'),
(3,'Evening','16:56'),
(5,'Drink water ','13:18');

/*Table structure for table `health_nutritionist` */

DROP TABLE IF EXISTS `health_nutritionist`;

CREATE TABLE `health_nutritionist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `image` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobile` bigint NOT NULL,
  `gender` varchar(10) NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `experience` int NOT NULL,
  `license` varchar(30) NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_nutritionist_lid_id_c463c4c4_fk_health_login_id` (`lid_id`),
  CONSTRAINT `health_nutritionist_lid_id_c463c4c4_fk_health_login_id` FOREIGN KEY (`lid_id`) REFERENCES `health_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_nutritionist` */

insert  into `health_nutritionist`(`id`,`name`,`image`,`email`,`mobile`,`gender`,`qualification`,`experience`,`license`,`lid_id`) values 
(4,'Aneeth','dcr1_3NAiiA0.jpg','anuaneetha2000@gmail.com',8848644022,'male','MSc Dietetics',5,'ASDFG56789',16),
(5,'Nasss','dcr2_RicVfWn.jpg','shajinik75@gmail.com',9400979650,'female','Msc Nutrition',5,'SDFGH123',17);

/*Table structure for table `health_reminder` */

DROP TABLE IF EXISTS `health_reminder`;

CREATE TABLE `health_reminder` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `medicine` varchar(30) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `num` int NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_reminder_lid_id_6a32451d_fk_health_login_id` (`lid_id`),
  CONSTRAINT `health_reminder_lid_id_6a32451d_fk_health_login_id` FOREIGN KEY (`lid_id`) REFERENCES `health_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_reminder` */

insert  into `health_reminder`(`id`,`medicine`,`startdate`,`enddate`,`num`,`lid_id`) values 
(63,'dolo','2023-04-19','2023-04-26',3,3),
(64,'antibiotic','2023-04-27','2023-04-30',2,3),
(66,'cutihyde','2023-04-24','2023-04-30',1,3),
(67,'sgff','2023-04-25','2023-04-29',0,3);

/*Table structure for table `health_reviewrating` */

DROP TABLE IF EXISTS `health_reviewrating`;

CREATE TABLE `health_reviewrating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `review` varchar(60) NOT NULL,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `uid_id` bigint NOT NULL,
  `nid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_reviewrating_uid_id_26d7622e_fk_health_user_id` (`uid_id`),
  KEY `health_reviewrating_nid_id_a31bb50c_fk_health_nutritionist_id` (`nid_id`),
  CONSTRAINT `health_reviewrating_nid_id_a31bb50c_fk_health_nutritionist_id` FOREIGN KEY (`nid_id`) REFERENCES `health_nutritionist` (`id`),
  CONSTRAINT `health_reviewrating_uid_id_26d7622e_fk_health_user_id` FOREIGN KEY (`uid_id`) REFERENCES `health_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_reviewrating` */

insert  into `health_reviewrating`(`id`,`review`,`rating`,`date`,`uid_id`,`nid_id`) values 
(9,'good',2,'2023-04-28',2,4),
(10,'bad',1,'2023-04-28',11,4),
(11,'excellent',3.5,'2023-04-28',11,5);

/*Table structure for table `health_user` */

DROP TABLE IF EXISTS `health_user`;

CREATE TABLE `health_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobile` bigint NOT NULL,
  `gender` varchar(10) NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_user_lid_id_fe505ee9_fk_health_login_id` (`lid_id`),
  CONSTRAINT `health_user_lid_id_fe505ee9_fk_health_login_id` FOREIGN KEY (`lid_id`) REFERENCES `health_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `health_user` */

insert  into `health_user`(`id`,`name`,`email`,`mobile`,`gender`,`lid_id`) values 
(2,'Aneetha','anuaneetha2000@gmail.com',8848644022,'Female',3),
(10,'Sanan','sanan@gmail.com',9061697367,'Male',11),
(11,'Ameena','ami@gmail.com',8921383950,'Female',12),
(12,'Raniya','rani@gmail.com',9988776655,'Female',13),
(14,'Shamna','shamnammukkam@gmail.com',8848644022,'Female',18);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
