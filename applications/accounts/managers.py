from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# CUSTOM || Function to raise error
def errorFieldEmpty(value, message):
    if not value:
        raise ValueError(message)


# CUSTOM || Class to overwrite Django User creation
class UserAdminCreationForm(BaseUserManager):

    # DJANGO || Function to create user | Function parameters = REQUIRED_FIELDS + USERNAME_FIELD
    def create_user(self, username, email, firstname, password=None):
        errorFieldEmpty(username, 'Username manquant.')
        errorFieldEmpty(email, 'Email manquant.')
        errorFieldEmpty(firstname, 'Prénom manquant.')

        user = self.model(
                username=username,
                email=email,
                firstname=firstname,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    # DJANGO || Function to create super user | Function parameters = REQUIRED_FIELDS + USERNAME_FIELD
    def create_superuser(self, username, email, firstname, password):
        user = self.create_user(
                password=password,
                username=username,
                email=email,
                firstname=firstname,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
