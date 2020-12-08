PACKAGE_NAME = 'SHACL'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.SHACL.Pins.DemoPin import DemoPin

# Function based nodes
from PyFlow.Packages.SHACL.FunctionLibraries.DataFileUpload import DataFileUpload


# Class based nodes
from PyFlow.Packages.SHACL.Nodes.SupportedOntology import SupportedOntology
from PyFlow.Packages.SHACL.Nodes.DirectConstraints import DirectConstraints
from PyFlow.Packages.SHACL.Nodes.LinkTraversal import LinkTraversal
from PyFlow.Packages.SHACL.Nodes.GetProperties import GetProperties
from PyFlow.Packages.SHACL.Nodes.OntologyClassesProperties import OntologyClassesProperties
from PyFlow.Packages.SHACL.Nodes.SHACLShape import SHACLShape
from PyFlow.Packages.SHACL.Nodes.Final_SHACL_Shape import Final_SHACL_Shape
from PyFlow.Packages.SHACL.Nodes.Cardinality import Cardinality
# Factories

_FOO_LIBS = {}
_NODES = {}
_PINS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_FOO_LIBS[DataFileUpload.__name__] = DataFileUpload(PACKAGE_NAME)


_NODES[SupportedOntology.__name__] = SupportedOntology
_NODES[DirectConstraints.__name__] = DirectConstraints
_NODES[LinkTraversal.__name__] = LinkTraversal
_NODES[GetProperties.__name__] = GetProperties
_NODES[OntologyClassesProperties.__name__] = OntologyClassesProperties
_NODES[SHACLShape.__name__] = SHACLShape
_NODES[Final_SHACL_Shape.__name__] = Final_SHACL_Shape
_NODES[Cardinality.__name__] = Cardinality

_PINS[DemoPin.__name__] = DemoPin


class SHACL(IPackage):
	def __init__(self):
		super(SHACL, self).__init__()

	@staticmethod
	def GetExporters():
		return _EXPORTERS

	@staticmethod
	def GetFunctionLibraries():
		return _FOO_LIBS

	@staticmethod
	def GetNodeClasses():
		return _NODES

	@staticmethod
	def GetPinClasses():
		return _PINS

	@staticmethod
	def GetToolClasses():
		return _TOOLS

