# -*- coding: utf-8 -*-

# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import requests

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app_id = "86802a5d"
app_key = "cc4438253a127ad2ed636db9194d18c3"

# This function provides the status of the specific line
def provide_line_status(user_input):
    link = "https://api.tfl.gov.uk/Line/{lineName}/Status?app_id={app_id}&app_key={app_key}".format(lineName=user_input, app_id=app_id, app_key=app_key)
    response = requests.get(link)
    if response.status_code == 200: # Checking if the connection is established
        line_status = response.json()[0]['lineStatuses'][0]
        service_status = line_status['statusSeverityDescription']
        sentence = service_status
        if(sentence != "Good Service"): # If the service is not working properly
            disruption = line_status['reason']
            speak_output = disruption
        else:
            speak_output = "The {lineName} line is working very well! TFL says: {status}".format(lineName=user_input, status=sentence)
    else:
        speak_output = "There is a problem with connecting to TFL services. Please try again later."
    
    return speak_output

# This class builds the lines that possibly not working well
class AvoidIntent(AbstractRequestHandler):
    """Handler for Avoid Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AvoidIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        lines_to_avoid = ""
        tfl_lines = ['bakerloo', 'central', 'circle', 'district', 'hammersmith-city', 'victoria', 'waterloo-city', 'jubilee', 'metropolitan', 'northern', 'piccadilly', 'london-overground', 'tfl-rail', 'dlr', 'tram']
        for line in tfl_lines:
            link = "https://api.tfl.gov.uk/Line/{lineName}/Status?app_id={app_id}&app_key={app_key}".format(lineName=line, app_id=app_id, app_key=app_key)
            response = requests.get(link)
            line_status = response.json()[0]['lineStatuses'][0]
            service_status = line_status['statusSeverityDescription']
            sentence = service_status
            if(sentence != 'Good Service'):
                lines_to_avoid += line + ", "
        
        speak_output = "Today's possible lines to avoid follow: {line}".format(line=lines_to_avoid[:-2])

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to the Tube Line Status. Simply tell me which line you want to check or say 'which lines to avoid?'"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class CentralLineIntent(AbstractRequestHandler):
    """Handler for Central line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CentralLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("central")
            
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class BakerlooLineIntent(AbstractRequestHandler):
    """Handler for Bakerloo Line Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BakerlooLineIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = provide_line_status("bakerloo")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class VictoriaLineIntent(AbstractRequestHandler):
    """Handler for Victoria Line Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("VictoriaLineIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = provide_line_status("victoria")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class CircleLineIntent(AbstractRequestHandler):
    """Handler for Victoria Line Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("VictoriaLineIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = provide_line_status("circle")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class DistrictLineIntent(AbstractRequestHandler):
    """Handler for District line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DistrictLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("district")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class JubileeLineIntent(AbstractRequestHandler):
    """Handler for Jubilee line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("JubileeLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("jubilee")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class PiccadillyLineIntent(AbstractRequestHandler):
    """Handler for Piccadilly line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PiccadillyLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("piccadilly")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class NorthernLineIntent(AbstractRequestHandler):
    """Handler for Northern line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NorthernLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("northern")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class MetropolitanLineIntent(AbstractRequestHandler):
    """Handler for Metropolitan line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MetropolitanLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("metropolitan")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class HammersmithCityLineIntent(AbstractRequestHandler):
    """Handler for Hammersmith and City line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HammersmithCityLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("hammersmith-city")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class WaterlooCityLineIntent(AbstractRequestHandler):
    """Handler for Waterloo and City line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WaterlooCityLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("waterloo-city")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class OvergroundLineIntent(AbstractRequestHandler):
    """Handler for Overground line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OvergroundLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("london-overground")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class TflRailLineIntent(AbstractRequestHandler):
    """Handler for TFL Rail line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TflRailLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("tfl-rail")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class DlrLineIntent(AbstractRequestHandler):
    """Handler for Dlr line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DlrLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("dlr")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class TramLineIntent(AbstractRequestHandler):
    """Handler for Tram line"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TramLineIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = provide_line_status("tram")

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can ask for a line status, for example: 'central line status!'"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AvoidIntent())
sb.add_request_handler(CentralLineIntent())
sb.add_request_handler(BakerlooLineIntent())
sb.add_request_handler(VictoriaLineIntent())
sb.add_request_handler(CircleLineIntent())
sb.add_request_handler(JubileeLineIntent())
sb.add_request_handler(PiccadillyLineIntent())
sb.add_request_handler(NorthernLineIntent())
sb.add_request_handler(MetropolitanLineIntent())
sb.add_request_handler(HammersmithCityLineIntent())
sb.add_request_handler(WaterlooCityLineIntent())
sb.add_request_handler(TflRailLineIntent())
sb.add_request_handler(DlrLineIntent())
sb.add_request_handler(TramLineIntent())
sb.add_request_handler(OvergroundLineIntent())
sb.add_request_handler(DistrictLineIntent())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()