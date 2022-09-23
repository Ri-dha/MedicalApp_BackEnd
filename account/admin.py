from django.contrib import adminfrom django.contrib.auth import get_user_modelfrom django.contrib.auth.admin import UserAdmin as BaseUserAdminfrom account.forms import UserAdminChangeForm, UserAdminCreationFormfrom account.models import EmailAccountUser = get_user_model()class EmailAccountAdmin(BaseUserAdmin):    # The forms to add and change user instances    form = UserAdminChangeForm    add_form = UserAdminCreationForm    # The fields to be used in displaying the User model.    # These override the definitions on the base UserAdmin    # that reference specific fields on auth.User.    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',)    list_filter = ('is_superuser', 'is_staff')    readonly_fields = ('account_type',)    fieldsets = (        (None, {'fields': ('email', 'password')}),        ('Personal info', {'fields': (            'first_name', 'last_name', 'phone_number', 'address')}),        ('Permissions',         {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions',)}),        ('Important dates', {'fields': ('last_login', 'date_joined')}),        ('readonly_fields', {'fields':('account_type',)}),    )    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin    # overrides get_fieldsets to use this attribute when creating a user.    add_fieldsets = (        (None, {            'classes': ('wide',),            'fields': ('email', 'password1', 'password2')}         ),    )    search_fields = ('first_name', 'last_name', 'email')    ordering = ('email',)    filter_horizontal = ()admin.site.register(EmailAccount, EmailAccountAdmin)