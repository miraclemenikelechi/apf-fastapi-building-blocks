import json

from fastapi import HTTPException

vehicles = []
vehicles_db: str = "vehicles.json"

with open(vehicles_db, "r") as file:
    content = file.read()
    vehicles = json.loads(content)


async def filter_vehicles(
    vehicle_make_from_user: str | None = None,
    vehicle_model_from_user: str | None = None,
    vehicle_year_from_user: int | None = None,
    price_range_from_user: str | None = None,
    vehicle_vin_from_user: str | None = None,
):
    try:
        filtered_vehicles = vehicles

        if vehicle_make_from_user:
            filtered_vehicles = [
                item
                for item in filtered_vehicles
                if item["vehicle_make"].lower() == vehicle_make_from_user.lower()
            ]

        if vehicle_model_from_user:
            filtered_vehicles = [
                item
                for item in filtered_vehicles
                if item["vehicle_model"].lower() == vehicle_model_from_user.lower()
            ]

        if vehicle_year_from_user:
            filtered_vehicles = [
                item
                for item in filtered_vehicles
                if item["vehicle_year"] == vehicle_year_from_user
            ]

        if price_range_from_user:
            price_range_values = price_range_from_user.split("-")

            if len(price_range_values) == 1:
                # Single price value provided
                max_price = float(price_range_values[0])
                min_price = 0  # Set a default minimum price

                filtered_vehicles = [
                    item
                    for item in filtered_vehicles
                    if min_price <= item["vehicle_price"] <= max_price
                ]

            elif len(price_range_values) == 2:
                # Price range provided
                min_price, max_price = map(float, price_range_values)

                filtered_vehicles = [
                    item
                    for item in filtered_vehicles
                    if min_price <= item["vehicle_price"] <= max_price
                ]

            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid price range format",
                )

        if vehicle_vin_from_user:
            filtered_vehicles = [
                item
                for item in filtered_vehicles
                if item["vehicle_vin"].lower() == vehicle_vin_from_user.lower()
            ]

        if not filtered_vehicles:
            raise HTTPException(
                status_code=404, detail="No vehicles found for the given filters"
            )

        return filtered_vehicles

    except HTTPException as error:
        raise error
