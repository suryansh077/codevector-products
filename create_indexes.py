from sqlalchemy import text
from app.database import engine

with engine.begin() as conn:
    conn.execute(text("""
        CREATE INDEX IF NOT EXISTS idx_products_pagination
        ON products(updated_at DESC, id DESC)
    """))

    conn.execute(text("""
        CREATE INDEX IF NOT EXISTS idx_products_category_pagination
        ON products(category, updated_at DESC, id DESC)
    """))

print("Indexes created successfully!")