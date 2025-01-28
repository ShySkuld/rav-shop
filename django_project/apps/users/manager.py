from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        # email - это USERNAME_FIELD из модели
        if not email:
            raise ValueError('Адрес электронной почты обязателен')

        # все знаки после @ в нижний регистр
        user = self.model(email=self.normalize_email(email)) # все после @ в нижний регистр
        user.set_password(password)
        user.save(using=self._db) # DATABASES = {'default':
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
