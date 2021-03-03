# Myfind

Console utility for find files and dirs.

## Instruction

`myfind [path] -name [PATTERN] -type [f|d]`

### Call example

`>> ls `

```
app.py
__init__.py
__main__.py
models.py
__pycache__
```

Call: `>> myfind . -type d`

Result:

```
__pycache__
```

Call: `>> myfind . -name mo*`

Result:

```
models.py
```

Call: `>> myfind . -name mo* -type d`

Result:

```
```

### Make example
To create venv:

`>> make venv`

To exec test:

`>> make test`

To exec lint:

`>> make lint`

