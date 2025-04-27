def choose_function(function_name, entities_names):
    if function_name == "CreateEvent":
        return create_event(entities_names)
    elif function_name == "EditEvent":
        return edit_event(entities_names)
    elif function_name == "DeleteEvent":
        return delete_event(entities_names)

def create_event(entities_names):
    try:
        return f"Ok, criei seu evento chamado {entities_names['EventName']}."
    except:
        return f"Ok, criei seu evento."

def delete_event(entities_names):
    try:
        return f"Ok, apaguei seu evento chamado {entities_names['EventName']}."
    except:
        return f"Ok, apaguei seu evento."

def edit_event(entities_names):
    try:
        return f"Ok, editei seu evento chamado {entities_names['EventName']}."
    except:
        return f"Ok, editei seu evento."