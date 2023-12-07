import tkinter  
import random as rd
import time 
import math as m
E = [ "white", "red", "yellow", "black", "green"]
Sec = 0.01

def confinement():
    print('save it')
def run():
    print('loading')
def deconfinement():
    print('deconfinement')






def tt(N):
    Window = tkinter.Tk()
    Window.geometry(f'{N}x{N}')
    return Window

def Canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="blue")
    canvas.pack(fill="both", expand=True)
    return canvas


                                                                                                                                                                      
def initialisation (N,n,m,r,canvas):

    B= []
    p = int(N/n)
    States = [ 0 for _ in range(n**2)]
    print(len(States))

    for x in range(n):
      for y in range(n): 
        ball= canvas.create_oval(x*p - r ,y*p - r ,x*p + r ,y*p + r , fill = E[0], outline = "black", width = "1" )
        B.append(ball)
        
    M = [ rd.randint(0,n**2-1) for _ in range(m) ]
    for i in range(m):
      canvas.itemconfig(B[M[i]], fill="red")
      States[M[i]]= 1 
    
    return B, States


def distance(x,y,xp,yp):
    return m.sqrt( (x-xp)**2 + (y-yp)**2 )
    

def voisin(j,r,R,B,States,canvas):
    V = []
    n = len(B)
    x_c,y_c, g , b = canvas.coords(B[j])
    x_c, y_c =  x_c + r , y_c + r
    
    for k in range (n):
        if k != j :
            
            a = canvas.coords(B[k])
            x_p , y_p , g , b = a
            x_p, y_p =  x_p + r , y_p + r
            if distance(x_c,y_c,x_p,y_p) <= R and States[k] == 1 :
                V.append(B[k])
            
    
    return V
            

def vaccination(States,B,tau,canvas):
    S=[]
    n= len(States)
    for i in range(n):
        if States[i] == 0:
            S.append(i)
        
    Vac= rd.sample(S, int(tau*len(S)))
    for i in Vac:
        canvas.itemconfig(B[i], fill = E[4])
        States[i] = 4
    




  

           

def survival(j,B,r,R,d,p,States,canvas,temps_maladie):
    V = voisin(j,r,R,B,States,canvas)
    
    
    m= len(V)
    Y = States[j]
    if Y == 0:
        if m == 0:
            return 0
        r= rd.random()
        if p**(1/m) > r :
            return 1 
        else:
            return 0
    if Y == 1:
        r = rd.random()
        y= rd.random()
        
        if 1/(temps_maladie)> y :
            if d > r :
                return 2
            else:
                return 3
        else:
            return 1 
    else:
        return Y

def Confinement():
    global x_max, y_max
    x_max, y_max = x_max/2 , y_max/2 
   
    
def Deconfinement():
    global x_max, y_max
    x_max, y_max = x_max*2 , y_max*2

def animation(N,n,m,r,R,d,p,temps_maladie,tau):
    global x_max,y_max, Sec 
    Window = tt(N)
    canvas= Canvas(Window)
    B,States = initialisation(N,n,m,r,canvas)
    button = tkinter.Button(Window, text = 'CONFINEMENT !', command = Confinement)
    button.pack()
    button2 = tkinter.Button(Window, text = 'DECONFINEMENT', command = Deconfinement)
    button2.pack()


    root = Window
    frame = tkinter.Frame(root)
    frame.pack()
    mainmenu = tkinter.Menu(frame)
    load = tkinter.Menu(mainmenu, tearoff = 0)
    load.add_command(   label='RUN',command=run)
    load.add_command(label='Stop')
    mainmenu.add_cascade(label='LOAD',menu=load)
    options=tkinter.Menu(mainmenu,tearoff=0)
    options.add_command(label='confinement',command=confinement)
    options.add_command(label='deconfinement',command=deconfinement)
    mainmenu.add_cascade(label='OPTIONS',menu=options)
    root.config(menu = mainmenu)

    
   
    
    for _ in range(1000):
        for k in range(n**2):
            States[k] = survival(k,B,r,R,d,p,States,canvas,temps_maladie)
            canvas.itemconfig(B[k], fill = E[States[k]])
            
        vaccination(States,B,tau,canvas)
        
        Window.update()
        
        for k in range(n**2):
        
            r_x = rd.uniform(-1,+1)
            r_y = rd.uniform(-1,+1)
            
            xinc, yinc = r_x*x_max, r_y*y_max 
            ball_pos = canvas.coords(B[k])
            
            al,bl,ar,br = ball_pos
            if States[k] == 3:
                xinc = 0 
                yinc = 0 
            
            if al < abs(xinc) :
                xinc = abs(xinc)
            if ar > N - abs(xinc):
                xinc = -abs(xinc)
                
            if bl < abs(yinc):
                yinc = abs(yinc)
            if br > N - abs(yinc):
                yinc= - abs(yinc)
                
                
            canvas.move(B[k],xinc,yinc) 
                
                
        time.sleep(Sec)  
        Window.update()
        
    Window.mainloop()
    
x_max,y_max = 20,20 

animation(500,10,2,5,15,0.3,0.2,200,0.005)

