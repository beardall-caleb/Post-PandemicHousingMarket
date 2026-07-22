import pandas as pd


def calculate_year_over_year_change(utah_df):
    """Calculate Utah's year-over-year percentage change."""

    analyzed_df = utah_df.copy()

    # Compare each monthly value with the same month one year earlier.
    analyzed_df["YoYPercentChange"] = (
        analyzed_df["HomeValue"]
        .pct_change(periods=12)
        .mul(100)
    )

    return analyzed_df


def find_highest_growth_rate(utah_analysis_df):
    """Return the row with Utah's highest YoY growth rate."""

    # Create a DataFrame containing only rows where
    # YoYPercentChange has a value.
    valid_rows = utah_analysis_df.dropna(
        subset=["YoYPercentChange"]
    )

    # Find the index of the largest growth rate,
    # then retrieve the complete row at that index.
    highest_growth_row = valid_rows.loc[
        valid_rows["YoYPercentChange"].idxmax()
    ]

    return highest_growth_row


def compare_growth_periods(
    utah_analysis_df,
    pandemic_start="2020-03-01"
):
    """
    Return the highest YoY growth rows before and since
    the beginning of the COVID-19 pandemic.
    """

    # Convert the string to a timestamp.
    pandemic_start = pd.Timestamp(pandemic_start)

    valid_rows = utah_analysis_df.dropna(
        subset=["YoYPercentChange"]
    )

    # Select rows occurring before March 2020.
    pre_pandemic_df = valid_rows[
        valid_rows["Date"] < pandemic_start
    ]

    # Select rows occurring on or after March 2020.
    post_pandemic_df = valid_rows[
        valid_rows["Date"] >= pandemic_start
    ]

    # Find the row with the highest growth rate
    # in each period.
    highest_pre_pandemic = pre_pandemic_df.loc[
        pre_pandemic_df["YoYPercentChange"].idxmax()
    ]

    highest_post_pandemic = post_pandemic_df.loc[
        post_pandemic_df["YoYPercentChange"].idxmax()
    ]

    return (highest_pre_pandemic, highest_post_pandemic)


def get_recent_growth_data(
    utah_analysis_df,
    months=36
):
    """Return Utah's most recent months of valid YoY data."""

    valid_rows = utah_analysis_df.dropna(
        subset=["YoYPercentChange"]
    )

    recent_growth_df = (
        valid_rows
        .sort_values("Date")
        .tail(months)
        .copy()
    )

    return recent_growth_df


def compare_recent_growth_rates(recent_growth_df):
    """Return current and earlier YoY growth data."""

    # Comparing the latest month with the same month two years
    # earlier requires at least 25 months.
    if len(recent_growth_df) < 25:
        raise ValueError(
            "At least 25 months are required "
            "for a two-year comparision."
        )
    
    # Select the latest available month, the same month one year
    # earlier, and the same month two years earlier.
    current_row = recent_growth_df.iloc[-1]
    one_year_ago_row = recent_growth_df.iloc[-13]
    two_years_ago_row = recent_growth_df.iloc[-25]

    return (
        current_row,
        one_year_ago_row,
        two_years_ago_row
    )


def calculate_recent_yearly_averages(
        recent_growth_df
):
    """Calculate the average YoY growth rate by year."""

    yearly_data = recent_growth_df.copy()

    # Add a Year column using the Date column.
    yearly_data["Year"] = (
        yearly_data["Date"].dt.year
    )

    # Group months by calendar year and calculate
    # the average YoY growth rate for each year.
    yearly_averages = (
        yearly_data
        .groupby("Year")["YoYPercentChange"]
        .mean()
        .round(2)
    )

    return yearly_averages