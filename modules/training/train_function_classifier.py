import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

SUPPORTED_CAPSULES = ['reminder','calendar','chat']

def train_all_function_classifier():
    for capsule in SUPPORTED_CAPSULES:
        print(f"\nTraining {capsule.title()} capsule...")

        try:
            train_function_classifier(capsule)
            print(f"✅ The {capsule.title()} capsule has been trained successfully!")
        except:
            print("❌ Something went wrong in the training process.")

def train_function_classifier(capsule):
    df = pd.read_csv(f'modules/training/data/{capsule}_function_classifier_data.csv')
    print(df.head())

    utterances = df['utterance'].values
    functions = df['function'].values

    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(utterances)
    y = functions

    
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
    joblib.dump(clf, f"modules/function_classifier/stiles_{capsule}/{capsule}_random_forest_function_classifier.joblib")
    joblib.dump(vectorizer, f"modules/function_classifier/stiles_{capsule}/{capsule}_tfidf_vectorizer.joblib")

if __name__ == "__main__":
    train_all_function_classifier()