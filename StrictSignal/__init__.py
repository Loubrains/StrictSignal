"""This module provides a type-checking signal implementation for PySide6.QtCore.Signal.

When imported, it will automatically patch the Signal class to enforce type checking on signal emissions.

This module requires the signal to be emitted from a method of a QObject subclass.

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

from .StrictSignal import Signal
