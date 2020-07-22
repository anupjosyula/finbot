# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from agilebot import FetchResourceslist
from continentlistgraphQl import FetchContinentslist
from weather import fetchWeatherinfo
from rasa_sdk.events import datetime, ReminderScheduled
from sendsmsmessage import sendSMS
from translate import Translator

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Name = tracker.get_slot("name")
        Empid = tracker.get_slot("empid")
        print(Name)
        print(Empid)
        # dispatcher.utter_message("Hi {}, Welcome to the Payroll Chatbot!, How may I help you?".format(Name))
        dispatcher.utter_template("utter_capture_empid", tracker, Name)

        return []

class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = str(tracker.get_slot("location"))
        print("I am from actions.py" + city)
        print("I am from actions.py converting myself to lowercase" + city.lower())
        if city is not None:
            temp = int(fetchWeatherinfo(city)['temp'] - 273)
            city = city.upper()
        dispatcher.utter_template("utter_temp", tracker, temp=temp, city=city)

        return []

    class ActionSampleGraphql(Action):
        def name(self) -> Text:
            return "action_sample_graphql"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            print('calling the method')
            report = FetchContinentslist()
            print("type of report is {}".format(type(report)))
            print(report)
            print(" ")
            # report contains the json data shown below
            # {"continents": [{"code": "AF", "name": "Africa"}, {"code": "AN", "name": "Antarctica"},
            #                {"code": "AS", "name": "Asia"}, {"code": "EU", "name": "Europe"},
            #                {"code": "NA", "name": "North America"}, {"code": "OC", "name": "Oceania"},
            #                {"code": "SA", "name": "South America"}]}

            # report2 extracts the continents dictionary from the json data

            # output for report 2 is

            # [{'code': 'AF', 'name': 'Africa'}, {'code': 'AN', 'name': 'Antarctica'}, {'code': 'AS', 'name': 'Asia'},
            # {'code': 'EU', 'name': 'Europe'}, {'code': 'NA', 'name': 'North America'},
            # {'code': 'OC', 'name': 'Oceania'}, {'code': 'SA', 'name': 'South America'}]

            report2 = report['continents']
            print("type of report2 is {}".format(type(report2)))
            print(report2)
            print(" ")

            # to fetch all the names values from report2 as a list
            # output of list1 is
            # ['Africa', 'Antarctica', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
            list1 = [d['name'] for d in report2]
            print("type of list1 is {}".format(type(list1)))
            print(list1)
            print(" ")

            # to fetch all the codes values from report2 as a list
            # output of list2 is
            # ['AF', 'AN', 'AS', 'EU', 'NA', 'OC', 'SA']
            list2 = [d['code'] for d in report2]
            print("type of list2 is {}".format(type(list2)))
            print(list2)
            print(" ")

            # to fetch all the name values and codes values from report2 as a dictionary
            # output of dict1 is
            # {'Africa': 'AF', 'Antarctica': 'AN', 'Asia': 'AS', 'Europe': 'EU',
            # 'North America': 'NA', 'Oceania': 'OC', 'South America': 'SA'}
            dict1 = {d['name']:d['code'] for d in report2}
            print("type of dict1 is {}".format(type(dict1)))
            print(dict1)
            print(" ")
            # you can pass list or dictionary in json dumps text to display the output in the chatbot
            dispatcher.utter_message(text=json.dumps(list1, indent=4, sort_keys=False))

            return []

    class ActionAgileBotGraphql(Action):
        def name(self) -> Text:
            return "action_agile_bot_graphql_resources_list"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            fetched_response = FetchResourceslist()
            print(fetched_response)
            print()
            report2 = fetched_response['listResources']["items"]
            print("type of report2 is {}".format(type(report2)))
            print(report2)
            print(" ")

            list1 = [d['resourceName'] for d in report2]
            print("type of list1 is {}".format(type(list1)))
            print(list1)
            print(" ")

            list2 = [d['resource_id'] for d in report2]
            print("type of list2 is {}".format(type(list2)))
            print(list2)
            print(" ")

            dict1 = {d['resourceName']:d['resource_id'] for d in report2}
            print("type of dict1 is {}".format(type(dict1)))
            print(dict1)
            print(" ")
            # you can pass list or dictionary in json dumps text to display the output in the chatbot
            dispatcher.utter_message(text=json.dumps(list1, indent=4, sort_keys=False))

            return []

    class Actionleavestype(Action):
        """Reminds the user to call someone."""

        def name(self) -> Text:
            return "action_type_of_leave"

        def run(
                self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            message = {"data": {
                "payload": "collapisible",
                "data": [
                    {
                        "title": "Sick Leave",
                        "description": "Sick leave is time off from work that workers can use to stay home to address their health and safety needs without losing pay"
                    },
                    {
                        "title": "Earned Leave",
                        "description": "Earned Leaves are the leaves which are earned in the previous year and enjoyed in the preceding years."
                    }
                ]
            }
            }
            dispatcher.utter_message(text=json.dumps(message["data"]))
            # print(json_message)
            return []

    class ActionReminder(Action):
        """Reminds the user to call someone."""

        def name(self) -> Text:
            return "action_set_reminder"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            # 1. In any method multiple dispatcher messages are not working. if you want to display buttons, images,
            #    text video attachments then it should be mentioned in one single message.
            # 2. In case you have more than one message and would like to display one after the other
            #    mention in domain.yml under utter or in stories where chat responses are mentioned else
            #    define different functions to send different messages.
            # 3. Remember only embedded videos can be played by bot. to embed a youtube video click on share and then
            #    select embed option and then paste the link in either domain.yml or actions.py for custom actions.

            dispatcher.utter_message(text="I will remind you in 30 seconds.Would you like to be notified by phone?",
                                     buttons=[{'title': 'Yes', 'payload': 'ask_phonenumber'},
                                              {'title': 'No', 'payload': 'deny'}])

            date = datetime.datetime.now() + datetime.timedelta(seconds=30)
            # dispatcher.utter_message("Hi {}, Welcome to the Payroll Chatbot!, How may I help you?".format(Name))
            reminder = ReminderScheduled(
                "EXTERNAL_reminder",
                trigger_date_time=date,
                name="my_reminder",
                kill_on_user_message=False,
            )

            return [reminder]

        class ActionReactToReminder(Action):
            """Reminds the user to call someone."""

            def name(self) -> Text:
                return "action_react_to_reminder"

            async def run(
                    self,
                    dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                user_phone = tracker.get_slot("phone")
                print(user_phone)
                if (user_phone):
                    sendSMS(user_phone)
                dispatcher.utter_message(
                    text="Reminder to submit your Investment Declaration\n Would you like to be reminded again?",
                    buttons=[{'title': 'Yes', 'payload': 'ask_remind_call'},
                             {'title': 'No', 'payload': 'deny'}],
                )
                return []
