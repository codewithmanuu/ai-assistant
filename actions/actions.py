# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import joblib
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .res import responses
class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_predict_intent"
    
    def __init__(self):

        self.model = joblib.load('ai_model')

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_input = tracker.latest_message.get('text')
        predicted_intent = self.model.predict([user_input])[0]
        response = responses[predicted_intent]
        dispatcher.utter_message(text=f"{response}")

        return []
    
class BotIntoduction(Action):
    def name(self) -> Text:
        return "bot_introduction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(text=f"👋 Hello! I'm Manny, Manu's personal AI assistant 🤖 – here to help, but sadly, I can't fetch coffee... ☕️ yet! 😂")

        return []
