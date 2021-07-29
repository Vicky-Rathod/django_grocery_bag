from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .manager import UserManager

class User(AbstractBaseUser):
    """User model."""
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=50, blank=False)
    is_superadmin = models.BooleanField(_('is_superadmin'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def has_perm(self, perm, obj=None):
        return self.is_superadmin
    def has_module_perms(self, app_label):
        return self.is_superadmin