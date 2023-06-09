import random

from otree.api import *
from random import choice

doc = """
Table where each row has a left/right choice,
like the strategy method.
This app enforces a single switching point
"""


class C(BaseConstants):
    NAME_IN_URL = 'risk_BDM_guide'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    win_payoff = cu(10)
    import csv
    with open('outcome.csv', 'r') as draw:
        draw = list(csv.DictReader(draw))
        total = len(draw)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def make_field():
    return models.IntegerField(
        blank=True,
        choices=[1,2,3,4],
        widget=widgets.RadioSelect,
    )

class Player(BasePlayer):
    is_random = models.BooleanField(initial=False)
    temp_payoff = models.CurrencyField(initial=cu(0))
    switching_point = models.IntegerField()
    num_draw = models.IntegerField(initial=3)
    trial_draw = models.IntegerField(initial=1)
    outcome1 = models.IntegerField(initial=1)
    outcome2 = models.IntegerField(initial=1)
    outcome3 = models.IntegerField(initial=1)
    is_red = models.IntegerField(initial=1)
    is_red_str = models.StringField()
    number = models.IntegerField(initial=1)
    lottery = models.IntegerField(initial=1)
    # quiz answer
 # quiz answer
    Q1 = models.IntegerField(
        # label="1. 下圖是「資料庫」中某次抽球的過程，目前已經從藍罐抽出兩顆藍球，假設此次總共要抽三顆球，請問下次抽出紅球的可能性是多少？",
        label="",
        choices=[
            [0, 'A. 1/3'], [1, 'B. 1'], [2, 'C. 2/3'], [3, 'D. 0'], ],
        widget=widgets.RadioSelect, )

    Q2 = models.IntegerField(
        #label="2. 如果本回合呈現的抽球結果如下圖，若本回合以「紅罐抽獎」作為酬賞決定方式，請問下列何者敘述正確？",
        label="",
        choices=[
            [0, 'A. 電腦從藍罐和紅罐隨機挑一個，如果挑到紅罐，本回合報酬為 200 法幣。'],
            [1, 'B. 電腦從所有抽球結果為 2 藍 1 紅的資料中，隨機挑出 100 筆。如果這 100 筆資料中答案罐是紅罐的比較多，本回合報酬為 200 法幣。'], 
            [2, 'C. 電腦從所有抽球結果為 2 藍 1 紅的資料中，隨機挑出 1 筆，若該筆資料答案罐是紅罐，本回合報酬為 200 法幣。'], 
            [3, 'D. 電腦從所有抽球結果為 2 藍 1 紅的資料中，隨機挑出 100 筆。再從這 100 筆資料中再隨機選 1 筆，若該筆資料答案罐是紅罐，本回合報酬為 200 法幣。'], 
            ],
        widget=widgets.RadioSelect, )

    Q3 = models.IntegerField(
        label="3. 如果本回合您認為答案罐是紅罐的可能性是 70/100 ，卻在表中填答 60/100 ，如下圖。請問下列何者敘述「錯誤」？",
        choices=[
            [0, 'A. 如果「隨機中獎可能性」為 33/100，本回合採用紅罐抽獎。根據題幹中您認為的情況，您得到 200 法幣的可能性為 70/100。'], 
            [1, 'B. 如果「隨機中獎可能性」為 66/100，本回合採用隨機抽獎，您得到 200 法幣的可能性為 66/100。'], 
            [2, 'C. 如果您在表中改選填「 70/100」，且「隨機中獎可能性」為 66/100，本回合採用紅罐抽獎。根據題幹中您認為的情況，您得到 200 法幣的可能性為 70/100。'], 
            [3, 'D. 跟據題幹中您認為的情況，無論「隨機中獎可能性」為何，下圖的填答能夠最大化獲得 200 法幣的可能性。'], 
            ],
        widget=widgets.RadioSelect, )

    Q1_wrong = models.IntegerField(initial=0)
    Q2_wrong = models.IntegerField(initial=0)
    Q3_wrong = models.IntegerField(initial=0)

    end_timestamp = models.FloatField()


# PAGES
class Intro(Page):
    pass

class Instruction(Page):
    pass

class Instruction2(Page):
    pass

