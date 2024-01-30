from NodeGraphQt import BaseNode


class FluentBaseNode(BaseNode):
    def output_value(self):
        raise NotImplementedError()

    def execute_children(self):
        nodes = self.connected_output_nodes()
        for values in nodes.values():
            for node in values:
                node.execute_children()

    def get_output_value_by_port_name(self):
        data = {}
        for port, nodes in self.connected_input_nodes().items():
            data[port.name()] = [n.output_value() for n in nodes]
        return data


class StartNode(FluentBaseNode):
    __identifier__ = 'fluent.start'
    NODE_NAME = 'Start Node'

    def __init__(self):
        super(StartNode, self).__init__()
        self.add_output('output')

    def output_value(self):
        return None


class ConstantNode(FluentBaseNode):
    __identifier__ = 'fluent.constant'
    NODE_NAME = 'Constant Node'


class HelperNode(FluentBaseNode):
    __identifier__ = 'fluent.helper'
    NODE_NAME = 'Helper Node'


class EndNode(FluentBaseNode):
    __identifier__ = 'fluent.end'
    NODE_NAME = 'End Node'

    def __init__(self):
        super(EndNode, self).__init__()
        self.add_input('Data')

    def output_value(self):
        nodes = self.connected_input_nodes()

        nodes_infos = []
        for values in nodes.values():
            for node in values:
                nodes_infos.append(node.output_value())

        return nodes_infos
