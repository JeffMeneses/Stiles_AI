def choose_function(function_name, entities_names):
    if function_name == "Greeting":
        return greeting(entities_names)
    elif function_name == "WhoAmI":
        return who_am_i(entities_names)
    elif function_name == "Joke":
        return joke(entities_names)

def greeting(entities_names):
    return "Olá, tudo bem?"

def who_am_i(entities_names):
    return "Você pode me chamar de Stiles."

def joke(entities_names):
    return "Por que o computador foi ao médico? Porque estava cheio de vírus! 😄"