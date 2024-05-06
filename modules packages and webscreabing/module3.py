#normal import
import module1 as m1
import module2 as m2

print(m1.a)
print(m2.b)
m1.f1()
m2.f2()
#from import
from module1 import *
print(a)
f1()
from module2 import b
print(b)
#from import as ie lias
from module1 import f1 as f11
f11()
#packages
#import package.module
import package.mod1
print(package.mod1.a)
package.mod1.f1()
#from package import module
from package.mod1 import*
print(a)
from package import*
print(b)
f1()


