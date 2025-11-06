
    
def calcirumference( radius: float)->float:
     ''' return the circumference on the radius '''
     return 2*(22/7)* radius
def calcircumference(radius=None, diameter=None):
    ''' return area of the  circle based on radius of the diameter  '''
    if radius is not None:
        return 22/7 * radius **2
    elif diameter is not None:
        return 22/7 *(diameter/22)**2