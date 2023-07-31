-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 16 Jun 2023 pada 14.39
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbapi`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `dosen`
--

CREATE TABLE `dosen` (
  `nid` int(11) NOT NULL,
  `nidn` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jk` enum('P','L') NOT NULL DEFAULT 'L',
  `prodi` varchar(20) NOT NULL,
  `jabatan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `dosen`
--

INSERT INTO `dosen` (`nid`, `nidn`, `nama`, `jk`, `prodi`, `jabatan`) VALUES
(1, 6001, 'Fahmi ', 'L', 'TIF', 'DLB'),
(3, 6003, 'Agust Isa Martinus, M.T', 'L', '0856543456', 'DT'),
(4, 6004, 'Harry Gunawan, M.kom', 'L', '0876897654', 'DT'),
(9, 6007, 'Arie Susetyo', 'P', 'IND', 'Kaprodi'),
(12, 6008, 'Dian Novianti, M.Kom', 'P', 'TIF', 'Kaprodi'),
(14, 6009, 'Khairul Anwarudin', 'L', 'TIF', 'DT'),
(17, 6002, 'Freddy Wicaksono,M.Kom', 'L', 'TIF', 'DT'),
(18, 6010, 'Ibu', 'P', 'PET', 'DPET');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `dosen`
--
ALTER TABLE `dosen`
  ADD PRIMARY KEY (`nid`),
  ADD UNIQUE KEY `unik` (`nidn`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `dosen`
--
ALTER TABLE `dosen`
  MODIFY `nid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
