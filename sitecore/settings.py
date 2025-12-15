import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost 127.0.0.1 Raymondred.pythonanywhere.com").split()

INSTALLED_APPS = [
    "django.contrib.admin","django.contrib.auth","django.contrib.contenttypes",
    "django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles",
    "protfolio",
    "crispy_forms",
    "markdownx",
    "crispy_bootstrap4",
    "rest_framework",
]
CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # serve static in production
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "sitecore.urls"

TEMPLATES = [{ "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"], "APP_DIRS": True, "OPTIONS": {"context_processors": [
        "django.template.context_processors.debug","django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth","django.contrib.messages.context_processors.messages",
    ]}}]

WSGI_APPLICATION = "sitecore.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        # MySQL database name (string). 
        "NAME": "myportfolio",        # <-- the DB you created in MySQL
        "USER": "Admin",              # your DB user (case-sensitive)
        "PASSWORD": "Admin@123",      # your DB password
        "HOST": "localhost",
        "PORT": "3306",
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

STATIC_URL = "/static/"
STATIC_ROOT =os.path.join( BASE_DIR / "staticfiles")
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Media (for uploaded images via markdownx)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"




DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email (development)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# For production, use SMTP/Mailgun/SendGrid and set credentials in .env
