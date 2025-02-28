import os

DEBUG = False

rdbms = os.environ.get("RDBMS", "sqlite")

if rdbms == "sqlite":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        },
        "secondary": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        },
    }
elif rdbms == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB", "default"),
            "USER": os.environ.get("POSTGRES_USER", "postgres"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
            "HOST": os.environ.get("POSTGRES_HOST", ""),
            "PORT": os.environ.get("POSTGRES_PORT", ""),
        },
        "secondary": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB", "secondary"),
            "USER": os.environ.get("POSTGRES_USER", "postgres"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
            "HOST": os.environ.get("POSTGRES_HOST", ""),
            "PORT": os.environ.get("POSTGRES_PORT", ""),
        },
    }
# elif rdbms == "mysql":  # pragma: no cover
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.mysql",
#             "NAME": os.environ.get("MYSQL_DATABASE", "default"),
#             "USER": os.environ.get("MYSQL_USER", "root"),
#             "PASSWORD": os.environ.get("MYSQL_PASSWORD", "root"),
#             "HOST": os.environ.get("MYSQL_HOST", "127.0.0.1"),
#             "PORT": os.environ.get("MYSQL_PORT", "3306"),
#         },
#         "secondary": {
#             "ENGINE": "django.db.backends.mysql",
#             "NAME": os.environ.get("MYSQL_DATABASE", "secondary"),
#             "USER": os.environ.get("MYSQL_USER", "root"),
#             "PASSWORD": os.environ.get("MYSQL_PASSWORD", "root"),
#             "HOST": os.environ.get("MYSQL_HOST", "127.0.0.1"),
#             "PORT": os.environ.get("MYSQL_PORT", "3306"),
#         }
#     }
# elif rdbms == "mariadb":  # pragma: no cover
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.mysql",
#             "NAME": os.environ.get("MARIADB_DATABASE", "default"),
#             "USER": os.environ.get("MARIADB_USER", "root"),
#             "PASSWORD": os.environ.get("MARIADB_PASSWORD", "root"),
#             "HOST": os.environ.get("MARIADB_HOST", "127.0.0.1"),
#             "PORT": os.environ.get("MARIADB_PORT", "3306"),
#         },
#         "secondary": {
#             "ENGINE": "django.db.backends.mysql",
#             "NAME": os.environ.get("MARIADB_DATABASE", "secondary"),
#             "USER": os.environ.get("MARIADB_USER", "root"),
#             "PASSWORD": os.environ.get("MARIADB_PASSWORD", "root"),
#             "HOST": os.environ.get("MARIADB_HOST", "127.0.0.1"),
#             "PORT": os.environ.get("MARIADB_PORT", "3306"),
#         }
#     }
# elif rdbms == "oracle":  # pragma: no cover
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.oracle",
#             "NAME": f"{os.environ.get('ORACLE_HOST', 'localhost')}:"
#             f"{os.environ.get('ORACLE_PORT', '1521')}"
#             f"/{os.environ.get('ORACLE_DATABASE', 'XEPDB1')}",
#             "USER": os.environ.get("ORACLE_USER", "system"),
#             "PASSWORD": os.environ.get("ORACLE_PASSWORD", "password"),
#         }
#     }


DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.admin",
    "polymorphic",
    "polymorphic.tests",
)
MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)
SITE_ID = 3
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (),
        "OPTIONS": {
            "loaders": (
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ),
            "context_processors": (
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
            ),
        },
    }
]
POLYMORPHIC_TEST_SWAPPABLE = "polymorphic.swappedmodel"
ROOT_URLCONF = None
SECRET_KEY = "supersecret"
