def choose_function(function_name, entities_names):
    if function_name == "CreateReminder":
        return create_reminder(entities_names)
    elif function_name == "EditReminder":
        return edit_reminder(entities_names)
    elif function_name == "DeleteReminder":
        return delete_reminder(entities_names)

def create_reminder(entities_names):
    try:
        return f"Ok, criei seu lembrete chamado {entities_names['EventName']}."
    except:
        return f"Ok, criei seu lembrete."

def edit_reminder(entities_names):
    try:
        return f"Ok, editei seu lembrete chamado {entities_names['EventName']}."
    except:
        return f"Ok, editei seu lembrete."

def delete_reminder(entities_names):
    try:
        return f"Ok, apaguei seu lembrete chamado {entities_names['EventName']}."
    except:
        return f"Ok, apaguei seu lembrete."