# Motor Vehicle Marketplace Sim 🚙💨

## Overview

This project is a web application built using [Flask](https://flask.palletsprojects.com/) that simulates a car shop where users can add or remove cars from a marketplace. It uses a MySQL database to store car information and dynamically displays available cars. The project structure also contains unit tests written with [pytest](https://docs.pytest.org/en/stable/).

## Project Structure

- **src/app.py**: The Flask application entry point. It handles routing and form submissions.  
  See [src/app.py](src/app.py).

- **src/entities/car_shop.py**: Contains the `CarShop` class responsible for database operations (adding, removing, and retrieving cars).  
  See [`entities.CarShop`](src/entities/car_shop.py).

- **src/entities/car.py**: Contains the `Car` class that represents the car object.  
  See [`entities.Car`](src/entities/car.py).

- **src/templates/index.html**: An HTML template rendered by Flask to display the car shop interface.  
  See [src/templates/index.html](src/templates/index.html).

- **src/static/style.css**: Contains the styling for the front-end of the application.  
  See [src/static/style.css](src/static/style.css).

- **tests/**: Contains unit tests that validate the functionality of the Flask app and entities.
  - [tests/test_app.py](tests/test_app.py): Tests for the Flask routes and behavior.
  - [tests/test_car_shop.py](tests/test_car_shop.py): Tests for the database operations.
  - [tests/test_car.py](tests/test_car.py): Tests for the Car model.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/your-username/car_db.git
   cd car_db
   ```
2. **Create a Virtual Environment (Optional but Recommended):**
   
  ```sh
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<!-- pip install -U pytest

docs
.gitignore
tests
setup.py
try except blocks and warnings -->
