import spacy
import json
import os

def choose_ner(utterance, capsule_name):
    # TODO: Make Chat be handled by LLM
    return predict(utterance, capsule_name)

def predict(utterance, capsule_name):
    # Carrega o modelo treinado
    nlp = spacy.load(f"modules/ner/stiles_{capsule_name}/{capsule_name}_ner/model-best")
    doc = nlp(utterance)

    entities_names = {}
    for ent in doc.ents:
        #print(f"({ent.text}):[{ent.label_}]")
        sub_label = _get_key_for_value(ent.text, capsule_name)
        if sub_label is not None:
            #print(f"✅ Normalized label: ({ent.text}):[{ent.label_}:{sub_label}]")
            dict_key = f"{ent.label_}:{sub_label}"
        else:
            #print(f"✅ Normalized label: ({ent.text}):[{ent.label_}]")
            dict_key = f"{ent.label_}"
        entities_names[dict_key] = ent.text
    
    #print(f"entities_names: {entities_names}")
    return entities_names

def _get_key_for_value(search_value, capsule_name):
    closed_vocab = _create_vocab_dict(capsule_name)
    #print(f"closed_vocab: {closed_vocab}")

    search_value_lower = search_value.lower()
    for category, sub_dict in closed_vocab.items():
        for key, values in sub_dict.items():
            if any(search_value_lower == v.lower() for v in values):
                return key
    return None

def _create_vocab_dict(capsule_name):
    json_dir = f"modules/ner/stiles_{capsule_name.lower()}/vocab"

    closed_vocab = {}
    # Iterate through all JSON files in the directory
    for filename in os.listdir(json_dir):
        filepath = os.path.join(json_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            new_data = json.load(f)  # Load JSON content
        
        for category, sub_dict in new_data.items():
            closed_vocab[category] = sub_dict
    
    return closed_vocab