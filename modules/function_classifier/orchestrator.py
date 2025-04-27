import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

def choose_function_classifier_capsule(utterance, capsule_name):
    if capsule_name == "Calendar":
        return predict(utterance, capsule_name)
    elif capsule_name == "Reminder":
        return predict(utterance, capsule_name)
    elif capsule_name == "Chat":
        return predict(utterance, capsule_name)

def predict(utterance, capsule_name):
    clf = joblib.load(f"modules/function_classifier/stiles_{capsule_name.lower()}/{capsule_name.lower()}_random_forest_function_classifier.joblib")
    vectorizer = joblib.load(f"modules/function_classifier/stiles_{capsule_name.lower()}/{capsule_name.lower()}_tfidf_vectorizer.joblib")

    X_new = vectorizer.transform([utterance])

    return  clf.predict(X_new)[0]