
ud = ['zhangtr','yulilong','zhanghanzhi','wanghan','zhanghailong']
cd = []
zzd = ['sry','sky','sle','sly']

#不同函数导入方法
import function2
function2.print_models(ud[:],cd)
print(cd)
import function2 as printing
printing.print_models(ud,cd[:])
print(cd)
from function2 import print_models as printing
printing(zzd,cd)

from function2 import *
print_models(ud,cd)

#情况，只打印了一次：ud在第一次被调用就已经变成空列表了




