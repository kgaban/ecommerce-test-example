# Flask E-Commerce Website and Playwright Testing Example

This is a simple Flask application that serves as an example of building a REST API with Swagger documentation. The application includes endpoints that read from dictionaries and also interfaces with external APIs. It provides functionality to retrieve Kevin's favorites based on a specified topic and fetches a random joke from the JokeAPI.

## Requirements

- Python 3.x
- Flask
- Playwright

## Installation

1. Clone the repository:

  ```bash
    git clone https://github.com/kgaban/ecommerce-test-example.git
  ```
    
2.  Navigate to the project directory:
    
    
  ```bash
    cd ecommerce-test-example
  ```
    
3.  Create a virtual environment (optional but recommended):
        
  ```bash
    python -m venv ./venv
  ```
    
4.  Activate the virtual environment:
    
  ```bash
    source venv/bin/activate   # On macOS/Linux

    venv\Scripts\activate      # On Windows
  ```
    
5.  Install the required dependencies:
    
  ```bash
  pip install -r requirements.txt
  ```
    

## Usage

Run the Flask application:

```bash
  python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Running Playwright Tests

```bash
  python scripts/playwright_script_example.py
```

Logging can be seen in the standard output
