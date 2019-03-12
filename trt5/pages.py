from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class Intro(Page):
    pass


class MyPage(Page):
    pass

class realStart(Page):
    def is_displayed(self):
        return self.round_number == 2

class KUchoices(Page):
    form_model = models.Player
    form_fields = ['K0', 'K1', 'K2','K3', 'K4', 'K5','K6', 'K7', 'K8', 'K9', 'K10',
                   'U0', 'U1', 'U2','U3', 'U4', 'U5','U6', 'U7', 'U8', 'U9', 'U10']

    def vars_for_template(self):
        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')
        return {
            'cols': cols,
        }
    def before_next_page(self):
        self.player.ten = self.player.p_tens()
        if self.round_number == 1:
            self.player.participant.vars['tens'] = []
        else:

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

        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')

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


class KUtensChoices1(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 10

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')

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

class KUtensChoices2(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 20

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')

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

class KUtensChoices3(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 30

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')

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

class KUtensChoices4(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 40

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.supplements

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

class KUtensChoices5(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 50

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')

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


class KUtensChoices6(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 60

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')

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

class KUtensChoices7(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 70

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')

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

class KUtensChoices8(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 80

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')

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


class KUtensChoices9(Page):
    form_model = models.Player
    form_fields = ['ten1', 'ten2','ten3', 'ten4', 'ten5', 'ten6', 'ten7', 'ten8', 'ten9',
                   'ten1U', 'ten2U', 'ten3U', 'ten4U', 'ten5U', 'ten6U', 'ten7U', 'ten8U', 'ten9U']

    def is_displayed(self):
        return self.player.p_tens() == 90

    def vars_for_template(self):
        print("p_tens", self.player.p_tens())
        self.player.ten = self.player.p_tens()

        cols = self.player.supplements.replace('[', ' ').replace(']', ' ')

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

class supplementsChoose(Page):
    form_model = models.Player
    form_fields =  ['supplements']

    def vars_for_template(self):
        return {
            'col_num': [1,1,3,5,5,7,9][self.round_number-1]
        }

    def before_next_page(self):
        self.player.supplements.replace('[', ' ').replace(']', ' ')
        if self.round_number == 1:
            self.player.participant.vars['supplements'] = []
        else:
            self.player.participant.vars['supplements'].append(self.player.supplements)

    def supplements_error_message(self, value):
        if value.count(',') != 0 and self.round_number in [1,2]:
            return 'Please choose 1 colors.'
        if value.count(',') != 2 and self.round_number == 3:
            return 'Please choose 3 color.'
        if value.count(',') != 4 and self.round_number in [4,5]:
            return 'Please choose 5 colors.'
        if value.count(',') != 6 and self.round_number == 6:
            return 'Please choose 7 colors.'
        if value.count(',') != 8 and self.round_number == 7:
            return 'Please choose 9 colors.'


page_sequence = [
    Intro,
    realStart,
    supplementsChoose,
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
