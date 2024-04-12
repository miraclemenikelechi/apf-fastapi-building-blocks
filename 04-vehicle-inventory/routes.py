from fastapi import APIRouter, Query
from controllers import filter_vehicles
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

vehicles = APIRouter(prefix="/vehicles", tags=["vehicles"])


@vehicles.get("/")
async def search_vehicle_inventory(
    vehicle_make: str = Query(
        default=None,
        description="the make of the vehicle",
        min_length=1,
        example="Toyota",
    ),
    vehicle_model: str = Query(
        default=None,
        description="the model of the vehicle",
        min_length=1,
        example="Camry",
    ),
    vehicle_year: int = Query(
        default=None,
        description="the manufacture year of the vehicle",
        ge=1700,
        lt=2100,
        example="2020",
    ),
    price_range: str = Query(
        default=None,
        description="the price range. min-max",
        example="1000-2000",
    ),
):

    data = await filter_vehicles(
        vehicle_make_from_user=vehicle_make,
        vehicle_model_from_user=vehicle_model,
        vehicle_year_from_user=vehicle_year,
        price_range_from_user=price_range,
    )

    json_compatible_data: dict[str, any] = {
        "message": "vehicle inventory",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(
        status_code=200,
        content=json_compatible_data,
    )


@vehicles.get("/{vin}")
async def get_vehicle_by_vin(vin: str):
    data = await filter_vehicles(vehicle_vin_from_user=vin)

    json_compatible_data: dict[str, any] = {
        "message": "vehicle inventory",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(
        status_code=200,
        content=json_compatible_data,
    )
