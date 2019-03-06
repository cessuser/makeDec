from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import  models

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass

class Questions(Page):
    form_model = models.Player
    form_fields = ['age', 'gender', 'Nationality', 'Job_status', 'Marital_status', 'Annual_household_income',
                   'Household_size', 'Education_level', 'Education_discipline', 'Political_preferences', 'Environmental_preferences',
                   'Charity', 'Satisfaction_experiment', 'Health_status', 'severe_disease', 'disease_explain',
                   'ongoing_disease', 'ongoing_disease_explain', 'smoke', 'drink', 'height', 'weight', 'seat_belt', 'over_speed']

page_sequence = [
    Questions
]
