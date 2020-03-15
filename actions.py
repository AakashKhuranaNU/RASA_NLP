# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import parser_v1, search


class ActionPrintRecipe(Action):

    def name(self) -> Text:
        return "action_print_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        recipe = tracker.get_slot("recipe_url")

        rf = parser_v1.RecipeFetcher()

        results = rf.scrape_recipe(recipe)

        dispatcher.utter_message(text="Alright. So let's start working with {}.".format(results["title"]))

        return [SlotSet("ingredients", results["ingredients"]), SlotSet("recipe", results["directions"]), SlotSet("nutrients", results["nutrients"]), SlotSet("step_no", 0.0)]


class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        gs = search.Goog_Search()

        user_query = tracker.get_slot("query_cheeku")
        # print("query: {}".format(user_query))
        answer = gs.search_keyword(user_query)

        dispatcher.utter_message(text="Here, I found a reference for you: {}".format(answer))

        user_choice = tracker.get_slot("choice")

        if user_choice == '1' or user_choice == '3':
            dispatcher.utter_message(
                text="What do you want to do next? Here are the options: [1] Go over ingredients list or [2] Go over recipe steps or [3] Go over nutrients list")

        else:
            dispatcher.utter_message(text="Should I continue to the next step?")

        return []


class ActionReset(Action):

    def name(self) -> Text:
        return "action_reset"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("step_no", 0.0)]


class ActionPrintStep(Action):

    def name(self) -> Text:
        return "action_print_step"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("choice")

        if user_choice == '1':
            ingredients = tracker.get_slot("ingredients")

            for i in range(len(ingredients)):
                dispatcher.utter_message(text=ingredients[i])

            dispatcher.utter_message(text="What do you want to do next? Here are the options: [1] Go over ingredients list or [2] Go over recipe steps or [3] Go over nutrients list")

            return [SlotSet("step_no", 0.0)]

        elif user_choice == '2':
            step = int(tracker.get_slot("step_no"))
            directions = tracker.get_slot("recipe")

            if step >= len(directions):
                dispatcher.utter_message(text="All recipe steps shown.")
                dispatcher.utter_message(
                    text="What do you want to do next? Here are the options: [1] Go over ingredients list or [2] Go over recipe steps or [3] Go over nutrients list")
                return [SlotSet("step_no", 0.0)]

            dispatcher.utter_message(text="Step {}: {}".format(step, directions[step]))
            dispatcher.utter_message(text="Should I continue to the next step?")

            return [SlotSet("step_no", float(step+1))]

        elif user_choice == '3':
            nutrients = tracker.get_slot("nutrients")

            for i in range(len(nutrients)):
                dispatcher.utter_message(text=nutrients[i])

            dispatcher.utter_message(text="What do you want to do next? Here are the options: [1] Go over ingredients list or [2] Go over recipe steps or [3] Go over nutrients list")
            return [SlotSet("step_no", 0.0)]


        dispatcher.utter_message(text="Please choose proper option.")

        return []







