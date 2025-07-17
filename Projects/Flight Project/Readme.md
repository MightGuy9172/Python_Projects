# Flight Deal Notification Project

This Python project searches for the cheapest flights from a specified origin city to multiple destinations and notifies users via email and WhatsApp when a low price is found.

## Features

- Fetches flight data using the Amadeus API.
- Retrieves and updates destination data from a Google Sheet.
- Notifies users of low price flights via email and WhatsApp using Twilio.
- Supports searching for both direct and indirect flights.

## Project Structure

- `main.py`: Main script to run the flight search and notification logic.
- `data_manager.py`: Handles Google Sheet data retrieval and updates.
- `flight_search.py`: Interfaces with the Amadeus API for flight and IATA code searches.
- `flight_data.py`: Processes flight data and finds the cheapest flight.
- `notification_manager.py`: Sends notifications via email and WhatsApp.
- `.env`: Stores environment variables (API keys, credentials).
- `.gitignore`: Ignores sensitive files like `.env`.

## Setup

1. Clone the repository.

2. Install dependencies:

   ```sh
   pip install requests python-dotenv twilio
   ```

3. Create a .env file with the following variables:
   ```sh
   SHEETY=<your sheety endpoint>
   SHEET_USERNAME=<your sheety username>
   SHEET_PASSWORD=<your sheety password>
   SHEETY_USERS_ENDPOINT=<your sheety users endpoint>
   USAMADE_KEY=<your amadeus api key>
   AMADEUS_SECRET=<your amadeus api secret>
   EMAIL_PROVIDER_SMTP_ADDRESS=<your smtp address>
   MY_EMAIL=<your email>
   MY_EMAIL_PASSWORD=<your email password>
   TWILIO_SID=<your twilio sid>
   TWILIO_AUTH_TOKEN=<your twilio auth token>
   TWILIO_VIRTUAL_NUMBER=<your twilio sms number>
   TWILIO_VERIFIED_NUMBER=<your verified phone number>
   TWILIO_WHATSAPP_NUMBER=<your whatsapp number>
   ```

### Run the main script:

```sh
python [main.py](http://_vscodecontentref_/0)
```
