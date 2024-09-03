# The Boys Sentiment Analysis

## Project Overview
This project performs sentiment analysis on user reviews of the TV series "The Boys." The dataset contains ratings and review titles, which have been analyzed to determine the overall sentiment of viewers. Additionally, a custom Python script was developed to scrape reviews from various sources.

## Features
- **Sentiment Analysis:** Analyze and categorize user reviews as positive or negative based on their ratings.
- **Data Visualization:** Generate visualizations to explore the distribution of ratings and review lengths.
- **Web Scraping:** A custom Python script (`review_scrapping.py`) is included to extract reviews from web pages.

## Getting Started

### Prerequisites
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- BeautifulSoup (for web scraping)
- Requests (for web scraping)
- Selenium

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/YourUsername/TheBoysSentimentAnalysis.git
    cd TheBoysSentimentAnalysis
    ```
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. **Run the Sentiment Analysis:**
    - Open `sentiment_analysis.ipynb` in Jupyter Notebook or any Python IDE.
    - Run the cells to load the dataset, clean the data, and perform the sentiment analysis.

2. **Scrape New Reviews:**
    - Use the `review_scrapping.py` script to scrape additional reviews.
    - Example usage:
    ```bash
    python review_scrapping.py
    ```
    - The script will save the scraped reviews in a CSV file.

### Results
The sentiment analysis results show the distribution of positive and negative reviews for "The Boys." Detailed visualizations provide insights into the length of reviews and how ratings correlate with sentiment.

### Contributing
Contributions are welcome! Please fork the repository and create a pull request to contribute.
