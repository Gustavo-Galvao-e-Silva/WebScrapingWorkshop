#Add imports


#Get base URL
base_url = 

def get_page_html(): #Add page number parameter and type hinting
    url = f"{base_url}/page/{page_number}"

    try:
        #Add get request
        #Add raise error
        #Add text return

    except RequestException as e:
        print(f"Error getting page {page_number}: {str(e)}")


def parse_game_row(row: BeautifulSoup) -> Optional[Dict[str, str]]:
    try:
        #Get the rank with find method
        if not rank_cell:
            return None
        #Assign value for rank

        #Get the name
        name_cell = row.find()
        if not name_cell or not name_cell.a:
            return None
        name = name_cell.a.text.strip()

        #Get the year
        year_cell = name_cell.find("span", {"class": "smallerfont"})
        year = year_cell.text.strip("()") if year_cell else "N/A"

        #Get the ratings
        rating_data = row.find_all(class_="collection_bggrating")

        #Only process if we have all three rating values
        if len(rating_data) >= 3:
            #Add assignments for rating data
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
        #Get HTML
        #Instantiate HTML parser

        #Find the games table
        games_table = soup.find()
        if not games_table:
             print(f"No games table found on page {page_number}")
             return []

        #Find all game rows
        rows = games_table.find_all("tr", {"id": }) #Add lambda function that returns rows in the table
        if not rows:
            print(f"No game rows found on page {page_number}")
            return []

        #Parse each row and filter out None values
        games = [] #Double list comprehension to get the list of games
        print(f"Found {len(games)} games on page {page_number}")
        return games

    except Exception as e:
        print(f"Error scraping page {page_number}: {str(e)}")
        return []

def scrape_pages(): #Add num_pages parameter and type hinting
    """Scrape multiple pages of board game data."""

    all_games = []
    #Loop to scrape all games
        
    print(f"Successfully scraped {len(all_games)} games out of {num_pages} pages")
    return all_games



def write_to_csv(data: List[Dict[str, str]], file_name: str = "boardgames.csv") -> None:
    """Write data to a CSV file."""
    try:
        if not data:
            print("No data to write")
            return

        #Create directory if it doesn't exist

        #Write to CSV pandas method
        print(f"Successfully wrote {len(data)} records to {file_name}")
    except Exception as e:
        print(f"Error writing to CSV: {str(e)}")


def main() -> None:
    """Main function to run the scraper."""
    try:
        #Get and validate number of pages

        #Call scraper function

        print(f"\nStarting to scrape {num_pages} pages...")
        

        if not games_data:
            print("No data was collected. Exiting...")


        print(f"\nSuccessfully collected data for {len(games_data)} games")

        # Write data to files
        print("\nSaving data to files...")


        print("\nScript completed successfully!")

    except Exception as e:
        print(f"\nError occurred: {e}")


#Make it run babyy :)
