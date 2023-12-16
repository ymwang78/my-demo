import os, zce
from collections import defaultdict
from typing import List, Tuple
from demo.rpcdemo import *

def RpcCallVoid():
    print("RpcCallVoid")

def RpcCallInt32(iVal):
    print("RpcCallInt32", iVal)
    return iVal * 2

def RpcCallInt32Vec(iValVec):
    print("RpcCallInt32Vec", iValVec)
    iValVecOut = [ v * 2 for v in iValVec ]
    return iValVecOut

def RpcCallInt64(iVal):
    print("RpcCallInt64", iVal)
    return iVal * 2

def RpcCallInt64Vec(iValVec):
    print("RpcCallInt64Vec", iValVec)
    iValVecOut = [ v * 2 for v in iValVec ]
    return iValVecOut

def RpcCallDouble(dVal):
    print("RpcCallDouble", dVal)
    return dVal * 2

def RpcCallString(strVal):
    print("RpcCallString", strVal)
    return "RpcCallString" + strVal

def RpcCallMixed(tMixed):
    print("RpcCallMixed", tMixed)
    tMixed.iVal = tMixed.iVal * 2
    return tMixed

def RpcCallDeepMixed(tDeepMixed):
    print("RpcCallDeepMixed", tDeepMixed)
    tDeepMixed.ui8Val = tDeepMixed.ui8Val * 2
    tDeepMixed.tMixed.iVal = tDeepMixed.tMixed.iVal * 2
    return tDeepMixed

registe_class()

zce.registe_callable("RpcCallVoid", RpcCallVoid)
zce.registe_callable("RpcCallInt32", RpcCallInt32)
zce.registe_callable("RpcCallInt32Vec", RpcCallInt32Vec)
zce.registe_callable("RpcCallInt64", RpcCallInt64)
zce.registe_callable("RpcCallInt64Vec", RpcCallInt64Vec)
zce.registe_callable("RpcCallDouble", RpcCallDouble)
zce.registe_callable("RpcCallString", RpcCallString)
zce.registe_callable("RpcCallMixed", RpcCallMixed)
zce.registe_callable("RpcCallDeepMixed", RpcCallDeepMixed)

zce.registe_meta("demo/demo.ptl")

serv_obj = zce.rpc_serve("127.0.0.1", 36001)

#zce.rpc_close(serv_obj)

