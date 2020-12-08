## Copyright 2015-2019 Ilgar Lunin, Pedro Cabrera

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

##     http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.


from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *

from rdflib import Namespace, URIRef, Graph
from rdflib.namespace import RDF, FOAF


class Final_SHACL_Shape(NodeBase):
    def __init__(self, name):
        super(Final_SHACL_Shape, self).__init__(name)
        #Input All SHACL shapes
        self.input1 = self.createInputPin('Input SHACL shapes', 'StringPin', structure=StructureType.Array)
        self.input1.enableOptions(PinOptions.AllowMultipleConnections)
        self.input1.disableOptions(PinOptions.ChangeTypeOnConnection)

        #Final SHACL shape pin
        self.output1 = self.createOutputPin('Generate', 'StringPin', structure=StructureType.Multi)
        self.output1.disableOptions(PinOptions.ChangeTypeOnConnection)

        self.result = self.createOutputPin('result', 'BoolPin')
        self.checkForErrors()

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addOutputDataType('StringPin')
        helper.addOutputDataType('BoolPin')
        helper.addInputStruct(StructureType.Array)
        helper.addOutputStruct(StructureType.Multi)
        return helper

    @staticmethod
    def category():
        return 'GENERATOR'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'Create final SHACL shape'

    def compute(self, *args, **kwargs):
        output1=[]
        for i in sorted(self.input1.affected_by, key=lambda pin: pin.owningNode().y):
            output1.append(i.getData())

        f=open("D:/ProgramFiles/FREECADv_19/Mod/PyFlow/PyFlow/Packages/SHACL/Data/FinalSHACLShapes.ttl","w")
        f.write(str(output1))

        """
        #Trying file writing with RDFLib - WORKS, BUT GOING TO TRY WITHOUT RDFLIB
        g = Graph()
        g.parse("https://gist.githubusercontent.com/kal/ee1260ceb462d8e0d5bb/raw/1364c2bb469af53323fdda508a6a579ea60af6e4/log_sample.ttl", format="ttl")
        g.serialize(destination="D:/ProgramFiles/FREECADv_19/Mod/PyFlow/PyFlow/Packages/SHACL/Data/output1.ttl", format ="ttl")
        """
        self.output1.setData('42')
        self.result.setData(True)
