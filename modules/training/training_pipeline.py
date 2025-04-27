import modules.training.train_capsule_classifier as train_capsule_classifier
import modules.training.train_function_classifier as train_function_classifier
import modules.training.train_ner as train_ner

def train_all():
    print("🚧 [STARTING TRAINING PIPELINE]")
    try:
        train_capsule_classifier.train_capsule_classifier()
        train_function_classifier.train_all_function_classifier()
        train_ner.train_all_ner()
        print("🫡 [THE TRAINING PIPELINE HAS BEEN SUCCESSFULLY COMPLETED!]")
    except:
        print("❌ [SOMETHING WENT WRONG IN THE TRAINING PIPELINE. PLEASE CHECK LOGS.")

if __name__ == "__main__":
    train_all()