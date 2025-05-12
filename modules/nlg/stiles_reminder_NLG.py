def choose_nlg(conversationID): 
    if not _check_required_entities(conversationID):
        response = choose_prompt_NLG(conversationID)
        return response

    if conversationID['nlg_macro']['nlg_id'] == "create_reminder_NLG_1_1":
        response = create_reminder_NLG_1_1(conversationID)
    elif conversationID['nlg_macro']['nlg_id'] == "edit_reminder_NLG_2_1":
        response =  edit_reminder_NLG_2_1(conversationID)
    elif conversationID['nlg_macro']['nlg_id'] == "delete_reminder_NLG_3_1":
        response =  delete_reminder_NLG_3_1(conversationID)
    
    return response

def create_reminder_NLG_1_1(conversationID):
    conversationID['nlg'] = {'text': f"Ok, criei seu lembrete chamado {conversationID['entities']['ReminderName']}."}
    conversationID['state'] = 'Root'
    return conversationID

def edit_reminder_NLG_2_1(conversationID):
    conversationID['nlg'] = {'text': f"Ok, editei seu lembrete chamado {conversationID['entities']['ReminderName']}."}
    conversationID['state'] = 'Root'
    return conversationID

def delete_reminder_NLG_3_1(conversationID):
    conversationID['nlg'] = {'text': f"Ok, apaguei seu lembrete chamado {conversationID['entities']['ReminderName']}."}
    conversationID['state'] = 'Root'
    return conversationID

def choose_prompt_NLG(conversationID):
    if 'ReminderName' not in conversationID['entities'].keys() and conversationID['nlg_macro']['nlg_id'] == 'create_reminder_NLG_1_1':
        conversationID['nlg'] = {'text': f"Do que devo te lembrar?"}
        conversationID['state'] = "Prompt"

    if 'ReminderName' not in conversationID['entities'].keys() and conversationID['nlg_macro']['nlg_id'] == 'edit_reminder_NLG_2_1':
        conversationID['nlg'] = {'text': f"Qual lembrete devo editar?"}
        conversationID['state'] = "Prompt"

    if 'ReminderName' not in conversationID['entities'].keys() and conversationID['nlg_macro']['nlg_id'] == 'delete_reminder_NLG_3_1':
        conversationID['nlg'] = {'text': f"Qual lembrete devo apagar?"}
        conversationID['state'] = "Prompt"

    return conversationID

def _check_required_entities(conversationID):
    required_entities = conversationID['nlg_macro']['required-entity']
    existing_entities = conversationID['entities'].keys()

    return all(entity in existing_entities for entity in required_entities)