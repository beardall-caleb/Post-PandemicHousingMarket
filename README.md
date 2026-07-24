# Post-PandemicHousingMarket

Like many people in their twenties and thirties who live in Utah, I am a renter. This is frustrating because I would prefer for my monthly housing payments to help me build equity in a home rather than leave my wallet, never to be seen again.

Utah’s housing market is frequently on my mind, and I find myself asking the same questions every year: Will this be the year the housing market corrects itself? Should I purchase a home even if the monthly payment would consume most of my paycheck so that I can enter the market and benefit from future appreciation? Or would it be better to continue saving as much as possible so that I am prepared to purchase a home if prices fall?

Everyone seems to have a strong opinion about the housing market, but no one can know with certainty when the ideal time to buy will be.

This uncertainty led me to create this application. Rather than marking a major financial decision based solely on the opinions of others or the fear of missing an ideal opportunity, I decided to analyze Utah housing-market data for myself. The application is designed to answer the following questions:

- How does Utah’s post-pandemic rate of change compare with previous years? Specifically, have Utah home values increased faster than at any other point since 2000?
- Over the past two to three years, has Utah’s rate of change in home values accelerated, slowed, or remained relatively consistent?
- How does Utah’s rate of change in home values since the COVID-19 pandemic compare with the national rate of change?

To investigate those questions, I will use the Zillow Home Value Index dataset provided on Kaggle by Rob Mulla. The dataset contains monthly Zillow Home Value Index values for all 50 states and the District of Columbia from January 2020 through May 2026.

The Zillow Home Value Index (ZHVI) is a measure of the typical home value within a geographic area. Rather than measuring only the prices of homes sold during a particular month, ZHVI uses Zillow’s property-level estimates.

The dataset is mostly complete, although several states are missing one or more monthly values. Five states are missing a single monthly value, and four states are missing 27 or more monthly values. Because of these gaps, the dataset must be inspected and cleaned before it can be analyzed. Fortunately, the Utah column is not missing any values.

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

- Question 1: How does Utah’s post-pandemic rate of change compare with previous years? Specifically, have Utah home values increased faster than at any other point since 2000?
  - Answer: Utah’s largest year-over-year increase in home values occurred in August 2021, following the initial COVID-19 outbreak in March 2020. In August 2021, Utah home values were 27.96% higher than they had been in August 2020.

    This rate was 10.62 percentage points higher than Utah’s largest pre-pandemic year-over-year increase, which occurred in May 2007. Therefore, according to this dataset, Utah home values increased faster during the post-pandemic period than at any earlier point since 2000.

- Question 2: Over the past two to three years, has Utah’s rate of change in home values accelerated, slowed, or remained relatively consistent?
  - Answer: Utah’s average monthly year-over-year rate of change was -3.96% in 2023, meaning that homes values were generally lower than they had been during the same months in 2022.

    Home values began increasing year over year again 2024. The average year-over-year growth rate was 1.48% in 2024, followed by 1.94% in 2025, and 1.80% during the available months of 2026.

    Across those three years, the average year-over-year growth rate was approximately 1.74%. Because the annual averages remained within a relatively narrow range, I would conclude that Utah’s rate of home-value growth has remained relatively consistent since it became positive again in 2024.

# Development Environment

{Describe the tools that you used to develop the software}

{Describe the programming language that you used and any libraries.}

# Useful Websites

- [Bro Code | Learn Pandas in 1 hour! 🐼](https://www.youtube.com/watch?v=VXtjG_GzO7Q)
- [pandas | Getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [Python for Data Analysis by Wes McKinney](https://wesmckinney.com/book/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Item 1
- Item 2
- Item 3
