import numpy as np
import matplotlib.pyplot as plt
import Runge_Kutta as RK
import math as m
import MSE

def f(x,y,t):
    '''
    Nếu làm với hệ pt, chọn hàm f tương ứng với y/v
    '''
    # return (x+y*2)/(x**2 + 2*y**2)
    return 0.6*x*y - 0.45*y

def g(x,y,t):
    '''
    Nếu làm với hệ pt, chọn hàm g tương ứng với x/u
    '''
    # print(t)
    # return -0.15*y + 0.12*x*y/(1+x)
    return x*(1-x)*(x-0.25)-0.2*x*y
#------------------------------------------------------------------------------------------------------------------------------
def AB2(i):
    return y_val[i] + (h/2)*(3*f(x_val[i],y_val[i],t_val[i]) - f(x_val[i-1],y_val[i-1],t_val[i-1]))

def AM2(t,s,i):
    return y_val[i] + (h/12)*(5*f(x_val[i+1],t,s) + 8*f(x_val[i],y_val[i],t_val[i]) - f(x_val[i-1],y_val[i-1],t_val[i-1]))
    # return y_val[i] +(h/12)*(5*f(t,s,t_val[i+1]) + 8*f(x_val[i],y_val[i],t_val[i]) - f(x_val[i-1],y_val[i-1],t_val[i-1]))
#------------------------------------------------------------------------------------------------------------------------------
def AB2_1(i):
    return x_val[i] + (h/2)*(3*g(x_val[i],y_val[i],t_val[0]) - g(x_val[i-1],y_val[i-1],t_val[i-1]))

def AM2_1(t,s,i):
    return x_val[i] + (h/12)*(5*g(x_val[i+1],t,s) + 8*g(x_val[i],y_val[i],t_val[0]) - g(x_val[i-1],y_val[i-1],t_val[i-1]))
    # return y_val[i] +(h/12)*(5*g(t,s,t_val[i+1]) + 8*g(x_val[i],y_val[i],t_val[0]) - g(x_val[i-1],y_val[i-1],t_val[i-1]))
#------------------------------------------------------------------------------------------------------------------------------
def AB2_AM2():
    
    x_val[:2],y_val[:2] = RK.RK4(x,y,1,h)
    
    for i in range(1,nstep):
        x_val[i+1] = x_val[i] +h
        t = AB2(i)
        y = AM2(t,0,i)
        y_val[i+1] = y
#------------------------------------------------------------------------------------------------------------------------------     
def AB3(i):
    return y_val[i] + (h/12)*(23*f(x_val[i],y_val[i],t_val[i]) - 16*f(x_val[i-1],y_val[i-1],t_val[i-1]) + 5*f(x_val[i-2],y_val[i-2],t_val[i-2]))
    
def AM3(t,s,i):
    return y_val[i] + (h/24)*(9*f(t,s,t_val[i+1]) + 19*f(x_val[i],y_val[i],t_val[i]) - 5*f(x_val[i-1],y_val[i-1],t_val[i-1]) + f(x_val[i-2],y_val[i-2],t_val[i-2]))  
    # return y_val[i] +(h/24)*(9*f(t,s,t_val[i+1]) + 19*f(x_val[i],y_val[i],t_val[i]) - 5*f(x_val[i-1],y_val[i-1],t_val[i-1]) + f(x_val[i-2],y_val[i-2],t_val[i-2]))  
#------------------------------------------------------------------------------------------------------------------------------

def AB3_1(i):
    return x_val[i] + (h/12)*(23*g(x_val[i],y_val[i],t_val[i]) - 16*g(x_val[i-1],y_val[i-1],t_val[i-1]) + 5*g(x_val[i-2],y_val[i-2],t_val[i-2]))
    
def AM3_1(t,s,i):
    return x_val[i] + (h/24)*(9*g(t,s,t_val[i+1]) + 19*g(x_val[i],y_val[i],t_val[i]) - 5*g(x_val[i-1],y_val[i-1],t_val[i-1]) + g(x_val[i-2],y_val[i-2],t_val[i-2]))  
    # return y_val[i] +(h/24)*(9*g(t,s,t_val[i+1]) + 19*g(x_val[i],y_val[i],t_val[0]) - 5*g(x_val[i-1],y_val[i-1],t_val[i-1]) + g(x_val[i-2],y_val[i-2],t_val[i-2]))  
#------------------------------------------------------------------------------------------------------------------------------ 
def AB3_AM3():
    
    x_val[:3],y_val[:3] = RK.RK4(x,y,2,h)
    
    for i in range(2,nstep):
        x_val[i+1] = x_val[i] +h
        t = AB3(i)
        y = AM3(t,i)
        y_val[i+1] = y
#------------------------------------------------------------------------------------------------------------------------------
def AB4(i):
    return y_val[i] + (h/24)*(55*f(x_val[i],y_val[i],t_val[i]) - 59*f(x_val[i-1],y_val[i-1],t_val[i-1]) + 37*f(x_val[i-2],y_val[i-2],t_val[i-2]) - 9*f(x_val[i-3],y_val[i-3],t_val[i-3]))

