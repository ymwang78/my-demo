import os, zce
from collections import defaultdict
from typing import List, Tuple
from tj010 import *
#from DLL007data import InputVariable, OutputVariable, UnitModel

print("hello, world!")

class Controller:
    def NoneArg(self):
        print("NoneArg")
        
    def SetupModel(self, 
                    InputNum: int,    # 输入变量总数        
                    OutputNum: int,   # 输出变量总数
                    ControlModel: List[UnitModel],     # 控制模型 typModel结构的二维数组
                                                       # 维数：（int输出变量总数, int输入变量总数），用于模型预测
                    PlantModel: List[UnitModel],    #工厂模型 typModel结构的二维数组
                                                    # 维数：（int输出变量总数, int输入变量总数），用于仿真时的工厂模型递推。
                    ControlModelFlag: int,  # 控制模型标志    
                                            # 为1，表示模型预测时使用的阶跃响应序列由传递函数计算得来
                                            # 为0，表示模型预测直接使用客户程序给定的阶跃响应序列
                    PlantModelFlag: int,    # 工厂模型标志    
                                            # 为1，表示仿真时工厂模型递推使用的阶跃响应序列由传递函数计算得来
                                            # 为0，表示仿真时工厂模型递推直接使用客户程序给定的阶跃响应序列
                    ControlInterval: int,   # 控制周期, 要与客户程序生成阶跃响应序列时使用的控制周期一致
                    **kargs                 # 输入输出变量名称数组，分别存放于InputTagName和OutputTagName
                    ) -> SetupModelOutput:
        print("SetupModel", InputNum, ControlInterval)
        #return [3.0, 4.0]

        outPut = SetupModelOutput()
        outPut.dOutput = 3.123456789012345678901
        outPut.fOutput = 1.1234567890123456
        outPut.szOutput = "hello,world"
        outPut.uModel = UnitModel()
        outPut.uModel.delay = 100
        outPut.uModel.StableGain = 10.212
        return outPut

    def Control(self, mat):
        pass
    
def PureFunctionCall(msg):
    print(msg)

def NoneArgFunctionCall(msg):
    print("NoneArgFunctionCall")
    
o = zce.zobject()

o2 = o

con = Controller()

registe_class()

zce.registe_callable("NoneArg", con.NoneArg)

zce.registe_callable("SetupModel", con.SetupModel)

zce.registe_callable("PureFunctionCall", PureFunctionCall)

zce.registe_callable("NoneArgFunctionCall", NoneArgFunctionCall)

zce.registe_meta("tj010.ptl")

serv_obj = zce.rpc_serve("127.0.0.1", 36001)

#zce.rpc_close(serv_obj)

