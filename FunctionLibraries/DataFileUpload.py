## -*- coding: utf-8 -*-
## Copyright 2015-2019 Ilgar Lunin, Pedro Cabrera

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

## http://www.apache.org/licenses/LICENSE-2.0

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
import os
import os.path as osPath

import requests


class DataFileUpload(FunctionLibraryBase):
    '''
    Os.Path Library wrap
    '''

    def __init__(self, packageName):
        super(DataFileUpload, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", []), meta={NodeMeta.CATEGORY: 'DataFileUpload', NodeMeta.KEYWORDS: ["get", "File", "dir", "Directory", "path"]})
    def getFilesURL(URL=("StringPin", "", {PinSpecifires.INPUT_WIDGET_VARIANT: "PathWidget"})
    ):
        r=requests.get(URL,allow_redirects=True)
        open('file.ttl','wb').write(r.content)      
        '''Lists selected file full path'''
        return [osPath.join(URL)]

    @staticmethod
    @IMPLEMENT_NODE(returns=("StringPin", []), meta={NodeMeta.CATEGORY: 'DataFileUpload', NodeMeta.KEYWORDS: ["get", "File", "dir", "Directory", "path"]})
    def getFilesLocal(path=("StringPin", "", {PinSpecifires.INPUT_WIDGET_VARIANT: "PathWidget"}),
                filename=("StringPin","")
    ):
        '''Lists selected file full path'''
        return [osPath.join(path, filename)]
