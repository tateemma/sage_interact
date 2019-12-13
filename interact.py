@interact
def sine_graph(n = slider(1,5,1,default = 1), a = slider(1,5,1,default = 1)):
    '''
    Plot the graph of f = sin(nx)^a given variable constants n and a.
    The derivative and integral of f are computed and the graphs plotted against f.
    The aim is to observe the behaviours of these functions.
    '''
    x = var('x')
    y = function('y')(x)
    y = (sin(n*x))^a                  #function f = sin(nx)^a
    d = diff( y, x)                   
    I = integrate(y, x)
    
    def f(x):
        return (sin(n*x))^a
    
    #printing the functions to be plotted on graphs   
    pretty_print(html('$ black : f =' + latex (f(x)) +'$'))
    pretty_print(html('$ orange : f ^ \prime =' + latex (d) +'$'))
    pretty_print(html('$ green : \int f =' + latex (I) +'$'))
    
    #plotting graphs. Circles move along the graph to show how fast each function moves
    c = animate([circle((i/4, f(i)), 0.2, fill = True, color = 'black') 
                 +  plot(f(x*4),xmin=-5,ymin=-4,xmax=10,ymax=4,color = 'black')
             + circle((i/4, d(i)), 0.2, fill = True, color = 'orange')
                 +  plot(d(x*4),xmin=-5,ymin=-4,xmax=10,ymax=4,color = 'orange')
             + circle((i/4, I(i)), 0.2, fill = True, color = 'green')
                 +  plot(I(x*4),xmin=-5,ymin=-4,xmax=10,ymax=4,color = 'green')
                 
             for i in srange(-20,40,0.6)],
          xmin=-5,ymin=-4,xmax=10,ymax=4,figsize=[8,8])
    c.show() 
