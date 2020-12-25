from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class VoterManager(BaseUserManager):
    def create_user(self, email, npm, name, password=None):
        if not email:
            raise ValueError("Voters must have an email address")
        if not npm:
            raise ValueError("Voters must have an NPM (Student Number)")

        user = self.model(
            email=self.normalize_email(email),
            npm=npm,
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, npm, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            npm=npm,
            password=password,
            name=name
        )

        user.is_registered = True
        user.is_verified = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

PRODI_CHOICES = [
    ('S1 - Angkatan 2014', 'S1 - Angkatan 2014'),
    ('S1 - Angkatan 2015', 'S1 - Angkatan 2015'),
    ('S1 - Angkatan 2016', 'S1 - Angkatan 2016'),
    ('S1 - Angkatan 2017', 'S1 - Angkatan 2017'),
    ('S1 - Angkatan 2018', 'S1 - Angkatan 2018'),
    ('S1 - Angkatan 2019', 'S1 - Angkatan 2019'),
    ('S1 - Angkatan 2020', 'S1 - Angkatan 2020'),
    ('S2', 'S2'),
    ('S3', 'S3'),
    ('Profesi Apoteker', 'Profesi Apoteker')
]

class Voter(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=256, unique=True)
    name = models.CharField(max_length=256)
    npm = models.CharField(max_length=10, unique=True, primary_key=True)
    prodi = models.CharField(max_length=50, choices=PRODI_CHOICES)
    bukti_foto = models.ImageField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'npm']
    is_registered = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    object = VoterManager()

    def __str__(self):
        return self.name

    def get_first_name(self):
        return self.name.split(" ")[0]