class Instruction3(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        import random
        player.trial_draw = random.randint(1,100000)
        trial_draw = player.trial_draw
        round_row_draw = C.draw[trial_draw]
        print(round_row_draw)
        player.outcome1 = int(round_row_draw['outcome1'])
        player.outcome2 = int(round_row_draw['outcome2'])
        player.outcome3 = int(round_row_draw['outcome3'])
        player.num_draw = int(round_row_draw['numofdraw'])
        player.is_red = int(round_row_draw['jar'])

class Instruction4(Page):
    pass

class Instruction5(Page):
    pass

class PracticeStart(Page):
    pass
class Draw(Page):
    form_model = 'player'
    form_fields = ['end_timestamp']

    @staticmethod
    def vars_for_template(player: Player):
        b = [player.outcome1, player.outcome2, player.outcome3]

        img_paths = ['risk/{}.png'.format(i) for i in b]
        return dict(img_paths=img_paths)

class Instruction_BDM(Page):
    pass
class Instruction_BDM2(Page):
    pass
class Instruction_BDM3(Page):
    pass
#class Instruction_BDM4(Page):
#    pass
class Instruction_BDM5(Page):
    pass
class beforequiz(Page):
    pass

class BDM(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    @staticmethod
    def vars_for_template(player):
        return dict(right_side_amounts=range(1, 9, 1))

    @staticmethod
    def before_next_page(player, timeout_happened):
        import random
        # draw N
        player.number = random.randint(0, 100)
        # draw B
        player.lottery = random.randint(0, 99)
        # payoff calculation
        if player.is_red == 0:
            player.is_red_str = "紅罐"
        else:
            player.is_red_str = "藍罐"

        if player.number >= player.switching_point:
            player.is_random = True
            if player.lottery >= player.number:
                player.temp_payoff = 0
            else:
                player.temp_payoff = 200
        else:
            player.is_random = False
            if player.is_red == 0:
                player.temp_payoff = 200
            else:
                player.temp_payoff = 0


class Quiz(Page):
    form_model = 'player'
    form_fields = ['quiz_1', 'quiz_2', 'quiz_3', 'quiz_4', 'quiz_5']

    @staticmethod
    def error_message(player, values):
        for q in ['quiz_1', 'quiz_2', 'quiz_3', 'quiz_4', 'quiz_5']:
            if values[q] == None:
                return 'Please answer all the questions'
    def before_next_page(player, timeout_happened):
        if player.quiz_1 == 3 and player.quiz_2 == 3 and player.quiz_3 == 3 and player.quiz_4 == 3 and player.quiz_5 == 3:
            player.Pass = True
    # 這裡寫答案！！！！！

class Quiz_result(Page):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        # print(player.session.config['name'])
        if player.session.config['name'] == "risk_BDM_whole_game":
            if player.Pass == False:
                participant= player.participant
                participant.final_payoff = -1
                return upcoming_apps[1]
    pass

class Page1(Page):
    form_model = 'player'
    form_fields = ['Q1']

class Page2(Page):
    form_model = 'player'
    form_fields = ['Q2']

class Page3(Page):
    form_model = 'player'
    form_fields = ['Q3']


class Result1(Page):
    form_model = 'player'
    form_fields = ['Q1']

    @staticmethod
    def vars_for_template(player: Player):
        if player.Q1 == 0:
            is_Q1_correct = True
        else:
            is_Q1_correct = False
            player.Q1_wrong = 1
        return dict(is_Q1_correct=is_Q1_correct)

class Result2(Page):
    form_model = 'player'
    form_fields = ['Q2']

    @staticmethod
    def vars_for_template(player: Player):
        if player.Q2 == 2:
            is_Q2_correct= True
        else:
            is_Q2_correct= False
            player.Q2_wrong = 1
        return dict(is_Q2_correct=is_Q2_correct)

class Result3(Page):
    form_model = 'player'
    form_fields = ['Q3']

    @staticmethod
    def vars_for_template(player: Player):
        if player.Q3 == 3:
            is_Q3_correct= True
        else:
            is_Q3_correct= False
            player.Q3_wrong = 1
        return dict(is_Q3_correct=is_Q3_correct)

class Ans(Page):
    pass


class Results(Page):
    pass

# page_sequence = [Intro, Instruction, Instruction2, Instruction3, Instruction_BDM, Instruction_BDM2,Instruction_BDM3, Instruction_BDM5, PracticeStart, Draw, BDM, Results]
# page_sequence = [Quiz, Quiz_result, Intro, Instruction, Instruction2, Instruction3, Instruction_BDM, Instruction_BDM2,Instruction_BDM3, Instruction_BDM5, PracticeStart, Draw, BDM, Results]
page_sequence = [
    Intro,
    Instruction, 
    Instruction2, 
    Instruction3,
    Instruction4,
    Instruction5, 
    Instruction_BDM, 
    Instruction_BDM2,
    Instruction_BDM3,
    Instruction_BDM5,
    beforequiz,
    # Quiz, 
    # Quiz_result, 
    Page1,
    Result1,
    Page2,
    Result2,
    Page3,
    Result3,
    Ans,
    PracticeStart, 
    Draw, 
    BDM, 
    Results]
