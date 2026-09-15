import pandas as pd

def process_data():
    print("1. Loading raw dataset...")
    df = pd.read_csv("raw_jobs_dataset.csv")
    print(f"Total rows loaded: {len(df)}")

    
    df = df.drop_duplicates()


    df = df.dropna()

    
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

    
    df.to_csv("cleaned_jobs_dataset.csv", index=False)
    print("Success! 'cleaned_jobs_dataset.csv' created.")

    
    df["Salary Category"] = pd.qcut(df["Salary"], q=3, labels=["Low", "Medium", "High"])
    
    
    df.to_csv("processed_jobs_dataset.csv", index=False)
    print("Success! 'processed_jobs_dataset.csv' created.")

if __name__ == "__main__":
    process_data()