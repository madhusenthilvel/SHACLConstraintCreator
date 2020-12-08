from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *


class SupportedOntology(NodeBase):
    def __init__(self, name):
        super(SupportedOntology, self).__init__(name)
        self.out = self.createOutputPin('BOT', 'StringPin',defaultValue="BOT")
        self.out = self.createOutputPin('DOT', 'StringPin',defaultValue="DOT")
        self.out = self.createOutputPin('ifcOWL', 'StringPin',defaultValue="ifcOWL")

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addOutputDataType('StringPin')
        helper.addInputStruct(StructureType.Single)
        helper.addOutputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'ONTOLOGY DATABASE'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."



