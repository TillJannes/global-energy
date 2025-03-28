import datetime as dt
import pandera as pa
from pandera import DataFrameModel
from typing import Optional

class PowerTimeseries(DataFrameModel):

    class Config:
        coerce = True
        strict = "filter"

    time: dt.datetime
    power: float = pa.Field(ge=0)
    kind: str = pa.Field(isin=[
        "electric",
        "thermic",
        "mechanic",
        "chemical"
    ])
    name: Optional[str] = pa.Field(nullable=True)
    source: Optional[str] = pa.Field(nullable=True)
