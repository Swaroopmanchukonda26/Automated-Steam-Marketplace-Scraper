import csv
import requests
from bs4 import BeautifulSoup

def scrape_steam_store(output_csv):
    # Target Steam's New Releases global data feed
    url = "https://store.steampowered.com/search/?sort_by=Released_DESC&supportedlang=english"
    
    # Send a mock browser agent header to prevent network blockers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print(f"🔄 Initializing connection to: {url}")
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ Connection failed with HTTP Status: {response.status_code}")
        return

    # Parse raw HTML data markup text
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Isolate all standard search result item tags
    game_rows = soup.find_all('a', class_='search_result_row')
    print(f"📦 Connection validated. Found {len(game_rows)} structural elements to parse.")
    
    # Initialize the CSV writer environment
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write column headers
        writer.writerow(["Game Title", "Release Date", "Price (USD)"])
        
        for game in game_rows:
            # Extract individual text targets safely using conditional try-blocks
            try:
                title = game.find('span', class_='title').text.strip()
                
                date_tag = game.find('div', class_='search_released')
                released = date_tag.text.strip() if date_tag else "N/A"
                
                price_tag = game.find('div', class_='search_price')
                price = price_tag.text.strip() if price_tag else "Free/Unreleased"
                # Clean up nested formatting breaks in the price text
                if "\n" in price:
                    price = price.split("\n")[-1].strip()
                
                # Write the row data matrix
                writer.writerow([title, released, price])
            except Exception:
                continue
                
    print(f"🏆 Data extraction cycle finalized! Output written to '{output_csv}'")

if __name__ == "__main__":
    scrape_steam_store("steam_games.csv")
