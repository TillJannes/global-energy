from dagster import define_asset_job

say_hello_pipeline = define_asset_job(
    name="say_hello_pipeline",
    selection=[
        "greet"
    ]
)
