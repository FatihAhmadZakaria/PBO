-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 18, 2022 at 06:49 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpus`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_buku`
--

CREATE TABLE `data_buku` (
  `id_buku` varchar(5) NOT NULL,
  `subjek` varchar(50) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `penulis` varchar(50) NOT NULL,
  `info` varchar(50) NOT NULL,
  `stok` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_buku`
--

INSERT INTO `data_buku` (`id_buku`, `subjek`, `judul`, `penulis`, `info`, `stok`) VALUES
('0001', 'Novel', 'Orang-orang Biasa', 'Andrea Hirata', 'Novel Lt 1 Rak No 23', 35),
('0002', 'Novel', 'Negeri Para Bedebah', 'Tere Liye', 'Novel Lt 1 Rak No 39', 25);

-- --------------------------------------------------------

--
-- Table structure for table `data_dvd`
--

CREATE TABLE `data_dvd` (
  `id_buku` varchar(5) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `info` varchar(50) NOT NULL,
  `stok` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_dvd`
--

INSERT INTO `data_dvd` (`id_buku`, `judul`, `info`, `stok`) VALUES
('1001', 'Basic JavaScript', 'DVD Lt 3 Rak No 40', 16),
('1002', 'Komponen Komputer', 'DVD Lt 3 Rak No 2', 20);

-- --------------------------------------------------------

--
-- Table structure for table `data_majalah`
--

CREATE TABLE `data_majalah` (
  `id_buku` varchar(5) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `vol` varchar(5) NOT NULL,
  `issue` varchar(50) NOT NULL,
  `info` varchar(50) NOT NULL,
  `stok` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_majalah`
--

INSERT INTO `data_majalah` (`id_buku`, `judul`, `vol`, `issue`, `info`, `stok`) VALUES
('2001', 'Motor Hits 2022', '1', 'Kendaraan', 'Majalah Lt 2 Rak No 1', 30),
('2002', 'Motor Hits 2022', '2', 'Kendaraan', 'Majalah Lt 2 Rak No 1', 30),
('2010', 'Smartphone Terbaik April 2022', '1', 'Teknologi', 'Majalah Lt 2 Rak No 29', 20);

-- --------------------------------------------------------

--
-- Table structure for table `kembali`
--

CREATE TABLE `kembali` (
  `id_kembali` int(5) NOT NULL,
  `subjek` varchar(50) NOT NULL,
  `id_buku` varchar(5) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `tgl_kembali` varchar(50) NOT NULL,
  `jumlah` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kembali`
--

INSERT INTO `kembali` (`id_kembali`, `subjek`, `id_buku`, `nama`, `tgl_kembali`, `jumlah`) VALUES
(1, 'Novel', '001', 'Andi', '2022-04-18 15:52:02', 3),
(4, 'DVD', '1001', 'Rian', '2022-04-18 21:33:16', 1);

--
-- Triggers `kembali`
--
DELIMITER $$
CREATE TRIGGER `del_in` AFTER DELETE ON `kembali` FOR EACH ROW BEGIN
	UPDATE data_buku SET stok= stok - OLD.jumlah
	WHERE id_buku = OLD.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `del_in_dvd` AFTER DELETE ON `kembali` FOR EACH ROW BEGIN
	UPDATE data_dvd SET stok= stok - OLD.jumlah
	WHERE id_buku = OLD.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `del_in_mj` AFTER DELETE ON `kembali` FOR EACH ROW BEGIN
	UPDATE data_majalah SET stok= stok - OLD.jumlah
	WHERE id_buku = OLD.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trig_in_dvd` AFTER INSERT ON `kembali` FOR EACH ROW BEGIN
	UPDATE data_dvd SET stok= stok + NEW.jumlah
	WHERE id_buku = NEW.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trig_in_mj` AFTER INSERT ON `kembali` FOR EACH ROW BEGIN
	UPDATE data_majalah SET stok= stok + NEW.jumlah
	WHERE id_buku = NEW.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trig_kembali` AFTER INSERT ON `kembali` FOR EACH ROW BEGIN
	UPDATE data_buku SET stok= stok + NEW.jumlah
	WHERE id_buku = NEW.id_buku;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `peminjam`
--

CREATE TABLE `peminjam` (
  `id_pinjam` int(5) NOT NULL,
  `subjek` varchar(50) NOT NULL,
  `id_buku` varchar(5) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `tgl_keluar` varchar(50) NOT NULL,
  `jumlah` int(5) NOT NULL,
  `kembali` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `peminjam`
--

INSERT INTO `peminjam` (`id_pinjam`, `subjek`, `id_buku`, `nama`, `tgl_keluar`, `jumlah`, `kembali`) VALUES
(1, 'Novel', '002', 'Adit', '2022-04-18 15:39:05', 1, '2022-04-20'),
(5, 'Novel', '0001', 'Bagas', '2022-04-18 21:31:54', 1, '2022-04-21');

--
-- Triggers `peminjam`
--
DELIMITER $$
CREATE TRIGGER `del_out` AFTER DELETE ON `peminjam` FOR EACH ROW BEGIN
	UPDATE data_buku SET stok= stok + OLD.jumlah
	WHERE id_buku = OLD.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `del_out_dvd` AFTER DELETE ON `peminjam` FOR EACH ROW BEGIN
	UPDATE data_majalah SET stok= stok + OLD.jumlah
	WHERE id_buku = OLD.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `del_out_mj` AFTER DELETE ON `peminjam` FOR EACH ROW BEGIN
	UPDATE data_majalah SET stok= stok + OLD.jumlah
	WHERE id_buku = OLD.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trig_out` AFTER INSERT ON `peminjam` FOR EACH ROW BEGIN
	UPDATE data_buku SET stok= stok - NEW.jumlah
	WHERE id_buku = NEW.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trig_out_dvd` AFTER INSERT ON `peminjam` FOR EACH ROW BEGIN
	UPDATE data_dvd SET stok= stok - NEW.jumlah
	WHERE id_buku = NEW.id_buku;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trig_out_mj` AFTER INSERT ON `peminjam` FOR EACH ROW BEGIN
	UPDATE data_majalah SET stok= stok - NEW.jumlah
	WHERE id_buku = NEW.id_buku;
END
$$
DELIMITER ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_buku`
--
ALTER TABLE `data_buku`
  ADD PRIMARY KEY (`id_buku`);

--
-- Indexes for table `data_dvd`
--
ALTER TABLE `data_dvd`
  ADD PRIMARY KEY (`id_buku`);

--
-- Indexes for table `data_majalah`
--
ALTER TABLE `data_majalah`
  ADD PRIMARY KEY (`id_buku`);

--
-- Indexes for table `kembali`
--
ALTER TABLE `kembali`
  ADD PRIMARY KEY (`id_kembali`);

--
-- Indexes for table `peminjam`
--
ALTER TABLE `peminjam`
  ADD PRIMARY KEY (`id_pinjam`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kembali`
--
ALTER TABLE `kembali`
  MODIFY `id_kembali` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `peminjam`
--
ALTER TABLE `peminjam`
  MODIFY `id_pinjam` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
