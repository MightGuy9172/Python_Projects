# Cafe & Wifi API

A RESTful API built with Flask and SQLAlchemy to manage a database of cafes, including their amenities and coffee prices. The API allows you to search, add, update, and delete cafe records.

## Features

- **Get a random cafe**  
  `GET /random`  
  Returns details of a random cafe.

- **Get all cafes**  
  `GET /all`  
  Returns a list of all cafes.

- **Search cafes by location**  
  `GET /search?loc=<location>`  
  Returns cafes matching the specified location.

- **Add a new cafe**  
  `POST /add`  
  Adds a new cafe. Requires form data:

  - `name`
  - `map_url`
  - `img_url`
  - `loc`
  - `seats`
  - `toilet` (bool)
  - `wifi` (bool)
  - `sockets` (bool)
  - `calls` (bool)
  - `coffee_price`

- **Update coffee price**  
  `PATCH /update/<cafe_id>?new_price=<price>`  
  Updates the coffee price for the specified cafe.

- **Delete a cafe**  
  `DELETE /delete/<cafe_id>?api_key=MyKey`  
  Deletes the specified cafe (requires API key).

## Setup

1. **Clone the repository**

   ```sh
   git clone <repo-url>
   cd Cafe\ API
   ```

2. **Install dependencies**

   ```sh
   pip install flask flask_sqlalchemy
   ```

3. **Run the application**

   ```sh
   python main.py
   ```

4. **Access the homepage**
   Open http://127.0.0.1:5000/ in your browser.

### Database

## SQLite database file: instance/cafes.db

- Table: Cafe
- id (int, primary key)
- name (str, unique)
- img_url (str)
- location (str)
- seats (str)
- map_url (str)
- has_toilet (bool)
- has_wifi (bool)
- has_sockets (bool)
- can_take_calls (bool)
- coffee_price (str, nullable)

### License

This project is licensed under the MIT License.
