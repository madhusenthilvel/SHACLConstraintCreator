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


class DirectConstraints(NodeBase):
    def __init__(self, name):
        super(DirectConstraints, self).__init__(name)
        self.ontologyinput = self.createInputPin('Ontology', 'StringPin', structure=StructureType.Single)
        self.ontologyinput.enableOptions(PinOptions.AllowMultipleConnections)
        self.ontologyinput.disableOptions(PinOptions.ChangeTypeOnConnection)

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
        helper.addInputStruct(StructureType.Single)
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
        return 'Creates a list from connected pins'

    def compute(self, *args, **kwargs):
        val=self.ontologyinput.getData()
        if val=="BOT":
            SHACLgenerator = """bot:BuildingShape
                            a sh:NodeShape ;
                            sh:targetClass bot:Building ;
                            sh:property [
                            sh:path rdfs:label ;
                            sh:minCount 1;
                            sh:datatype xsd:string;
                            ] ."""
        if val=="DOT":
            SHACLgenerator="World"
        self.SHACLgenerator.setData(SHACLgenerator)
        self.result.setData(True)
