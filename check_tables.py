from sqlalchemy import inspect
from app.database import engine

print("Connecting...")

with engine.connect() as conn:
    print("Connected!")

inspector = inspect(engine)

print("Fetching tables...")
print(inspector.get_table_names())
print("Done!")