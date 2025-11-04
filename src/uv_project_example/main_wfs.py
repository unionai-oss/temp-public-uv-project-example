from pathlib import Path

import flyte
from flyte import Image

from uv_project_example.library_a.utils import some_test

ROOT_DIR = Path("./")

image = (
    Image.from_debian_base(python_version=(3, 12))
    .with_apt_packages("ca-certificates", "build-essential")
    .with_uv_project(pyproject_file="./pyproject.toml")
    .with_source_folder(Path("./src/data_loading"))
)


env = flyte.TaskEnvironment(name="v2-uv_project", image=image)


@env.task
async def t1(data: str = "hello") -> str:
    i = some_test()
    sql = Path("./data_loading/raw_data.sql")
    print(f"SQL file is a file: {sql.exists()}")
    print(f"SQL file path: {sql.resolve()}")
    return f"Hello {data} {i=}"

# PYTHONPATH=/Users/ytong/go/src/github.com/flyteorg/flyte-sdk/src: flyte -vvv -c ~/.flyte/demo.yaml run --root-dir `pwd`/src/ src/uv_project_example/main_wfs.py t1
if __name__ == "__main__":
    flyte.init_from_config(root_dir="./src")  # should we make this work?
    run = flyte.with_runcontext("local", ).run(t1, data="world")
    print(run.name)
    print(run.url)
