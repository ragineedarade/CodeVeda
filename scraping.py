import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape data


def scrape_website(url, element, class_name):
    try:
        # Fetch the web page content
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data
        data_list = []
        elements = soup.find_all(element, class_=class_name)

        for item in elements:
            data_list.append(item.get_text(strip=True))

        return data_list

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# Function to save data to CSV


def save_to_csv(data, filename):
    df = pd.DataFrame(data, columns=['Extracted Data'])
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Data saved to {data}")


# Example usage
url = "https://google.com"  # Replace with the target website
element = "h2"  # Replace with the HTML tag (e.g., h2 for headlines)
class_name = "headline-class"  # Replace with the actual class name

scraped_data = scrape_website(url, element, class_name)

if scraped_data:
    save_to_csv(scraped_data, "C:/Users/ASUS/Downloads/codeveda/data.csv")
else:
    print("No data found or an error occurred.")
