## general path: print all
* greet
  - utter_greet
* fetch_recipe
  - utter_ask_for_url
* provide_url
  - action_print_recipe
  - utter_choices
* user_choice
  - action_print_step
* user_choice
  - action_print_step
* affirm
  - action_print_step
* affirm
  - action_print_step
* affirm
  - action_print_step
* deny
  - action_reset
  - utter_choices
* user_choice
  - action_print_step
* goodbye
  - utter_goodbye
  
## general path: only recipe
* greet
  - utter_greet
* fetch_recipe
  - utter_ask_for_url
* provide_url
  - action_print_recipe
  - utter_choices
* user_choice
  - action_print_step
* affirm
  - action_print_step
* affirm
  - action_print_step
* affirm
  - action_print_step
* deny
  - action_reset
  - utter_choices
* goodbye
  - utter_goodbye
  
## general path: print recipe with queries
* greet
  - utter_greet
* fetch_recipe
  - utter_ask_for_url
* provide_url
  - action_print_recipe
  - utter_choices
* user_choice
  - action_print_step
* user_query_search
  - action_search
* affirm
  - action_print_step
* user_query_search
  - action_search
* user_query_search
  - action_search
* affirm
  - action_print_step
* user_query_search
  - action_search
* goodbye
  - utter_goodbye

## general path: end recipe midway and query anything
* greet
  - utter_greet
* fetch_recipe
  - utter_ask_for_url
* provide_url
  - action_print_recipe
  - utter_choices
* user_choice
  - action_print_step
* user_query_search
  - action_search
* user_choice
  - action_print_step
* goodbye
  - utter_goodbye



