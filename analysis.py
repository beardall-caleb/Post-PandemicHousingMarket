import pandas as pd


def calculate_year_over_year_change(utah_df):
    """Calculate Utah's year-over-year percentage change."""

    analyzed_df = utah_df.copy()

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