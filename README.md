## Directory structure generation

01. UI Layer
02. Application Layer
03. Data Layer
04. ML Layer
05. Reporting Layer
06. Utility Layer
07. Data Jobs
08. ML Jobs
09. Data Lib
10. ML Lib

```bash
mkdir modern_app && mkdir -p ./modern_app/{ui_layer,application_layer,data_layer,ml_layer,reporting_layer,utility_layer,data_jobs,ml_jobs,data_lib,ml_lib}  && cd modern_app && touch README.md && find . -type d -empty -not -path "./.git/*" -exec touch {}/{.gitkeep,Dockerfile,README.md,.env,mkdocs.yml,VERSION,requirements.txt,Makefile,setup.py,pyproject.toml} \; && mkdir -p ./ui_layer/{app,data,backup,wiki,library} && mkdir -p ./application_layer/{app,data,backup,wiki,library} && mkdir -p ./data_layer/{app,data,backup,wiki,library} && mkdir -p ./ml_layer/{app,data,backup,wiki,library} && mkdir -p ./reporting_layer/{app,data,backup,wiki,library} && mkdir -p ./utility_layer/{app,data,backup,wiki,library} && mkdir -p ./data_jobs/{app,data,backup,wiki,library} && mkdir -p ./ml_jobs/{app,data,backup,wiki,library} && mkdir -p ./data_lib/{src,data,backup,wiki,notebooks} && mkdir -p ./ml_lib/{src,data,backup,wiki,notebooks} && find . -type d -empty -not -path "./.git/*" -exec touch {}/{README.md,.env,__init__.py,__main__.py} \; && git init && git add . && git commit -m "inital directory structure creation." && code .
```