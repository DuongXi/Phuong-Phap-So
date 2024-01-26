import numpy as np
import matplotlib.pyplot as plt
import MSE
import math as m

# tuỳ chỉnh hàm ở đây
# ------------------------------------------------

def f(x,y,t):
    return 0.25*x*(1-x/20) - 0.1*x*y/(1+x)
    # return (x+y*2)/(x**2 + 2*y**2)

def g(x,y,t):
    return -0.15*y + 0.12*x*y/(1+x)

# ------------------------------------------------
# Giải hệ 2 PTVP
        
def EulerForward2(u,v,t,nstep,h):
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    t_val = np.zeros(nstep+1)

    x_val[0] = u
    y_val[0] = v
    t_val[0] = t
    for i in range(0,nstep):
        u += h*f(x_val[i],y_val[i],t_val[i])
        v += h*g(x_val[i],y_val[i],t_val[i])
        t += h
        t_val[i+1] = t
        x_val[i+1] = u
        y_val[i+1] = v
    return x_val,y_val,t_val

def EulerBackward2(u,v,t,nstep,h):
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    t_val = np.zeros(nstep+1)

    x_val[0] = u
    y_val[0] = v
    t_val[0] = t
    for j in range(0,nstep):
        ts = x + h*f(x_val[j],y_val[j],t_val[j])
        ks = y + h*g(x_val[j],y_val[j],t_val[j])
        for i in range (5):
            ts = x + h*f(ts,y_val[j],t_val[j])
            ks = y + h*g(x_val[j],ks,t_val[j])
        u += h*f(ks,y_val[j])
        v += h*g(x_val[j],ts)
        t += h
        t_val[i+1] = t
        x_val[j+1] = u
        y_val[j+1] = v
    return x_val,y_val,t_val

def HinhThang2(u,v,t,nstep,h):
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    t_val = np.zeros(nstep+1)

    x_val[0] = u
    y_val[0] = v
    t_val[0] = t
    for j in range(0,nstep):
        ts = y + h*f(x_val[j],y_val[j],t_val[j])
        ks = y + h*g(x_val[j],y_val[j],t_val[j])
        for i in range (5):
            ts = x + h*f(ts,y_val[j])
            ks = y + h*g(x_val[j],ks)
        u += (h/2)*(f(x_val[j],y_val[j],t_val[j]) + f(ts,y_val[j],t_val[j]))
        v += (h/2)*(g(x_val[j],y_val[j],t_val[j]) + g(x_val[j],ks,t_val[j]))
        t += h
        t_val[i+1] = t
        x_val[j+1] = u
        y_val[j+1] = v
    return x_val,y_val,t_val
# ------------------------------------------------
# Giải PTVP cấp 1

def EulerForward(x,y,step):
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    
    x_val[0] = x
    y_val[0] = y
    
    for i in range(0,step):
        y += h*f(x_val[i],y_val[i],0)
        x += h
        x_val[i+1] = x
        y_val[i+1] = y
    return x_val,y_val

def EulerBackward(x,y,step):
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    
    x_val[0] = x
    y_val[0] = y
    
    for j in range(0,step):
        ts = y + h*f(x_val[j],y_val[j],0)
        for i in range (5):
            ts = y + h*f(x_val[j],ts,0)
        x += h
        x_val[j+1] = x
        y += h*f(x_val[j],ts,0)
        y_val[j+1] = y
    return x_val,y_val
    
def HinhThang(x,y,step):
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    
    x_val[0] = x
    y_val[0] = y
    
    for j in range(0,step):
        ts = y + h*f(x_val[j],y_val[j],0)
        for i in range(5):
            ts = y + h*f(x_val[j],ts,0)
        x += h
        x_val[j+1] = x
        y += (h/2)*(f(x_val[j],y_val[j],0) + f(x_val[j],ts),0)
        y_val[j+1] = y
    return x_val,y_val
    
# ------------------------------------------------
if __name__ == "__main__":
    x = 12
    y = 7
    h = 0.1
    t = 0
    t0 = 300
    nstep = abs(int(t0/h))

    # Phần tử đầu mảng x_val, y_val, t_val là x_0, y_0, t_0
    x_val = np.zeros(nstep+1)
    y_val = np.zeros(nstep+1)
    t_val = np.zeros(nstep+1)

    t_val[0] = t
    x_val[0] = x
    y_val[0] = y

    # x_val,y_val = EulerForward()
    # EulerBackward()
    # HinhThang()
    x_val,y_val,t_val = EulerForward2(x,y,t,nstep,h)

    print("Một số nút lưới")
    print(x_val[1:4],x_val[len(x_val)-3:])
    print(y_val[1:4],y_val[len(y_val)-3:])

    # Plot cho PTVP đơn
    # plt.plot(x_val,y_val)
    # plt.show()

    # Sử dụng khi cần cho bài toán hệ PTVP
    time_values = np.arange(0, t0+1*h, h)
    plt.plot(time_values , x_val, label="u")
    plt.plot(time_values , y_val, label="v")
    plt.xlabel("t")
    plt.ylabel("Giá trị")
    plt.legend()
    plt.show()

    # BPTT để tìm dạng hàm xấp xỉ
    # MSE.Menu(t_val,x_val)
    # print(t_val)
    # MSE.Menu(t_val,y_val)