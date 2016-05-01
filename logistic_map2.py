from pylab import *
x0=abs(sin(random()))
r=linspace(1.8,4.0,2000)
for i in range(150):
    x0=r*x0*(1-x0)
    
print x0
for i in range(200):
    x0=r*x0*(1-x0)
    plot(r,x0,",",color="k")
