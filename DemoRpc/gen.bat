rem ===========================================================================================
cd demo

zgen -t zpy -f * -i demo.ptl -o rpcdemo
zgen -t header_zds -f * -I ding_inc.h -i demo.ptl -o rpcdemo
zgen -t cpp_zds -f * -I ding_inc.h -I rpcdemo.h -I rpcdemo_pack.h -i demo.ptl -o rpcdemo

cd ..
