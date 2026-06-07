-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jun 07, 2026 at 10:55 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rf_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `frequency_logs`
--

CREATE TABLE `frequency_logs` (
  `log_id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `power_level` int(11) DEFAULT NULL,
  `mode` varchar(20) DEFAULT 'MANUAL',
  `timestamp` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `frequency_logs`
--

INSERT INTO `frequency_logs` (`log_id`, `username`, `frequency`, `power_level`, `mode`, `timestamp`) VALUES
(1, 'qhris', 50, -20, 'MANUAL', '2026-04-11 23:56:23'),
(2, 'qhris', 50, -20, 'MANUAL', '2026-04-11 23:56:28'),
(3, 'qhris', 1000, -20, 'MANUAL', '2026-04-11 23:56:47'),
(4, 'qhris', 1000, -41, 'MANUAL', '2026-04-11 23:57:00'),
(5, 'qhris', 392, -31, 'MANUAL', '2026-04-12 00:01:59'),
(6, 'qhris', 345, -20, 'MANUAL', '2026-04-12 00:21:06'),
(7, 'qhris', 251, -30, 'MANUAL', '2026-04-12 00:21:18'),
(8, 'qhris', 171, -30, 'MANUAL', '2026-04-12 00:21:22'),
(9, 'qhris', 300, -16, 'MANUAL', '2026-04-12 00:23:47'),
(10, 'qhris', 327, -16, 'MANUAL', '2026-04-12 00:24:00'),
(11, 'qhris', 418, -16, 'MANUAL', '2026-04-12 00:24:19'),
(12, 'qhris', 80, -16, 'MANUAL', '2026-04-12 00:24:25'),
(13, 'qhris', 118, -20, 'MANUAL', '2026-04-12 00:29:36'),
(14, 'qhris', 221, -11, 'MANUAL', '2026-04-12 00:33:05'),
(15, 'qhris', 160, -6, 'MANUAL', '2026-04-12 00:33:36'),
(16, 'qhris', 221, -36, 'MANUAL', '2026-04-12 00:51:24'),
(17, 'qhris', 224, -34, 'MANUAL', '2026-04-12 01:03:02'),
(18, 'qhris', 509, -5, 'MANUAL', '2026-04-12 01:05:31'),
(19, 'qhris', 312, -5, 'MANUAL', '2026-04-12 01:05:41'),
(20, 'qhris', 297, -36, 'MANUAL', '2026-04-12 01:12:51'),
(21, 'qhris', 210, -36, 'MANUAL', '2026-04-12 01:13:57'),
(22, 'qhris', 799, -15, 'MANUAL', '2026-04-12 01:17:18'),
(23, 'qhris', 974, -7, 'MANUAL', '2026-04-12 01:17:36'),
(24, 'qhris', 216, -17, 'MANUAL', '2026-04-12 01:23:00'),
(25, 'qhris', 906, -40, 'MANUAL', '2026-04-12 01:23:19'),
(26, 'qhris', 474, 7, 'MANUAL', '2026-04-12 01:24:18'),
(27, 'qhris', 735, -50, 'AUTOMATIC', '2026-04-12 01:31:20'),
(28, 'qhris', 60, 1, 'AUTOMATIC', '2026-04-12 01:32:05'),
(29, 'qhris', 202, -48, 'AUTOMATIC', '2026-04-12 01:34:13'),
(30, 'qhris', 339, -41, 'AUTOMATIC', '2026-04-12 01:35:52'),
(31, 'qhris', 270, -41, 'MANUAL', '2026-04-12 01:35:59'),
(32, 'qhris', 790, -11, 'AUTOMATIC', '2026-04-12 01:36:57'),
(33, 'qhris', 360, -36, 'AUTOMATIC', '2026-04-12 01:39:04'),
(34, 'qhris', 156, -12, 'MANUAL', '2026-04-12 01:40:09'),
(35, 'qhris', 999, -39, 'AUTOMATIC', '2026-04-12 01:40:16'),
(36, 'user', 889, -29, 'AUTOMATIC', '2026-04-12 01:57:02'),
(37, 'qhris', 221, -20, 'MANUAL', '2026-04-12 01:58:18'),
(38, 'qhris', 247, -20, 'MANUAL', '2026-04-12 01:58:25'),
(39, 'qhris', 125, -17, 'AUTOMATIC', '2026-04-12 01:58:37'),
(40, 'qhris', 1000, 2, 'MANUAL', '2026-04-16 15:40:17'),
(41, 'qhris', 1000, 1, 'MANUAL', '2026-04-16 15:42:33'),
(42, 'qhris', 50, -50, 'MANUAL', '2026-04-16 16:08:55'),
(43, 'qhris', 559, -28, 'MANUAL', '2026-04-16 16:09:20'),
(44, 'qhris', 243, 2, 'MANUAL', '2026-04-16 16:10:56'),
(45, 'qhris', 563, 2, 'MANUAL', '2026-04-16 16:11:12'),
(46, 'qhris', 984, 10, 'MANUAL', '2026-04-16 16:11:43'),
(47, 'qhris', 194, -25, 'AUTOMATIC', '2026-04-16 16:20:14'),
(48, 'qhris', 645, 9, 'AUTOMATIC', '2026-04-16 16:24:41'),
(49, 'qhris', 274, -8, 'MANUAL', '2026-04-16 16:24:48'),
(50, 'qhris', 270, -20, 'MANUAL', '2026-04-16 16:28:44'),
(51, 'qhris', 171, -19, 'MANUAL', '2026-04-16 16:29:30'),
(52, 'qhris', 696, -19, 'MANUAL', '2026-04-16 16:29:44'),
(53, 'qhris', 933, 0, 'AUTOMATIC', '2026-04-16 21:56:21'),
(54, 'qhris', 129, 0, 'MANUAL', '2026-04-16 21:59:51'),
(55, 'qhris', 351, -50, 'AUTOMATIC', '2026-04-16 22:00:04'),
(56, 'qhris', 871, -1, 'AUTOMATIC', '2026-04-16 22:00:16'),
(57, 'qhris', 163, -48, 'AUTOMATIC', '2026-04-16 22:00:20'),
(58, 'qhris', 961, -16, 'AUTOMATIC', '2026-04-16 22:03:06'),
(59, 'qhris', 839, -38, 'AUTOMATIC', '2026-04-16 22:03:08'),
(60, 'qhris', 262, 7, 'AUTOMATIC', '2026-04-16 22:03:11'),
(61, 'qhris', 348, -34, 'AUTOMATIC', '2026-04-16 22:03:15'),
(62, 'qhris', 423, -24, 'MANUAL', '2026-04-16 22:03:16'),
(63, 'qhris', 991, 5, 'AUTOMATIC', '2026-04-16 22:03:19'),
(64, 'qhris', 659, -31, 'AUTOMATIC', '2026-04-16 22:03:57'),
(65, 'qhris', 345, -12, 'AUTOMATIC', '2026-04-16 22:03:59'),
(66, 'qhris', 690, -12, 'AUTOMATIC', '2026-04-16 22:04:06'),
(67, 'qhris', 425, -2, 'AUTOMATIC', '2026-04-16 22:04:07'),
(68, 'qhris', 724, -6, 'AUTOMATIC', '2026-04-16 22:04:09'),
(69, 'qhris', 756, 3, 'AUTOMATIC', '2026-04-16 22:04:10'),
(70, 'qhris', 774, -18, 'AUTOMATIC', '2026-04-16 22:04:11'),
(71, 'qhris', 935, -42, 'AUTOMATIC', '2026-04-16 22:04:13'),
(72, 'qhris', 535, -22, 'AUTOMATIC', '2026-04-16 22:04:15'),
(73, 'qhris', 727, -49, 'AUTOMATIC', '2026-04-16 22:04:17'),
(74, 'qhris', 551, -39, 'AUTOMATIC', '2026-04-16 22:04:18'),
(75, 'qhris', 380, -12, 'AUTOMATIC', '2026-04-16 22:04:19'),
(76, 'qhris', 971, -46, 'AUTOMATIC', '2026-04-16 22:04:23'),
(77, 'qhris', 217, -24, 'AUTOMATIC', '2026-04-16 22:04:28'),
(78, 'qhris', 157, -46, 'AUTOMATIC', '2026-04-16 22:04:48'),
(79, 'qhris', 388, -2, 'AUTOMATIC', '2026-04-16 22:05:01'),
(80, 'qhris', 883, -15, 'AUTOMATIC', '2026-04-16 22:05:05'),
(81, 'qhris', 799, -5, 'AUTOMATIC', '2026-04-16 22:05:07'),
(82, 'qhris', 429, -47, 'AUTOMATIC', '2026-04-16 22:05:10'),
(83, 'qhris', 696, -21, 'AUTOMATIC', '2026-04-16 22:05:13');

-- --------------------------------------------------------

--
-- Table structure for table `system_logs`
--

CREATE TABLE `system_logs` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `action` varchar(255) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `system_logs`
--

INSERT INTO `system_logs` (`id`, `username`, `action`, `timestamp`) VALUES
(1, 'qhris', 'Logged In', '2026-04-11 16:45:31'),
(2, 'qhris', 'Logged In', '2026-04-11 16:50:07'),
(3, 'qhris', 'Account Created: prin', '2026-04-11 16:50:54'),
(4, 'qhris', 'Account Updated: prin', '2026-04-11 16:51:01'),
(5, 'qhris', 'Account Deleted: prin', '2026-04-11 16:51:08'),
(6, 'qhris', 'Used Radio: Adjusted Frequency to 221 MHz', '2026-04-11 16:51:24'),
(7, 'qhris', 'Logged In', '2026-04-11 16:58:14'),
(8, 'qhris', 'Logged In', '2026-04-11 16:59:52'),
(9, 'qhris', 'Logged In', '2026-04-11 17:09:22'),
(10, 'qhris', 'Logged In', '2026-04-11 17:10:59'),
(11, 'qhris', 'Account Created: pin', '2026-04-11 17:12:05'),
(12, 'qhris', 'Account Deleted: pin', '2026-04-11 17:12:15'),
(13, 'qhris', 'Used Radio: Adjusted Frequency to 297 MHz', '2026-04-11 17:12:51'),
(14, 'qhris', 'Used Radio: Adjusted Frequency to 210 MHz', '2026-04-11 17:13:57'),
(15, 'qhris', 'Used Radio: Adjusted Frequency to 799 MHz', '2026-04-11 17:17:18'),
(16, 'qhris', 'Used Radio: Adjusted Frequency to 974 MHz', '2026-04-11 17:17:36'),
(17, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 216 MHz', '2026-04-11 17:23:00'),
(18, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 906 MHz', '2026-04-11 17:23:19'),
(19, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 474 MHz', '2026-04-11 17:24:18'),
(20, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 735 MHz', '2026-04-11 17:31:20'),
(21, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 60 MHz', '2026-04-11 17:32:05'),
(22, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 202 MHz', '2026-04-11 17:34:13'),
(23, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 339 MHz', '2026-04-11 17:35:52'),
(24, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 270 MHz', '2026-04-11 17:35:59'),
(25, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 790 MHz', '2026-04-11 17:36:57'),
(26, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 360 MHz', '2026-04-11 17:39:04'),
(27, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 156 MHz', '2026-04-11 17:40:09'),
(28, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 999 MHz', '2026-04-11 17:40:16'),
(29, 'qhris', 'Account Created: p', '2026-04-11 17:40:47'),
(30, 'qhris', 'Account Updated: p', '2026-04-11 17:40:57'),
(31, 'qhris', 'Account Deleted: p', '2026-04-11 17:41:05'),
(32, 'qhris', 'Logged out (System Closed)', '2026-04-11 17:43:56'),
(33, 'qhris', 'Account Updated: qhris', '2026-04-11 17:47:41'),
(34, 'qhris', 'Logged out (System Closed)', '2026-04-11 17:47:43'),
(35, 'qhris', 'Logged out (System Closed)', '2026-04-11 17:53:40'),
(36, 'qhris', 'Logged in', '2026-04-11 17:54:48'),
(37, 'qhris', 'Logged out (System Closed)', '2026-04-11 17:55:28'),
(38, 'user', 'Logged in', '2026-04-11 17:56:53'),
(39, 'user', 'Used Radio (AUTOMATIC): Adjusted Frequency to 889 MHz', '2026-04-11 17:57:02'),
(40, 'user', 'Logged out (System Closed)', '2026-04-11 17:57:10'),
(41, 'qhris', 'Logged in', '2026-04-11 17:57:45'),
(42, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 221 MHz', '2026-04-11 17:58:18'),
(43, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 247 MHz', '2026-04-11 17:58:25'),
(44, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 125 MHz', '2026-04-11 17:58:37'),
(45, 'qhris', 'Logged out (System Closed)', '2026-04-11 17:59:35'),
(46, 'qhris', 'Logged in', '2026-04-16 07:39:44'),
(47, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 1000 MHz', '2026-04-16 07:40:17'),
(48, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 1000 MHz', '2026-04-16 07:42:33'),
(49, 'qhris', 'Logged in', '2026-04-16 08:08:22'),
(50, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 50 MHz', '2026-04-16 08:08:55'),
(51, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 559 MHz', '2026-04-16 08:09:20'),
(52, 'qhris', 'Logged in', '2026-04-16 08:10:41'),
(53, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 243 MHz', '2026-04-16 08:10:56'),
(54, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 563 MHz', '2026-04-16 08:11:12'),
(55, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 984 MHz', '2026-04-16 08:11:43'),
(56, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 194 MHz', '2026-04-16 08:20:14'),
(57, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 645 MHz', '2026-04-16 08:24:41'),
(58, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 274 MHz', '2026-04-16 08:24:48'),
(59, 'qhris', 'Logged out (System Closed)', '2026-04-16 08:24:59'),
(60, 'qhris', 'Logged in', '2026-04-16 08:25:33'),
(61, 'qhris', 'Logged out (System Closed)', '2026-04-16 08:25:41'),
(62, 'qhris', 'Logged in', '2026-04-16 08:28:38'),
(63, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 270 MHz', '2026-04-16 08:28:44'),
(64, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 171 MHz', '2026-04-16 08:29:30'),
(65, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 696 MHz', '2026-04-16 08:29:44'),
(66, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 933 MHz', '2026-04-16 13:56:21'),
(67, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 129 MHz', '2026-04-16 13:59:51'),
(68, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 351 MHz', '2026-04-16 14:00:04'),
(69, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 871 MHz', '2026-04-16 14:00:16'),
(70, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 163 MHz', '2026-04-16 14:00:20'),
(71, 'qhris', 'Logged out (System Closed)', '2026-04-16 14:00:21'),
(72, 'qhris', 'Logged in', '2026-04-16 14:03:01'),
(73, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 961 MHz', '2026-04-16 14:03:06'),
(74, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 839 MHz', '2026-04-16 14:03:08'),
(75, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 262 MHz', '2026-04-16 14:03:11'),
(76, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 348 MHz', '2026-04-16 14:03:15'),
(77, 'qhris', 'Used Radio (MANUAL): Adjusted Frequency to 423 MHz', '2026-04-16 14:03:16'),
(78, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 991 MHz', '2026-04-16 14:03:19'),
(79, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 659 MHz', '2026-04-16 14:03:57'),
(80, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 345 MHz', '2026-04-16 14:03:59'),
(81, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 690 MHz', '2026-04-16 14:04:06'),
(82, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 425 MHz', '2026-04-16 14:04:07'),
(83, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 724 MHz', '2026-04-16 14:04:09'),
(84, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 756 MHz', '2026-04-16 14:04:10'),
(85, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 774 MHz', '2026-04-16 14:04:11'),
(86, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 935 MHz', '2026-04-16 14:04:13'),
(87, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 535 MHz', '2026-04-16 14:04:15'),
(88, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 727 MHz', '2026-04-16 14:04:17'),
(89, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 551 MHz', '2026-04-16 14:04:18'),
(90, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 380 MHz', '2026-04-16 14:04:19'),
(91, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 971 MHz', '2026-04-16 14:04:23'),
(92, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 217 MHz', '2026-04-16 14:04:28'),
(93, 'qhris', 'Logged out (System Closed)', '2026-04-16 14:04:29'),
(94, 'qhris', 'Logged in', '2026-04-16 14:04:41'),
(95, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 157 MHz', '2026-04-16 14:04:48'),
(96, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 388 MHz', '2026-04-16 14:05:01'),
(97, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 883 MHz', '2026-04-16 14:05:05'),
(98, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 799 MHz', '2026-04-16 14:05:07'),
(99, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 429 MHz', '2026-04-16 14:05:10'),
(100, 'qhris', 'Used Radio (AUTOMATIC): Adjusted Frequency to 696 MHz', '2026-04-16 14:05:13'),
(101, 'qhris', 'Logged out (System Closed)', '2026-04-16 14:05:42'),
(102, 'user', 'Logged in', '2026-05-02 12:47:58'),
(103, 'user', 'Logged out (System Closed)', '2026-05-02 12:47:59'),
(104, 'qhris', 'Logged in', '2026-05-02 13:00:07'),
(105, 'qhris', 'Logged out (System Closed)', '2026-05-02 13:00:08'),
(106, 'qhris', 'Logged in', '2026-05-02 13:01:39'),
(107, 'qhris', 'Logged out (System Closed)', '2026-05-02 13:01:44'),
(108, 'qhris', 'Logged in', '2026-05-02 15:52:32'),
(109, 'qhris', 'Logged out (System Closed)', '2026-05-02 15:52:34'),
(110, 'qhris', 'Logged in', '2026-05-02 16:20:50'),
(111, 'qhris', 'Logged out (System Closed)', '2026-05-02 16:20:51'),
(112, 'qhris', 'Logged in', '2026-06-07 20:19:31'),
(113, 'qhris', 'Logged in', '2026-06-07 20:21:20'),
(114, 'qhris', 'Logged in', '2026-06-07 20:34:01'),
(115, 'qhris', 'Logged out (Manual)', '2026-06-07 20:35:42'),
(116, 'user', 'Logged in', '2026-06-07 20:35:46'),
(117, 'user', 'Account Deleted: admin', '2026-06-07 20:36:47'),
(118, 'user', 'Logged out (Manual)', '2026-06-07 20:39:21'),
(119, 'qhris', 'Logged in', '2026-06-07 20:39:30'),
(120, 'qhris', 'Account Created: admin (type: admin)', '2026-06-07 20:39:56'),
(121, 'qhris', 'Logged out (System Closed)', '2026-06-07 20:42:52'),
(122, 'user', 'Logged in', '2026-06-07 20:44:00'),
(123, 'user', 'Account Updated: user (type: user)', '2026-06-07 20:45:25'),
(124, 'user', 'Logged out (System Closed)', '2026-06-07 20:45:47'),
(125, 'user', 'Logged in', '2026-06-07 20:47:05'),
(126, 'user', 'Logged out (Manual)', '2026-06-07 20:47:11'),
(127, 'qhris', 'Logged in', '2026-06-07 20:47:16'),
(128, 'qhris', 'Logged out (System Closed)', '2026-06-07 20:47:20');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `usertype` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `name`, `email`, `usertype`) VALUES
(2, 'user', 'user', 'user', 'user@gmail.com', 'user'),
(3, 'loi', 'loi', 'loi floro', 'loifloro@gmail.com', 'admin'),
(5, 'qhris', 'qhris', 'qhris', 'qhrislora2004@gmail.com', 'admin'),
(14, 'admin', '1234', 'admin', 'loifloro@gmail.com', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `frequency_logs`
--
ALTER TABLE `frequency_logs`
  ADD PRIMARY KEY (`log_id`),
  ADD KEY `username` (`username`);

--
-- Indexes for table `system_logs`
--
ALTER TABLE `system_logs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `frequency_logs`
--
ALTER TABLE `frequency_logs`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT for table `system_logs`
--
ALTER TABLE `system_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `frequency_logs`
--
ALTER TABLE `frequency_logs`
  ADD CONSTRAINT `frequency_logs_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
