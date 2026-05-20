import os
from src.data_preprocessing import load_and_clean_data
from src.train_model import train_model
from src.config import DATA_RAW, DATA_PROCESSED

def run_pipeline():
    # Ensure folders exist
    os.makedirs(os.path.dirname(DATA_PROCESSED), exist_ok=True)
    os.makedirs("models", exist_ok=True)

    # Step 1: Load & clean
    df = load_and_clean_data(DATA_RAW)
    df.to_csv(DATA_PROCESSED, index=False)
    print("✅ Data cleaned & saved!")

    # Step 2: Train model
    train_model()

if __name__ == "__main__":
    run_pipeline()