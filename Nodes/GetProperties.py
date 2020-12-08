'''

'''

from PyFlow.Packages.PyFlowFreeCAD.Nodes import *
from PyFlow.Packages.PyFlowFreeCAD.Nodes.FreeCAD_Base import timer, FreeCadNodeBase, FreeCadNodeBase2


class GetProperties(FreeCadNodeBase2):
    '''
    load and save objects in FreeCAD document
    '''

    dok=4
    def __init__(self, name="MyObject"):
        super(self.__class__, self).__init__(name)

        self.inp1 = self.createInputPin('Ontology', 'AnyPin', None, self.compute)
        self.inp2 = self.createInputPin('Instance', 'AnyPin', None, self.compute)

        self.shapeout = self.createOutputPin('Shape_out', 'ShapePin')

        self.objname = self.createInputPin("objectname", 'String')
        self.objname.setData("Box")

        self.createInputPin('Reload_from_FC', 'ExecPin', None, self.reload)
        self.createInputPin('Store_to_FC', 'ExecPin', None, self.store,)




    def reload(self, *args, **kwargs):
        print ("reload from FreeCADobject and refresh data")
        import nodeeditor.dev
        reload (nodeeditor.dev)
        nodeeditor.dev.reload_obj(self)
        sayl()



    def store(self, *args, **kwargs):

        print ("store  data to  FreeCAD object and to the output pins" )

        data={}
        pps=self.getOrderedPins()
        for p in pps:
            dat=p.getData()
            print ("#+#+#",p.getName(),dat)
            data[str(p.name)+"_out"]=dat

        say("data")
        say(data)
        say("pps")
        say(pps)

        for p in pps:
            if p.group=='FOP':
                n=p.getName()
                if n.endswith('_out'):
                    p.setData(data[str(n)])
                    pn=n[:-4]
                    vn=data[str(n)]
                    say("set",n,pn,vn)
                    setattr(self.fob,pn,vn)
                    continue

                try:
                    pn=n.split('_')[1]
                    if pn=="Object": # hack for names FreeCAD_Object #+#
                        pn=n.split('_')[2]

                    vn=p.getData()

                    try:
                        v=self.fob.getPropertyByName(pn).Value
                    except:
                        v=self.fob.getPropertyByName(pn)
                    say("change value",n,pn,v,vn)
                    if v  !=  vn:  # value has changed
                        setattr(self.fob,pn,vn)
                except:
                    sayl("problem with store",n)
    
        FreeCAD.activeDocument().recompute()



    def createPins(self, *args, **kwargs):
        say('hack outsourced to nodeetitor.dev')
        import nodeeditor.dev
        reload (nodeeditor.dev)
        return  nodeeditor.dev.runraw(self)
        say("pins created")


    @staticmethod
    def description():
        return GetProperties.__doc__

    @staticmethod
    def category():
        return 'Information'

    @staticmethod
    def keywords():
        return []

__all__= [
		GetProperties,
	]

def nodelist():
	return __all__
