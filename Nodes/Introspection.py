#This node was created by sbalot.
#Then node performs introspection and smart lookup. 
#It obtains the name of the object under consideration in an input pin
#Based on the input, it creates a lookup, and looks for subClassOf relationship and associated properties.

from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *


class DemoNode(NodeBase):
    def __init__(self, name):
        super(DemoNode, self).__init__(name)
        self.inp = self.createInputPin('inp', 'BoolPin')
        self.out = self.createOutputPin('out', 'BoolPin')

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('BoolPin')
        helper.addOutputDataType('BoolPin')
        helper.addInputStruct(StructureType.Single)
        helper.addOutputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'Generated from wizard'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def compute(self, *args, **kwargs):
        inputData = self.inp.getData()
        self.out.setData(not inputData)
