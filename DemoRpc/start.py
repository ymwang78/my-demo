import os, zce
from collections import defaultdict
from typing import List, Tuple

vm_rpcdemo = zce.zvm_new("rpcdemo", "./demo/rpcdemo_start.py")

vm_rpcdemo = zce.zvm_new("rpcdemo2", "./demo/rpcdemo_start.py")

serv_obj = zce.rpc_serve("127.0.0.1", 36001)

