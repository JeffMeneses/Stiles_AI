import modules.functions.stiles_calendar as calendar_capsule
import modules.functions.stiles_reminder as reminder_capsule
import modules.functions.stiles_chat as chat_capsule
import modules.functions.stiles_datetime as datetime_capsule

def choose_function_code_capsule(capsule_name, function_name, entities_names):
    if capsule_name == "Calendar":
        return calendar_capsule.choose_function(function_name, entities_names)
    elif capsule_name == "Reminder":
        return reminder_capsule.choose_function(function_name, entities_names)
    elif capsule_name == "Chat":
        return chat_capsule.choose_function(function_name, entities_names)
    elif capsule_name == "Datetime":
        return datetime_capsule.choose_function(function_name, entities_names)