# Zillow-Scraper
Scrape US Real State Data with this Scraper

## Overview

This Python script scrapes data from Zillow.com using the Zillow API. It extracts property details such as price, location, and more.

![script_example](https://github.com/acbouzas/Zillow-Scraper/blob/main/images/zillowscreenshot.png)
![data_example](https://github.com/acbouzas/Zillow-Scraper/blob/main/images/Screenshot%20from%202023-09-01%2014-23-32.png)

## Usage

1. Clone the repository to your local machine
2. Navigate to the project directory
3. Open the script file `zillowscraper.py` in a text editor.
4. Customize the script:

   - You may want to modify the search parameters in the `get_zillow_data` function to specify your desired location and search criteria.
   - Ensure that the `headers` variable contains the necessary headers and cookies for accessing the Zillow API.
5. Run the script
6. The script will fetch data from Zillow and save it as a CSV file named `scraped_data.csv`.

## Data Format

The CSV file `scraped_data.csv` will contain the following columns:

- `price`: The property price.
- `latitude`: The latitude of the property's location.
- `longitude`: The longitude of the property's location.
- `homeStatus`: The status of the home (e.g., for sale, sold, etc.).
- `zestimate`: The Zillow estimate (if available).
- `rentZestimate`: The Zillow rent estimate (if available).
- `detailUrl`: The URL to the property's details on Zillow.
- `address`: The address of the property.

---

Good luck with your Zillow scraping! If you have any questions or need further assistance, please don't hesitate to ask.
