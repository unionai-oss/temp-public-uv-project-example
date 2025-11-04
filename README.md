# UV Project Example

Example repo for repro'ing the issues and desired UX from Kevin T. et al.

Goals:
* Able to run image builder only when dependencies change
* Able to access all Python and data files through the correct combination of files built into the Image and files in the Code Bundle.

A simple command like should be sufficient
```bash
flyte -c ~/.flyte/config-k3d.yaml run --root-dir ./src/ src/uv_project_example/main_wfs.py t1
```

Known issues today:
* `./src` doesn't work, needs the full path



