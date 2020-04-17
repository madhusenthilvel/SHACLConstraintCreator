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


class ConstraintsLib(FunctionLibraryBase):
    """doc string for ConstraintsLib"""
    def __init__(self, packageName):
        super(ConstraintsLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=(("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"})), meta={NodeMeta.CATEGORY: 'Constraints', NodeMeta.KEYWORDS: ['</>', "cardinality", "min/max"]})
    def cardinality(path=("AnyPin",None, {PinSpecifires.CONSTRAINT:"1"}),
        MinCount=("IntPin", None, {PinSpecifires.CONSTRAINT: "1"}), 
        MaxCount=("IntPin", None, {PinSpecifires.CONSTRAINT: "1"})):
        a="sh:minCount {};\nsh:maxCount {};\n].".format(path,MinCount,MaxCount)
        return a

    @staticmethod
    @IMPLEMENT_NODE(returns=(("StringPin", None, {PinSpecifires.CONSTRAINT: "1"})), meta={NodeMeta.CATEGORY: 'Constraints', NodeMeta.KEYWORDS: ['</>', "cardinality", "min/max"]})
    def Select_Properties(property1=("StringPin",None, {PinSpecifires.CONSTRAINT:"1"}),
        property2=("StringPin",None, {PinSpecifires.CONSTRAINT:"1"}),
        property3=("StringPin",None, {PinSpecifires.CONSTRAINT:"1"})):
        return property1
        return property2
        return property3

    @staticmethod
    @IMPLEMENT_NODE(returns=(("StringPin", None, {PinSpecifires.CONSTRAINT: "1"})), meta={NodeMeta.CATEGORY: 'Constraints', NodeMeta.KEYWORDS: ["data type"]})
    def datatype(
        String=("BoolPin",False),
        Int=("BoolPin",False),
        Float=("BoolPin",False),
        Boolean=("BoolPin",False)):
        if String:
            datatype="String"
        if Int:
            datatype="Int"
        if Float:
            datatype="Float"
        if Boolean:
            datatype="bool"
        a="sh:datatype {};\n".format(datatype)
        return a
