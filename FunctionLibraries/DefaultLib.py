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


import os
import platform
from copy import copy, deepcopy
from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow import getHashableDataTypes
from PyFlow.Core.Common import *
from PyFlow.Core.PathsRegistry import PathsRegistry
from nine import IS_PYTHON2
from rdflib import Graph


PIN_ALLOWS_ANYTHING = {PinSpecifires.ENABLED_OPTIONS: PinOptions.AllowAny | PinOptions.ArraySupported | PinOptions.DictSupported}


class DefaultLib(FunctionLibraryBase):
    """Default library builting stuff, variable types and conversions
    """

    def __init__(self, packageName):
        super(DefaultLib, self).__init__(packageName)

    """Prefixes"""
    @staticmethod
    @IMPLEMENT_NODE(returns=('StringPin', ''), meta={NodeMeta.CATEGORY: 'Prefixes', NodeMeta.KEYWORDS: []})
    def DASHDataShapes(DASHDataShapes=('StringPin', '')):
        '''add prefix.'''
        s="@prefix dash: <http://datashapes.org/dash#> .\n"
        return (s)

    @staticmethod
    @IMPLEMENT_NODE(returns=('StringPin', ''), meta={NodeMeta.CATEGORY: 'Prefixes', NodeMeta.KEYWORDS: []})
    def OWL(owl=('StringPin', '')):
        '''add prefix.'''
        s="@prefix owl: <http://www.w3.org/2002/07/owl#>.\n"
        return (s)

    @staticmethod
    @IMPLEMENT_NODE(returns=('StringPin', ''), meta={NodeMeta.CATEGORY: 'Prefixes', NodeMeta.KEYWORDS: []})
    def RDF(rdf=('StringPin', '')):
        '''add prefix.'''
        s="@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.\n"
        return (s)

    @staticmethod
    @IMPLEMENT_NODE(returns=('StringPin', ''), meta={NodeMeta.CATEGORY: 'Prefixes', NodeMeta.KEYWORDS: []})
    def RDFS(rdfs=('StringPin', '')):
        '''add prefix.'''
        s="@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.\n"
        return (s)

    @staticmethod
    @IMPLEMENT_NODE(returns=('StringPin', ''), meta={NodeMeta.CATEGORY: 'Prefixes', NodeMeta.KEYWORDS: []})
    def shacl(sh=('StringPin', '')):
        '''add prefix.'''
        s="@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.\n"
        return (s)

    @staticmethod
    @IMPLEMENT_NODE(returns=('StringPin', ''), meta={NodeMeta.CATEGORY: 'Prefixes', NodeMeta.KEYWORDS: []})
    def ifc(IFC=('StringPin', '')):
        '''add prefix.'''
        s="@prefix ifc: <http://www.buildingsmart-tech.org/ifcOWL/IFC2x3_TC1#>.\n"
        return (s)
    

