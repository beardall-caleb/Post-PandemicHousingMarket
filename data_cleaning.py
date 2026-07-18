import pandas as pd


def load_and_clean_data(file_path):
    """Load and clean the Zillow home-value dataset."""

    # Load the CSV file.
    housing_df = pd.read_csv(file_path)

    # Give the date column a meaningful name.
    housing_df = housing_df.rename(
        columns={"Unnamed: 0": "Date"}
    )

    # Convert the date column from text to datetime values.
    housing_df["Date"] = pd.to_datetime(
        housing_df["Date"]
    )

    # Sort the records chronologically.
    housing_df = (
        housing_df
        .sort_values("Date")
        .reset_index(drop=True)
    )

    # Identify the state and territory columns.
    state_columns = housing_df.columns.drop("Date")

    # Ensure all home-value columns contain numeric data.
    housing_df[state_columns] = housing_df[
        state_columns
    ].apply(
        pd.to_numeric,
        errors="coerce"
    )

    return housing_df


def check_cleaned_dataset(housing_df):
    """Print summary information about the cleaned dataset."""

    print("DataFrame dimensions:")
    print(housing_df.shape)

    print("\nDate range:")
    print(
        housing_df["Date"].min(),
        "through",
        housing_df["Date"].max()
    )

    print(
        f"\nDuplicate rows: "
        f"{housing_df.duplicated().sum()}"
    )

    print(
        f"Duplicate dates: "
        f"{housing_df['Date'].duplicated().sum()}"
    )

    print("\nColumns with missing values:")
    missing_values = housing_df.isna().sum()
    print(missing_values[missing_values > 0])


def create_utah_dataframe(housing_df):
    """Create a DataFrame containing Utah home values."""

    # Create a separate Utah DataFrame.
    utah_df = (
        housing_df[["Date", "Utah"]]
        .rename(columns={"Utah": "HomeValue"})
        .copy()
    )

    return utah_df