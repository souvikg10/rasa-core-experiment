from rasa_core_sdk import Action


class ActionCheckOrder(Action):
   def name(self):
      # type: () -> Text
      return "check_order_available"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_suggest_alternatives", tracker)

class ActionAddOrder(Action):
   def name(self):
      # type: () -> Text
      return "add_order"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_card_retrieval_confirmed", tracker)

class ActionSetOrderNumber(Action):
   def name(self):
      # type: () -> Text
      return "set_order_number"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_card_retrieval_confirmed", tracker)

class ActionRemoveOrder(Action):
   def name(self):
      # type: () -> Text
      return "remove_order"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_card_retrieval_confirmed", tracker)

class ActionOrderConfirmation(Action):
   def name(self):
      # type: () -> Text
      return "order_confirmation"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_card_retrieval_confirmed", tracker)      

class ActionOrderSummary(Action):
   def name(self):
      # type: () -> Text
      return "order_summary"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_card_retrieval_confirmed", tracker)      

class ActionProcessOrder(Action):
   def name(self):
      # type: () -> Text
      return "process_order"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        dispatcher.utter_template("utter_card_retrieval_confirmed", tracker)      