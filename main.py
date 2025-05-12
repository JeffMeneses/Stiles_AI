import modules.asr.asr as asr
import modules.capsule_classifier.predict as capsule_classifier
import modules.function_classifier.orchestrator as function_classifier
import modules.ner.orchestrator as ner
import modules.functions.orchestrator as functions
import modules.nlg.orchestrator as nlgs
import modules.tts.tts as tts
import asyncio
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

## Colors
GREEN = "\033[32m"
WHITE = "\033[37m"

def main():
    print('\033[1m') # BOLD

    conversationID = {
        "state": 'Root',
        'utterance': '',
        'capsule': '',
        'function': '',
        'entities': [],
        'nlg_macro': {},
        'nlg': {},
        'required-entity': []
    }
    #Stiles_response = asyncio.run(tts.say_utterance({"text": f"Olá, eu sou Stiles. No que posso te ajudar?", "speech": f"Olá, eu sou Stáius. No que posso te ajudar?"}))
    #print(f"🤖 Stiles said: {Stiles_response}")

    while True:
        # 1. Automatic Speech Recognition (ASR)
        #utterance = asr.get_utterance(state)
        conversationID['utterance'] = get_command()
        print ("\n"+"="*25+" [STEP 1] "+"="*25)
        print("🎙️ Listening to the user...")
        print(f"The user said: {GREEN}'{conversationID['utterance']}'{WHITE}")

        if conversationID['utterance'] == "Tchau, Stiles":
            Stiles_response = asyncio.run(tts.say_utterance({"text": f"Até mais. Se precisar de algo é só me chamar."}))
            print(f"🤖 Stiles said: {GREEN}{Stiles_response}{WHITE}")
            break

        if conversationID['state'] == 'Root':
            root_handler(conversationID)
        else:
            prompt_handler(conversationID)

        # 5. Function code
        conversationID['nlg_macro'] = functions.choose_function_code_capsule(conversationID['capsule'], conversationID['function'], conversationID['entities'])
        print ("\n"+"="*25+" [STEP 5] "+"="*25)
        print(f"The Function returned: {GREEN}{conversationID['nlg_macro']}{WHITE}")
            
        # 6. NLG
        conversationID = nlgs.choose_capsule_nlg(conversationID)
        print ("\n"+"="*25+" [STEP 6] "+"="*25)
        print(f"The NLG returned: {GREEN}{conversationID['nlg']}{WHITE}")

        # 7. Text to Speak (TTS)
        print ("\n"+"="*25+" [STEP 7] "+"="*25)
        asyncio.run(tts.say_utterance(conversationID['nlg']))
        print(f"🤖 Stiles said: {GREEN}{conversationID['nlg']}{WHITE}")

        if conversationID['state'] == "Prompt":
            state = 'Prompt'
            continue
        break

## ASR BypPass for tests. I will be removed
def get_command():
    print("\nStiles is waiting for a command...")
    return input()

def root_handler(conversationID):
    # 2. conversationID['capsule'] Classifier
    conversationID['capsule'] = capsule_classifier.predict(conversationID['utterance'])
    print ("\n"+"="*25+" [STEP 2] "+"="*25)
    print(f"The Capsule Classifier returned: {GREEN}{conversationID['capsule']}{WHITE}")

    # 3. Function Classifier
    conversationID['function'] = function_classifier.choose_function_classifier_capsule(conversationID['utterance'], conversationID['capsule'])
    print ("\n"+"="*25+" [STEP 3] "+"="*25)
    print(f"The Function Classifier returned: {GREEN}{conversationID['function']}{WHITE}")

    # 4. Named Entity Recognition (NER)
    conversationID['entities'] = ner.choose_ner(conversationID['utterance'], conversationID['capsule'])
    print ("\n"+"="*25+" [STEP 4] "+"="*25)
    print(f"The Entity Extractor returned: {GREEN}{conversationID['entities']}{WHITE}")

    return conversationID

def prompt_handler(conversationID):

    # The whole utterance will be the value for the required entity
    conversationID['entities'][conversationID['nlg_macro']['required-entity'][0]] = conversationID['utterance']
    return conversationID


if __name__ == "__main__":
    main()