##################################################
#
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
##################################################
	   
def PolygonArea(lstPnts):

    ##################################################
    #
    # Calculation of Signed Area of Polygon
    #
    # Pnts: List of Points.  The list contains tuples
    #       the first element is the x value and the
    #       second is y.
    #
    # The code assumes that the points form a 'closed'
    # polygon, i.e. the first point is duplicated at
    # the end of the array.  Check the documentation
    # of the data source.  If the polygon is not
    # 'closed, some extra code will be needed to handle
    # the first and last points.
    #
    # Note
    #
    # Code originally written in VB.net
    #
    ##################################################
                    
    # Declarations - Area
        
    fltArea = 0.0
        
    # Area Calculation
        
    for i in range(len(lstPnts)-1):
        fltArea += lstPnts[i][0] * lstPnts[i + 1][1] - lstPnts[i + 1][0] * lstPnts[i][1]
        print i,fltArea
      
    fltArea *= 0.5
        
    # Return the signed area
        
    return fltArea
        
##################################################
#
# Test code for Polygon Area
#
# If Clockwise is set to true, then Pnt contains
# a clockwise polygon, if false the test data
# is an anticlockwise polygon.
#
##################################################
        
# Empty list for points

lstPnts = []
                     
# Test - Clockwise or Anticlockwise
        
blnClockwise = True
        
# Test Data
        
if blnClockwise:
    lstPnts.append((10.0,10.0))     # Start
    lstPnts.append((10.0,5.0))       
    lstPnts.append((5.0,5.0))
    lstPnts.append((5.0,10.0))      # End
    lstPnts.append((10.0,10.0))     # Start repeated to close polygon
else:   
    lstPnts.append((10.0,10.0))     # Start
    lstPnts.append((5.0,10.0))        
    lstPnts.append((5.0,5.0))
    lstPnts.append((10.0,5.0))      # End
    lstPnts.append((10.0,10.0))     # Start repeated to close polygon
        
# Dump Area
        
print PolygonArea(lstPnts)
