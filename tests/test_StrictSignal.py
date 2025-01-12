import pytest
from PySide6.QtCore import QObject, QCoreApplication
from StrictSignal.StrictSignal import Signal


@pytest.fixture(scope="module")
def app():
    app = QCoreApplication([])
    yield app
    app.exit()


class CorrectDataType(QObject):
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.received = None
        self.signal.connect(self.on_signal)
        self.signal.emit("Hello, world!")

    def on_signal(self, text: str):
        self.received = text


def test_correct_data_type(app: QCoreApplication):
    test_instance = CorrectDataType()

    assert type(test_instance.received) == str
    assert test_instance.received == "Hello, world!"


class MultipleDataTypes(QObject):
    signal = Signal(str, int)

    def __init__(self):
        super().__init__()
        self.received = None
        self.signal.connect(self.on_signal)
        self.signal.emit("Hello, world!", 42)

    def on_signal(self, text: str, number: int):
        self.received = (text, number)


def test_multiple_data_types(app: QCoreApplication):
    test_instance = MultipleDataTypes()

    assert type(test_instance.received) == tuple
    assert len(test_instance.received) == 2
    assert type(test_instance.received[0]) == str
    assert type(test_instance.received[1]) == int
    assert test_instance.received[0] == "Hello, world!"
    assert test_instance.received[1] == 42


class IncorrectDataType(QObject):
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.received = None
        self.signal.connect(self.on_signal)
        self.signal.emit(42)

    def on_signal(self, text: str):
        self.received = text


def test_incorrect_data_type(app: QCoreApplication):
    with pytest.raises(TypeError):
        test_instance = IncorrectDataType()


class NoDataType(QObject):
    signal = Signal()

    def __init__(self):
        super().__init__()
        self.received = None
        self.signal.connect(self.on_signal)
        self.signal.emit()

    def on_signal(self):
        self.received = True


def test_no_data_type(app: QCoreApplication):
    test_instance = NoDataType()

    assert test_instance.received == True


class NoDataTypeIncorrect(QObject):
    signal = Signal()

    def __init__(self):
        super().__init__()
        self.received = None
        self.signal.connect(self.on_signal)
        self.signal.emit("Hello, world!")

    def on_signal(self):
        self.received = True


def test_no_data_type_incorrect(app: QCoreApplication):
    with pytest.raises(TypeError):
        test_instance = NoDataTypeIncorrect()


class EmitOutsideClass(QObject):
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.received = None
        self.signal.connect(self.on_signal)

    def on_signal(self, text: str):
        self.received = text


def test_emit_outside_class(app: QCoreApplication):
    test_instance = EmitOutsideClass()
    test_instance.signal.emit("Hello, world!")

    assert type(test_instance.received) == str
    assert test_instance.received == "Hello, world!"


class EmitOutsideClassWrongType(QObject):
    signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.received = None
        self.signal.connect(self.on_signal)

    def on_signal(self, text: str):
        self.received = text


def test_emit_outside_class_wrong_type(app: QCoreApplication):
    test_instance = EmitOutsideClassWrongType()
    with pytest.raises(TypeError):
        test_instance.signal.emit(42)
