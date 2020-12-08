from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *

class LinkTraversal(NodeBase):
    '''
    load and save objects in FreeCAD document
    '''

    dok=4
    def __init__(self, name="MyObject"):
        super(self.__class__, self).__init__(name)
        self.PredicatePattern = self.createInputPin('Predicate Pattern', 'StringPin', structure=StructureType.Multi)
        self.FirstPredicate = self.createInputPin('First Predicate', 'StringPin', structure=StructureType.Multi)
        self.PredicatePattern.enableOptions(PinOptions.AllowMultipleConnections)
        self.PredicatePattern.disableOptions(PinOptions.ChangeTypeOnConnection)

        self.SHACLgenerator = self.createOutputPin('SHACLShapes', 'StringPin', structure=StructureType.Multi)
        self.SHACLgenerator.disableOptions(PinOptions.ChangeTypeOnConnection)

        self.result = self.createOutputPin('result', 'BoolPin')
        self.checkForErrors()

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addOutputDataType('StringPin')
        helper.addOutputDataType('BoolPin')
        helper.addInputStruct(StructureType.Multi)
        helper.addOutputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return 'CONSTRAINTS'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'Link Traversal and Pattern Validation'

    def compute(self, *args, **kwargs):
        SHACLgenerator='''
        bot:subgraphvalidation1
            sh:targetObjectsOf {val1} ;
            sh:property [
                sh:path  ({val2}) ;
                sh:message "Property chain is broken" ;
                sh:minCount 1
            ] .'''.format(val1=self.FirstPredicate.getData(), val2=self.PredicatePattern.getData())

        self.SHACLgenerator.setData(SHACLgenerator)
        self.result.setData(True)