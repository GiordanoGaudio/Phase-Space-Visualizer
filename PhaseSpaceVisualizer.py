from manim import *
from sympy import *

m, ω, ε = 1,1,0 # parameters of the problem  ε = 0 and 0.05
x, p = symbols('x p') 

H_0 = p**2/(2*m) + (m*ω**2)*(x**2)/ 2   # unperturbed Hamiltonian
δH = sin(x**4)                          # perturbation
H = H_0 + ε*δH                          # perturbed Hamiltonian


fx = lambdify([x,p], diff(H,p))    # dx/dt = dH/dp 
fp = lambdify([x,p],-diff(H,x))   # dp/dt = -dH/dx as numerical functions 

def f(pt):  # Make a vector field out of <dx/dt, dp/dt> = <fx, fp>
  return fx(pt[0], pt[1])*RIGHT + fp(pt[0], pt[1])*UP

class PhaseSpace(Scene): # Phase Space Animator
    def construct(self):

        # vector field striemlines

        stream_lines = StreamLines( f,    
                                    stroke_width=3,
                                    max_anchors_per_line=30,
                                    opacity = 0.5)
        
        ax = Axes([-10,10,1], # axes
                  [-5,5,1],
                  tips = False,
                  axis_config= {"include_numbers": False},
                  x_axis_config= {"numbers_to_include" : [1]}, 
                  y_axis_config= {"numbers_to_include" : [1]})
        
        labels = ax.get_axis_labels('x', 'p').set_color(WHITE) # axis labels
        
        self.add(ax, labels, stream_lines)                     # animate
        stream_lines.start_animation(warm_up=False, flow_speed=1)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
