import json
import math

def lift(CL,ro,S,V):  # calculate lift
        L = (CL * ro * S * (V ** 2)) / 2
        return L 

def stallspeed(W,g,ro,S,CL):  # calculate stallspeed
        Vs = ((2 * W * g) /(ro * S * CL)) ** (1 / 2)
        return Vs

def drag(ro,V,CD,S):  # calculate drag
        D = (ro * (V ** 2) * CD * S) / 2
        return D
