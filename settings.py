from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'Baseline_trt1',
        'display_name': "trt1",
        'num_demo_participants': 1,
        'app_sequence': ['baseline','questionnaire'],
        'x': 0,
        'trt': 1,
        'prize': 20,

    },
    {
        'name': 'Baseline_trt2',
        'display_name': "trt2",
        'num_demo_participants': 1,
        'app_sequence': ['baseline','questionnaire'],
        'x':0,
        'trt': 2,
        'prize': 10,

    },
    {
        'name': 'Baseline_trt3',
        'display_name': "trt3",
        'num_demo_participants': 1,
        'app_sequence': ['baseline','questionnaire'],
        'prize': 20,
        'trt': 3,
        'x': 2
    },
{
        'name': 'Baseline_trt4',
        'display_name': "trt4",
        'num_demo_participants': 1,
        'app_sequence': ['baseline','questionnaire'],
        'trt':4,
        'x':0,
        'prize': 20,
    },
{
        'name': 'trt5',
        'display_name': "trt5",
        'num_demo_participants': 1,
        'app_sequence': ['trt5','questionnaire'],
        'trt':4,
        'x':0,
        'prize': 20,
    },
{
        'name': 'questionnaire',
        'display_name': "questionnaire",
        'num_demo_participants': 1,
        'app_sequence': ['questionnaire'],
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3)lr6ue2cd!kf!nwl-%06o1!f9zn7b+a*-8)toil2s@(f_be!1'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
