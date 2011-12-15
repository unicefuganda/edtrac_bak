#Toggle On/Off Training mode for schools reporting
TRAINING_MODE = False

COUNTRY_CALLING_CODE = '256'
BACKEND_PREFIXES = [('75', 'zain'), ('71', 'utl'), ('', 'dmark')]
REFRESH_WHITELIST_URL = "http://127.0.0.1:13013/cgi-bin/refreshlist?username=kannel&password=kannel&name=education"

# for postgresql:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "emis",
        "HOST": "localhost",
	"USER": "postgres",
	"PASSWORD": "postgres",
    }
}

SITE_ID = 5

import datetime
SCHOOL_TERM_START = datetime.datetime(2011, 9, 5)
SCHOOL_TERM_LENGTH = 12 #Average school term length in weeks
SCHOOL_HOLIDAYS = [
# (start_of_holiday_datetime, end_of_holidate_datetime),
# (start_of_holiday2_datetime...),
# (,),
# ...
]
SCHOOL_ANNUAL_MESSAGES_START = 12 #Number of Weeks