def AM4(t,s,i):
    return y_val[i] + (h/720)*(251*f(t,s,t_val[i+1]) + 646*f(x_val[i],y_val[i],t_val[i]) - 264*f(x_val[i-1],y_val[i-1],t_val[i-1]) + 106*f(x_val[i-2],y_val[i-2],t_val[i-2]) - 19*f(x_val[i-3],y_val[i-3],t_val[i-3]))   
    # return y_val[i] + (h/720)*(251*f(t,s,t_val[i+1]) + 646*f(x_val[i],y_val[i],t_val[i]) - 264*f(x_val[i-1],y_val[i-1],t_val[i-1]) + 106*f(x_val[i-2],y_val[i-2],t_val[i-2]) - 19*f(x_val[i-3],y_val[i-3],t_val[i-3]))   
#------------------------------------------------------------------------------------------------------------------------------
def AB4_1(i):
    return x_val[i] + (h/24)*(55*g(x_val[i],y_val[i],t_val[i]) - 59*g(x_val[i-1],y_val[i-1],t_val[i-1]) + 37*g(x_val[i-2],y_val[i-2],t_val[i-2]) - 9*g(x_val[i-3],y_val[i-3],t_val[i-3]))

def AM4_1(t,s,i):
    return x_val[i] + (h/720)*(251*g(t,s,t_val[i+1]) + 646*g(x_val[i],y_val[i],t_val[i]) - 264*g(x_val[i-1],y_val[i-1],t_val[i-1]) + 106*g(x_val[i-2],y_val[i-2],t_val[i-2]) - 19*g(x_val[i-3],y_val[i-3],t_val[i-3]))   
    # return y_val[i] + (h/720)*(251*g(t,s,t_val[i+1]) + 646*g(x_val[i],y_val[i],t_val[0]) - 264*g(x_val[i-1],y_val[i-1],t_val[i-1]) + 106*g(x_val[i-2],y_val[i-2],t_val[i-2]) - 19*g(x_val[i-3],y_val[i-3]))   
#------------------------------------------------------------------------------------------------------------------------------
def AB4_AM4(x,y):
        
    x_val[:4],y_val[:4] = RK.RK4(x,y,3,h)
    
    for i in range(3,nstep):
        x_val[i+1] = x_val[i] + h
        t = AB4(i)
        y = AM4(t,0,i)
        y_val[i+1] = y
#------------------------------------------------------------------------------------------------------------------------------
def He_AB2_AM2(x,y,t):
    x_val[:2],y_val[:2],t_val[:2] = RK.RK4_2(x,y,t,1,h)

    for i in range(1,nstep):
        t_val[i+1] = t_val[i] + h
        s = AB2(i)
        k = AB2_1(i)
        y = AM2(k,s,i)
        x = AM2_1(k,s,i)
        x_val[i+1] = x
        y_val[i+1] = y
#------------------------------------------------------------------------------------------------------------------------------      
def He_AB3_AM3(x,y,t):
    x_val[:3],y_val[:3],t_val[:3] = RK.RK4_2(x,y,t,2,h)
    
    for i in range(2,nstep):
        t_val[i+1] = t_val[i] + h
        s = AB3(i)
        k = AB3_1(i)
        y = AM3(k,s,i)
        x = AM3_1(k,s,i)
        x_val[i+1] = x
        y_val[i+1] = y
#------------------------------------------------------------------------------------------------------------------------------     
def He_AB4_AM4(x,y,t):
    x_val[:4],y_val[:4],t_val[:4] = RK.RK4_2(x,y,t,3,h)
    
    for i in range(3,nstep):
        t_val[i+1] = t_val[i] + h
        s = AB4(i)
        k = AB4_1(i)
        y = AM4(k,s,i)
        x = AM4_1(k,s,i)
        x_val[i+1] = x
        y_val[i+1] = y
    
#-----------------------------------------------------------
x = 0.8
y = 0.3
h = 0.01
t = 0
t0 = 100

nstep = abs(int(t0/h))

# Phần tử đầu mảng x_val, y_val, t_val là x_0, y_0, t_0
x_val = np.zeros(nstep+1)
y_val = np.zeros(nstep+1)
t_val = np.zeros(nstep+1)

t_val[0] = t
x_val[0] = x
y_val[0] = y

# AB4_AM4(x,y)
He_AB3_AM3(x,y,t)
# He_AB4_AM4(x,y,t)

print("Một số nút lưới")
print(x_val[1:8],x_val[len(x_val)-3:])
print(y_val[1:8],y_val[len(y_val)-3:])

# Plot cho PTVP đơn
# plt.plot(x_val,y_val)
# plt.show()

# Sử dụng khi cần cho bài toán hệ PTVP
plt.plot(t_val , x_val, label="u")
plt.plot(t_val , y_val, label="v")
plt.xlabel("t")
plt.ylabel("Giá trị")
plt.legend()
plt.show()

# BPTT để tìm dạng hàm xấp xỉ
# MSE.Menu(t_val,x_val)
# print(t_val)
# MSE.Menu(t_val,y_val)