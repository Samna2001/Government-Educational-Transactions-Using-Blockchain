/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - egovernment
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`egovernment` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `egovernment`;

/*Table structure for table `assign_plans` */

DROP TABLE IF EXISTS `assign_plans`;

CREATE TABLE `assign_plans` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `office_id` int(11) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  `scheduled_time` varchar(100) DEFAULT NULL,
  `scheduled_staff` varchar(100) DEFAULT NULL,
  `deadline` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `assign_plans` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `officer_id` int(11) DEFAULT NULL,
  `complaint` varchar(300) DEFAULT NULL,
  `upload` varchar(1000) DEFAULT NULL,
  `reply` varchar(300) DEFAULT NULL,
  `date` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`officer_id`,`complaint`,`upload`,`reply`,`date`) values 
(1,1,'okk','static/images/92d33138-b7cd-4cef-ab94-b9ad64835e0etajmahal.jpg','plz update','2024-05-09');

/*Table structure for table `facilities` */

DROP TABLE IF EXISTS `facilities`;

CREATE TABLE `facilities` (
  `facilities_id` int(11) NOT NULL AUTO_INCREMENT,
  `offices_id` int(11) DEFAULT NULL,
  `facility` varchar(300) DEFAULT NULL,
  `images` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`facilities_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `facilities` */

/*Table structure for table `images` */

DROP TABLE IF EXISTS `images`;

CREATE TABLE `images` (
  `image_id` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` int(11) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`image_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `images` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(300) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  `usertype` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'fathima','Fathi@789','AEO'),
(3,'athila','Athila@67','DEO'),
(4,'samna','Samna@13','DDE'),
(5,'revathy','Revu@345','AD'),
(6,'abin','Abin@567','RDD');

/*Table structure for table `offices` */

DROP TABLE IF EXISTS `offices`;

CREATE TABLE `offices` (
  `offices_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `office` varchar(100) DEFAULT NULL,
  `place` varchar(300) DEFAULT NULL,
  `phone` varchar(300) DEFAULT NULL,
  `email` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`offices_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `offices` */

/*Table structure for table `plans` */

DROP TABLE IF EXISTS `plans`;

CREATE TABLE `plans` (
  `plans_id` int(11) NOT NULL AUTO_INCREMENT,
  `planid` varchar(100) DEFAULT NULL,
  `plan` varchar(300) DEFAULT NULL,
  `desc` varchar(100) DEFAULT NULL,
  `filename` varchar(1000) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `staff_id_rdd` int(11) DEFAULT NULL,
  `staff_id_ad` int(11) DEFAULT NULL,
  `staff_id_dde` int(11) DEFAULT NULL,
  `staff_id_deo` int(11) DEFAULT NULL,
  `staff_id_aeo` int(11) DEFAULT NULL,
  PRIMARY KEY (`plans_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `plans` */

insert  into `plans`(`plans_id`,`planid`,`plan`,`desc`,`filename`,`status`,`staff_id_rdd`,`staff_id_ad`,`staff_id_dde`,`staff_id_deo`,`staff_id_aeo`) values 
(1,'866176695','Laptop distribution','laptop distribution for students in BPL category with 90% marks in higher secondary education','static/images/24c532aa-387c-4bc1-82e0-db89da886e11man.png','deo_verify',3,4,3,2,1),
(5,'455310585','dfghjk','bvnbmn','static/images/b172f90b-c774-45b0-bd04-f71a84d16720activitydiagramuser.png','rejected',5,4,0,0,0);

/*Table structure for table `public_complaint` */

DROP TABLE IF EXISTS `public_complaint`;

CREATE TABLE `public_complaint` (
  `pcomplaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `public_name` varchar(100) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pcomplaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `public_complaint` */

insert  into `public_complaint`(`pcomplaint_id`,`public_name`,`complaint`,`date`,`reply`) values 
(1,'okk','kunju','2024-05-09','pending');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `requestdetails` varchar(300) DEFAULT NULL,
  `details` varchar(300) DEFAULT NULL,
  `date` varchar(300) DEFAULT NULL,
  `status` varchar(300) DEFAULT NULL,
  `staff_id_aeo` int(11) DEFAULT NULL,
  `staff_id_deo` int(11) DEFAULT NULL,
  `staff_id_dde` int(11) DEFAULT NULL,
  `staff_id_ad` int(11) DEFAULT NULL,
  `staff_id_rdd` int(11) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`requestdetails`,`details`,`date`,`status`,`staff_id_aeo`,`staff_id_deo`,`staff_id_dde`,`staff_id_ad`,`staff_id_rdd`) values 
(1,'fan in varkala govt school ','fan in varkala govt school ,needed in 10 class average estimate of 10000','2024-05-09','sanctioned',1,2,3,4,5);

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(300) DEFAULT NULL,
  `lname` varchar(300) DEFAULT NULL,
  `email` varchar(300) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`fname`,`lname`,`email`,`category`,`phone`,`place`) values 
(1,2,'fathima','tb','sunu@gmail.com','AEO','9824678551','varkala'),
(2,3,'athila','pareeth','athila@gmail.com','DEO','9876543212','varkala'),
(3,4,'samna','salam','samnasalam2001@gmail.com','DDE','9188586756','thiruvananthapuram'),
(4,5,'revathy','Sunil','rev@gmail.com','AD','9867568778','thiruvananthapuram'),
(5,6,'Abin','Babu','abinbabu@gmail.com','RDD','6789060948','thiruvananthapuram');

/*Table structure for table `suggestion` */

DROP TABLE IF EXISTS `suggestion`;

CREATE TABLE `suggestion` (
  `suggestion_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `suggestions` varchar(300) DEFAULT NULL,
  `details` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`suggestion_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `suggestion` */

/*Table structure for table `transcations` */

DROP TABLE IF EXISTS `transcations`;

CREATE TABLE `transcations` (
  `transcation_id` int(11) NOT NULL AUTO_INCREMENT,
  `plans_id` int(11) DEFAULT NULL,
  `transcationid` varchar(100) DEFAULT NULL,
  `transcation_name` varchar(5000) DEFAULT NULL,
  `details` varchar(300) DEFAULT NULL,
  `amount` varchar(300) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`transcation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `transcations` */

insert  into `transcations`(`transcation_id`,`plans_id`,`transcationid`,`transcation_name`,`details`,`amount`,`date`,`status`) values 
(1,1,'341673768','Laptops distribution','govt school schools of varkala region provided 6 laptops for the best outgoing BPL students of 6 schools','300000','2024-05-09','deo_verify');

/*Table structure for table `uploadwork` */

DROP TABLE IF EXISTS `uploadwork`;

CREATE TABLE `uploadwork` (
  `upload_id` int(11) NOT NULL AUTO_INCREMENT,
  `plan_id` int(11) DEFAULT NULL,
  `upload` varchar(1000) DEFAULT NULL,
  `datetime` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`upload_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `uploadwork` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
