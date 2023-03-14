from otree.api import *
# import requests

author = 'Thorben Woelk'

doc = """
adjusted to suit otree 5 by Jay
Raven IQ Test. 10 Raven matrices to be solved by participants.
Solutions are 
5, 6, 6, 4, 5, 3, 2, 6, 8, 2.
2, 3, 7, 2, 5, 6, 4, 1, 1, 8, 5.
"""

class C(BaseConstants):

    NAME_IN_URL = 'iq_raven_copy'
    PLAYERS_PER_GROUP = None
    # NUM_ROUNDS = 1

    # # numbers = range(1, 11, 1)
    # numbers = range(1, 22, 1)
    # # numbers = [1]
    NUM_ROUNDS = 21
    # NUM_ROUNDS = 3


    SCALE = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'),
             (7, '7'), (8, '8')]
    iq_solution = [
        5, 6, 6, 4, 5, 3, 2, 6, 8, 2,
        2, 3, 7, 2, 5, 6, 4, 1, 1, 8,
        5
    ]

             
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    correct_answers = models.IntegerField(initial=0)
    feedback=models.IntegerField(
            choices=C.SCALE,
            # verbose_name='Which one is correct?',
            verbose_name='哪一個選項是正確的?',
            widget=widgets.RadioSelectHorizontal,
            required = True
        )
    start_timestamp = models.FloatField()
    end_timestamp = models.FloatField()

# PAGES

class FirstIntro(Page):
    def is_displayed(player):
        return player.round_number == 1

class IntroRaven(Page):
    def is_displayed(player):
        return player.round_number == 1
    
            

class Raven_test_page(Page):
    timeout_seconds = 60

    form_model = 'player'
    form_fields = ['feedback','start_timestamp','end_timestamp']
    @staticmethod
    def vars_for_template(player):
        return dict(
            image_path='iq_raven/Raven{}.jpg'.format(player.round_number)
        )

    def before_next_page(player: Player, timeout_happened):
        initial = 0 if (player.round_number ==1) else player.in_round(player.round_number-1).correct_answers
        if player.feedback == C.iq_solution[player.round_number-1]:
            player.correct_answers = initial +1
        else:
            player.correct_answers = initial
        

class Results(Page):
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS

    def vars_for_template(player: Player):
        if player.round_number == C.NUM_ROUNDS:
            player.payoff = 10 * player.correct_answers
            # player.set_payoff_raven()


page_sequence = [
    FirstIntro,
    IntroRaven,
    Raven_test_page,
    Results
]
