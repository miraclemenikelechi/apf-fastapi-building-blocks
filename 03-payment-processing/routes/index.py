from controllers.index import payment_process_from_client
from models.index import PaymentRequest

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/payments", tags=["payment"])


@router.post("/")
async def make_payment(payment_request: PaymentRequest):
    data = await payment_process_from_client(payment_request)

    json_compatible_data: dict[str, any] = {
        "message": "payment recieved",
        "data": jsonable_encoder(data),
    }

    return JSONResponse(
        status_code=200,
        content=json_compatible_data,
    )
