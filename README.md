# Mini ML Monolithic Plataform

Project to learn and discuss components of an ML Plataform. Therefore, this project will not be use in production environment, but will develop to behave as such.

### Why this name?

**Mini** -> A mini/small project version

**ML** -> For Machine Learning projects

**Monolithic** -> All Plataform components is in this project

**Plataform** -> Contains all model life cicle 

### Components

The project is divide in 5 components:

- Data Warehouse

- Development Env (Jupyter Notebooks)

- Model Logging

- Model Registry (In some cases know as Model Store)

- Model Serving

> Note: There's a README in each component with details as architecture, flows, implementations details and etc.

#### Development status components

- Data Warehouse: **TO DO**

Simple, tables in a CSV file. Manually generated.

- Development Env: **DOING**

Developing base notebooks. Manually generated.

- Model Logging: **DOING**

Saving logging in a file. Very simple.

- Model Registry: **DOING**

Module with more advanced development. For now saving metadata in files. 

- Model Serving: **DOING WITH ERRORS**

Code generated for tests, the management of models is simple. Component incompleted and must be appears errors.


### Missing Components
- Feature Store (Batch e Offline)
- Monitoring
- Logging and Observability
- Feature Engineering


### Techologies and Tools

| Tool      | Version     |
| --------  | ----------  |
| Python    | ^3.10       |
| Pandas    | ^2.2.3      |
| FastAPI   | ^0.115.12   |
| Sklearn   | ^1.6.1      |
| Notebook  | ^0.115.12   |
