# alu-back-end

Python scripts that gather data from the
[JSONPlaceholder](https://jsonplaceholder.typicode.com/) REST API.

## Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- `requests` module
- PEP 8 style, all files executable

## Files (`api/`)

| File | Description |
| --- | --- |
| `0-gather_data_from_an_API.py` | Prints an employee's TODO list progress |
| `1-export_to_CSV.py` | Exports an employee's tasks to `USER_ID.csv` |
| `2-export_to_JSON.py` | Exports an employee's tasks to `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all employees' tasks to `todo_all_employees.json` |

## Usage

```
./0-gather_data_from_an_API.py 2
./1-export_to_CSV.py 2
./2-export_to_JSON.py 2
./3-dictionary_of_list_of_dictionaries.py
```

