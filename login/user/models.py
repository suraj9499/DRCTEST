from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            name=name,
            phone=phone,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email = self.normalize_email(email),
            name=name,
            password=password,
            phone=phone,
      
        )
        user.is_admin = True
        user.save(using=self._db)
        return user




class My_User(AbstractBaseUser):
  email = models.EmailField(verbose_name='email address', max_length=100, unique=True )
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message='''Phone number must be entered in the format:
                                  '+999999999'. Up to 15 digits allowed.''')

  phone = models.CharField(validators=[phone_regex],max_length=17, null=True, blank=True, unique=True)
  name = models.CharField(max_length=100)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  objects = MyUserManager()

  USERNAME_FIELD = 'phone'
  REQUIRED_FIELDS = ['name', 'email']

  def __str__(self) -> str:
    return self.email

  def __str__(self):
        return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return True

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin





class File_upload(models.Model):
  name=models.CharField(max_length=100)
  file=models.FileField()
  