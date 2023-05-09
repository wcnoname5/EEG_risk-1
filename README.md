# EEG_risk
This is the otree files for EEG_risk behavioral experiment.

## Discription for the experiment:
There're 3 conditions in the current experiment, representing 3 kind of forms for participants filling out to report their beliefs about some uncertain events. They're BDM, LC, QSR respectively.

There're two apps with perfix "_main_game", "_guide" for each form, thus total 6 apps in the row, constructing the main stage of the experiment.
Moreover, another two apps 'Basicinfo', and  'payment_info', writes down the data and information of the participants for payment.

## Features
At the outer folders, inside a python file `settings.py`, a variable "roundnumfixed" can used to change the trial number in the main game stage conveniently. Defalut is set to "42", an integer between "1-63" is allowed for the changing.

### RT Stuffs:

In LC, BDM, QSR pages of `main_game` apps, there're a few parameters that record the RTs.
First, `end_timestamp_for_draw` records the duration time from the 'Draw' page being loaded to the `Next` button is activated.
Secord, `start_timestamp` records the duration time from the Form page (either be `LC`, `BDM`, or `QSR` ) loaded until the last response of the Form is filled.
And the last, `start_timestamp` records the duration time from the Form page (either be `LC`, `BDM`, or `QSR` ) loaded until the `Next` button is activated.

