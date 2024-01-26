import numpy as np
import matplotlib.pyplot as plt
import math as m
import MSE

# tuỳ chỉnh hàm ở đây
# ------------------------------------------------
def f(x,y,t):
    # return 0.25*x*(1-x/20) - 0.1*x*y/(1+x)
    # return (x+y*2)/(x**2 + 2*y**2)
    return x*(1-x)*(x-0.25)-0.2*x*y

def g(x,y,t):
    return 0.6*x*y - 0.45*y
    # return (50*m.cos(10*t)-30*y-x/0.016)/2

# ------------------------------------------------
# PTVP đơn cấp 1
def RK1(x,y,step):
    x_val = np.zeros(step+1)
    y_val = np.zeros(step+1)
    
    x_val[0] = x
    y_val[0] = y
    # Khá giống Euler hiện
    for i in range(0,step):
        k1 = h*f(x_val[i],y_val[i],0)
        y += k1
        x += h
        x_val[i+1] = x
        y_val[i+1] = y
    return x_val,y_val

def RK2(x,y,step):
    x_val = np.zeros(step+1)
    y_val = np.zeros(step+1)
    
    x_val[0] = x
    y_val[0] = y
    for i in range(0,step):
        k1 = h*f(x_val[i],y_val[i],0)
        k2 = h*f(x_val[i] + h,y_val[i] + k1,0)
        y += (k1/2 + k2/2)
        x += h
        x_val[i+1] = x
        y_val[i+1] = y
    return x_val,y_val


def RK3(x,y,step):
    x_val = np.zeros(step+1)
    y_val = np.zeros(step+1)
    
    x_val[0] = x
    y_val[0] = y
    for i in range(0,step):
        k1 = h*f(x_val[i],y_val[i],0)
        k2 = h*f(x_val[i] + h/2,y_val[i] + k1/2,0)
        k3 = h*f(x_val[i] + h,y_val[i] - k1 + 2*k2,0)
        y += ((k1 + 4*k2 + k3)/6)
        x += h
        x_val[i+1] = x
        y_val[i+1] = y
    return x_val,y_val

def RK3Heun(x,y,step):
    x_val = np.zeros(step+1)
    y_val = np.zeros(step+1)
    
    x_val[0] = x
    y_val[0] = y
    for i in range(0,step):
        k1 = h*f(x_val[i],y_val[i],0)
        k2 = h*f(x_val[i] + h/3,y_val[i] + k1/3,0)
        k3 = h*f(x_val[i] + 2*h/3,y_val[i] + 2*k2/3,0)
        
        y += ((k1 + 3*k3)/4)
        x += h
        x_val[i+1] = x
        y_val[i+1] = y
    return x_val,y_val

def RK4(x,y,nstep,h):
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    
    x_val[0] = x
    y_val[0] = y
    
    for i in range(0,nstep):
        k1 = h*f(x_val[i],y_val[i],0)
        k2 = h*f(x_val[i] + h/2,y_val[i] + k1/2,0)
        k3 = h*f(x_val[i] + h/2,y_val[i] + k2/2,0)
        k4 = h*f(x_val[i] + h,y_val[i] + k3,0)
        y += ((k1 + 2*k2 + 2*k3 + k4)/6)
        x += h
        x_val[i+1] = x
        y_val[i+1] = y
    return x_val,y_val
# ------------------------------------------------
# Giải hệ 2 PTVP
def RK3_2(u,v,t,step,h):
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    t_val = np.zeros(nstep+1)

    x_val[0] = u
    y_val[0] = v
    t_val[0] = t
    for i in range(0,step):
        
        k1 = h*f(x_val[i],y_val[i],t_val[i])
        l1 = h*g(x_val[i],y_val[i],t_val[i])
        
        k2 = h*f(x_val[i] + k1/2,y_val[i] + l1/2,t_val[i] + h/2)
        l2 = h*g(x_val[i] + k1/2,y_val[i] + l1/2,t_val[i] + h/2)
        
        k3 = h*f(x_val[i] + - k1 + 2*k2,y_val[i] - l1 + 2*l2,t_val[i])
        l3 = h*g(x_val[i] + - k1 + 2*k2,y_val[i] - l1 + 2*l2,t_val[i])
        
        u += ((k1 + 4*k2 + k3)/6)
        v += ((l1 + 4*l2 + l3)/6)
        t += h

        t_val[i+1] = t
        x_val[i+1] = u
        y_val[i+1] = v
    return x_val,y_val,t_val

def RK4_2(u,v,t,nstep,h):
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    t_val = np.zeros(nstep+1)

    x_val[0] = u
    y_val[0] = v
    t_val[0] = t
    
    for i in range(0,nstep):
        
        k1 = h*f(x_val[i],y_val[i],t_val[i])
        l1 = h*g(x_val[i],y_val[i],t_val[i])
        
        k2 = h*f(x_val[i]+ k1/2,y_val[i] + l1/2,t_val[i] + h/2)
        l2 = h*g(x_val[i]+ k1/2,y_val[i] + l1/2,t_val[i] + h/2)
        
        k3 = h*f(x_val[i]+ k2/2,y_val[i] + l2/2,t_val[i] + h/2)
        l3 = h*g(x_val[i]+ k2/2,y_val[i] + l2/2,t_val[i] + h/2)
        
        k4 = h*f(x_val[i]+ k3 ,y_val[i] + l3,t_val[i] + h)
        l4 = h*g(x_val[i]+ k3 ,y_val[i] + l3,t_val[i] + h)
        
        u += ((k1 + 2*k2 + 2*k3 + k4)/6)
        v += ((l1 + 2*l2 + 2*l3 + l4)/6)
        t += h
        
        t_val[i+1] = t
        x_val[i+1] = u
        y_val[i+1] = v
    return x_val,y_val,t_val

if __name__ == "__main__":
    x = 0.8
    y = 0.3
    h = 0.01
    t = 0
    t0 = 100
    nstep = abs(int(t0/h))

    # Note:
    # Phần tử đầu mảng x_val và y_val là x_0, y_0

    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    t_val = np.zeros(nstep+1)

    x_val[0] = x
    y_val[0] = y
    t_val[0] = t

    # RK1(x,y,nstep)
    # RK2(x,y,nstep)
    # RK3(x,y,nstep)
    # x_val,y_val = RK4(x,y,nstep,h)
    x_val, y_val, t_val = RK4_2(x,y,t,nstep,h)
    
    print("Một số nút lưới")
    print(x_val[1:4],x_val[len(x_val)-3:])
    print(y_val[1:4],y_val[len(y_val)-3:])

    # Plot cho PTVP đơn
    plt.plot(x_val,y_val)
    plt.show()
    
    # Sử dụng khi cần cho bài toán hệ PTVP
    # time_values = np.arange(0, t0+1*h, h)
    # plt.plot(time_values , x_val, label="u")
    # plt.plot(time_values , y_val, label="v")
    # plt.xlabel("t")
    # plt.ylabel("Giá trị")
    # plt.legend()
    # plt.show()
    
    # BPTT để tìm dạng hàm xấp xỉ
    # MSE.Menu(t_val,x_val)
    # print(t_val)
    # MSE.Menu(t_val,y_val)