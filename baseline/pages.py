from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.set_payoff()
        return{
            'payoff': self.player.payoff
        }

class colorChoose(Page):
    form_model = models.Player
    form_fields = ['colors']

    def get_form_fields(self):
        if self.session.config['trt'] != 4:
            return ['colors']
        else:
            return ['regions']

    def colors_error_message(self, value):
        print('len is ', value.count(','))
        if value.count(',') != 0 and self.round_number in [1,2]:
            return 'Please choose 1 colors.'
        if value.count(',') != 2 and self.round_number == 3:
            return 'Please choose 3 color.'
        if value.count(',') != 4 and self.round_number == 4:
            return 'Please choose 5 colors.'

    def regions_error_message(self, value):
        print('len is ', value.count(','))
        if value.count(',') != 0 and self.round_number in [1,2]:
            return 'Please choose 1 regions.'
        if value.count(',') != 2 and self.round_number == 3:
            return 'Please choose 3 region.'
        if value.count(',') != 4 and self.round_number == 4:
            return 'Please choose 5 regions.'

    def vars_for_template(self):
        col_num = 1
        if self.round_number == 3:
            col_num = 3
        if self.round_number == 4:
            col_num = 5
        return {
            'col_num': col_num,
        }

    def before_next_page(self):
        if self.round_number == 1:
            self.player.participant.vars['cols'] = []
        if self.round_number > 1:
            if self.session.config['trt'] != 4:
                self.player.participant.vars['cols'].append(self.player.colors)
            else:
                self.player.participant.vars['cols'].append(self.player.regions)


class KUchoices(Page):
    form_model = models.Player
    form_fields = ['K0', 'K1', 'K2','K3', 'K4', 'K5','K6', 'K7', 'K8', 'K9', 'K10',
                   'U0', 'U1', 'U2','U3', 'U4', 'U5','U6', 'U7', 'U8', 'U9', 'U10']

    def vars_for_template(self):
        cols = str(self.player.colors.replace('[', ' ').replace(']', ' '))
        print(cols)
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        col_reg = 'colors'
        if self.session.config['trt'] == 4:
            col_reg = 'regions'
        return {
            'trt': self.session.config['trt'],
            'cols': cols,
            'winlose': winlose,
            'pay': c(pay),
            'x': self.session.config['x'],
            'prize': c(pay),
            'lose': lose,
            'var': col_reg
        }

    def before_next_page(self):
        if self.round_number == 1:
            self.player.participant.vars['tens'] = []
        self.player.ten = self.player.p_tens()
        if self.round_number > 1:
            self.player.participant.vars['tens'].append(self.player.ten)


class KUtensChoices4(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 40

    def vars_for_template(self):
        self.player.ten = self.player.p_tens()
        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')
        return {
            'cols': cols,
            'winlose': winlose,
            'pay': pay,
            'prize': pay,
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten+1,
            'ten1_comp':99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,

        }


class KUtensChoices2(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']


    def is_displayed(self):
        return self.player.p_tens() == 20

    def vars_for_template(self):
        self.player.ten = self.player.p_tens()
        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        return {
            'cols': cols,
            'winlose': winlose,
            'pay': c(pay),
            'prize': c(pay),
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten+1,
            'ten1_comp':99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,

        }

class KUtensChoices1(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 10

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        return {
            'cols': cols,
            'winlose': winlose,
            'pay': pay,
            'prize': pay,
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten+1,
            'ten1_comp':99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,

        }


class KUtensChoices0(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 0

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        return {
            'cols': cols,
            'winlose': winlose,
            'pay': pay,
            'prize': pay,
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten+1,
            'ten1_comp':99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,

        }

class KUtensChoices3(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2', 'ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 30

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        return {
            'cols': cols,
            'winlose': winlose,
            'pay': pay,
            'prize': pay,
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten + 1,
            'ten1_comp': 99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,

        }

class KUtensChoices5(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2', 'ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 50

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        return {
            'cols': cols,
            'winlose': winlose,
            'pay': pay,
            'prize': pay,
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten + 1,
            'ten1_comp': 99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,

        }

class KUtensChoices6(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2', 'ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 60

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        return {
            'cols': cols,
            'winlose': winlose,
            'pay': pay,
            'prize': pay,
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten + 1,
            'ten1_comp': 99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,

        }

class KUtensChoices7(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2', 'ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 70

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        return {
            'cols': cols,
            'winlose': winlose,
            'pay': pay,
            'prize': pay,
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten + 1,
            'ten1_comp': 99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,

        }
class KUtensChoices8(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2', 'ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 80

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        return {
            'cols': cols,
            'winlose': winlose,
            'pay': pay,
            'prize': pay,
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten + 1,
            'ten1_comp': 99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,

        }
class KUtensChoices9(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2', 'ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 90

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.colors.replace('[', ' ').replace(']', ' ')
        cols.replace(']', ' ')
        winlose = 'lose'
        pay = Constants.lose
        lose = c(self.session.config['prize'])
        if self.round_number in [1,2]:
            winlose = 'win'
            pay = c(self.session.config['prize'])
            lose = Constants.lose
        if self.round_number == 3:
            cols.replace(',', ' ')
        if self.round_number == 4:
            pay = Constants.lose
            lose = c(self.session.config['prize'])
            cols.replace(',', ' ')

        return {
            'cols': cols,
            'winlose': winlose,
            'pay': pay,
            'prize': pay,
            'lose': lose,
            'k0': 'checked',
            'ten1': self.player.ten + 1,
            'ten1_comp': 99 - self.player.ten,
            'ten2': self.player.ten + 2,
            'ten2_comp': 98 - self.player.ten,
            'ten3': self.player.ten + 3,
            'ten3_comp': 97 - self.player.ten,
            'ten4': self.player.ten + 4,
            'ten4_comp': 96 - self.player.ten,
            'ten5': self.player.ten + 5,
            'ten5_comp': 95 - self.player.ten,
            'ten6': self.player.ten + 6,
            'ten6_comp': 94 - self.player.ten,
            'ten7': self.player.ten + 7,
            'ten7_comp': 93 - self.player.ten,
            'ten8': self.player.ten + 8,
            'ten8_comp': 92 - self.player.ten,
            'ten9': self.player.ten + 9,
            'ten9_comp': 91 - self.player.ten,
        }


class OutcomeWait(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_p()


class Intro1(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'pay': self.session.config['prize']
        }


class Intro2(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'pay': self.session.config['prize']
        }


class Intro3(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'pay': self.session.config['prize']
        }


class charity(Page):

    def is_displayed(self):
        return self.session.config['trt'] == 4 and self.round_number == 1

class realStart(Page):
    def is_displayed(self):
        return self.round_number == 2

page_sequence = [
    Intro1,
    Intro2,
    Intro3,
    realStart,
    charity,
    colorChoose,
    KUchoices,
    KUtensChoices0,
    KUtensChoices1,
    KUtensChoices2,
    KUtensChoices3,
    KUtensChoices4,
    KUtensChoices5,
    KUtensChoices6,
    KUtensChoices7,
    KUtensChoices8,
    KUtensChoices9,
    OutcomeWait,
    Results
]
