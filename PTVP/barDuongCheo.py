import numpy as np

def TruyDuoi(matrix):
    n = len(matrix)
    
    alpha = np.zeros((1,n))
    beta = np.zeros((1,n))
    kq = np.zeros((1,n))
    
    alpha = alpha[0]
    beta = beta[0]
    kq = kq[0]
    
    alpha[0] = matrix[0,1]/matrix[0,0]
    beta[0] = matrix[0,n]/matrix[0,0]
    
    for i in range(1,n):
        alpha[i] = matrix[i,i+1] / (matrix[i,i] - alpha[i-1]*matrix[i,i-1])
        beta[i] = (-matrix[i,i-1]* beta[i-1] + matrix[i,n]) / (matrix[i,i]-alpha[i-1]*matrix[i,i-1])
    #kq[n-1] = (matrix[n-1,n-2]*beta[n-1] - matrix[n-1,n])/(-matrix[n-1,n-1] - matrix[n-1,n-2]*alpha[n-1])
    kq[n-1] = beta[n-1]
    for i in range (1,n):
        kq[n-1-i] = beta[n-1-i] - alpha[n-1-i] * kq[n-i]
    return kq

if __name__ == "__main__":
    matrix = np.loadtxt("matrix.txt")
    print(matrix)
    kq = TruyDuoi(matrix)
    # kq = gaussNghich(matrix)
    print("Nghiệm của hệ phương trình là: \n", kq)