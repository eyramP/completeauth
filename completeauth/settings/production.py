from .base import * #noqa
from .base import env

# Any exceptions on the site in production will be sent to the
# email addresses listed in admins,
# Must be a tuple with full name and email address
ADMINS = [("Eyram Cobblah", "e.cobblah@credo-itsoluttions.com",),]

#TODO add domain names of the production server
CSRF_TRUSTED_ORIGINS = [""]
