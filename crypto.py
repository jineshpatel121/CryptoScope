from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
from collections import Counter

class CryptoTrendTracker:
    def __init__(self):
        self.driver = webdriver.Safari()
        self.wait = WebDriverWait(self.driver, 20)
        self.large_caps = {'BTC', 'ETH', 'BNB', 'SOL', 'XRP', 'ADA', 'DOGE'}
        
    def login(self, username, password):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)  # Wait for page load

        try:
            # Enter username
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "text")))
            username_field.send_keys(username)
            print("Username entered successfully.")

            # Click next button
            time.sleep(3)
            next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]")))
            next_button.click()
            print("Clicked 'Next' button.")
            time.sleep(2)  # Wait for the password field to load

            # Wait for the password field to appear
            try:
                password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
                print("Password field found.")
            except Exception as e:
                print("Password field not found. Printing page source for debugging:")
                print(self.driver.page_source)
                raise e

            # Enter password
            password_field.send_keys(password)
            print("Password entered successfully.")

            # Submit login form
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Log in')]")))
            login_button.click()
            print("Clicked 'Log in' button.")
            time.sleep(5)  # Wait for login to complete

            # Check if login was successful
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/home']")))
                print("Login successful!")
            except:
                print("Login might have failed. Check for errors on the page.")
        except Exception as e:
            print(f"Error during login: {e}")
            # Print the page source for debugging
            print("Page source for debugging:")
            print(self.driver.page_source)
        
    def get_trending_crypto(self, hours_back=24):
        coin_mentions = Counter()
        meme_coin_mentions = Counter()
        
        # Search for top large crypto gainers in the Latest section
        self.driver.get("https://twitter.com/search?q=top%20large%20crypto%20gainers&src=typed_query&f=live")
        time.sleep(5)  # Wait for page load
        
        # Scroll to load more tweets
        for _ in range(5):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        try:
            tweets = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[@data-testid='tweet']")))
            print(f"Number of tweets found for large caps: {len(tweets)}")
            
            for tweet in tweets[:100]:  # Process first 100 tweets
                try:
                    text = tweet.find_element(By.XPATH, ".//div[@lang='en']").text
                    print(f"Tweet text: {text}")  # Debugging
                    
                    # Extract cashtags
                    cashtags = {word.strip('$') for word in text.split() if word.startswith('$')}
                    print(f"Cashtags found: {cashtags}")  # Debugging
                    
                    # Extract engagement metrics
                    try:
                        likes = tweet.find_element(By.XPATH, ".//div[@data-testid='like']//span").text
                        likes = int(likes) if likes else 0
                    except:
                        likes = 0  # If likes are not found, assume 0
                    
                    try:
                        comments = tweet.find_element(By.XPATH, ".//div[@data-testid='reply']//span").text
                        comments = int(comments) if comments else 0
                    except:
                        comments = 0  # If comments are not found, assume 0
                    
                    try:
                        retweets = tweet.find_element(By.XPATH, ".//div[@data-testid='retweet']//span").text
                        retweets = int(retweets) if retweets else 0
                    except:
                        retweets = 0  # If retweets are not found, assume 0
                    
                    try:
                        poll_votes = tweet.find_element(By.XPATH, ".//div[@data-testid='poll']//span").text
                        poll_votes = int(poll_votes) if poll_votes else 0
                    except:
                        poll_votes = 0  # If poll is not found, assume 0
                    
                    # Calculate total engagement
                    total_engagement = likes + comments + retweets + poll_votes
                    print(f"Engagement: Likes={likes}, Comments={comments}, Retweets={retweets}, Poll Votes={poll_votes}, Total={total_engagement}")  # Debugging
                    
                    # Update mentions based on cashtags
                    for tag in cashtags:
                        if tag in self.large_caps:
                            coin_mentions[tag] += total_engagement
                        else:
                            meme_coin_mentions[tag] += total_engagement
                except Exception as e:
                    print(f"Error processing tweet: {e}")
        except Exception as e:
            print(f"Error finding tweets: {e}")
        
        # Search for top meme coins in the Latest section
        self.driver.get("https://twitter.com/search?q=top%20meme%20coins&src=typed_query&f=live")
        time.sleep(5)  # Wait for page load
        
        # Scroll to load more tweets
        for _ in range(5):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        try:
            tweets = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//article[@data-testid='tweet']")))
            print(f"Number of tweets found for meme coins: {len(tweets)}")
            
            for tweet in tweets[:100]:  # Process first 100 tweets
                try:
                    text = tweet.find_element(By.XPATH, ".//div[@lang='en']").text
                    print(f"Tweet text: {text}")  # Debugging
                    
                    # Extract cashtags
                    cashtags = {word.strip('$') for word in text.split() if word.startswith('$')}
                    print(f"Cashtags found: {cashtags}")  # Debugging
                    
                    # Extract engagement metrics
                    try:
                        likes = tweet.find_element(By.XPATH, ".//div[@data-testid='like']//span").text
                        likes = int(likes) if likes else 0
                    except:
                        likes = 0  # If likes are not found, assume 0
                    
                    try:
                        comments = tweet.find_element(By.XPATH, ".//div[@data-testid='reply']//span").text
                        comments = int(comments) if comments else 0
                    except:
                        comments = 0  # If comments are not found, assume 0
                    
                    try:
                        retweets = tweet.find_element(By.XPATH, ".//div[@data-testid='retweet']//span").text
                        retweets = int(retweets) if retweets else 0
                    except:
                        retweets = 0  # If retweets are not found, assume 0
                    
                    try:
                        poll_votes = tweet.find_element(By.XPATH, ".//div[@data-testid='poll']//span").text
                        poll_votes = int(poll_votes) if poll_votes else 0
                    except:
                        poll_votes = 0  # If poll is not found, assume 0
                    
                    # Calculate total engagement
                    total_engagement = likes + comments + retweets + poll_votes
                    print(f"Engagement: Likes={likes}, Comments={comments}, Retweets={retweets}, Poll Votes={poll_votes}, Total={total_engagement}")  # Debugging
                    
                    # Update mentions based on cashtags
                    for tag in cashtags:
                        meme_coin_mentions[tag] += total_engagement
                except Exception as e:
                    print(f"Error processing tweet: {e}")
        except Exception as e:
            print(f"Error finding tweets: {e}")
                    
        return {
            'large_caps': coin_mentions.most_common(5),
            'meme_coins': meme_coin_mentions.most_common(5)
        }
    def close(self):
        self.driver.quit()

def main():
    tracker = CryptoTrendTracker()
    try:
        # Replace with your Twitter credentials
        USERNAME = " "
        PASSWORD = " "
        
        tracker.login(USERNAME, PASSWORD)
        
        while True:
            trends = tracker.get_trending_crypto()
            
            print("\n=== Top 5 Large Cap Cryptocurrencies ===")
            for coin, mentions in trends['large_caps']:
                print(f"${coin}: {mentions} engagements")
                
            print("\n=== Top 5 Trending Meme Coins ===")
            for coin, mentions in trends['meme_coins']:
                print(f"${coin}: {mentions} engagements")
            
            print(f"\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(900)  # Update every 15 minutes
            
    except KeyboardInterrupt:
        print("\nStopping tracker...")
    finally:
        tracker.close()

if __name__ == "__main__":
    main()
