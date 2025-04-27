import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import modules.utils.constants as constants
from pathlib import Path

def train_all_function_classifier():
    print ("\n"+"="*25+" [STEP 2] "+"="*25)
    print(f"⏳ Training Function Classifier models...")
    for capsule in constants.SUPPORTED_CAPSULES:
        print(f"⏳ Training Function Classifier model for {capsule.title()} capsule...")

        try:
            train_function_classifier(capsule)
            print(f"✅ The Function Classifier model for {capsule.title()} capsule has been trained successfully!")
        except:
            print(f"❌ Something went wrong while training the Function Classifier model for {capsule.title()} capsule.")
            raise
    
    print(f"\n✅ All the Function Classifier models have been trained successfully!")

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
    clf_path = Path(f"modules/function_classifier/stiles_{capsule}")
    vectorizer_path = Path(f"modules/function_classifier/stiles_{capsule}")

    clf_path.mkdir(parents=True, exist_ok=True)
    vectorizer_path.mkdir(parents=True, exist_ok=True)

    joblib.dump(clf, f"{clf_path}/{capsule}_random_forest_function_classifier.joblib")
    joblib.dump(vectorizer, f"{vectorizer_path}/{capsule}_tfidf_vectorizer.joblib")