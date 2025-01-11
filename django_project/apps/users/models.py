from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    # иначе будет ОШИБКА:  повторяющееся значение ключа нарушает
    # ограничение уникальности
    username = None

    email = models.EmailField(max_length=255,
                              verbose_name='Электронный адрес',
                              unique=True)  # сделал уникальным
    birth_date = models.DateField(blank=True,
                                  null=True,
                                  verbose_name='Дата рождения')
    avatar = models.ImageField(upload_to='users/avatars/%Y/%m/%d',
                               blank=True,
                               verbose_name='Аватар')
    balance = models.DecimalField(max_digits=10,
                                  decimal_places=2,
                                  default=0,
                                  verbose_name='Баланс')

    phone_regex = RegexValidator(regex=r'^((\+7)|8)\d{10}$',
                                 message="Номер телефона должен быть в формате: '+79999999999' или '89999999999'.")
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=12,
                                    null=True,
                                    blank=True,
                                    verbose_name='Телефон')

    USERNAME_FIELD = 'email'  # уникальный идентификатор юзера, теперь это мыло
    REQUIRED_FIELDS = []  # только для создание пользователя через менеджер и createuser

    objects = CustomUserManager()  # кастомный менеджер для юзеров (create_user / superuser)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']

    def __str__(self):
        return self.email
