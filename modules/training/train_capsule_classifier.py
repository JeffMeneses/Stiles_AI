import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

def train_capsule_classifier():
    print ("\n========== [STEP 1] ========== ")
    print(f"⏳ Training Capsule Classifier model...")
    df = pd.read_csv('modules/training/data/capsule_classifier_data.csv')
    print(df.head())

    utterances = df['utterance'].values
    capsules = df['capsule'].values

    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(utterances)
    y = capsules

    
    # Split data into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Predict on test data
    y_pred = clf.predict(X_test)

    # Print performance metrics
    print(classification_report(y_test, y_pred))

    # Save the model and vectorizer
    joblib.dump(clf, "modules/capsule_classifier/random_forest_capsule_classifier.joblib")
    joblib.dump(vectorizer, "modules/capsule_classifier/tfidf_vectorizer.joblib")
    print(f"\n✅ The Capsule Classifier model has been trained successfully!")