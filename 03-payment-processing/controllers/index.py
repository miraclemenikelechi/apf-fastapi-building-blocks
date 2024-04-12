from models.index import PaymentRequest


async def payment_process_from_client(payment: PaymentRequest):
    data_from_user = {
        "amount_from_user": payment.amount,
        "currency_from_user": payment.currency,
        "card_number_from_user": payment.card_number,
        "card_expiration_date_from_user": payment.expiration_date,
        "cvv_from_user": payment.cvv,
    }

    return data_from_user
