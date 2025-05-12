def choose_function(function_name, entities_names):
    if function_name == "CreateReminder":
        return create_reminder(entities_names)
    elif function_name == "EditReminder":
        return edit_reminder(entities_names)
    elif function_name == "DeleteReminder":
        return delete_reminder(entities_names)

def create_reminder(entities_names):
    #TODO: Interact with mongoDB to simulate a Device
    return {'nlg_id': 'create_reminder_NLG_1_1', 'required-entity': ['ReminderName']}

def edit_reminder(entities_names):
    #TODO: Interact with mongoDB to simulate a Device
    return {'nlg_id': 'edit_reminder_NLG_2_1', 'required-entity': ['ReminderName']}

def delete_reminder(entities_names):
    #TODO: Interact with mongoDB to simulate a Device
    return {'nlg_id': 'delete_reminder_NLG_3_1', 'required-entity': ['ReminderName']}