from flask import Flask, render_template, request
from entities import Car, CarShop

app = Flask(__name__)

car_shop = CarShop()

@app.route("/", methods=["GET", "POST"])
def index():

    # car_shop.shut_down_store()

    message = ""

    if request.method == "POST":
        if "add_custom_car" in request.form:  # Check if "add_custom_car" button was pressed
            car_name = request.form.get("car_name")
            car_price = request.form.get("car_price")
            
            if car_name and car_price:
                try:
                    car_price_int = int(car_price)
                    custom_car = Car(car_name, car_price_int)
                    car_shop.add_car(custom_car)
                    message = f"{custom_car.name} added to the shop!"
                except ValueError:
                    message = "Invalid price entered. Please enter a valid number."

        elif "remove_custom_car" in request.form:  # Check if "remove_custom_car" button was pressed
            car_id = request.form.get("car_ID")
            
            if car_id:
                try:
                    car_shop.remove_car(int(car_id))  # Convert car_id to integer
                    message = "Car removed from shop!"
                except ValueError:
                    message = "Invalid car ID entered. Please enter a valid ID."
            else:
                message = "No car ID provided to remove."

    # Get all cars from the database
    cars = car_shop.get_all_cars()

    return render_template("index.html", message=message, cars=cars)

if __name__ == '__main__':
    app.run(debug=True)
