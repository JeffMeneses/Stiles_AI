import speech_recognition as asr

# Configurações
WAKE_WORD = "teste"
SILENCE_TIMEOUT = 1.0  # segundos de silêncio para finalizar
PHRASE_TIMEOUT = 8.0   # tempo máximo escutando o comando

recognizer = asr.Recognizer()
mic = asr.Microphone()


def get_utterance(state):
    while True:
        if state == "Prompt":
            return listen_for_command()
        if listen_for_wake_word():
            return listen_for_command()

def listen_for_wake_word():
    print("🎤 Aguardando palavra-chave ('stiles')...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="pt-BR").lower()
        print(f"🗣️ Detecção: {text}")
        return WAKE_WORD in text
    except asr.UnknownValueError:
        return False
    except asr.RequestError as e:
        print(f"Erro no reconhecimento: {e}")
        return False

def listen_for_command():
    print("🎧 Aguardando comando...")
    with mic as source:
        audio = recognizer.listen(source, timeout=PHRASE_TIMEOUT, phrase_time_limit=PHRASE_TIMEOUT)
    try:
        command = recognizer.recognize_google(audio, language="pt-BR")
        print(f"✅ Comando recebido: {command}")
        return command
    except asr.UnknownValueError:
        print("❌ Não entendi o que foi dito.")
    except asr.RequestError as e:
        print(f"Erro no reconhecimento: {e}")