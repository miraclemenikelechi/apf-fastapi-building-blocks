from fastapi import Query, APIRouter
from controllers.index import filter_products_on_search

router = APIRouter()


@router.get("/products")
async def search_products(
    product_name: str = Query(default=None, description="product name"),
    price_range: str = Query(default=None, description="price range"),
    category: str = Query(default=None, description="product category")
):

    product_name_from_search = product_name
    product_category_from_search = category
    price_range_from_search = price_range

    data = await filter_products_on_search(
        name=product_name_from_search,
        range=price_range_from_search,
        category=product_category_from_search
    )

    return data
