from flask import Flask, request
from database import get_connection
from price_calculator import calculate_price

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "application": "House Price Prediction",
        "status": "running"
    }


@app.route("/health")
def health():
    try:
        connection = get_connection()
        connection.close()

        return {
            "status": "UP",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "DOWN",
            "database": "not connected",
            "error": str(e)
        }, 500


@app.route("/api/calculate", methods=["POST"])
def calculate():

    data = request.get_json()

    required_fields = [
        "location",
        "area",
        "bedrooms",
        "bathrooms",
        "parking",
        "property_age"
    ]

    for field in required_fields:
        if field not in data:
            return {
                "error": f"Missing field: {field}"
            }, 400

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT rate_per_sqft
            FROM locations
            WHERE location_name = %s
            """,
            (data["location"],)
        )

        location = cursor.fetchone()

        if not location:
            return {
                "error": "Location not found"
            }, 404

        estimated_price = calculate_price(
            float(location["rate_per_sqft"]),
            int(data["area"]),
            int(data["bedrooms"]),
            int(data["bathrooms"]),
            int(data["parking"]),
            int(data["property_age"])
        )

        cursor.execute(
            """
            INSERT INTO predictions
            (
                location_name,
                area,
                bedrooms,
                bathrooms,
                parking,
                property_age,
                estimated_price
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                data["location"],
                data["area"],
                data["bedrooms"],
                data["bathrooms"],
                data["parking"],
                data["property_age"],
                estimated_price
            )
        )

        connection.commit()

        return {
            "location": data["location"],
            "estimated_price": estimated_price
        }

    except Exception as e:

        return {
            "error": str(e)
        }, 500

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
