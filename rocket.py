#!/usr/bin/env python3

import math
import sys

# REM ROCKET.BAS by Brian Tung
# REM
A = 1.032 # REM Earth gravity in light-years per year squared
try:
    D = float(sys.argv[1])
except IndexError:
    D = -1.0
while (D < 0.0) or (D > 100000000.0):
    D = float(input("Distance in light-years (0-100 million): "))
D1 = D / 2.0
T = math.sqrt(D1*D1 + (2.0*D1/A))
X = A * T
M = 1.0 # REM compute inverse sinh
if X < 0.0:
    M = -1.0
S = math.log(abs(X)+1.0)
S1 = S + 1.0
while True:
    X1 = (math.exp(S) - math.exp(S*-1.0)) / 2.0 - abs(X)
    S1 = X1 / (math.exp(S)+math.exp(S*-1.0)) / 2.0
    S = S - S1 
    if (abs(S1) <= 0.0000001):
        break
T1 = 1.0 / A*S*M
V = A*T/math.sqrt(1.0+(A*T)*(A*T))
print("Time on Earth: %013.3f years" % (2.0*T))
print("Time on board: %013.3f years" % (2.0*T1))
print("    Top speed: %0.11f c" % V)
# END
# REM  ---------------------------
# REM  APPEARED IN COMPUTERS IN
# REM  ASTRONOMY, SKY & TELESCOPE,
# REM  FEBRUARY 2002, PAGE 66
# REM  ---------------------------

