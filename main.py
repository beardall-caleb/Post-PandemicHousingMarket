from data_cleaning import (
    load_and_clean_data,
    check_cleaned_dataset,
    create_utah_dataframe
)

from analysis import (
    calculate_year_over_year_change,
    find_highest_growth_rate,
    compare_growth_periods,
    get_recent_growth_data,
    compare_recent_growth_rates,
    calculate_recent_yearly_averages
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

    highest_pre, highest_post = compare_growth_periods(utah_analysis_df)

    print("\nHighest pre-pandemic growth:")
    print(f"Date: {highest_pre['Date']:%B %Y}")
    print(f"YoY change: {highest_pre['YoYPercentChange']:.2f}%")

    print("\nHighest post-pandemic growth:")
    print(f"Date: {highest_post['Date']:%B %Y}")
    print(f"YoY change: {highest_post['YoYPercentChange']:.2f}%")

    recent_growth_df = get_recent_growth_data(utah_analysis_df)

    print("\nUtah's most recent 36 months:")
    print(recent_growth_df[
        ["Date", "HomeValue", "YoYPercentChange"]
    ].to_string(index=False))

    current, one_year_ago, two_years_ago = (
        compare_recent_growth_rates(recent_growth_df)
    )

    print("\nRecent growth-rate comparison:")
    print(
        f"Current rate "
        f"({current['Date']:%B %Y}): "
        f"{current['YoYPercentChange']:.2f}%"
    )

    print(
        f"One year earlier "
        f"({one_year_ago['Date']:%B %Y}): "
        f"{one_year_ago['YoYPercentChange']:.2f}%"
    )

    print(
        f"Two years earlier "
        f"({two_years_ago['Date']:%B %Y}): "
        f"{two_years_ago['YoYPercentChange']:.2f}%"
    )

    yearly_averages = calculate_recent_yearly_averages(recent_growth_df)
    
    print("\nAverage YoY growth rate by year:")
    print(yearly_averages)


if __name__ == "__main__":
    main()