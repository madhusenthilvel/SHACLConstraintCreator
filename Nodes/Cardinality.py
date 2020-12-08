from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *

class Cardinality(NodeBase):
    def __init__(self, name):
        super(self.__class__, self).__init__(name)
        self.input1 = self.createInputPin('minValue', 'IntPin', structure=StructureType.Single)
        self.input2 = self.createInputPin('maxValue', 'IntPin', structure=StructureType.Single)
        self.output1 = self.createOutputPin('minValue', 'IntPin', structure=StructureType.Array)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addInputputDataType('StringPin')
        helper.addInputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'CONSTRAINTS'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'Cardinality Constraint'

    def compute(self, *args, **kwargs):

        code =1
        output1=[]
        output1.append(self.input1.getData())
        output1.append(self.input2.getData())
        output1.append(code)

        self.output1.setData(output1)
        
"""
        self.output1.setData(input1)
        self.output2.setData(input2)
        """