import random

from otree.api import *
from random import choice

doc = """
Table where each row has a left/right choice,
like the strategy method.
This app enforces a single switching point
"""


class C(BaseConstants):
    NAME_IN_URL = 'risk_QSR_main_game'
    PLAYERS_PER_GROUP = None
    # NUM_ROUNDS = 5
    NUM_ROUNDS = 63
    win_payoff = cu(10)
    import csv
    with open('table.csv', 'r') as para:
        para = list(csv.DictReader(para))
        row = len(para)  # number of row

    with open('outcome.csv', 'r') as draw:
        draw = list(csv.DictReader(draw))
        total = len(draw)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_random = models.BooleanField(initial=False)
    temp_payoff = models.CurrencyField(initial=cu(0))
    switching_point = models.IntegerField()
    red_payoff = models.CurrencyField(initial=cu(0))
    blue_payoff = models.CurrencyField(initial=cu(0))
    num_draw = models.IntegerField(initial=3)
    trial_draw = models.IntegerField(initial=1)
    outcome1 = models.IntegerField(initial=1)
    outcome2 = models.IntegerField(initial=1)
    outcome3 = models.IntegerField(initial=1)
    is_red = models.IntegerField(initial=1)
    is_red_str = models.StringField()

    start_timestamp = models.FloatField()
    end_timestamp = models.FloatField()

    end_timestamp_for_draw = models.FloatField()


# PAGES
class Instruction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Draw(Page):
    form_model = 'player'
    form_fields = ['end_timestamp_for_draw']


    @staticmethod
    def vars_for_template(player: Player):
        import random
        player.trial_draw = random.randint(1,C.total)
        trial_draw = player.trial_draw
        round_row_draw = C.draw[trial_draw]
        print(round_row_draw)
        player.outcome1 = int(round_row_draw['outcome1'])
        player.outcome2 = int(round_row_draw['outcome2'])
        player.outcome3 = int(round_row_draw['outcome3'])
        player.num_draw = int(round_row_draw['numofdraw'])
        player.is_red = int(round_row_draw['jar'])

        b = [player.outcome1,player.outcome2,player.outcome3]

        img_paths = ['risk/{}.png'.format(i) for i in b]
        return dict(img_paths=img_paths)


class QSR(Page):
    form_model = 'player'
    form_fields = ['switching_point','start_timestamp','end_timestamp']

    @staticmethod
    def vars_for_template(player):
        return dict(right_side_amounts=range(1, 9, 1))

    @staticmethod
    def before_next_page(player, timeout_happened):
        # payoff calculation
        a = int(player.switching_point/10)
        round_row = C.para[a]
        print(round_row)
        player.red_payoff = int(round_row['red'])
        player.blue_payoff = int(round_row['blue'])

        if player.is_red == 0:
            player.is_red_str = "紅罐"
            player.temp_payoff = player.red_payoff
        else:
            player.is_red_str = "藍罐"
            player.temp_payoff = player.blue_payoff

class Results(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # draw one round as final payoff
        import random
        participant = player.participant

        # if it's the last round
        # if player.round_number == C.NUM_ROUNDS:
        #     random_round = random.randint(1, C.NUM_ROUNDS)
        if player.round_number == player.session.config["num_of_round"]:
            random_round = random.randint(1, player.session.config["num_of_round"])
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            participant.final_payoff  = int(player_in_selected_round.temp_payoff)
            participant.total_payoff = int(100 + player_in_selected_round.temp_payoff)
            
    def app_after_this_page(player, upcoming_apps):
        # print(player.session.config["app_sequence"][2])
        # print(player.session.config["num_of_round"])
        if player.round_number == player.session.config["num_of_round"]:             
            # 假如回合數已經到達變跳到最後一頁
            return upcoming_apps[0]


page_sequence = [Instruction, Draw, QSR, Results]
