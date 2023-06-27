from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email to be provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if not kwargs['is_staff']:
            raise ValueError('Is_staff to be provided')
        if not kwargs['Is_superuser']:
            raise ValueError('Is_superuser to be provided')

        user = self.create_user(email, password, **kwargs)
        return user
