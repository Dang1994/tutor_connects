import pandas as pd
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os

class ActionFindTutor(Action):

    def name(self) -> Text:
        return "action_find_tutor"

    def __init__(self):
        # Load the CSV data once when the action server starts
        current_directory = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_directory, "tutor_data", "tutor_dataset.csv")
        self.tutor_data = pd.read_csv(csv_path)

        # Ensure consistency in string cases for matching
        self.tutor_data['Location'] = self.tutor_data['Location'].str.lower()
        self.tutor_data['Subjects'] = self.tutor_data['Subjects'].str.lower()

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot('location')
        subject = tracker.get_slot('subject')

        # If either location or subject is missing
        if not location or not subject:
            dispatcher.utter_message(text="I need both location and subject to find the best tutors for you.")
            return []

        # Normalize input for case-insensitive matching
        location = location.lower()
        subject = subject.lower()

        # Filter tutors based on location and subject
        matching_tutors = self.tutor_data[
            (self.tutor_data['Location'] == location) &
            (self.tutor_data['Subjects'].str.contains(subject))
        ]

        if matching_tutors.empty:
            dispatcher.utter_message(text=f"Sorry, I couldn't find any tutors for {subject.title()} in {location.title()}.")
            return []

        # Select top tutors based on Experience and Rates (assuming higher rates correlate with more experienced tutors)
        top_tutors = matching_tutors.sort_values(by=['Experience_Years', 'Rates_Per_Hour'], ascending=False).head(5)

        response = f"Here are the top tutors for {subject.title()} in {location.title()}:\n\n"

        for index, tutor in top_tutors.iterrows():
            response += (
                f"**Name:** {tutor['Name']}\n"
                f"**Phone:** {tutor['Phone']}\n"
                f"**Email:** {tutor['Email']}\n"
                f"**Experience:** {tutor['Experience_Years']} years\n"
                f"**Rates:** ₹{tutor['Rates_Per_Hour']} per hour\n"
                f"**Mode:** {tutor['Mode_of_Tutoring']}\n"
                f"**Education:** {tutor['Education']}\n\n"
            )

        dispatcher.utter_message(text=response)

        return []

class ActionSubmitForm(Action):
    """
    This action handles the final form submission.
    It confirms to the user that the tutor search is complete, using the slots 'location' and 'subject'.
    """
    def name(self) -> Text:
        return "action_submit_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot('location')
        subject = tracker.get_slot('subject')

        if not location or not subject:
            dispatcher.utter_message(text="I still need some information to find a tutor.")
            return []

        dispatcher.utter_message(
            text=f"Thank you! You've requested a tutor for {subject.title()} in {location.title()}. I'll find the best options for you."
        )

        # Now trigger the action that finds the tutor based on the provided information
        return []

class ActionFallback(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="I'm sorry, I didn't quite get that. Can you please provide more information?")
        return []
