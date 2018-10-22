## Welcome
* WELCOME
- utter_welcome
- utter_display_menu

## Welcome
* WELCOME
- utter_welcome
- utter_display_menu
* hello
- utter_greet

## Order process
* order_item{"item":"Coffee"}
- check_order_available
- slot{"available": "available"}
- utter_ask_how_many
* inform{"number":3}
- add_order
- utter_anything_else
* affirm
- utter_display_menu
* order_item{"item":"Cake"}
- check_order_available
- slot{"available":"not_available"}
- utter_suggest_alternative
* order_item{"item":"Muffins"}
- check_order_available
- slot{"available":"available"}
- utter_ask_how_many
* inform{"number":3}
- add_order
- utter_anything_else
* deny
- order_summary
- utter_order_confirmation
* affirm
- process_order

##Bye
* bye
- utter_goodbye

## story
* order_item{"item":"Cake"}
- check_order_available
- slot{"available":"not_available"}
- utter_suggest_alternative

##
## Order process
* order_item{"item":"Coffee", "number":3}
- check_order_available
- slot{"available": "available"}
- utter_ask_how_many
- add_order
- utter_anything_else