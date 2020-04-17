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


from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core.Common import *


class MathAbstractLib(FunctionLibraryBase):
    """doc string for MathAbstractLib"""
    def __init__(self, packageName):
        super(MathAbstractLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=(("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"})), meta={NodeMeta.CATEGORY: 'Math|Basic Functions', NodeMeta.KEYWORDS: ['+', 'append', "sum", "operator"]})
    def Add_Prefixes(a=("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"}), b=("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"}),
            c=("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"}), d= ("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"}),
            e=("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"}), f=("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"})):
        return a + b + c + d + e + f

    @staticmethod
    @IMPLEMENT_NODE(returns=(("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"})), meta={NodeMeta.CATEGORY: 'Creator', NodeMeta.KEYWORDS: ['+', 'append', "sum", "operator"]})
    def CreateSHACLFile(Prefixes=("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"}), 
            Constraining_Class_information=("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"}),
            Constraining_property_information=("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"}), 
            Constraints= ("AnyPin", None, {PinSpecifires.CONSTRAINT: "1"})):
            file=Prefixes+Constraining_Class_information+Constraining_property_information+Constraints
            f = open("D:\output.ttl", mode="w")
            f.write(file)
            '''g=Graph()
            file=Prefixes+Constraining_Class_information+Constraining_property_information+Constraints
            g.serialize(data=file,destination='D:\output.txt',serialize='turtle')'''
            return (file)
