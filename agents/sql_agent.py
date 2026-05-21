from sqlalchemy import text
from database.db import engine

def run_query(query):

    try:

        with engine.connect() as conn:

            result = conn.execute(text(query))

            rows = result.fetchall()

            return rows

    except Exception as e:

        return str(e)