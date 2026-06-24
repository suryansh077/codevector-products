\# CodeVector Product Browser Backend



\## Tech Stack



\* FastAPI

\* PostgreSQL (Neon)

\* SQLAlchemy



\## Features



\* Browse products sorted by newest first

\* Category filtering

\* Cursor-based pagination

\* Indexed queries for performance



\## Pagination Strategy



I used cursor pagination based on `(updated\_at, id)`.



Why:



\* Faster than OFFSET pagination on large datasets

\* Prevents duplicate records

\* Prevents missing records when products are inserted or updated while users browse



\## Indexes



```sql

CREATE INDEX idx\_products\_pagination

ON products(updated\_at DESC, id DESC);



CREATE INDEX idx\_products\_category\_pagination

ON products(category, updated\_at DESC, id DESC);

```



\## Run Locally



```bash

pip install -r requirements.txt

uvicorn app.main:app --reload

```



\## API Examples



GET /products



GET /products?category=Electronics



GET /products?limit=5



GET /products?limit=5\&cursor\_updated\_at=<timestamp>\&cursor\_id=<id>



