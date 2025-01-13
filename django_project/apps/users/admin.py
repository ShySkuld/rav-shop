from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'phone_number', 'display_avatar', 'is_superuser',
                    'is_staff', 'is_active')
    readonly_fields = ('display_avatar', )  # иначе FieldError Unknown field(s)
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    ordering = ('-date_joined', )
    search_fields = ("email", )

    #  отображение полей в админке - Изменить Пользователь
    fieldsets = (
        (None, {'fields': (
                'email', 'password', 'first_name', 'last_name', 'phone_number',
                'birth_date', 'display_avatar', 'avatar', 'is_superuser',
                'is_staff', 'is_active'
        )}),
        ("Разрешения", {"fields": ("groups", "user_permissions")}),
    )

    #  отображение полей в админке - Добавить Пользователь
    add_fieldsets = (
        (None, {'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name',
                'birth_date', 'phone_number', 'is_superuser', 'is_staff',
                'is_active', 'avatar', 'groups', 'user_permissions')}
         ),
    )

    #  кастомное отображаемое поле Аватар
    @admin.display(description='Изображние')
    def display_avatar(self, user: CustomUser):
        #  mark_safe экранирует теги
        return mark_safe(f'<img src={user.avatar.url} width=50>')
