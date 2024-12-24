from dagster import Definitions, load_assets_from_modules
from .jobs import say_hello_pipeline

from orchestrator.orchestrator.assets import greet

all_assets = load_assets_from_modules(
    [
        greet,
    ]
)
all_jobs = [say_hello_pipeline]

defs = Definitions(
    assets=all_assets,
    jobs=all_jobs,
)
