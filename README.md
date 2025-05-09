
# Kenh14 News Scraper

This Python script scrapes the latest social news articles from Kenh14.vn's "Nóng trên mạng" section and saves the data to a CSV file. The script uses Selenium and BeautifulSoup for scraping and `schedule` to run daily at 06:00 AM.

## Features

- Scrapes article title, description, image URL, and article URL.
- Scrolls the page to load more content.
- Saves data in `CSV` format.
- Automatically runs daily at 06:00 AM using `schedule`.

## Requirements

Install the required packages using:

```
pip install -r requirements.txt
```

**requirements.txt**
```
requests
beautifulsoup4
pandas
schedule
selenium
```

You also need to have [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed and compatible with your Chrome browser version.

## Usage

1. Run the script manually:
   ```
   python kenh14_scraper.py
   ```

2. Or let it run continuously (schedules daily at 06:00 AM):
   ```
   python kenh14_scraper.py
   ```

3. CSV output will be saved as:
   - `kenh14_data.csv` (or with a timestamp if modified)

## Notes

- Make sure ChromeDriver is in your system's PATH or specify its location in the script if needed.
- This script is for educational and non-commercial use only.

## Upload to GitHub

1. Initialize Git:
   ```
   git init
   ```

2. Add files:
   ```
   git add .
   ```

3. Commit:
   ```
   git commit -m "Initial commit"
   ```

4. Create a new repo on GitHub, then connect your local folder:
   ```
   git remote add origin https://github.com/your-username/your-repo-name.git
   ```

5. Push to GitHub:
   ```
   git push -u origin master
   ```
