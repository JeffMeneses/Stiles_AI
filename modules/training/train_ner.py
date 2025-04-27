import json
import spacy
from spacy.tokens import DocBin
from spacy.cli.train import train
from pathlib import Path

SUPPORTED_CAPSULES = ['reminder','calendar','chat']

CLOSED_VOCAB = {
    "Capsule": {
        "Reminder": ["lembrete", "Lembretes", "Reminder"],
        "Calendar": ["Calendário", "Agenda", "Calendar"]
    }
}

def train_all_ner():
    for capsule in SUPPORTED_CAPSULES:
        print(f"\nTraining NER model for {capsule.title()} capsule...")

        try:
            train_ner(capsule)
            print(f"✅ The NER model for {capsule.title()} capsule has been trained successfully!")
        except:
            print(f"❌ Something went wrong while training {capsule.title()} capsule.")


def train_ner(capsule):
    nlp = spacy.blank("pt")
    ner = nlp.add_pipe("ner")

    with open(f"modules/training/data/{capsule}_ner_data.jsonl", "r", encoding="utf-8") as f:
        train_data = [json.loads(line) for line in f]

    #print(train_data)
    # Get all labels from dataset
    entities = []
    for item in train_data:
        #print(f"Utterance: {item['utterance']}/ Entity: {item['entities']}")
        for start, end, entity in item['entities']:
            #print(f"Entity found: {entity}")
            if entity not in entities:
                entities.append(entity)
    
    #print(f'All the entities found: {entities}')
    
    # Add labels (open + closed)
    for entity in entities:
        ner.add_label(entity)

    nlp = spacy.blank("pt")
    db = DocBin()

    for utterance in train_data:
        doc = nlp.make_doc(utterance["utterance"])
        ents = []
        for start, end, label in utterance["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is not None:
                ents.append(span)
        doc.ents = ents
        db.add(doc)

    db.to_disk(f"modules/training/data/{capsule}_ner_data.spacy")

    config_path = Path(f"modules/training/data/config.cfg")
    output_path = Path(f"modules/ner/stiles_{capsule}/{capsule}_ner")
    train_data_path = Path(f"modules/training/data/{capsule}_ner_data.spacy")
    dev_data_path = Path(f"modules/training/data/{capsule}_ner_data.spacy")

    output_path.mkdir(parents=True, exist_ok=True)

    train(
        config_path=config_path,
        output_path=output_path,
        overrides={
            "paths.train": str(train_data_path),
            "paths.dev": str(dev_data_path),
        }
    )

if __name__ == "__main__":
    train_all_ner()