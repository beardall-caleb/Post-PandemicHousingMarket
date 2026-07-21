from data_cleaning import (
    load_and_clean_data,
    check_cleaned_dataset,
    create_utah_dataframe
)

from analysis import (
    calculate_year_over_year_change,
    find_highest_growth_rate,
    compare_growth_periods
)

def main():
    file_path = "data/ZHVI.csv"
    
    housing_df = load_and_clean_data(file_path)
    check_cleaned_dataset(housing_df)

    utah_df = create_utah_dataframe(housing_df)

    utah_analysis_df = calculate_year_over_year_change(utah_df)

    print("\nUtah year-over-year analysis:")
    print(utah_analysis_df.head(15))

    highest_growth = find_highest_growth_rate(utah_analysis_df)

    print("\nHighest year-over-year growth rate:")
    print(f"Date: {highest_growth['Date']:%B %Y}")
    print(f"Home value: ${highest_growth['HomeValue']:,.2f}")
    print(f"YoY change: {highest_growth['YoYPercentChange']:.2f}%")

    highest_pre, highest_post = compare_growth_periods(utah_analysis_df) # Unpack the tuple

    print("\nHighest pre-pandemic growth:")
    print(f"Date: {highest_pre['Date']:%B %Y}")
    print(f"YoY change: {highest_pre['YoYPercentChange']:.2f}%")

    print("\nHighest post-pandemic growth:")
    print(f"Date: {highest_post['Date']:%B %Y}")
    print(f"YoY change: {highest_post['YoYPercentChange']:.2f}%")


if __name__ == "__main__":
    main()