from sympy import Symbol
import math
theta=Symbol('theta')
u=Symbol('u')
t=Symbol('t')
g=Symbol('g')

theta=Symbol('theta')

x=Symbol('x')

from sympy import Limit,S

l=Limit(1/x,x,S,dir='-')     #limit,s burada sonsuzluk belirtir.
print(l)

t=Symbol('t')
t1=Symbol('t1')
delta_t=Symbol('delta_t')

st=5t**2+2t+8

st1=st.subs({t:t1})

st1_delta=(st.subs({t:t+delta_t}))

f_d=Limit((st1_delta-st1)/delta_t),0)

print(f_d)