AUTHOR = 'Mark Grosen'
SITENAME = 'MicroPython Extras'
SITEURL = ''

PATH = 'content'

THEME = 'flex'
SITELOGO = "images/constitution.png"
SITETITLE = "MicroPython Extras"
SITESUBTITLE = "Packages and modules for boards and peripherals"
SITEDESCRIPTION = "Packages and modules for boards and peripherals"
FAVICON = "images/favicon.ico"
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

STATIC_PATHS = ("images", "binaries", "static")

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('MicroPython', 'https://github.com/micropython/micropython'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
