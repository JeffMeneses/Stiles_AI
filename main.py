import modules.asr.asr as asr
import modules.capsule_classifier.predict as capsule_classifier
import modules.function_classifier.orchestrator as function_classifier
import modules.ner.orchestrator as ner
import modules.functions.orchestrator as functions
import modules.tts.tts as tts

def main():
     # 1. Automatic Speech Recognition (ASR)
    utterance = asr.get_utterance()
    print ("\n========== [STEP 1] ========== ")
    print("🎙️ Listening to the user...")
    print(f"The user said: '{utterance}'")

    # 2. capsule_name Classifier
    capsule_name = capsule_classifier.predict(utterance)
    print ("\n========== [STEP 2] ========== ")
    print(f"The Capsule Classifier returned: {capsule_name}")

    # 3. Function Classifier
    function_name = function_classifier.choose_function_classifier_capsule(utterance, capsule_name)
    print ("\n========== [STEP 3] ========== ")
    print(f"The Function Classifier returned: {function_name}")

    # 4. Named Entity Recognition (NER)
    entities_names = ner.choose_ner_capsule(utterance, capsule_name)
    print ("\n========== [STEP 4] ========== ")
    print(f"The Entity Extractor returned: {entities_names}")

    # 5. Function code
    Stiles_response = functions.choose_function_code_capsule(capsule_name, function_name, entities_names)
    print ("\n========== [STEP 5] ========== ")
    print(f"The Function returned: {Stiles_response}")

    # 6. Text to Speak (TTS)
    print ("\n========== [STEP 6] ========== ")
    tts.say_utterance(Stiles_response)
    print(f"🤖 Stiles said: {Stiles_response}")


if __name__ == "__main__":
    main()