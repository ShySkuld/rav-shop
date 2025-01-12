from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'phone_number', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    ordering = ('-date_joined',)
    search_fields = ("email",)

    #  отображение полей в админке - Изменить Пользователь
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name',
                           'phone_number', 'birth_date', 'avatar',
                           'is_superuser', 'is_staff', 'is_active')}),
        ("Разрешения", {"fields": ("groups", "user_permissions")}),
    )

    #  отображение полей в админке - Добавить Пользователь
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name',
                'birth_date', 'phone_number', 'is_superuser', 'is_staff',
                'is_active', 'avatar', 'groups', 'user_permissions'
            )}
        ),
    )

#admin.site.register(CustomUser, CustomUserAdmin)
