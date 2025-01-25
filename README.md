
# Crypto$cope - Cryptocurrency Trend Tracker on Twitter (X)

This Python script uses Selenium to scrape Twitter (X) for trending cryptocurrency mentions. It tracks the engagement (likes, comments, retweets, and poll votes) of tweets containing cashtags (e.g., `$BTC`, `$ETH`) and categorizes them into **large-cap cryptocurrencies** and **small-cap/meme coins**. The script then ranks the top 5 cryptocurrencies in each category based on total engagement.

---

## Features

- **Login to Twitter (X)**: Automatically logs into Twitter using provided credentials.
- **Scrape Tweets**: Searches for tweets related to "top large crypto gainers" and "top meme coins."
- **Engagement Tracking**: Extracts likes, comments, retweets, and poll votes for each tweet.
- **Cashtag Extraction**: Identifies and processes cashtags (e.g., `$BTC`, `$DOGE`) in tweets.
- **Ranking**: Ranks the top 5 large-cap cryptocurrencies and meme coins based on engagement.
- **Automated Updates**: Runs every 15 minutes to provide updated trends.

---

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/).
2. **Selenium**: Install Selenium using pip:
   ```bash
   pip install selenium
   ```
3. **Safari WebDriver**: Ensure Safari's WebDriver is enabled. Follow these steps:
   - Open Safari.
   - Go to `Preferences` > `Advanced` and enable "Show Develop menu in menu bar."
   - From the `Develop` menu, select "Allow Remote Automation."

---

## How It Works

1. **Login**:
   - The script logs into Twitter (X) using the provided credentials.

2. **Scrape Tweets**:
   - Searches for tweets containing "top large crypto gainers" and "top meme coins."
   - Scrolls through the results to load more tweets.

3. **Process Tweets**:
   - Extracts cashtags (e.g., `$BTC`, `$DOGE`) from each tweet.
   - Calculates total engagement (likes + comments + retweets + poll votes) for each cashtag.

4. **Rank Cryptocurrencies**:
   - Ranks the top 5 large-cap cryptocurrencies and meme coins based on engagement.

5. **Output Results**:
   - Prints the top 5 cryptocurrencies in each category along with their engagement metrics.
   - Updates every 15 minutes.

---

## Example Output

```plaintext
=== Top 5 Large Cap Cryptocurrencies ===
$BTC: 1234 engagements
$ETH: 987 engagements
$BNB: 765 engagements
$SOL: 654 engagements
$XRP: 543 engagements

=== Top 5 Trending Meme Coins ===
$DOGE: 432 engagements
$SHIB: 321 engagements
$PEPE: 210 engagements
$FLOKI: 109 engagements
$BONK: 98 engagements

Last updated: 2025-01-25 15:21:24
```

---

## Customization

- **Add/Remove Cryptocurrencies**:
  - Update the `large_caps` set in the `CryptoTrendTracker` class to include or exclude specific cryptocurrencies.
  ```python
  self.large_caps = {'BTC', 'ETH', 'BNB', 'SOL', 'XRP', 'ADA', 'DOGE'}
  ```

- **Change Search Queries**:
  - Modify the search queries in the `get_trending_crypto` method to track different trends.
  ```python
  self.driver.get("https://twitter.com/search?q=top%20large%20crypto%20gainers&src=typed_query&f=live")
  ```

- **Adjust Update Interval**:
  - Change the `time.sleep(900)` line in the `main` function to update more or less frequently.
  ```python
  time.sleep(600)  # Update every 10 minutes
  ```

---

## Limitations

- **Twitter Rate Limits**: Twitter may block your IP or account if the script makes too many requests in a short period.
- **Two Factor Authentication**: Depending on your account settings, Twitter may require 2FA, to use turn it off.
- **Dynamic UI Changes**: Twitter frequently updates its UI, which may break the script. You may need to update the element locators periodically.
- **CAPTCHA**: If Twitter detects automated activity, it may prompt a CAPTCHA, which the script cannot handle.

---

