from fastapi import APIRouter
from sqlalchemy import text
from app.database import engine

router = APIRouter()

@router.get("/products")
def get_products(
    limit: int = 20,
    category: str | None = None,
    cursor_updated_at: str | None = None,
    cursor_id: int | None = None
):

    query = """
        SELECT *
        FROM products
        WHERE 1=1
    """

    params = {"limit": limit}

    if category:
        query += " AND category = :category "
        params["category"] = category

    if cursor_updated_at and cursor_id:
        query += """
        AND (
            updated_at < :cursor_updated_at
            OR (
                updated_at = :cursor_updated_at
                AND id < :cursor_id
            )
        )
        """
        params["cursor_updated_at"] = cursor_updated_at
        params["cursor_id"] = cursor_id

    query += """
        ORDER BY updated_at DESC, id DESC
        LIMIT :limit
    """

    with engine.connect() as conn:
        result = conn.execute(text(query), params)
        products = [dict(row._mapping) for row in result]

    next_cursor = None

    if products:
        last = products[-1]
        next_cursor = {
            "updated_at": last["updated_at"],
            "id": last["id"]
        }

    return {
        "count": len(products),
        "next_cursor": next_cursor,
        "data": products
    }