from Qt import QtWidgets
from Qt import QtCore

from NodeGraphQt import NodeGraph
from fluent.utils import bus


class GraphMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(GraphMainWindow, self).__init__(parent)

        self.init_ui()
        self.init_menu()
        self.register_nodes()

    def init_ui(self):
        self.resize(1300, 800)
        self.setWindowTitle('Fluent Studio Graph')

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        layout = QtWidgets.QVBoxLayout(central_widget)

        self.graph = NodeGraph()
        self.graph_widget = self.graph.widget

        header_layout = QtWidgets.QHBoxLayout()
        header_layout.setAlignment(QtCore.Qt.AlignRight)

        self.run_button = QtWidgets.QPushButton('运行')
        header_layout.addWidget(self.run_button)

        self.log_view = QtWidgets.QPlainTextEdit()
        self.log_view.setReadOnly(True)

        layout.addLayout(header_layout)
        layout.addWidget(self.graph_widget)
        layout.addWidget(self.log_view)

        bus.send_log_signal.connect(self.set_log_view_text)
        self.run_button.clicked.connect(self.run_button_clicked)

    def init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('文件')

        new_action = QtWidgets.QAction('新建', self)
        open_action = QtWidgets.QAction('打开', self)
        save_action = QtWidgets.QAction('保存', self)
        save_action.setShortcut('Ctrl+S')
        save_as_action = QtWidgets.QAction('另存为', self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)

    def run_button_clicked(self):
        try:
            self.set_log_view_text('开始运行啦<br>sss')
        except:
            import traceback
            self.set_log_view_text(traceback.format_exc(), 'error')

    def set_log_view_text(self, text, text_type='info'):
        text_color_by_type = {
            'info': 'black',
            'error': 'red'
        }
        self.log_view.appendHtml(
            '<p style="color:{}">{}</p>'.format(
                text_color_by_type[text_type],
                text.replace('\n', '<br/>'),
            ))

    def register_nodes(self):
        pass


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication([])
    gmw = GraphMainWindow()
    gmw.show()
    app.exec_()
