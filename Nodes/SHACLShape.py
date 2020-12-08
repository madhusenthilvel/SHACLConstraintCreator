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

from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF , XSD

class SHACLShape(NodeBase):
    def __init__(self, name):
        super(SHACLShape, self).__init__(name)
        #Target Class Pin
        self.input1 = self.createInputPin('Target Class', 'StringPin', structure=StructureType.Single)
        self.input1.enableOptions(PinOptions.AllowMultipleConnections)
        self.input1.disableOptions(PinOptions.ChangeTypeOnConnection)
        #Target Property Pin
        self.input2 = self.createInputPin('Target Property', 'StringPin', structure=StructureType.Single)
        self.input2.enableOptions(PinOptions.AllowMultipleConnections)
        self.input2.disableOptions(PinOptions.ChangeTypeOnConnection)
        #Constraint Pin
        self.input3 = self.createInputPin('Constraint', 'AnyPin', structure=StructureType.Single)
        self.input3.enableOptions(PinOptions.AllowMultipleConnections)
        self.input3.enableOptions(PinOptions.ChangeTypeOnConnection)

        self.SHACLgenerator = self.createOutputPin('SHACLShapes', 'StringPin', structure=StructureType.Multi)
        self.SHACLgenerator.disableOptions(PinOptions.ChangeTypeOnConnection)

        self.result = self.createOutputPin('result', 'BoolPin')
        self.checkForErrors()

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('StringPin')
        helper.addInputDataType('StringPin')
        helper.addInputDataType('AnyPin')
        helper.addOutputDataType('StringPin')
        helper.addOutputDataType('BoolPin')
        helper.addInputStruct(StructureType.Single)
        helper.addInputStruct(StructureType.Single)
        helper.addInputStruct(StructureType.Single)
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
        return 'Creates SHACL shape from given Target Class, Property and Constraint'

    def compute(self, *args, **kwargs):
        #Target Class
        val1=self.input1.getData()
        #Define name of the SHACL shape based on the TargetClass
        ShapeName=val1+"Shape"
        #Target Property
        val2=self.input2.getData()

        #Find out which constraint type: Cardinality/DataType/MinMax
        a=[]
        a=self.input3.getData()
        val3=a[2]
        if val3==1:
        #Generate SHACL for Cardinality Constraint
            constraint_data="""sh:minCount {minCount};
                            sh:maxCount {maxCount};
                            """.format(minCount=a[0],maxCount=a[1])
        #Serialize this ttl


        #Generate SHACLShape for the Class, property and constraint
        SHACLgenerator = """{shapename}
                            bot:BuildingShape
                            a sh:NodeShape ;
                            sh:targetClass {Target_Class} ;
                            sh:property [
                            sh:path {Target_Property} ;
                            {constraint_data}
                            ] .""" .format(shapename=ShapeName,Target_Class=val1, Target_Property=val2,constraint_data=constraint_data)
        """
        #Serialize this as ttl
        g2= Graph()

        data = Namespace("http://www.instancedata.org#")
        shacl = Namespace("http://www.w3.org/ns/shacl#")
        bot = Namespace("https://w3id.org/bot#")
        g2.add((URIRef(bot.ShapeName),))"""

        self.SHACLgenerator.setData(SHACLgenerator)
        self.result.setData(True)
