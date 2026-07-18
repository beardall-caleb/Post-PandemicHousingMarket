from data_cleaning import (
    load_and_clean_data,
    check_cleaned_dataset,
    create_utah_dataframe
)


def main():
    housing_df = load_and_clean_data("data/ZHVI.csv")
    check_cleaned_dataset(housing_df)

    utah_df = create_utah_dataframe(housing_df)
    print(utah_df.head())


if __name__ == "__main__":
    main()