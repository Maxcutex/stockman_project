from django.db import models

# Create your models here.

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


# Create your models here.


class UserProfileManager(BaseUserManager):
    """ Helps Django work with our custom user model """

    def create_user(self, email, first_name, last_name, password=None):
        """ Creates a new user object """
        if not email:
            raise ValueError("Users must have an email address.")
        email = self.normalize_email(email)
        # validate if email exists.
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, is_active=True
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """ Creates and saves a new super user with given details. """
        user = self.create_user(email, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents a 'user profile' inside our system """

    username = None
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_full_name(self):
        """ Used to get a users full name. """
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        """ Used to get a users short name. """
        return self.first_name

    def __str__(self):
        """ For converting object to a string """
        return self.email
