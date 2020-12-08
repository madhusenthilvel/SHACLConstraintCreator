from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *


class OntologyClassesProperties(NodeBase):
    def __init__(self, name):
        super(OntologyClassesProperties, self).__init__(name)
        self.inp = self.createInputPin('Ontology', 'StringPin', structure=StructureType.Multi)
        self.out1 = self.createOutputPin('bot:Building', 'StringPin')
        self.out2 = self.createOutputPin('bot:Element', 'StringPin')
        self.out3 = self.createOutputPin('bot:Interface', 'StringPin')
        self.out4 = self.createOutputPin('bot:Site', 'StringPin')
        self.out5 = self.createOutputPin('bot:Space', 'StringPin')
        self.out6 = self.createOutputPin('bot:Storey', 'StringPin')
        self.out7 = self.createOutputPin('bot:Zone', 'StringPin')
        self.out8 = self.createOutputPin('bot:adjacentElement', 'StringPin')
        self.out9 = self.createOutputPin('bot:adjacentZone', 'StringPin')
        self.out10 = self.createOutputPin('bot:containsElement', 'StringPin')
        self.out11= self.createOutputPin('bot:containsZone', 'StringPin')
        self.out12 = self.createOutputPin('bot:interfaceOf', 'StringPin')
        self.out13 = self.createOutputPin('bot:intersectingElement', 'StringPin')
        self.out14 = self.createOutputPin('bot:intersectsZone', 'StringPin')
        self.out15 = self.createOutputPin('bot:has3DModel', 'StringPin')
        self.out16 = self.createOutputPin('bot:hasBuilding', 'StringPin')
        self.out17 = self.createOutputPin('bot:hasElement', 'StringPin')
        self.out18 = self.createOutputPin('bot:hasSubElement', 'StringPin')
        self.out19 = self.createOutputPin('bot:hasSpace', 'StringPin')
        self.out20 = self.createOutputPin('bot:hasZeroPoint', 'StringPin')
        self.out21 = self.createOutputPin('bot:hasSimple3DModel', 'StringPin')       



    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addOutputDataType('StringPin')
        helper.addInputStruct(StructureType.Multi)
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



