# dbtest.py

# Connecting
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///./data/books.db", echo=True, future=True)
conn = engine.connect()
result = conn.execute(text("select * from author"))
print(result.all())
conn.close()