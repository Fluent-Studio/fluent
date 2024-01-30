from Qt import QtCore


class SignalBus(QtCore.QObject):
    """ 全局事件总线 """

    send_log_signal = QtCore.Signal(str)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SignalBus, cls).__new__(cls, *args, **kwargs)

        return cls._instance


bus = SignalBus()
