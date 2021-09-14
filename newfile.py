from math import sin, cos

eps=0.001
h0 = 0.1
k0=100
t0=0
T=[]
T.append(t0)

def real_function_x(t):
	return sin(t)+1
	
def real_function_y(t):
	return t**2

def function_x(t,x,y):
	return 2*x-y+t**2-2*(sin(t)+1)+cos(t)

def function_y(t,x,y):
	return x+2*y-sin(t)-2*t**2+2*t-1
	
def find_x_y_iteration(t,x_start,y_start):
	while True:
		x_iter=x_start
		y_iter=y_start
		for i in range (1,k0+1):
			x_next=x_iter+h*function_x(t,x_iter,y_iter)
			y_next=y_iter+h*function_y(t,x_iter,y_iter)
			if(abs(x_next-x_iter)+abs(y_next-y_iter)<eps):
				return x_next,y_next,h,t
			x_iter=x_next
			y_iter=y_next
		h/=2
        t=t0
        t+=h
        

def find_x_y_Adams(t,x,y,h):
		x_solve=[]
		y_solve=[]
		x_solve=x
		y_solve=y
		i=3
		while(t<=1):
		
		    x_solve.append(x_solve[i]+(h/24)*	(55*function_x(t,x_solve[i],y_solve[i])-59*function_x(t,x_solve[i-1],y_solve[i-1])+37*function_x(t,x_solve[i-2],y_solve[i-2])-9*function_x(t,x_solve[i-3],y_solve[i-3])))
		    
		    y_solve.append(y_solve[i]+(h/24)*(55*function_y(t,x_solve[i],y_solve[i])-59*function_y(t,x_solve[i-1],y_solve[i-1])+37*function_y(t,x_solve[i-2],y_solve[i-2])-9*function_y(t,x_solve[i-3],y_solve[i-3])))
		    t+=h
		    i+=1
		
		return x_solve, y_solve

		
				
x=[]
y=[]

x_solve=[]
y_solve=[]

for i in range(4):
	x.append(0)
	y.append(0)

x[0]=1
t=t0
t+=h0
x[1],y[1],h,t=find_x_y_iteration(t,1,0)
if(h < h0):
	h0=h
T.append(t)
t0=t
t+=h0
x[2],y[2],h,t=find_x_y_iteration(t,x[1],y[1])

if(h < h0):
	h0=h
T.append(t)
t0=t
t+=h0
x[3],y[3],h,t = find_x_y_iteration(t,x[2],y[2])

if(h<h0):
	h0=h
T.append(t)
t0=t
t+=h0
x_solve,y_solve=find_Adams(t,x,y,h0)


"__________ Masiv X ____________"
for i in range(len(x_solve)):
	print(x_solve[i],real_function_x(T[i]))
	
"__________ Masiv Y ____________"
for i in range(len(x_solve)):
	print(y_solve[i],real_function_y(T[i]))
