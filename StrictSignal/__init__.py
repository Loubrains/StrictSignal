"""This module provides a type-checking signal implementation for PySide6.QtCore.Signal.

When imported, it will automatically patch the Signal class and override the emit method to enforce type checking on signal emissions.

---
Usage:
---
```python
from StrictSignal import Signal
from PySide6.QtCore import QObject

class MyObject(QObject):
    signal = Signal(int)
```

---
Example:
---
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
"""

__version__ = "1.0.0"

from .StrictSignal import Signal
