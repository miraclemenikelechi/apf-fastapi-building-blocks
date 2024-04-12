import json

from fastapi import HTTPException

products: list = []
products_file: str = "assets/products.json"

with open(products_file, "r") as f:
    content = f.read()
    products = json.loads(content)


async def filter_products_on_search(name: str, range: str, category: str):

    try:
        if not any([name, range, category]):
            return {"products": products}

        filtered_products = []

        for item in products:

            if name and name.lower() not in item["product_name"].lower():
                continue

            if range:
                min_price_range, max_price_range = map(float, range.split("-"))

                if not min_price_range <= item["price"] <= max_price_range:
                    continue

            if category and category.lower() not in item["category"].lower():
                continue

            filtered_products.append(item)

        if not filtered_products:
            raise HTTPException(
                status_code=404,
                detail="no products found for this search"
            )

        return {"products": filtered_products}

    except HTTPException as error:
        return {"error": error}
