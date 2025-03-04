#Add imports

class BoardGameScraper:

    def __init__(self):
        self.base_url =

    def _get_page_html(self): #Add page_number and type hinting
        url = f"{self.base_url}/page/{page_number}"

        try:
            response = requests.get(url, timeout=10)
            #Add raise for exception
            #Add return text

        except RequestException as e:
            print(f"Error getting page {page_number}: {str(e)}")

        raise Exception(f"Failed to get page {page_number} after {self.max_retries} attempts")

    def _parse_game_row(self, row: BeautifulSoup):
        try:
            # Get the rank
            if not rank_cell:
                return None
            #Assign the stripped text converted to an integer to get rank

            # Get the name
            name_cell = row.find()
            if not name_cell or not name_cell.a:
                return None
            name = name_cell.a.text.strip()

            # Get the year
            year_cell = name_cell.find("span", {"class": "smallerfont"})
            #Won't return none if the year field is empty
            year = year_cell.text.strip("()") if year_cell else "N/A"

            # Get the ratings
            rating_data = row.find_all(class_="collection_bggrating")

            # Only process if we have all three rating values
            if len(rating_data) >= 3:

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
        except Exception as e:
            print(f"Error parsing game row: {str(e)}")
            return None

    def _scrape_page(self, page_number: int) -> List[Dict[str, str]]:
        """Scrape a single page of board game data."""
        try:
            #Get HTML
            #Instantiate BeautifulSoup parser

            # Find the games table
            games_table = soup.find()
            if not games_table:
                print(f"No games table found on page {page_number}")
                return []

            # Find all game rows
            rows = games_table.find_all("tr", {}) #Add lambda function that finds all rows in a table
            if not rows:
                print(f"No game rows found on page {page_number}")
                return []

            # Parse each row and filter out None values
            games = [] #Double comprehension to get the list of games
            print(f"Found {len(games)} games on page {page_number}")
            return games

        except Exception as e:
            print(f"Error scraping page {page_number}: {str(e)}")
            return []

    def scrape_pages(self, num_pages: int) -> List[Dict[str, str]]:
        """Scrape multiple pages of board game data."""

        all_games = []

        print(f"Successfully scraped {len(all_games)} games out of {num_pages} pages")
        return all_games


class DataWriter:
    """A class to handle writing data to different file formats."""

    def write_to_csv(data: List[Dict[str, str]], file_name: str = "boardgames.csv") -> None:
        """Write data to a CSV file."""
        try:
            if not data:
                print("No data to write")
                return

            # Create directory if it doesn't exist

            #Write to CSV
            print(f"Successfully wrote {len(data)} records to {file_name}")
        except Exception as e:
            print(f"Error writing to CSV: {str(e)}")



def main() -> None:
    """Main function to run the scraper."""
    try:
        # Get and validate number of pages

        # Initialize scraper and get data
        print(f"\nStarting to scrape {num_pages} pages...")

        if not games_data:
            print("No data was collected. Exiting...")

        #Get game data
        print(f"\nSuccessfully collected data for {len(games_data)} games")

        # Write data to files
        print("\nSaving data to files...")

        print("\nScript completed successfully!")

    except Exception as e:
        print(f"\nError occurred: {e}")


#Make it run babyy
