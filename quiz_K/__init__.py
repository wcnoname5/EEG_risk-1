from otree.api import *
from random import choice
import random

# 題目模板
class C(BaseConstants):
    NAME_IN_URL = 'quiz_K'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    #定義：輪、階段數
    num_subsession = 1
    num_cycle = 2
    num_game_round = 15

    #定義乘數
    MULTIPLIER1 = 1.2
    MULTIPLIER2 = 0.9
    MULTIPLIER3 = 0.2


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Q1 = models.IntegerField(
        label="1. 假設當您本回合看到的報酬表如下圖左，且您於本回合選擇 α ，而最終結果是如下圖右，請問您於本回合可以拿多少法幣 ？",
        choices=[
            [0, '0'], [1, '2'], [2, '9'], [3, '12'], ],
        widget=widgets.RadioSelect, )

    Q2 = models.IntegerField(
        label="2. 假設當您本回合看到的報酬表如下圖左，且您於本回合選擇 α ，而最終結果是如下圖右，請問您於本回合可以拿多少法幣 ？",
        choices=[
            [0, '0'], [1, '2'], [2, '9'], [3, '12'], ],
        widget=widgets.RadioSelect, )

    Q3 = models.IntegerField(
        label="3. 假設當您本回合看到的報酬表如下圖左，且您於本回合選擇 γ ，而最終結果是如下圖右，請問您於本回合可以拿多少法幣 ？",
        choices=[
            [0, '0'], [1, '2'], [2, '9'], [3, '12'], ],
        widget=widgets.RadioSelect, )

    Q4 = models.IntegerField(
        label="4. 假設當您本回合看到的報酬表如下圖左，且您於本回合選擇 γ ，而最終結果是如下圖右，因為三種選項選的人一樣多，電腦會隨機決定一個選項，視為最多人選，請問下列敘述何者錯誤 ？",
        choices=[
            [0, '若電腦本回合隨機選中 β 為最多人選，則您得 0 法幣'], [1, '若電腦本回合隨機選中 β 為最多人選，則您得 2 法幣'], [2, '若電腦本回合隨機選中 α 為最多人選，則您得 12 法幣'], [3, '若電腦本回合隨機選中 γ 為最多人選，則您得 9 法幣'], ],
        widget=widgets.RadioSelect, )

    Q5 = models.IntegerField(
        label="5. 假設您在某回合看到的報酬表如下圖左，而其他 11 人的選擇結果如下圖右，請問下列敘述何者正確 ？",
        choices=[
            [0, '您選擇 α，可得 2 法幣'], [1, '您選擇 β，可得 9 法幣'], [2, '您選擇 γ，有 1/2 機會得 2 法幣，有 1/2 機會得 9 法幣'], [3, '以上敘述皆正確'], ],
        widget=widgets.RadioSelect, )

    Q6 = models.IntegerField(
        label="6. 假設您在某回合的第一階段是一開始被選中先做選擇的 4 人，請問下列哪個選項的敘述正確 ？",
        choices=[
            [0, '你們 4 人的選擇不會計入最終的人數統計，只有後面 8 人的會計入'], [1, '你們 4 人的選擇不會計入最終的人數統計，後面 8 人的也不會計入。'], [2, '你們 4 人的選擇會計入最終的人數統計，後面 8 人的也會計入。'], [3, '你們 4 人的選擇會計入最終的人數統計，後面 8 人的不會計入。'], [4, '以上皆非'] ],
        widget=widgets.RadioSelect, )

    Q7 = models.IntegerField(
        label="7. 關於本場實驗開始前受試者獲得的資訊，請問下列哪個選項的敘述正確 ？",
        choices=[
            [0, '分到 5 人一組的受試者會知道自己組有 5 人。'], [1, '分到 4 人一組的受試者會知道自己組有 4 人。'], [2, '分到 3 人一組的受試者會知道自己組有 3 人。'], [3, '所有人都不知道自己在的組的人數。'], ],
        widget=widgets.RadioSelect, )

    Q1_wrong = models.IntegerField(initial=0)
    Q2_wrong = models.IntegerField(initial=0)
    Q3_wrong = models.IntegerField(initial=0)
    Q4_wrong = models.IntegerField(initial=0)
    Q5_wrong = models.IntegerField(initial=0)
    Q6_wrong = models.IntegerField(initial=0)
    Q7_wrong = models.IntegerField(initial=0)

# PAGES

class Introduction(Page):
    pass

class Ready(Page):
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

class Page4(Page):
    form_model = 'player'
    form_fields = ['Q4']

class Page5(Page):
    form_model = 'player'
    form_fields = ['Q5']

class Page6(Page):
    form_model = 'player'
    form_fields = ['Q6']

class Page7(Page):
    form_model = 'player'
    form_fields = ['Q7']


class Result1(Page):
    form_model = 'player'
    form_fields = ['Q1']

    @staticmethod
    def vars_for_template(player: Player):
        if player.Q1 == 3:
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
        if player.Q2 == 1:
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

class Result4(Page):
    form_model = 'player'
    form_fields = ['Q4']

    @staticmethod
    def vars_for_template(player: Player):
        if player.Q4 == 0:
            is_Q4_correct= True
        else:
            is_Q4_correct= False
            player.Q4_wrong = 1
        return dict(is_Q4_correct=is_Q4_correct)

class Result5(Page):
    form_model = 'player'
    form_fields = ['Q5']

    @staticmethod
    def vars_for_template(player: Player):
        if player.Q5 == 3:
            is_Q5_correct= True
        else:
            is_Q5_correct= False
            player.Q5_wrong = 1
        return dict(is_Q5_correct=is_Q5_correct)

class Result6(Page):
    form_model = 'player'
    form_fields = ['Q6']

    @staticmethod
    def vars_for_template(player: Player):
        if player.Q6 == 2:
            is_Q6_correct= True
        else:
            is_Q6_correct= False
            player.Q6_wrong = 1
        return dict(is_Q6_correct=is_Q6_correct)

class Result7(Page):
    form_model = 'player'
    form_fields = ['Q7']

    @staticmethod
    def vars_for_template(player: Player):
        if player.Q7 == 2:
            is_Q7_correct= True
        else:
            is_Q7_correct= False
            player.Q6_wrong = 1
        return dict(is_Q7_correct=is_Q7_correct)

class Ans(Page):
    pass


class bye(Page):
    pass



page_sequence = [
    Ready,
    Page1,Result1,
    Page2,Result2,
    Page3,Result3,
    Page4,Result4,
    Page5,Result5,
    Page6,Result6,
    Page7,Result7,
    Ans,
    bye]

