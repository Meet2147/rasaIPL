## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
* ipl
  - utter_ask_date
* ipl
  - action_ipl_schedule
* thanks
  - utter_thanks

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* ipl
  - utter_ask_date
* ipl
  - action_ipl_schedule
* thanks
  - utter_thanks

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* ipl
  - utter_ask_date
* ipl
  - action_ipl_schedule
* thanks
  - utter_thanks


## ipl schedule path
* greet
  - utter_greet
* ipl
  - utter_ask_date
* ipl
  - action_ipl_schedule
* thanks
  - utter_thanks


## say goodbye
* goodbye
  - utter_goodbye


## bot challenge
* bot_challenge
  - utter_iamabot
