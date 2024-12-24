import datetime
from dagster import (
    AssetExecutionContext,
    asset,
)

@asset(kinds=["python"])
def greet(context: AssetExecutionContext):
    context.log.info(f"Hey there, current local timestamp is {datetime.datetime.now()}.")
