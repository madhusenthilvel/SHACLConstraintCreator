PACKAGE_NAME = 'SHACL'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.SHACL.Pins.DemoPin import DemoPin

# Function based nodes
from PyFlow.Packages.SHACL.FunctionLibraries.DefaultLib import DefaultLib
from PyFlow.Packages.SHACL.FunctionLibraries.MathAbstractLib import MathAbstractLib
from PyFlow.Packages.SHACL.FunctionLibraries.ConstraintsLib import ConstraintsLib
from PyFlow.Packages.SHACL.FunctionLibraries.NodeShapeLib import NodeShapeLib

# Class based nodes
from PyFlow.Packages.SHACL.Nodes.DemoNode import DemoNode

# Tools
from PyFlow.Packages.SHACL.Tools.DemoShelfTool import DemoShelfTool
from PyFlow.Packages.SHACL.Tools.DemoDockTool import DemoDockTool

# Exporters
from PyFlow.Packages.SHACL.Exporters.DemoExporter import DemoExporter

# Factories
from PyFlow.Packages.SHACL.Factories.UIPinFactory import createUIPin
from PyFlow.Packages.SHACL.Factories.UINodeFactory import createUINode
from PyFlow.Packages.SHACL.Factories.PinInputWidgetFactory import getInputWidget
# Prefs widgets
from PyFlow.Packages.SHACL.PrefsWidgets.DemoPrefs import DemoPrefs

_FOO_LIBS = {
	DefaultLib.__name__:DefaultLib(PACKAGE_NAME),
	MathAbstractLib.__name__:MathAbstractLib(PACKAGE_NAME),
	ConstraintsLib.__name__:ConstraintsLib(PACKAGE_NAME),
	NodeShapeLib.__name__:NodeShapeLib(PACKAGE_NAME)
}
_NODES = {}
_PINS = {}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()


_NODES[DemoNode.__name__] = DemoNode

_PINS[DemoPin.__name__] = DemoPin

_TOOLS[DemoShelfTool.__name__] = DemoShelfTool
_TOOLS[DemoDockTool.__name__] = DemoDockTool

_EXPORTERS[DemoExporter.__name__] = DemoExporter

_PREFS_WIDGETS["Demo"] = DemoPrefs


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

	@staticmethod
	def UIPinsFactory():
		return createUIPin

	@staticmethod
	def UINodesFactory():
		return createUINode

	@staticmethod
	def PinsInputWidgetFactory():
		return getInputWidget

	@staticmethod
	def PrefsWidgets():
		return _PREFS_WIDGETS

