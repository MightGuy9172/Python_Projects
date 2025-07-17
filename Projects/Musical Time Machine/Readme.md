# Musical Time Machine

Musical Time Machine lets you travel back in time to discover the top Indian songs from any date after March 1, 2022. Enter a date, and the app fetches the Billboard India chart for that day, then creates a private Spotify playlist with those songs.

## Features

- Fetches top Indian songs from Billboard for a given date
- Searches for songs on Spotify
- Automatically creates a private Spotify playlist with the found tracks

## Usage

1. Run the script.
2. Enter a date in the format `YYYY-MM-DD` (after 2022-03-01).
3. Authorize Spotify access when prompted.
4. Enjoy your personalized playlist!

## Requirements

- Python 3
- `requests`, `beautifulsoup4`, `spotipy`, `python-dotenv` libraries
- Spotify account and API credentials

## Setup

1. Install dependencies:  
   `pip install requests beautifulsoup4 spotipy python-dotenv`
2. Create a `.env` file with your Spotify API credentials
3. Run `main.py` and follow the prompts.
