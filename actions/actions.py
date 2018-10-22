from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionCheckOrder(Action):
   def name(self):
      # type: () -> Text
      return "check_order_available"

   def run(self, dispatcher, tracker, domain):
     # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
    if(tracker.get_slot("item")):
      if(tracker.get_slot("item")== "Coffee"):
        result = SlotSet("available",True)
      elif(tracker.get_slot("item")=="Cake"):
        result = SlotSet("available",True)
    else:
      dispatcher.utter_template("utter_suggest_alternatives", tracker)
    return result

class ActionAddOrder(Action):
   def name(self):
      # type: () -> Text
      return "add_order"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        
        dispatcher.utter_message("Awesome!We have noted your order")

class ActionSetOrderNumber(Action):
   def name(self):
      # type: () -> Text
      return "set_order_number"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        number = tracker.get_slot("number")
        return SlotSet("order_number",number)

class ActionRemoveOrder(Action):
   def name(self):
      # type: () -> Text
      return "remove_order"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_message("Ok. We have removed your order. :(")

class ActionOrderSummary(Action):
   def name(self):
      # type: () -> Text
      return "order_summary"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_message("Here is the summary for your order")    

class ActionProcessOrder(Action):
   def name(self):
      # type: () -> Text
      return "process_order"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_card_retrieval_confirmed", tracker)      