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

registe_class()

zce.registe_callable("RpcCallVoid", RpcCallVoid)
zce.registe_callable("RpcCallInt32", RpcCallInt32)
zce.registe_callable("RpcCallInt32Vec", RpcCallInt32Vec)
zce.registe_callable("RpcCallInt64", RpcCallInt64)
zce.registe_callable("RpcCallInt64Vec", RpcCallInt64Vec)
zce.registe_callable("RpcCallFloat", RpcCallFloat)
zce.registe_callable("RpcCallFloatVec", RpcCallFloatVec)
zce.registe_callable("RpcCallDouble", RpcCallDouble)
zce.registe_callable("RpcCallDoubleVec", RpcCallDoubleVec)
zce.registe_callable("RpcCallString", RpcCallString)
zce.registe_callable("RpcCallMixed", RpcCallMixed)
zce.registe_callable("RpcCallDeepMixed", RpcCallDeepMixed)
zce.registe_callable("RpcCallDeepMixedVecArgs", RpcCallDeepMixedVecArgs)
zce.registe_callable("RpcCallDeepMixedVecArgsReturnList", RpcCallDeepMixedVecArgsReturnList)

zce.registe_meta("demo/demo.ptl")

#zce.rpc_close(serv_obj)

