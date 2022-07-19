import os
import subprocess
from celery import Celery

app = Celery()

app.config_from_object("celeryconfig")


@app.task
# TODO: change run_pipeline to run_<my_pipeline_name>
def run_pipeline(*args, **kwargs):
    # TODO: adjust command if necessary
    command = "Rscript code/code.R"

    # configure environment
    env = os.environ.copy()
    path = kwargs.get("PATH", None)
    kwargs.pop("PATH", None)
    if path is not None:
        env["PATH"] = path + ":" + env["PATH"]
    for key, value in kwargs.items():
        env[key] = value

    # run subprocess
    result = subprocess.call(
        command,
        env=env,
        shell=True,
        universal_newlines=True,
    )

    if result != 0:
        raise Exception("command failed")
