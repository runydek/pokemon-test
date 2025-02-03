# Pokemon Scraper API

This is a simple Flask-based API that scrapes Pokémon data (name and types) from the PokeAPI, stores it in a local SQLite database, and exposes it via a REST API following [JSON:API](https://jsonapi.org/) standards.

## Features

- Scrapes Pokémon data (name, types) from the external PokeAPI.
- Stores the scraped data in a local SQLite database.
- Provides an API to view all Pokémon or individual Pokémon by ID.
- Follows [JSON:API](https://jsonapi.org/) standards for responses.

## Prerequisites

Before you can run this application, make sure you have the following installed:

- Python 3.x
- `pip` (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pokemon-scraper-api.git
    cd pokemon-scraper-api
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Setup

### Database

The app uses SQLite as the database. When you first run the app, it will scrape the Pokémon data and populate the database automatically.

### Configuration

You can configure the app by setting the following environment variables (optional):

- `FLASK_APP`: The entry point for the Flask app (default is `app.py`).
- `FLASK_ENV`: Set to `development` for debugging and reloading features.
- `DATABASE_URI`: URI to the database file (default is `sqlite:///pokemon.db`).

## Running the App

**Start the Flask development server:**

    ```bash
    flask run
    ```

    By default, the app will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### `GET /pokemon`

Get a list of all Pokémon in the database.

**Response:**

```json
{
  "data": [
    {
      "type": "pokemon",
      "id": "1",
      "attributes": {
        "name": "Bulbasaur",
        "type": "grass, poison"
      }
    },
    {
      "type": "pokemon",
      "id": "2",
      "attributes": {
        "name": "Ivysaur",
        "type": "grass, poison"
      }
    }
  ]
}
