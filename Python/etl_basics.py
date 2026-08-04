import pandas as pd


def extract(file_path):
    return pd.read_csv(file_path)


def transform(df):
    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove rows containing missing values
    df = df.dropna()

    return df


def load(df, output_path):
    df.to_csv(output_path, index=False)


try:
    data = extract("patients.csv")

    cleaned_data = transform(data)

    load(cleaned_data, "cleaned_patients.csv")

    print("ETL pipeline completed successfully.")

except Exception as error:
    print("Pipeline failed:", error)