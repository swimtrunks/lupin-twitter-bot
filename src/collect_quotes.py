import json as _json

import scraper as _scraper

if __name__ == "__main__":
    quotes= _scraper.scrape_quotes()
    with open("quotes.json", mode = "w") as quotes_file:
        _json.dump(quotes, quotes_file, ensure_ascii =False)