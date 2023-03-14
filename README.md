# EEG_risk
This is the otree files for EEG_risk behavioral experiment.

## Discription for the experient:
There're 3 conditions in the current experient, representing 3 kind of forms for participants filling out to report their beliefs about some uncertain events. They're BDM, LC, QSR respectively.

There're two apps with perfix '_main_game', '_guide' for each form, thus total 6 apps in the row, constructing the main stage of the experiment.
Moreover, another two apps 'Basicinfo', and  'payment_info', writes down the data and information of the participants for payment.

## Features
At the outer folders, inside a python file `settings.py`, a variable 'roundnumfixed' can used to change the trial number in the main game stage conveniently. Defalut is set to '42', an integer between '1-63' is allowed for the changing.

