# UV Project Example

Example repo for repro'ing the issues and desired UX from Kevin T. et al.

Goals:
* Able to run image builder only when dependencies change
* Able to access all Python and data files through the correct combination of files built into the Image and files in the Code Bundle.

A simple command like should be sufficient
```bash
flyte -c ~/.flyte/config-k3d.yaml run --root-dir ./src/ src/uv_project_example/main_wfs.py t1
```

## Kevin's issue:

### Having "--root-dir `pwd`" or without `--root-dir`
```bash
PYTHONPATH="."
flyte -vvv run --root-dir `pwd` src/uv_project_example/main_wfs.py t1
```
Gives the following structure (missing sql and csv):
```
12:04:26.523519 INFO     _packaging.py:56 -  File structure:                                                                                                                                                                                                                                                           
                         📂 /Users/kevin/temp-public-uv-project-example                                                                                                                                                                                                                                                
                         ┗━━ src                                                                                                                                                                                                                                                                                
                             ┣━━ core                                                                                                                                                                                                                                                                    
                             ┃   ┣━━ __init__.py                                                                                                                                                                                                                                                  
                             ┃   ┗━━ config.py                                                                                                                                                                                                                                                    
                             ┗━━ uv_project_example                                                                                                                                                                                                                                                      
                                 ┣━━ __init__.py                                                                                                                                                                                                                                                  
                                 ┣━━ library_a                                                                                                                                                                                                                                                    
                                 ┃   ┣━━ __init__.py                                                                                                                                                                                                                                       
                                 ┃   ┗━━ utils.py                                                                                                                                                                                                                                          
                                 ┗━━ main_wfs.py    
                                                            
                                                                                                                                                                                                                                                                                                                       
12:04:26.525201 DEBUG    bundle.py:145 -  Building code bundle.                                                                                                                                                                                                                                                        
12:04:26.534007 INFO     bundle.py:148 -  Code bundle created at /var/folders/ps/hgb6_5tn42b_nmbwzhsyt1f00000gn/T/tmp67q10u14/fast00c70228032bdf4e9ef44b889f1c7fda.tar.gz, size: 0.01953125 MB, archive size: 0.001064300537109375 MB   
```
In the Union UI these are the logs:
```
Nov 05 12:14:21.770 This is a test function from utils.py
Nov 05 12:14:21.770 SQL file is a file: False
Nov 05 12:14:21.770 SQL file path: /root/src/data_loading/raw_data.sql
Nov 05 12:14:21.770 CSV file is a file: False
Nov 05 12:14:21.770 CSV file path: /root/src/data_loading/some_data/my_data.csv
```

### Including `--root-dir`
```bash
PYTHONPATH="."
flyte -vvv run --root-dir `pwd`/src/ src/uv_project_example/main_wfs.py t1
```

Gives the following structure:
```
12:06:07.584601 INFO     _packaging.py:56 -  File structure:                                                                                                                                                                                                                                                           
                         📂 /Users/kevin/temp-public-uv-project-example/src/                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                       
12:06:07.585136 DEBUG    bundle.py:145 -  Building code bundle.                                                                                                                                                                                                                                                        
12:06:07.587943 INFO     bundle.py:148 -  Code bundle created at /var/folders/ps/hgb6_5tn42b_nmbwzhsyt1f00000gn/T/tmplyy8pkj3/fastd41d8cd98f00b204e9800998ecf8427e.tar.gz, size: 0.009765625 MB, archive size: 8.20159912109375e-05 MB                                                                                 
```
In the Union UI these are the logs (execution crashes):
```
Nov 05 12:06:18.995 ModuleNotFoundError: No module named 'uv_project_example'
Nov 05 12:06:18.995 
Nov 05 12:06:18.995 [ImportError Diagnostics]
Nov 05 12:06:18.995 Module 'uv_project_example' not found in either the Python virtual environment or the current working directory.
Nov 05 12:06:18.995 Current working directory: /root
Nov 05 12:06:18.995 Files found under current directory:
Nov 05 12:06:18.995   - _flyte_abs_context
Nov 05 12:06:18.995   - data_loading
Nov 05 12:06:18.995   - .bashrc
Nov 05 12:06:18.995   - .profile
Nov 05 12:06:18.995   - fastd41d8cd98f00b204e9800998ecf8427e.tar.gz
Nov 05 12:06:18.995   - .wget-hsts
Nov 05 12:06:18.995   - _flyte_abs_context/Users
Nov 05 12:06:18.995   - _flyte_abs_context/Users/kevin
Nov 05 12:06:18.995   - _flyte_abs_context/Users/kevin/temp-public-uv-project-example
Nov 05 12:06:18.995   - _flyte_abs_context/Users/kevin/temp-public-uv-project-example/uv.lock
Nov 05 12:06:18.995   - data_loading/some_data
Nov 05 12:06:18.995   - data_loading/__init__.py
Nov 05 12:06:18.995   - data_loading/raw_data.sql
Nov 05 12:06:18.995   - data_loading/some_data/my_data.csv
```


# Known issues today:
* `./src` doesn't work, needs the full path



