from django.db import models

# Create your models here.

class Absen(models.Model):
    category_kelas = (
        ('X','X'),
        ('XI', 'XI'),
        ('XII', 'XII'),
    )

    category_jurusan = (
        ('Teknik Komputer dan Jaringan', 'Teknik Komputer dan Jaringan'),
        ('Rekayasa Perangkat Lunak', 'Rekayasa Perangkat Lunak'),
        ('Perbankan Syariah', 'Perbankan Syariah'),
        ('Kriya Tekstil', 'Kriya Tekstil'),
        ('Teknik Kendaraan Ringan', 'Teknik Kendaraan Ringan'),
    )

    nama_depan     = models.CharField(max_length=100)
    nama_belakang  = models.CharField(max_length=100)
    kelas          = models.CharField(max_length=20, choices=category_kelas, default='x')
    jurusan        = models.CharField(max_length=100, choices=category_jurusan, default='tkj')
    alamat         = models.TextField()

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_depan)
