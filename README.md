# Simple Python Data source

## Autor: Shantanu Narale

### Installation

Install uv and run the below commands.
```shell
uv build
```

The wheels are available in `dist/` folder. Place the wheels in Unity Catalog volume and use below code in notebook

```python
%pip install /Volumes/<name_of_catalog>/<name_of_schema>/<name_of_volue>/python_datasource-0.1.0-py3-none-any.whl
```
