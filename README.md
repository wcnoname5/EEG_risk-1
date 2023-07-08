# EEG_risk
This is the otree files for EEG_risk behavioral experiment.

## Discription of The Experiment:
There're 3 conditions in the current experiment, which is `BDM`, `LC`, `QSR` respectively. They representing 3 kinds of forms for participants filling out to report their beliefs about some uncertain events.

There're two apps with perfix `_main_game`, `_guide` for each form, thus total 6 apps in the row, constructing the main stage of the experiment.

Moreover, another two apps `Basicinfo`, and  `payment_info` for the whole experiment, which write down the data and information of the participants for payment.

## Features
### Trial numbers
At the outer folders, inside `settings.py`, a variable `roundnumfixed` can used to change the trial number in the main game stage conveniently. Defalut is set to "42", integers between "1-63" are allowed to change.

### RT recordings:

In LC, BDM, QSR pages of `main_game` apps, there're a few parameters that record a few time durations that resemble to RT.

First, `end_timestamp_for_draw` records the duration time from the `Draw` page being loaded until the `Next` button is activated.

Secord, `start_timestamp` records the duration time from the Form page (either be `LC`, `BDM`, or `QSR` ) loaded until the "first" response of the Form is filled. That's why it called "start_timestamp".

At last, `end_timestamp` records the duration time from the Form page (either be `LC`, `BDM`, or `QSR` ) loaded until the `Next` button is activated.

