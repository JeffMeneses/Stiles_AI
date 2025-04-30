def choose_function(function_name, entities_names):
    if function_name == "GetCurrentTime":
        return get_current_time(entities_names)
    elif function_name == "GetCurrentDate":
        return get_current_date(entities_names)
    elif function_name == "CalculateTimeUntil":
        return calculate_time_until(entities_names)

def get_current_time(entities_names):
    return {"text": f"Agora são 16:51."}

def get_current_date(entities_names):
    return {"text": f"Hoje é dia 27 de Abril de 2025."}

def calculate_time_until(entities_names):
    return {"text": f"Faltam 108 dias para o Natal."}