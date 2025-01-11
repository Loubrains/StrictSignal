from typing import Type

import inspect
from collections import defaultdict

import executing
from PySide6.QtCore import Signal as _Signal, SignalInstance

signals_map = defaultdict(dict)


def make_signal(*args: Type) -> _Signal:
    """Create a new Signal.

    args are stored with the signal name for type-checking upon signal emissions.
    """
    frame = inspect.currentframe().f_back

    node = executing.Source.executing(frame).node.parent
    signal_name = node.targets[0].id

    locals = inspect.getargvalues(frame).locals
    signals_map[(locals["__module__"], locals["__qualname__"])][signal_name] = args

    return _Signal(*args)


# patch QtCore.Signal for seamless usage
# PySide6.QtCore.Signal = make_signal
Signal = make_signal


old_emit = SignalInstance.emit


def new_emit(self, *args, **kwargs):
    """Method used to override SignalInstance.emit to enforce type checking on signal emissions.

    args are retrieved with the signal name and checked against the arguments passed to emit.
    """
    frame = inspect.currentframe().f_back

    node = executing.Source.executing(frame).node
    signal_name = node.func.value.attr

    clz = inspect.getargvalues(frame).locals["__class__"]
    types = signals_map[(clz.__module__, clz.__qualname__)][signal_name]

    # Type-checking
    for arg, type in zip(args, types):
        if not isinstance(arg, type):
            raise TypeError(f"{arg} is not instance of {type}")

    old_emit(self, *args, **kwargs)


SignalInstance.emit = new_emit
