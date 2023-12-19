rem ===========================================================================================
cd demo
zgen -t zpy -f * -i demo.ptl -o rpcdemo
zgen -t header_zds -f * -I ding_inc.h -i demo.ptl -o rpcdemo
zgen -t cpp_zds -f * -I ding_inc.h -I rpcdemo.h -I rpcdemo_pack.h -i demo.ptl -o rpcdemo
move /y *.h ../../../../ding/
move /y *.cpp ../../../../ding/
cd ..

cd tj010
zgen -t zpy -f * -i tj010.ptl -o tj010
zgen -t header_zds -f * -I ding_inc.h -i tj010.ptl -o tj010
zgen -t cpp_zds -f * -I ding_inc.h -I tj010.h -I tj010_pack.h -i tj010.ptl -o tj010
move /y *.h ../../../../ding/
move /y *.cpp ../../../../ding/
cd ..

pause