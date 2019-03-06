from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Danlin chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=18, max=100)
    gender = models.StringField(choices=['Female', 'Male'], widget=widgets.RadioSelect)
    Nationality = models.StringField(choices=['UK', 'EU (not UK)', 'North America', 'South America', 'Africa', 'Asia'], widget=widgets.RadioSelect)
    Job_status = models.StringField(choices=['Full - time','employed', 'Part - time employed', 'Unemployed', 'Retired'], widget=widgets.RadioSelect)
    Marital_status = models.StringField(choices=['Married', 'Partnership', 'Single', 'Widowed', 'Divorced'], widget=widgets.RadioSelect)
    Annual_household_income = models.StringField(choices=['£0 - £20000','20, 001 – 40, 000','40, 001 – 80, 000','80, 001'], widget=widgets.RadioSelect)
    Household_size=models.StringField(choices=['Single','People, 3 - 4','People,5 + people'], widget=widgets.RadioSelect)
    Education_level= models.StringField(choices = ['Middle - school','High - school','Bachelor','Master','PhD'], widget=widgets.RadioSelect)
    Education_discipline= models.IntegerField()
    Political_preferences= models.IntegerField(widget=widgets.Slider())
    Environmental_preferences = models.IntegerField(widget=widgets.Slider())
    Charity = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect, label='Involed in Charity organisations?')
    Satisfaction_experiment= models.IntegerField(choices=[0,1,2,3,4,5,6,7,8,9,10],widget=widgets.RadioSelect)
    Health_status = models.StringField(choices=['Poor', 'Moderate', 'Good', 'Very Good', 'Excellent'], widget=widgets.RadioSelect)
    severe_disease = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect, label='Any severe disease experienced over the last year?')
    disease_explain = models.StringField(label='If yes, pleae explain', blank=True)
    ongoing_disease = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelect, label='Any ongoing severe disease experienced?')
    ongoing_disease_explain = models.StringField(label='If yes, pleae explain', blank=True)
    smoke = models.StringField(choices=['Yes', 'No'], label='Do you smoke?', widget=widgets.RadioSelect)
    drink = models.IntegerField(choices=[0, 1, 2, 3, 4, 5, 6, 7], label='How many days per week do you drink alcohol?', widget=widgets.RadioSelect)
    height = models.IntegerField(min=1, max=240, label='What is your height?')
    weight = models.IntegerField(min=1, max=1000, label='What is your weight?')
    seat_belt = models.StringField(choices=['Yes', 'No'], label='Do you regularly wear seat-belt in a vehicle that requires seat-belt use?', widget=widgets.RadioSelect)
    over_speed = models.StringField(choices = ['Not applicable',
                                               'Never',
                                               'Occasionally',
                                               'Sometimes',
                                               'Often',
                                               'Always]'], label='How many times do you drive over speed limit?', widget=widgets.RadioSelect)