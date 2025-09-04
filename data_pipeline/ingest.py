import xarray as xr
import pandas as pd
import sqlalchemy

class DataIngest:
    def __init__(self, netcdf_path):
        self.netcdf_path = netcdf_path

    def load_netcdf(self):
        return xr.open_dataset(self.netcdf_path)

    def to_dataframe(self):
        ds = self.load_netcdf()
        df = ds.to_dataframe().reset_index()
        return df

    def store_to_postgresql(self, df, db_url):
        engine = sqlalchemy.create_engine(db_url)
        df.to_sql('argo_data', con=engine, if_exists='replace', index=False)

    def process(self, db_url):
        df = self.to_dataframe()
        self.store_to_postgresql(df, db_url)
