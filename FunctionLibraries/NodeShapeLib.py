## Created by Madhumitha Senthilvel

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

##     http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.


from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core.Common import *
from PyFlow.Core.GraphManager import *



class NodeShapeLib(FunctionLibraryBase):
    """doc string for NodeShapeLib"""
    def __init__(self, packageName):
        super(NodeShapeLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=(("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"})), meta={NodeMeta.CATEGORY: 'NodeShapeLib', NodeMeta.KEYWORDS: ['</>', "cardinality", "min/max"]})
    def NodeShape(Name_the_Node=("AnyPin",None,{PinSpecifires.CONSTRAINT:"1"}),
        targetclass=("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"})
        ):
            t=targetclass.replace(" ","")
            
            a="{} sh:targetClass ifc:{};".format(Name_the_Node,t)
            return a

    @staticmethod
    @IMPLEMENT_NODE(returns=(("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"})), meta={NodeMeta.CATEGORY: 'NodeShapeLib', NodeMeta.KEYWORDS: ['</>', "cardinality", "min/max"]})
    def Property(property_name=("AnyPin",None,{PinSpecifires.CONSTRAINT:"1"})):
            t=property_name.replace(" ","")
            
            #b=GraphManager.getUniqGraphPinName(self=b)

            a="sh:property [\nsh:path ifcowl:{};".format(t)
            return a

"""    @staticmethod
    @IMPLEMENT_NODE(returns=(("StringPin", None, {PinSpecifires.CONSTRAINT: "1"})), meta={NodeMeta.CATEGORY: 'NodeShapeLib', NodeMeta.KEYWORDS: ['</>', "cardinality", "min/max"]})
    def NodeShape(Prefix=("StringPin",None,{PinSpecifires.CONSTRAINT:"1"}),
            ShapeName=("StringPin", None, {PinSpecifires.CONSTRAINT: "1"}), 
            targetclass=("StringPin", None, {PinSpecifires.CONSTRAINT: "1"})):
            if Prefix=="@prefix ifc: <http://www.buildingsmart-tech.org/ifcOWL/IFC2x3_TC1#>.":
                p="ifc"
            else:
                p="test"
            a="{}:{} a NodeShape;\n sh:targetClass {};".format(p,ShapeName,targetclass)
            return a

            """