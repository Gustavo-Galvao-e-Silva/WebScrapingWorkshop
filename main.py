import requests
import pandas as pd
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import time
import random


base_url = "https://boardgamegeek.com/browse/boardgame"

def get_page_html(page_number: int) -> str:
    url = f"{base_url}/page/{page_number}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad status codes
        return response.text

    except Exception as e:
        print(f"Error getting page {page_number}: {str(e)}")


def parse_game_row(row: BeautifulSoup) -> Optional[Dict[str, str]]:
    try:
        # Get the rank
        rank_cell = row.find("td", {"class": "collection_rank"})
        if not rank_cell:
            return None
        rank = int(rank_cell.text.strip())

        # Get the name
        name_cell = row.find("td", {"class": "collection_objectname"})
        if not name_cell or not name_cell.a:
            return None
        name = name_cell.a.text.strip()

        # Get the year
        year_cell = name_cell.find("span", {"class": "smallerfont"})
        year = year_cell.text.strip("()") if year_cell else "N/A"

            # Get the ratings
        rating_data = row.find_all(class_="collection_bggrating")

        # Only process if we have all three rating values
        if len(rating_data) >= 3:
            geek_rating = float(rating_data[0].text.strip())
            average_rating = float(rating_data[1].text.strip())
            num_voters = int(rating_data[2].text.strip())
        else:
            return None

        return {
                "Rank": rank,
                "Name": name,
                "Year": year,
                "Geek Rating": geek_rating,
                "Average Rating": average_rating,
                "Number of Voters": num_voters
        }

    except (ValueError, AttributeError) as e:
        print(f"Error parsing game row: {str(e)}")
        return None

def scrape_page(page_number: int) -> List[Dict[str, str]]:
    """Scrape a single page of board game data."""
    try:
        html = get_page_html(page_number)
        soup = BeautifulSoup(html, "html.parser")

        # Find the games table
        games_table = soup.find("table", {"class": "collection_table"})
        if not games_table:
             print(f"No games table found on page {page_number}")
             return []

        # Find all game rows
        rows = games_table.find_all("tr", {"id": lambda x: x and x.startswith("row_")})
        if not rows:
            print(f"No game rows found on page {page_number}")
            return []

            # Parse each row and filter out None values
        games = [game for game in (parse_game_row(row) for row in rows) if game is not None]
        print(f"Found {len(games)} games on page {page_number}")
        return games

    except Exception as e:
        print(f"Error scraping page {page_number}: {str(e)}")
        return []

def scrape_pages(num_pages: int) -> List[Dict[str, str]]:
    """Scrape multiple pages of board game data."""

    all_games = []
    for page in range(1, num_pages + 1):
        print(f"Scraping page {page}/{num_pages}")
        games = scrape_page(page) 
        all_games.extend(games)
        sleep_time = 3 + random.uniform(-1.0, 2.0)
        time.sleep(sleep_time)  # Be nice to the server

    print(f"Successfully scraped {len(all_games)} games out of {num_pages} pages")
    return all_games



def write_to_csv(data: List[Dict[str, str]], file_name: str = "boardgames.csv") -> None:
    """Write data to a CSV file."""
    try:
        if not data:
            print("No data to write")
            return

        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
        print(f"Successfully wrote {len(data)} records to {file_name}")
    except Exception as e:
        print(f"Error writing to CSV: {str(e)}")


def main() -> None:
    """Main function to run the scraper."""
    try:
        # Get and validate number of pages
        num_pages = int(input("How many pages to scrape (1-10): "))
        # Initialize scraper and get data
        print(f"\nStarting to scrape {num_pages} pages...")
        games_data = scrape_pages(num_pages=num_pages)

        if not games_data:
            print("No data was collected. Exiting...")


        print(f"\nSuccessfully collected data for {len(games_data)} games")

        # Write data to files
        print("\nSaving data to files...")
        write_to_csv(games_data)

        print("\nScript completed successfully!")

    except Exception as e:
        print(f"\nError occurred: {e}")


if __name__ == "__main__":
    main()
