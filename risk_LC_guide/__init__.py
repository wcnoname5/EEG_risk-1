import random
from otree.api import *
from random import choice

doc = """
Table where each row has a left/right choice,
like the strategy method.
This app enforces a single switching point
"""


class C(BaseConstants):
    NAME_IN_URL = 'risk_LC_guide'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    win_payoff = cu(10)


    # import drawing dataset
    import csv
    with open('outcome.csv', 'r') as draw:
        draw = list(csv.DictReader(draw))
        total = len(draw)  # number of row


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
    left_side_amount = models.IntegerField(initial=100)
    switching_point = models.IntegerField()
    num_draw = models.IntegerField(initial=3)
    trial_draw = models.IntegerField(initial=1)
    outcome1 = models.IntegerField(initial=1)
    outcome2 = models.IntegerField(initial=1)
    outcome3 = models.IntegerField(initial=1)
    is_red = models.IntegerField(initial=1)
    is_red_str = models.StringField()
    row = models.IntegerField(initial=1)
    row_lottery = models.IntegerField(initial=1)
    lottery = models.IntegerField(initial=1)

    # quiz answer
    Q1 = models.IntegerField(
        # label="1. 下圖是「資料庫」中某次抽球的過程，目前已經從藍罐抽出兩顆藍球，假設此次總共要抽三顆球，請問下次抽出紅球的機率是多少？",
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
        label="3. 如果您認為本回合「答案罐」是紅罐的可能性為 70/100，並且填答如下圖。請問以下敘述何者「錯誤」？ ",
        #label="",
        choices=[
            [0, 'A. 如果電腦隨機抽到第 6 行（紅框處）作為決定報酬的依據，本回合會採用紅罐抽獎。則根據題幹中您認為的情況，得到 200 法幣的可能性為 70/100 。'], 
            [1, 'B. 如果電腦隨機抽到第 7 行（黃框處）作為決定報酬的依據，本回合會採用隨機抽獎，您得到 200 法幣的可能性為 65/100 。'], 
            [2, 'C. 如果將第 7 行（黃框處）的填答改成「採用紅罐抽獎」，根據題幹中您認為的情況，若電腦隨機抽中該行作為決定報酬的依據，您得到 200 法幣的可能性為 70/100 。'], 
            [3, 'D. 根據題幹中您認為的情況，下圖的填答方式能夠最大化在每一行得到 200 法幣的機率。'], 
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
        # draw the trial of dataset used in this round
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
        # output ball image by result above
        b = [player.outcome1,player.outcome2,player.outcome3]

        img_paths = ['risk/{}.png'.format(i) for i in b]
        return dict(img_paths=img_paths)


class Instruction_LC(Page):
    pass
class Instruction_LC2(Page):
    pass
class Instruction_LC3(Page):
    pass
class Instruction_LC4(Page):
    pass
class Instruction_LC5(Page):
    pass
class Instruction_LC6(Page):
    pass
class beforequiz(Page):
    pass

class LC(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    @staticmethod
    def vars_for_template(player):
        return dict(right_side_amounts=range(1, 9, 1))

    @staticmethod
    def before_next_page(player, timeout_happened):
        import random
        # draw the row used for determination
        player.row = random.randint(1, 10)
        player.row_lottery = (player.row)*10-5
        # draw random lottery number
        player.lottery = random.randint(1, 100)
        # payoff calculation
        if player.is_red == 0:
            player.is_red_str = "紅罐"
        else:
            player.is_red_str = "藍罐"

        if player.row >= player.switching_point:
            player.is_random = True
            if player.lottery >= player.row_lottery:
                player.temp_payoff = 0
            else:
                player.temp_payoff = 200
        else:
            player.is_random = False
            if player.is_red == 0:
                player.temp_payoff = 200
            else:
                player.temp_payoff = 0


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


page_sequence = [
    Intro, 
    Instruction, 
    Instruction2, 
    Instruction3,
    Instruction4,
    Instruction5, 
    Instruction_LC, 
    Instruction_LC2, 
    Instruction_LC3, 
    #Instruction_LC4,
    Instruction_LC5, 
    Instruction_LC6, 

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
    LC , 
    Results
    ]



# class Quiz(Page):
#     form_model = 'player'
#     form_fields = ['quiz_1', 'quiz_2', 'quiz_3', 'quiz_4', 'quiz_5']

#     @staticmethod
#     def error_message(player, values):
#         for q in ['quiz_1', 'quiz_2', 'quiz_3', 'quiz_4', 'quiz_5']:
#             if values[q] == None:
#                 return 'Please answer all the questions'
#     def before_next_page(player, timeout_happened):
#         if player.quiz_1 == 3 and player.quiz_2 == 3 and player.quiz_3 == 3 and player.quiz_4 == 3 and player.quiz_5 == 3:
#             player.Pass = True
#     # 這裡寫答案！！！！！

# class Quiz(Page):
######################## 測試用##########################
#     form_model = 'player'
#     form_fields = ['quiz_1', 'quiz_2', 'quiz_3', 'quiz_4', 'quiz_5']

#     @staticmethod
#     # def error_message(player, values):
#     #     for q in ['quiz_1', 'quiz_2', 'quiz_3', 'quiz_4', 'quiz_5']:
#     #         if values[q] == None:
#     #             return 'Please answer all the questions'
#     def before_next_page(player, timeout_happened):
#         if player.quiz_1 == 3:
#             player.Pass = True
#     # 這裡寫答案！！！！！

# class Quiz_result(Page):
#     @staticmethod
#     def app_after_this_page(player, upcoming_apps):
#         print(player.session.config["app_sequence"][1])
#         print(player.session.config["num_of_round"])
#         if player.session.config['name'] == "risk_LC_whole_game":
#             if player.Pass == False:
#                 participant= player.participant
#                 participant.final_payoff = -1                
#                 return upcoming_apps[1]
#     pass