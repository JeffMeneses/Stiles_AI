import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

def predict(utterance):
    clf = joblib.load("modules/capsule_classifier/random_forest_capsule_classifier.joblib")
    vectorizer = joblib.load("modules/capsule_classifier/tfidf_vectorizer.joblib")

    X_new = vectorizer.transform([utterance])

    return  clf.predict(X_new)