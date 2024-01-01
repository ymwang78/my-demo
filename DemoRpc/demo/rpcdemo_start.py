import os, sys, zce
from collections import defaultdict
from typing import List, Tuple
from rpcdemo import *

def RpcCallVoid():
    print("RpcCallVoid")

def RpcCallInt32(iVal):
    print("RpcCallInt32", iVal)
    return iVal * 2

def RpcCallInt32Vec(iValVec):
    print("RpcCallInt32Vec", iValVec)
    iValVecOut = [ v  for v in iValVec ]
    return iValVecOut

def RpcCallInt64(iVal):
    print("RpcCallInt64", iVal)
    return iVal * 2

def RpcCallInt64Vec(iValVec):
    print("RpcCallInt64Vec", iValVec)
    iValVecOut = [ v  for v in iValVec ]
    return iValVecOut

def RpcCallFloat(dVal):
    print("RpcCallFloat", dVal)
    return dVal * 2

def RpcCallFloatVec(dValVec):
    print("RpcCallFloatVec", dValVec)
    dValVecOut = [ v for v in dValVec ]
    return dValVecOut

def RpcCallDouble(dVal):
    print("RpcCallDouble", dVal)
    return dVal * 2

def RpcCallDoubleVec(dValVec):
    print("RpcCallDoubleVec", dValVec)
    dValVecOut = [ v  for v in dValVec ]
    return dValVecOut

def RpcCallString(strVal):
    print("RpcCallString", strVal)
    return "RpcCallString" + strVal

def RpcCallMixed(tMixed):
    print("RpcCallMixed", tMixed)
    #tMixed.iVal = tMixed.iVal * 2
    return tMixed

def RpcCallDeepMixed(tDeepMixed):
    print("RpcCallDeepMixed", tDeepMixed)
    return tDeepMixed

def RpcCallDeepMixedVecArgs(ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec):
    print("RpcCallDeepMixedVecArgs", ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec)
    return (ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec)

def RpcCallDeepMixedVecArgsReturnList(ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec):
    print("RpcCallDeepMixedVecArgs", ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec)
    return [ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec]

class DemoClass:
    def __init__(self, name):
        self.name = name
        self.ui8Val = 0
        self.ui8ValVec = []
        self.ui16Val = 0
        self.ui16ValVec = []
        self.tMixed = ArgsMixed()
        self.ui32Val = 0
        self.ui32ValVec = []
        self.ui64Val = 0
        self.ui64ValVec = []
        self.tMixedVec = []

    def SetName(self, name):
        self.name = name
       
    def GetName(self):
        return self.name; 

    def SetStatus(self, ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec):
        self.ui8Val = ui8Val
        self.ui8ValVec = ui8ValVec
        self.ui16Val = ui16Val
        self.ui16ValVec = ui16ValVec
        self.tMixed = tMixed
        self.ui32Val = ui32Val
        self.ui32ValVec = ui32ValVec
        self.ui64Val = ui64Val
        self.ui64ValVec = ui64ValVec
        self.tMixedVec = tMixedVec
        print("SetStatus", ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec)

    def GetStatus(self):
        print("GetStatus", self.ui8Val, self.ui8ValVec, self.ui16Val, self.ui16ValVec, self.tMixed, self.ui32Val, self.ui32ValVec, self.ui64Val, self.ui64ValVec, self.tMixedVec)
        return (self.ui8Val, self.ui8ValVec, self.ui16Val, self.ui16ValVec, self.tMixed, self.ui32Val, self.ui32ValVec, self.ui64Val, self.ui64ValVec, self.tMixedVec)

def RpcDemoInstanceCreate(name):
    obj = DemoClass(name)
    return zce.registe_object(obj)

def RpcDemoInstanceSetStatus(obj, ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec):
    obj.SetStatus(ui8Val, ui8ValVec, ui16Val, ui16ValVec, tMixed, ui32Val, ui32ValVec, ui64Val, ui64ValVec, tMixedVec)

def RpcDemoInstanceGetStatus(obj):
    return obj.GetStatus()

def StartRpcServe():
    
    import inspect    
    
    registe_class()
    
    def get_functions():
        return [(name, obj) for name, obj in globals().items() if inspect.isfunction(obj)]

    # 当前模块中的所有函数
    current_module_functions = get_functions()
    for name, obj in current_module_functions:
        if (name.startswith("Rpc")):
            zce.registe_callable(name, obj)    

    zce.registe_meta(os.path.join(os.path.dirname(__file__), 'demo.ptl'))

StartRpcServe()

