import zce
class UnitModel :
    def __init__(self) :
        self.NumberofNumerator = 0
        self.NumberofDenominator = 0
        self.NumeratorCoefficient = []
        self.DenominatorCoefficient = []
        self.UnitStepRespLength = 0
        self.UnitStepResponse = []
        self.delay = 0
        self.StableGain = 0.0
        self.IntegralMark = 0
class SetupModelInput :
    def __init__(self) :
        self.InputNum = 0
        self.OutputNum = 0
        self.ControlModel = []
        self.PlantModel = []
        self.ControlModelFlag = 0
        self.PlantModelFlag = 0
        self.ControlInterval = 0
class SetupModelOutput :
    def __init__(self) :
        self.iOutput = 0
        self.szOutput = ""
        self.fOutput = 0.0
        self.dOutput = 0.0
        self.uModel = UnitModel()
def registe_class():
    zce.registe_class(UnitModel)
    zce.registe_class(SetupModelInput)
    zce.registe_class(SetupModelOutput)
