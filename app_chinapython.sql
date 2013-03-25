-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- 主机: w.rdc.sae.sina.com.cn:3307
-- 生成日期: 2013 年 03 月 25 日 14:32
-- 服务器版本: 5.5.23
-- PHP 版本: 5.2.9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `app_chinapython`
--

-- --------------------------------------------------------

--
-- 表的结构 `sessions`
--

CREATE TABLE IF NOT EXISTS `sessions` (
  `session_id` char(128) NOT NULL,
  `atime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data` text,
  UNIQUE KEY `session_id` (`session_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `sessions`
--

INSERT INTO `sessions` (`session_id`, `atime`, `data`) VALUES
('fea96e568d46ae6eea2c2fafdf62982c72b0ee1e', '2013-03-25 14:28:33', 'KGRwMQpTJ2FjY2Vzc190b2tlbicKcDIKUyd0cnVlJwpwMwpzUydpcCcKcDQKVjIyMi4zMy44MS4x\nOQpwNQpzUyd1c2VyaW5mbycKcDYKY2NvcHlfcmVnCl9yZWNvbnN0cnVjdG9yCnA3Cihjd2ViLnV0\naWxzClN0b3JhZ2UKcDgKY19fYnVpbHRpbl9fCmRpY3QKcDkKKGRwMTAKUyduYW1lJwpwMTEKVmNo\ndTg4OApwMTIKc1MnYWRtaW4nCnAxMwpJMApzUydsb2dpbl9jb3VudCcKcDE0CkwxMEwKc1MnZW1h\naWwnCnAxNQpWY2h1ODg4QGdtYWlsLmNvbQpwMTYKc1MnbGFzdF9sb2dpbicKcDE3CkwyMDEwMDEw\nMUwKc1MnZnVsbF9uYW1lJwpwMTgKVmNodTg4OApwMTkKc1MncGFzc3dvcmQnCnAyMApWY2h1ODg4\nCnAyMQpzUydpZCcKcDIyCkwxTApzUydndWVzdCcKcDIzCkkxCnN0UnAyNApzUydzZXNzaW9uX2lk\nJwpwMjUKUydmZWE5NmU1NjhkNDZhZTZlZWEyYzJmYWZkZjYyOTgyYzcyYjBlZTFlJwpwMjYKcy4=\n'),
('30e983b4c7a72dc2c95cb54162f64894363328ab', '2013-03-25 13:32:26', 'KGRwMQpTJ2lwJwpwMgpWMjE4LjMwLjExNi45NQpwMwpzUydzZXNzaW9uX2lkJwpwNApTJzMwZTk4\nM2I0YzdhNzJkYzJjOTVjYjU0MTYyZjY0ODk0MzYzMzI4YWInCnA1CnMu\n'),
('26fa3217a621a30ebc757956ad81521a21b2c6ed', '2013-03-25 13:10:20', 'KGRwMQpTJ2lwJwpwMgpWMjE4LjMwLjExNi45NQpwMwpzUydzZXNzaW9uX2lkJwpwNApTJzI2ZmEz\nMjE3YTYyMWEzMGViYzc1Nzk1NmFkODE1MjFhMjFiMmM2ZWQnCnA1CnMu\n'),
('0fce145574b289c1ecfbb71879d6faa97dc5cc96', '2013-03-25 10:19:12', 'KGRwMQpTJ2FjY2Vzc190b2tlbicKcDIKUyd0cnVlJwpwMwpzUydpcCcKcDQKVjEyMy4xNTAuMTgy\nLjE1MgpwNQpzUyd1c2VyaW5mbycKcDYKY2NvcHlfcmVnCl9yZWNvbnN0cnVjdG9yCnA3Cihjd2Vi\nLnV0aWxzClN0b3JhZ2UKcDgKY19fYnVpbHRpbl9fCmRpY3QKcDkKKGRwMTAKUyduYW1lJwpwMTEK\nVmNodTg4OApwMTIKc1MnYWRtaW4nCnAxMwpJMApzUydsb2dpbl9jb3VudCcKcDE0CkwxMEwKc1Mn\naWQnCnAxNQpMMUwKc1MnbGFzdF9sb2dpbicKcDE2CkwyMDEwMDEwMUwKc1MnZnVsbF9uYW1lJwpw\nMTcKVmNodTg4OApwMTgKc1MncGFzc3dvcmQnCnAxOQpWY2h1ODg4CnAyMApzUydlbWFpbCcKcDIx\nClZjaHU4ODhAZ21haWwuY29tCnAyMgpzUydndWVzdCcKcDIzCkkxCnN0UnAyNApzUydzZXNzaW9u\nX2lkJwpwMjUKUycwZmNlMTQ1NTc0YjI4OWMxZWNmYmI3MTg3OWQ2ZmFhOTdkYzVjYzk2JwpwMjYK\ncy4=\n');

-- --------------------------------------------------------

--
-- 表的结构 `todo`
--

CREATE TABLE IF NOT EXISTS `todo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(300) DEFAULT NULL,
  `finished` int(11) DEFAULT '0',
  `post_date` datetime DEFAULT NULL,
  `userid` int(11) NOT NULL,
  `detail` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=38 ;

--
-- 转存表中的数据 `todo`
--

INSERT INTO `todo` (`id`, `title`, `finished`, `post_date`, `userid`, `detail`) VALUES
(35, '测试2', 0, '2013-03-25 13:49:19', 1, '9999999999999999999999'),
(36, '测试2', 1, '2013-03-25 13:49:30', 1, '测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2测试2');

-- --------------------------------------------------------

--
-- 表的结构 `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(9) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `password` varchar(64) NOT NULL,
  `login_count` int(10) unsigned NOT NULL DEFAULT '0',
  `last_login` int(10) unsigned NOT NULL DEFAULT '0',
  `email` varchar(64) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT '0',
  `guest` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `users`
--

INSERT INTO `users` (`id`, `name`, `full_name`, `password`, `login_count`, `last_login`, `email`, `admin`, `guest`) VALUES
(1, 'chu888', 'chu888', 'chu888', 10, 20100101, 'chu888@gmail.com', 0, 1),
(2, 'chu999', 'chu999', 'chu999', 1, 1, 'chu999@gmail.com', 1, 1);
