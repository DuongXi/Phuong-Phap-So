import numpy as np
import matplotlib.pyplot as plt
import math

def LayData(x,y):
    with open('data.txt','r+') as f:
        for line in f.readlines():
            xi = float(line.split('\t')[0])
            yi = float(line.split('\t')[1])
            x.append(xi)
            y.append(yi)

def Plot():
    plt.plot(x,y,marker = "o")
    plt.show()

def Calc(M,y):
    A = M @ np.transpose(M)
    print("\nMa trận M^T*M: \n",A)
    
    B = M @ y
    print("\nMa trận M^T*f_h: \n",B)
    
    result = np.linalg.inv(A) @ B
    
    print("\nCác hệ số trong hàm lựa chọn lần lượt là: \n", result)
    return result

def CalcE(M,y):
    A = M @ np.transpose(M)
    print("\nMa trận M^T*M: \n",A)
    
    B = M @ y
    print("\nMa trận M^T*f_h: \n",B)
    
    result = np.linalg.inv(A) @ B
    result[0] = math.exp(result[0])
    
    print("\nCác hệ số trong hàm lựa chọn lần lượt là: \n", result)
    return result
    
def MSE_p1(x,y):
    y_ = y.copy()
    
    M = np.array(x)
    M = np.vstack((M,np.ones((1,len(x)))))
    
    return Calc(M,y_)

def MSE_p2(x,y):
    y_ = y.copy()
    
    M = np.array(x**2)
    M = np.vstack((M,x))
    M = np.vstack((M,np.ones((1,len(x)))))
    
    return Calc(M,y_)

def MSE_p3(x,y):
    y_ = y.copy()
    
    M = np.array(x**3)
    M = np.vstack((M,x**2))
    M = np.vstack((M,x))
    M = np.vstack((M,np.ones((1,len(x)))))
    
    return Calc(M,y_)

def NormalizeE(add,y):
    y += add
    y = np.log(y)

def MSE_e1(x,y):
    y_ = y.copy()
    Min = y_.min()
    if Min < 0:
        adder = abs(round(Min)) + 1
        print("Số cần cộng thêm cho dữ liệu :", adder)
        NormalizeE(adder,y_)
    
    M = np.ones((1,len(x)))
    M = np.vstack((M,x))
    
    return CalcE(M,y_)

def MSE_e2(x,y):
    y_ = y.copy()
    Min = y_.min()
    if Min < 0:
        adder = abs(round(Min)) + 1
        print("Số cần cộng thêm cho dữ liệu :", adder)
        NormalizeE(adder,y_)
    
    M = np.ones((1,len(x)))
    M = np.vstack((M,x**2))
    M = np.vstack((M,x))
    
    return CalcE(M,y)

def NormalizeLn(y):
    y = np.exp(y)

def MSE_ln1(x,y):
    x_ = x.copy()
    y_ = y.copy()
    Min = x.min()
    if Min <= 0:
        adder = abs(round(Min)) + 1
        print("Số cần cộng thêm cho dữ liệu :", adder)
        NormalizeLn(y_)
    
    M = np.array(x_)
    M = np.vstack((M,np.ones((1,len(x_)))))
    
    return Calc(M,y)

def Menu(x,y):
    print("1. y = ax + b")
    print("2. y = ax^2 + bx + c")
    print("3. y = ax^3 + bx^2 + cx + d")
    print("4. y = a*e^(bx)")
    print("5. y = a*e^(bx^2+cx)")
    print("6. y = ln(ax+b)")

    p = int(input("Chọn hàm phù hợp: "))

    match p:
        case 1:
            MSE_p1(x,y)
        case 2:
            MSE_p2(x,y)
        case 3:
            MSE_p3(x,y)
        case 4:
            MSE_e1(x,y)
        case 5:
            MSE_e2(x,y)
        case 6:
            MSE_ln1(x,y)
        case default:
            pass

if __name__ == "__main__":
    x = []
    y = []

    LayData(x,y)
    x = np.asarray(x)
    y = np.asarray(y)
    Plot()
    Menu(x,y)