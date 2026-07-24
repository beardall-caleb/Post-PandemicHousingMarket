from data_cleaning import (
    load_and_clean_data,
    check_cleaned_dataset,
    create_utah_dataframe,
    create_utah_and_state_average_dataframe
)

from analysis import (
    calculate_year_over_year_change,
    find_highest_growth_rate,
    compare_growth_periods,
    get_recent_growth_data,
    compare_recent_growth_rates,
    calculate_recent_yearly_averages,
    calculate_comparison_growth_rates,
    get_post_pandemic_comparison,
    calculate_cumulative_growth
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

    comparison_df = (
        create_utah_and_state_average_dataframe(housing_df)
    )

    comparison_analysis_df = (
        calculate_comparison_growth_rates(comparison_df)
    )

    post_pandemic_comparison_df = (
        get_post_pandemic_comparison(comparison_analysis_df)
    )

    cumulative_comparison_df = (
        calculate_cumulative_growth(post_pandemic_comparison_df)
    )

    initial_comparison = cumulative_comparison_df.iloc[0]
    latest_comparison = cumulative_comparison_df.iloc[-1]

    print("\nPost-pandemic cumulative comparison:")

    print(f"\nInitial values ({initial_comparison['Date']:%B %Y}):")
    print(f"Utah home value: ${initial_comparison['UtahHomeValue']:,.2f}")
    print(f"Average state home value: ${initial_comparison['StateAverage']:,.2f}")

    print(f"\nCurrent values ({latest_comparison['Date']:%B %Y}):")
    print(f"Utah home value: ${latest_comparison['UtahHomeValue']:,.2f}")
    print(f"Average state home value: ${latest_comparison['StateAverage']:,.2f}")

    print("\nCumulative change:")
    print(f"Utah: {latest_comparison['UtahCumulativePercentChange']:.2f}%")
    print(
        f"Average state value: "
        f"{latest_comparison['StateAverageCumulativePercentChange']:.2f}%"
    )

    difference = (
        latest_comparison["UtahCumulativePercentChange"]
        - latest_comparison[
            "StateAverageCumulativePercentChange"
        ]
    )

    print(f"Difference: {difference:.2f} percentage points")


if __name__ == "__main__":
    main()