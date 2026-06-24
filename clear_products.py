from sqlalchemy import text
from app.database import engine

with engine.begin() as conn:
    conn.execute(text("DELETE FROM products"))

print("All products deleted!")