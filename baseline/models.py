from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django import forms
import random
import numpy as np

author = 'Danlin Chen'

doc = """
Francesco experiment baseline 
picture from:
South Sudanese children starving while aid falling short ...
worldhunger.org
"""

KS = [
    ('Yellow', 'Yellow'),
    ('Orange', 'Orange'),
    ('Red', 'Red'),
    ('Purple', 'Purple'),
    ('Pink', 'Pink'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Grey', 'Grey'),
    ('Brown', 'Brown'),
    ('Black', 'Black')
]
REGIONS = [
    ('Region 1', 'Region 1'),
    ('Region 2', 'Region 2'),
    ('Region 3', 'Region 3'),
    ('Region 4', 'Region 4'),
    ('Region 5', 'Region 5'),
    ('Region 6', 'Region 6'),
    ('Region 7', 'Region 7'),
    ('Region 8', 'Region 8'),
    ('Region 9', 'Region 9'),
    ('Region 10', 'Region 10'),
]
K_KS = [
    (0, 'Bag K'),
    (10, 'Bag K'),
    (20, 'Bag K'),
    (30, 'Bag K'),
    (40, 'Bag K'),
    (50, 'Bag K'),
    (60, 'Bag K'),
    (70, 'Bag K'),
    (80, 'Bag K'),
    (90, 'Bag K'),
    (100, 'Bag K'),
]
U_KS = [
    (100, 'Bag U'),
    (90, 'Bag U'),
    (80, 'Bag U'),
    (70, 'Bag U'),
    (60, 'Bag U'),
    (50, 'Bag U'),
    (40, 'Bag U'),
    (30, 'Bag U'),
    (20, 'Bag U'),
    (10, 'Bag U'),
    (0, 'Bag U'),
]


class Constants(BaseConstants):
    name_in_url = 'baseline'
    players_per_group = None
    num_rounds = 3

    prize = c(20)
    lose = c(0)

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['ten_var'] = []
            self.session.vars['tens'] = []



class Group(BaseGroup):
    def set_p(self):
        for p in self.get_players():
            p.store_p()


class Player(BasePlayer):
    colors = models.StringField(widget=forms.CheckboxSelectMultiple(choices=KS), label=' ')
    regions = models.StringField(widget=forms.CheckboxSelectMultiple(choices=REGIONS), label=' ')

    K0 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K1 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K2 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K3 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K4 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K5 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K6 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K7 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K8 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K9 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')
    K10 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag K')

    U0 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U1 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U2 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U3 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U4 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U5 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U6 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U7 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U8 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U9 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')
    U10 = models.BooleanField(widget=widgets.CheckboxInput, label='Bag U')

    ten = models.IntegerField()
    ten1 = models.BooleanField(widget=widgets.CheckboxInput)
    ten1U = models.BooleanField(widget=widgets.CheckboxInput)
    ten2 = models.BooleanField(widget=widgets.CheckboxInput)
    ten2U = models.BooleanField(widget=widgets.CheckboxInput)
    ten3 = models.BooleanField(widget=widgets.CheckboxInput)
    ten3U = models.BooleanField(widget=widgets.CheckboxInput)
    ten4 = models.BooleanField(widget=widgets.CheckboxInput)
    ten4U = models.BooleanField(widget=widgets.CheckboxInput)
    ten5 = models.BooleanField(widget=widgets.CheckboxInput)
    ten5U = models.BooleanField(widget=widgets.CheckboxInput)
    ten6 = models.BooleanField(widget=widgets.CheckboxInput)
    ten6U = models.BooleanField(widget=widgets.CheckboxInput)
    ten7 = models.BooleanField(widget=widgets.CheckboxInput)
    ten7U = models.BooleanField(widget=widgets.CheckboxInput)
    ten8 = models.BooleanField(widget=widgets.CheckboxInput)
    ten8U = models.BooleanField(widget=widgets.CheckboxInput)
    ten9 = models.BooleanField(widget=widgets.CheckboxInput)
    ten9U = models.BooleanField(widget=widgets.CheckboxInput)

    p = models.IntegerField()

    chosen_sec = models.IntegerField()
    chosen_sec_p = models.IntegerField()
    chosen_p = models.IntegerField()


    def p_tens(self):
        if self.K0:
            self.p = -1
            return -1
        if self.K0 != self.K1:
            return 0
        elif self.K1 != self.K2:
            return 10
        elif self.K2 != self.K3:
            return 20
        elif self.K3 != self.K4:
            return 30
        elif self.K4 != self.K5:
            return 40
        elif self.K5 != self.K6:
            return 50
        elif self.K6 != self.K7:
            return 60
        elif self.K7 != self.K8:
            return 70
        elif self.K8 != self.K9:
            return 80
        elif self.K9 != self.K10:
            return 90
        elif self.U10:
            return 100
        else:
            return -1

    def store_p(self):
        p = self.ten
        print("++++++++++++++++++p: ", self.ten, ' ', self.K0, ' ', self.K1)
        if self.ten1:
            p = self.ten
        elif self.ten1 != self.ten2:
            p = p + 2
        elif self.ten2 != self.ten3:
            p = p + 3
        elif self.ten3 != self.ten4:
            p = p + 4
        elif self.ten4 != self.ten5:
            p = p + 5
        elif self.ten5 != self.ten6:
            p = p + 6
        elif self.ten6 != self.ten7:
            p = p + 7
        elif self.ten7 != self.ten8:
            p = p + 8
        elif self.ten8 != self.ten9:
            p = p+8
        else:
            p = p + 9

        self.p = p

        if self.round_number == 1:
            self.participant.vars['p'] = []
        self.participant.vars['p'].append(self.p)

    def set_payoff(self):
        tens = self.participant.vars['tens']
        cols = self.participant.vars['cols']
        p = self.participant.vars['p']
        cur_round = random.randint(0, 2)

        self.chosen_sec = [3,1,5][cur_round]

        cur_cols = cols[cur_round]
        cur_ten = tens[cur_round]
        cur_p = p[cur_round] # value of p
        self.chosen_sec_p = cur_p
        cur_q = random.randint(0, 100) # choosen quesiton

        self.chosen_p = cur_q
        win = 0
        print('cur_cols ', cur_cols, ' cur_ten ', cur_ten, ' cur_p', cur_p, ' win ')

        if cur_ten == -1:
            print("all k")
            win = np.random.choice(np.arange(0, 2), p=[1 - cur_q / 100.0, cur_q / 100.0])

        if cur_ten == 100:
            print('all U')
            ball_cols = ['Yellow','Orange','Red', 'Purple', 'Pink', 'Blue', 'Green', 'Grey', 'Brown', 'Black']
            if self.session.config['trt'] == 4:
                ball_cols = ['Region 1','Region 2','Region 3','Region 4','Region 5','Region 6','Region 7','Region 8', 'Region 9','Region 10']
            balls = [random.choices(ball_cols) for i in range(0,100)]

            num_chosen_cols = 0
            for col in cur_cols:
                num_chosen_cols += balls.count(col)
            win = np.random.choice(np.arange(0, 2), p=[1 - num_chosen_cols / 100.0, num_chosen_cols / 100.0])
        if cur_ten not in [-1,100]:
            if cur_q >= cur_p: # use k
                win = np.random.choice(np.arange(0, 2), p=[1 - cur_q / 100.0, cur_q / 100.0])
            else:
                ball_cols = ['Yellow', 'Orange', 'Red', 'Purple', 'Pink', 'Blue', 'Green', 'Grey', 'Brown', 'Black']
                if self.session.config['trt'] == 4:
                    ball_cols = ['Region 1', 'Region 2', 'Region 3', 'Region 4', 'Region 5', 'Region 6', 'Region 7',
                                 'Region 8', 'Region 9', 'Region 10']
                balls = [random.choices(ball_cols) for i in range(0, 100)]

                num_chosen_cols = 0
                for col in cur_cols:
                    num_chosen_cols += balls.count(col)
                win = np.random.choice(np.arange(0, 2), p=[1 - num_chosen_cols / 100.0, num_chosen_cols / 100.0])

        if win == 1:
            if self.chosen_sec == 3:
                self.payoff = self.session.config['prize']
            else:
                self.payoff = 0
        else:
            if self.chosen_sec == 3:
                self.payoff = 0
            else:
                self.payoff = self.session.config['prize']






