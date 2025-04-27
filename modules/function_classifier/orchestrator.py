from modules.function_classifier.stiles_calendar import predict as calendar_capsule
from modules.function_classifier.stiles_reminder import predict as reminder_capsule
from modules.function_classifier.stiles_chat import predict as chat_capsule

def choose_function_classifier_capsule(utterance, capsule_name):
    if capsule_name == "Calendar":
        return calendar_capsule.predict(utterance, capsule_name)
    elif capsule_name == "Reminder":
        return reminder_capsule.predict(utterance, capsule_name)
    elif capsule_name == "Chat":
        return chat_capsule.predict(utterance, capsule_name)