import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Step 1: Load the dataset
file_path = r"C:\Users\prana\Downloads\New folder\data.xlsx" 
data = pd.read_excel(file_path)

print("Original Data with Missing Values:\n", data)

# Step 2: Handle missing numerical values (replace with mean)
num_imputer = SimpleImputer(strategy="mean")  # Impute with the mean for numerical columns
numeric_columns = data.select_dtypes(include=[np.number]).columns

if not numeric_columns.empty:
    data[numeric_columns] = num_imputer.fit_transform(data[numeric_columns])
    print("\nNumerical Columns After Imputation:\n", data[numeric_columns])

# Step 3: Handle missing categorical values (replace with most frequent)
cat_imputer = SimpleImputer(strategy="most_frequent")  # Impute with most frequent value
categorical_columns = data.select_dtypes(include=["object"]).columns

if not categorical_columns.empty:
    data[categorical_columns] = cat_imputer.fit_transform(data[categorical_columns])
    print("\nCategorical Columns After Imputation:\n", data[categorical_columns])

# Step 4: Consolidate "Name_Person" columns (if applicable)
name_person_columns = [col for col in data.columns if col.startswith("Name_Person")]
if name_person_columns:
    # Create a single column to represent the "Name_Person" value
    data["Name_Person"] = data[name_person_columns].idxmax(axis=1).str.replace("Name_Person_", "")
    # Drop the individual one-hot encoded columns
    data = data.drop(columns=name_person_columns)

print("\nData after consolidating 'Name_Person' columns:\n", data)

# Step 5: Save the processed dataset to a new CSV file
data.to_csv("processed_data.csv", index=False)
print("\nProcessed data saved to 'processed_data.csv'.")
