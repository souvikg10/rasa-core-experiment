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
        return [SlotSet("available","available")]
      elif(tracker.get_slot("item")=="Cake"):
        return [SlotSet("available","available")]
      else:
        return [SlotSet("available","not_available")]

class ActionAddOrder(Action):
   def name(self):
      # type: () -> Text
      return "add_order"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        
        dispatcher.utter_message("Awesome!We have noted your order (Saving the order in the database)")

class ActionSetOrderNumber(Action):
   def name(self):
      # type: () -> Text
      return "set_order_number"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        number = tracker.get_slot("number")
        return [SlotSet("order_number",number)]

class ActionRemoveOrder(Action):
   def name(self):
      # type: () -> Text
      return "remove_order"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_message("Ok. We have removed your order.(Deleting the order from the database)")

class ActionOrderSummary(Action):
   def name(self):
      # type: () -> Text
      return "order_summary"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        message = "Here is the summary of your order: (Fetching Order from Database)" 
        dispatcher.utter_message(message)    

class ActionProcessOrder(Action):
   def name(self):
      # type: () -> Text
      return "process_order"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_message("Thanks, We have sent your order to our kitchen. Please wait in the queque")      