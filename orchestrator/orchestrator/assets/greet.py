import datetime
from dagster import (
    AssetExecutionContext,
    asset,
)
from orchestrator.orchestrator.data.table_types import PowerTimeseries
from dagster_pandera import pandera_schema_to_dagster_type

@asset(
    kinds=["python"],
    dagster_type=pandera_schema_to_dagster_type(PowerTimeseries)
    )
def greet(context: AssetExecutionContext):
    context.log.info(f"Hey there, current local timestamp is {datetime.datetime.now()}.")
