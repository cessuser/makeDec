from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import numpy as np
from django import forms

author = 'Danlin chen'

doc = """
Your app description
"""

SUPPLEMENTS =[
    ('S1', 'S1'),
    ('S2', 'S2'),
    ('S3', 'S3'),
    ('S4', 'S4'),
    ('S5', 'S5'),
    ('S6', 'S6'),
    ('S7', 'S7'),
    ('S8', 'S8'),
    ('S9', 'S9'),
    ('S10', 'S10')
]
class Constants(BaseConstants):
    name_in_url = 'trt5'
    players_per_group = None
    num_rounds = 7

    supplements = [' S1 ', ' S1, S3, S5 ', ' S1, S3, S5, S7, S9 ', ' S2,S4,S6,S8,S10 ', 'S2, S4, S6, S7, S8, S9, S10 ', ' S2, S3, S4, S5, S6, S7, S8, S9, S10 ']
    all_supp = ['S1' 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10']

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_p(self):
        for p in self.get_players():
            p.store_p()


class Player(BasePlayer):
    supplements = models.StringField(widget=forms.CheckboxSelectMultiple(choices=SUPPLEMENTS), label=' ')
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

    chosen_supplements = models.StringField()
    chosen_sec_p = models.IntegerField()
    chosen_p = models.IntegerField()
    chosen_row = models.IntegerField()
    cured = models.BooleanField()

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
            if self.ten not in [-1,100]:
                p = p + 9
        self.p = p

        if self.round_number == 1:
            self.participant.vars['p'] = []
        else:
            self.participant.vars['p'].append(self.p)

    def set_payoff(self):
        cur_round = random.randint(0, Constants.num_rounds - 1) + 1
        cur_supplements = self.participant.vars['supplements'][cur_round-1]
        cur_ten = self.participant.vars['tens'][cur_round-1]
        cur_p = self.participant.vars['p'][cur_round-1]
        cur_q = 0

        self.chosen_supplements = cur_supplements
        self.chosen_sec_p = cur_ten
        self.chosen_p = cur_p

        print('cur_round ', cur_round, 'cur_supp ', cur_supplements, ' cur_ten ', self.participant.vars['tens'], ' ps ', self.participant.vars['p'])
        win = 0
        if cur_ten == -1: # all k
            ten_lst = [i*10 for i in range(0,11)]
            cur_q = random.choice(ten_lst)
            win = np.random.choice(np.arange(0, 2), p=[1 - cur_q / 100.0, cur_q / 100.0]) # 0 is not cured

        if cur_ten == 100: # all u
            print('all U')
            diseases = [random.choice(Constants.all_supp) for i in range(0,100)]
            cur_disease = random.choice(diseases)
            if cur_disease in cur_supplements:
                win = 1

        if cur_ten not in [-1,100]: # not all u or k
            cur_q = random.randint(0,100)
            if cur_q > cur_p: # use k
                win = np.random.choice(np.arange(0, 2), p=[1 - cur_q / 100.0, cur_q / 100.0])
            else:
                diseases = [random.choice(Constants.all_supp) for i in range(0, 100)]
                cur_disease = random.choice(diseases)

                if cur_disease in cur_supplements:
                    win = 1

        self.chosen_row = cur_q

        if win == 1:
            self.cured = True
        else:
            self.cured = False
