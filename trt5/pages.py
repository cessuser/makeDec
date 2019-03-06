from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class Intro(Page):
    pass


class MyPage(Page):
    pass


class KUchoices(Page):
    form_model = models.Player
    form_fields = ['K0', 'K1', 'K2','K3', 'K4', 'K5','K6', 'K7', 'K8', 'K9', 'K10',
                   'U0', 'U1', 'U2','U3', 'U4', 'U5','U6', 'U7', 'U8', 'U9', 'U10']

    def vars_for_template(self):
        cols = Constants.supplements[self.round_number-1]
        col_reg = 'colors'
        # if self.session.config['trt'] == 4:
        #     col_reg = 'regions'
        return {
            'cols': cols,
            'var': col_reg
        }
    def before_next_page(self):
        if self.round_number == 1:
            self.player.participant.vars['tens'] = []
        self.player.ten = self.player.p_tens()
        self.player.participant.vars['tens'].append(self.player.ten)


class KUtensChoices0(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 0

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = Constants.supplements[self.round_number-1]

        return {
            'cols': cols,
            'k0': 'checked',
            'ten1': self.player.ten+1,
            'ten2': self.player.ten + 2,
            'ten3': self.player.ten + 3,
            'ten4': self.player.ten + 4,
            'ten5': self.player.ten + 5,
            'ten6': self.player.ten + 6,
            'ten7': self.player.ten + 7,
            'ten8': self.player.ten + 8,
            'ten9': self.player.ten + 9,

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

        cols = Constants.supplements[self.round_number-1]

        return {
            'cols': cols,
            'k0': 'checked',
            'ten1': self.player.ten+1,
            'ten2': self.player.ten + 2,
            'ten3': self.player.ten + 3,
            'ten4': self.player.ten + 4,
            'ten5': self.player.ten + 5,
            'ten6': self.player.ten + 6,
            'ten7': self.player.ten + 7,
            'ten8': self.player.ten + 8,
            'ten9': self.player.ten + 9,

        }



class OutcomeWait(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_p()


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.set_payoff()
        if self.player.cured:
            msg = 'You are cured and can live 30 years longer from now on in good health'
        else:
            msg = 'You are not cured, can live only 1 year longer from now on in good health.'
        return{
            'payoff': self.player.payoff,
            'msg': msg
        }




page_sequence = [
    Intro,
    KUchoices,
    KUtensChoices0,
    OutcomeWait,
    Results
]
