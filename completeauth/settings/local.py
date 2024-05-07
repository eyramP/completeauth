# Below tells the linter to ignore this line below
from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",
                 default="qQ0za0ZVq8BN7zNRy7NGEf-k06WZnCPHRfmfDw73EGAnygr3GfQ",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# List of domains that are allowed to make cross site request to your site
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
]