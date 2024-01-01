import zce,os,sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\PyTaiji'))
os.putenv("TCL_LIBRARY", os.path.join(os.path.dirname(__file__), '..\\Python312\\tcl\\tcl8.6'))

vm_rpcdemo = zce.zvm_new("rpcdemo", "./demo/rpcdemo_start.py")

#vm_rpcdemo = zce.zvm_new("rpcdemo2", "./demo/rpcdemo_start.py")

serv_obj = zce.rpc_serve("127.0.0.1", 36001)

