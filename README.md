# Egg Price Prediction - A Regression Analysis (Seattle U - CPSC 5071 DSA Project)

### Members: Sung Ahn, Dan Nguyen, Aakash Krishna, Chris Yang

## I. Problem Statement
In recent times, the price of eggs has increased significantly in the U.S, causing concern among many consumers. This price hike may be attributed to various factors, extreme weather events, disease outbreaks such as avian flu, and possible human manufacturing factors such as the pandemic. The ability to predict potential changes in egg prices would empower individuals to better manage their personal finances by allowing them to plan and prioritize their spending in response to these factors, thereby reducing the stress of unexpected expenses.

## II. Data Set
1. [Average price of eggs](https://www.bls.gov/charts/consumer-price-index/consumer-price-index-average-price-data.htm)
This dataset contains monthly average prices for eggs dating back to 1980. The data is in tabular format with and will serve as the target in the regression model.
2. [Natural Disaster Data](https://ourworldindata.org/natural-disasters#explore-data-on-natural-disasters)
This dataset includes information on natural disasters (e.g., hurricanes, floods, droughts) and their impacts, such as economic costs, fatalities, and affected regions. Natural disasters can disrupt supply chains, damage infrastructure, and reduce agricultural output, all of which may influence egg prices.
3. [Aviation Disease Data](https://www.cdc.gov/bird-flu/situation-summary/data-map-commercial.html)
This dataset tracks outbreaks of avian diseases (e.g., avian flu) that directly affect poultry populations. Disease outbreaks can lead to culling of infected birds, reduced egg production, and increased costs for farmers, all of which contribute to price fluctuations.
4. [Human Disease Data - US](https://data.cdc.gov/Foodborne-Waterborne-and-Related-Diseases/NORS/5xkq-dg7x/about_data)
This dataset includes information on human disease outbreaks other than the pandemic in the US that may indirectly impact egg prices. Local epidemics can disrupt labor availability, transportation, and consumer demand, all of which can affect the supply and cost of eggs.
5. [Human Disease Data - Global Pandemic](https://ourworldindata.org/covid-hospitalizations)
This dataset includes information on the Covid-19 pandemic that may indirectly impact egg prices. The pandemic had a tremendous effect on labor availability, transportation, and consumer demand, all of which can affect the supply and cost of eggs.
6. [Weather Temperature Data](https://open-meteo.com/en/docs/historical-weather-api)
This dataset provides historical weather data, including temperature, precipitation, and extreme weather events. Weather conditions can influence feed costs for poultry, transportation logistics, and overall agricultural productivity, which in turn affect egg prices.

## III. Algorithms and Technologies: Detail your approach, including variables, algorithms, and preliminary results.
- Data Warehousing/Storage: The raw data files (e.g., egg prices, natural disaster data, avian disease data, human disease data, and weather data) will be uploaded to S3 buckets. S3 provides scalable and secure storage for large datasets. The data from S3 will be loaded into Amazon Redshift which serves as our data warehousing solution. 
- Pre-processing: The pre-processing phase will involve cleaning, aligning, and transforming the data to ensure it is ready for analysis and modeling. This will be done using Python. 
Ensure the join factor (date) is in a consistent format (e.g., yyyy-mm) across all datasets. Create new features from existing data that may better explain variations in egg prices (Aggregate disaster-related costs or fatalities by month, create binary indicators for severity of disease outbreaks)
- EDA Results: See file


## IV.  Risks: Highlight uncertainties or challenges.
Storing and processing large datasets in AWS S3 and querying with Redshift may incur significant costs. We’ll use Redshift mainly for initial querying and do the rest in python.
Data on Avian Flu outbreaks in the US are not readily available for periods prior to 2020. We are considering using the number of cases detected in humans as the proxy for the impact of Avian Flu.

## V. Challenges: Specify the unique challenge aspect of your project.
Data: Some datasets (e.g., natural disaster, avian disease outbreaks) don’t occur every single month, so we need to figure out a way to create features better suited for these data.
Prices: Egg prices are influenced by a wide range of factors (e.g., weather, disease outbreaks, supply chain disruptions), many of which are interconnected. Isolating the impact of each factor is complex.

## VI. Plan for Completion: Outline steps, time estimates, and any remaining concerns.
- Finalize the EDA, merge datasets based on the related features to be used.
- Split the data into training and testing sets, build a baseline regression model (linear regression) and evaluate its performance, experiment with more advanced models (XGboost, DT, RF).
- Use cross-validation to assess model performance, evaluate features importance, etc.
- Finalize the best-performing model through accuracy, precision, sensitivity, etc and document its assumptions, limitations, and results. Create visualizations and summaries.
- Prepare the presentation outlining the methodology, results, and recommendations.

## VII. References: A list of references related to your problem(s).
1. Adjemian, Michael K., et al. "Factors affecting recent food price inflation in the United States." Applied Economic Perspectives and Policy 46.2 (2024): 648-676: Rising transportation/fuel cost, russia/ukraine war, fertilizer use/price increase, covid, and labor shortage leads to increase in all food prices in the US
Bakhtavoryan, Rafael, et al. “An Empirical Evaluation of Egg Demand in the United States: Journal of Agricultural and Applied Economics.” Cambridge Core, Cambridge University Press, 23 June 2021, www.cambridge.org/core/journals/journal-of-agricultural-and-applied-economics/article/an-empirical-evaluation-of-egg-demand-in-the-united-states/7864639C84815808DADFD607CCD583E7: Uses Exact Affine Ston Index (EASI) econometric model to estimate demand of eggs and studies the relationship between the change in price of eggs impacting the consumer demand and vice versa.
2. Brüssow, Harald. “The arrival of highly pathogenic avian influenza viruses in North America, ensuing epizootics in poultry and dairy farms and difficulties in scientific naming.” Microbial Biotechnology, vol. 17, no. 12, Dec. 2024, https://doi.org/10.1111/1751-7915.70062: Climate change facilitates the spread of diseases like the avian flu which leads to increased food prices like, eggs and dairy products
3. (Article) Muhammad, Andrew, Charles Martinez, and Abdelaziz Lawani. "Why are eggs so expensive? Understanding the recent spike in egg prices." Choices 38.2 (2023).: While other factors, such as tariffs, climate change, wars, etc. also contribute to the increase in egg prices, Avian flu is the biggest factor.

