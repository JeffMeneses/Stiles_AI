def choose_nlg(nlg_name, entities_names):
    if nlg_name == "create_reminder_NLG_1_1":
        response = create_reminder_NLG_1_1(entities_names)
    elif nlg_name == "edit_reminder_NLG_2_1":
        response =  edit_reminder_NLG_2_1(entities_names)
    elif nlg_name == "delete_reminder_NLG_3_1":
        response =  delete_reminder_NLG_3_1(entities_names)
    
    if 'required-entity' in response:
        return choose_prompt_NLG(response)

def create_reminder_NLG_1_1(entities_names):
    if 'ReminderName' in entities_names:
        return {"text": f"Ok, criei seu lembrete chamado {entities_names['ReminderName']}.", "state": "Root"}
    return {"required-entity": 'ReminderName',"state": "Prompt"}

def edit_reminder_NLG_2_1(entities_names):
    if 'ReminderName' in entities_names:
        return {"text": f"Ok, editei seu lembrete chamado {entities_names['ReminderName']}.", "state": "Root"}
    return {"required-entity": 'ReminderName',"state": "Prompt"}

def delete_reminder_NLG_3_1(entities_names):
    if 'ReminderName' in entities_names:
        return {"text": f"Ok, apaguei seu lembrete chamado {entities_names['ReminderName']}.", "state": "Root"}
    return {"required-entity": 'ReminderName',"state": "Prompt"}

def choose_prompt_NLG(response):
    if response['required-entity'] == "ReminderName":
        return {"text": f"Do que devo te lembrar?", "state": "Prompt"}