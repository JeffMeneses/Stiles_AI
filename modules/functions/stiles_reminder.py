def choose_function(function_name, entities_names):
    if function_name == "CreateReminder":
        return create_reminder(entities_names)

def create_reminder(entities_names):
    return f"Ok, criei seu lembrete chamado {entities_names['ReminderName']}."