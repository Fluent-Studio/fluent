from fluent.nodes.base import EndNode
from fluent.utils import bus


class PrintNode(EndNode):
    NODE_NAME = 'Print Node'

    def execute_children(self):
        bus.send_log_signal.emit('/n'.join(self.output_value()))
