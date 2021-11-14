import pandas as pd
from django.core.management import BaseCommand
from ...models import Product
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "A command to add data from an Excel file to the database"

    def handle(self, *args, **options):

        file = "data.xlsx"
        df = pd.read_excel(file)

        engine = create_engine("sqlite:///db.sqlite3")
        df.to_sql(Product._meta.db_table, con=engine, if_exists="replace", index=False)

