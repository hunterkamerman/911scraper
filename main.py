from bs4 import BeautifulSoup
import requests

def scrape_craigslist(url, max_price, max_miles, desired_features):
  """
  This function scrapes craigslist for Porsche 911 deals with specific filters.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  # Find all the Porsche 911 listings
  listings = soup.find_all("li", class_="result-row")

  # Filter and extract data for each listing
  for listing in listings:
    title = listing.find("a", class_="result-title hdrlnk").text
    price = listing.find("span", class_="result-price").text
    location = listing.find("span", class_="result-hood").text
    image_url = listing.find("img").get("src")
    details = listing.find("p", class_="result-info").text

    # Check if the listing meets the filters
    if float(price.replace("$", "")) <= max_price and int(details.split()[0]) <= max_miles:
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
locations = ["mnh", "losangeles", "nyc", "miami"]

# Define the filters
max_price = 60000
max_miles = 100000
desired_features = ["manual transmission", "sunroof"]

# Iterate through each location
for location in locations:
  # Build the complete URL
  url = f"{base_url}&location={location}"
  
  # Scrape and process listings
  scrape_craigslist(url, max_price, max_miles, desired_features)

# Execute the script
scrape_craigslist(base_url, max_price, max_miles, desired_features)
