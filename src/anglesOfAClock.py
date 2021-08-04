# Angles of the clock (Microsoft)
'''
Given a time in the format of hour and minute, calculate the angle of the 
hour and minute hand on a a clock.
'''

def calcAngle(h: int, m: int) -> float:
    if (type(h) is not int) or (type(m) is not int):
        raise Exception("Wrong input type!")
    
    ang = (-((h%12))/12*360+ ((m%60))/60*360)
    return ang

print(calcAngle(3, 30))
# 90
print(calcAngle(12, 30))
# 180
print(calcAngle(0,15))
# 90
print(calcAngle(0,45))
# 270
print(calcAngle(3,0))
# -90
print(calcAngle(9,45))
# 0
