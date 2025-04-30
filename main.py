import modules.asr.asr as asr
import modules.capsule_classifier.predict as capsule_classifier
import modules.function_classifier.orchestrator as function_classifier
import modules.ner.orchestrator as ner
import modules.functions.orchestrator as functions
import modules.tts.tts as tts
import asyncio
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def main():
    print('\033[1m') # BOLD

     # 1. Automatic Speech Recognition (ASR)
    utterance = asr.get_utterance()
    print ("\n"+"="*25+" [STEP 1] "+"="*25)
    print("🎙️ Listening to the user...")
    print(f"The user said: '{utterance}'")

    # 2. capsule_name Classifier
    capsule_name = capsule_classifier.predict(utterance)
    print ("\n"+"="*25+" [STEP 2] "+"="*25)
    print(f"The Capsule Classifier returned: {capsule_name}")

    # 3. Function Classifier
    function_name = function_classifier.choose_function_classifier_capsule(utterance, capsule_name)
    print ("\n"+"="*25+" [STEP 3] "+"="*25)
    print(f"The Function Classifier returned: {function_name}")

    # 4. Named Entity Recognition (NER)
    entities_names = ner.choose_ner(utterance, capsule_name)
    print ("\n"+"="*25+" [STEP 4] "+"="*25)
    print(f"The Entity Extractor returned: {entities_names}")

    # 5. Function code
    nlg = functions.choose_function_code_capsule(capsule_name, function_name, entities_names)
    print ("\n"+"="*25+" [STEP 5] "+"="*25)
    print(f"The Function returned: {nlg}")

    # TODO: Implement NLG handler

    # 6. Text to Speak (TTS)
    print ("\n"+"="*25+" [STEP 6] "+"="*25)
    Stiles_response = asyncio.run(tts.say_utterance(nlg))
    print(f"🤖 Stiles said: {Stiles_response}")


if __name__ == "__main__":
    main()