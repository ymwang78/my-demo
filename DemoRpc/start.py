import zce,os,sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\PyTaiji'))
os.putenv("TCL_LIBRARY", 'D:\\Github\\cxxproj\\DingCheng\\bin\\x64\\Python312\\tcl\\tcl8.6')

#import examples.example1

#run tj010 in "main" vm
import tj010.tj010_start

#vm_rpcdemo = zce.zvm_new("rpcdemo", "./demo/rpcdemo_start.py")

#vm_rpcdemo = zce.zvm_new("rpcdemo2", "./demo/rpcdemo_start.py")

#vm_tj010 = zce.zvm_new("tj010", "./tj010/start.py")

#zce.zvm_new("example", "./examples/example1.py")

serv_obj = zce.rpc_serve("127.0.0.1", 36001)


vm_example = zce.zvm_new("example", "../PyTaiji/examples/example_rpc.py")
