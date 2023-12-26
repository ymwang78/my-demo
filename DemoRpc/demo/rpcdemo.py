class ArgsMixed :
    def __init__(self) :
        self.anyVal = None
        self.i8Val = 0
        self.i8ValVec = []
        self.i16Val = 0
        self.i16ValVec = []
        self.i32Val = 0
        self.i32ValVec = []
        self.i64Val = 0
        self.i64ValVec = []
        self.fltVal = 0.0
        self.fltValVec = []
        self.dblVal = 0.0
        self.dblValVec = []
        self.strVal = ""

class ArgsDeepMixed :
    def __init__(self) :
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

def registe_class():

    import zce

    zce.registe_class(ArgsMixed)

    zce.registe_class(ArgsDeepMixed)

