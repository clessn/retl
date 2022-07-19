from celery import Celery

app = Celery()

app.config_from_object("celeryconfig")

result = app.send_task(
    # TODO: change run_pipeline to run.run_<my_pipeline_name>
    # (as in run.py, but with "run." as prefix)
    "run.run_pipeline",
    args=[],
    kwargs={
        "HUB3_URL": "https://clhub.dev.clessn.cloud/",
        "HUB3_USERNAME": "potato",
        "HUB3_PASSWORD": "tomato",
    },
    # TODO: change my-queue to <my-pipeline-name>
    queue="my-queue",
)

while not result.ready():
    pass

print(result.result)
