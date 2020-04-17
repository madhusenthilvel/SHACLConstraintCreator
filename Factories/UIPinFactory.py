from PyFlow.UI.Canvas.UIPinBase import UIPinBase
from PyFlow.Packages.SHACL.Pins.DemoPin import DemoPin
from PyFlow.Packages.SHACL.UI.UIDemoPin import UIDemoPin


def createUIPin(owningNode, raw_instance):
    if isinstance(raw_instance, DemoPin):
        return UIDemoPin(owningNode, raw_instance)
    else:
        return UIPinBase(owningNode, raw_instance)
