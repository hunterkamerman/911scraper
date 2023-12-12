from bs4 import BeautifulSoup
import requests

def scrape_craigslist(url, max_price, max_miles, desired_features):
    print(f"Scraping: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the Porsche 911 listings
    listings = soup.find_all("li", class_="result-row")

    # Filter and extract data for each listing
    for listing in listings:
        title_element = listing.find("a", class_="result-title hdrlnk")
        price_element = listing.find("span", class_="result-price")
        location_element = listing.find("span", class_="result-hood")
        image_element = listing.find("img")
        details_element = listing.find("p", class_="result-info")

        # Check if all required elements are present
        if title_element and price_element and location_element and image_element and details_element:
            title = title_element.text
            price = price_element.text
            location = location_element.text
            image_url = image_element.get("src")
            details = details_element.text

            # Check if the listing meets the filters
            if float(price.replace("$", "")) <= max_price and int(details.split()[0].replace(",", "")) <= max_miles:
                for feature in desired_features:
                    if feature not in details.lower():
                        break
                else:
                    # Print the data for each filtered listing
                    print(f"Title: {title}")
                    print(f"Price: {price}")
                    print(f"Location: {location}")
                    print(f"Image URL: {image_url}")
                    print("-" * 20)

# Define the craigslist URL
base_url = "https://www.craigslist.org/search/cto?query=porsche+911&sort=priceasc&searchNearby=1"

# Define the desired locations
locations = ["losangeles", "nyc", "miami"]

# Define the filters
max_price = 60000
max_miles = 100000
desired_features = ["manual transmission"]

# Iterate through each location
for location in locations:
    # Build the complete URL
    url = f"{base_url}&location={location}"
  
    # Scrape and process listings
    scrape_craigslist(url, max_price, max_miles, desired_features)
