import modules.nlg.stiles_calendar_NLG as calendar_capsule_nlg
import modules.nlg.stiles_reminder_NLG as reminder_capsule_nlg
import modules.nlg.stiles_chat_NLG as chat_capsule_nlg
import modules.nlg.stiles_datetime_NLG as datetime_capsule_nlg

def choose_capsule_nlg(conversationID):
    if conversationID['capsule'] == "Calendar":
        return calendar_capsule_nlg.choose_nlg(conversationID)
    elif conversationID['capsule'] == "Reminder":
        return reminder_capsule_nlg.choose_nlg(conversationID)
    elif conversationID['capsule'] == "Chat":
        return chat_capsule_nlg.choose_nlg(conversationID)
    elif conversationID['capsule'] == "Datetime":
        return datetime_capsule_nlg.choose_nlg(conversationID)