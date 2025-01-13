# StrictSignal

## Overview

This module provides a type-checking signal implementation for PySide6.QtCore.Signal.

When imported, it will automatically patch the Signal class and override the emit method to enforce type checking on signal emissions.

## Installation

```bash
pip install git+https://github.com/Loubrains/StrictSignal
```

## Usage

```python
from StrictSignal import Signal
from PySide6.QtCore import QObject

class MyObject(QObject):
    signal = Signal(int)
```

## Example

```python
from StrictSignal import Signal
from PySide6.QtCore import QObject

class MyObject(QObject):
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.on_signal)
        self.signal.emit("Hello, world!")
        self.signal.emit(42)

    def on_signal(self, text: str):
        print(text)

obj = MyObject()
# Output:
# Hello, world!
# TypeError: 42 is not instance of <class 'str'>
```

## Contributing

Contributions are welcome!

## License

This project is licensed under the GNU General Public License v3.0 (GPLv3). See the [LICENSE](LICENSE) file for details.

### Dependency Licenses

- **PySide6**: Licensed under the LGPL v3. See [PySide6 License](https://doc.qt.io/qtforpython/licenses.html).
- **executing**: Licensed under the Apache License 2.0. See [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
