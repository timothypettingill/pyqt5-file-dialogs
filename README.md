# pyqt5-file-dialogs
Interactive file selection prompts using Qt5.

## Usage

```python
import json
from pathlib import Path

from pyqt5filedialogs import get_open_filepath, get_save_filepath

def read_data():
    """
    Load data from a JSON file selected by the user.
    """
    filepath = get_open_filepath(caption="Select a JSON data file.")
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def export_config():
    """
    Export a config `dict` object to a JSON file selected by the user.
    """
    config = {
        'preferences': {
            'theme': 'light',
            'font_size': 16,
            'font_family': 'Roboto',
        }
    }

    config_dir = Path.home().joinpath('.config', 'myapp')
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    filepath = get_save_filepath(filter='JSON Files (*.json)')
    with open(filepath, 'w') as f:
        json.dump(config, f)
    return filepath.stat().st_size
```

## Installation

Install with pip.

```bash
$ pip install pyqt5filedialogs
```

## Dependencies

* `PySide2` - Qt5 bindings for Python.