def choose_function(function_name, entities_names):
    if function_name == "CreateEvent":
        create_event(entities_names)

def create_event(entities_names):
    return f"Ok, criei seu evento chamado {entities_names['EventName']}."