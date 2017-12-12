import math
from Tkinter import *           # The Tkinter package
import Pmw                      # The Python MegaWidget package
master = Tk()                   # build Tk-environment

g = Pmw.Blt.Graph( master )     # make a new graph area
g.pack( expand=1, fill='both' )
 
# Make a set of x- and y-coordinates
def f(x):
    return int(10*math.sin(x/40.0))

vector_x = range(400)
vector_y = map(f,vector_x)

# create graph with label, x-data, and y-data
g.line_create( "f(x)=abs(x-5)", xdata=vector_x, ydata=vector_y )

master.mainloop()  # and wait...
