from faker import Faker
from datetime import timedelta
from sqlalchemy import text
from app.database import engine
import random

fake = Faker()

categories = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Home",
    "Beauty"
]

BATCH_SIZE = 100
TOTAL_RECORDS = 1000


def generate_batch(start_id, batch_size):
    records = []

    for i in range(batch_size):
        product_id = start_id + i

        created = fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )

        updated = created + timedelta(
            days=random.randint(0, 30)
        )

        records.append({
            "id": product_id,
            "name": fake.word() + f" {product_id}",
            "category": random.choice(categories),
            "price": round(random.uniform(100, 10000), 2),
            "created_at": created,
            "updated_at": updated
        })

    return records


print("Script started")

with engine.begin() as conn:

    print("DB connected")

    for start in range(1, TOTAL_RECORDS + 1, BATCH_SIZE):

        print(f"Generating batch {start}")

        batch = generate_batch(
            start,
            min(BATCH_SIZE, TOTAL_RECORDS - start + 1)
        )

        print("Batch generated")

        conn.execute(
            text("""
                INSERT INTO products
                (id,name,category,price,created_at,updated_at)
                VALUES
                (:id,:name,:category,:price,:created_at,:updated_at)
            """),
            batch
        )

        print("Batch inserted")
        print(f"Inserted {start + len(batch) - 1} records")

print("Finished seeding")