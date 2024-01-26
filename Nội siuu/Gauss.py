import numpy as np

eps = 0.0001

def gaussThuan(matrix):
    #Trả về ma trận đã được biến đổi qua quá trình thuận cảu thuật toán Gauss
    print("Các bước biến đổi Gauss: ")
    for j in range(0,len(matrix)-1):
        for i in range(j+1,len(matrix)):
            if int(matrix[j,j])==0:
                swap(matrix,j)
            matrix[i] = matrix[i] - (matrix[i,j]/matrix[j,j])*matrix[j]
        print(matrix)
        print()
    s = len(matrix)
    for i in range(s):
        for j in range(s):
            if abs(matrix[i,j]) < eps:
                matrix[i,j] = 0
    print(matrix)
            
def gaussNghich(matrix):
    kq = []
    #Tìm nghiệm hệ phương trình qua quá trình nghịch của thuật toán Gauss
    size = len(matrix)
    for i in range(0,size):
        k=len(kq)-1
        sum = 0
        for j in range(size-i,size):
            sum += matrix[size-1-i,j]*kq[k]
            k-=1 
        n = ((matrix[size-1-i,size])-sum)/matrix[size-1-i,size-1-i]
        kq.append(n)
    kq.reverse()
    return kq
        
def swap(matrix,j):
    #thay hàng có phần tử vị trí (i,i) bằng 0 bằng một sau nó có vị trí (i,i+k) khác 0
    for i in range(j+1,len(matrix)):
        if matrix[i,j] != 0:
            tmp = matrix[i].copy()
            matrix[i] = matrix[j]
            matrix[j] = tmp
        return
    
def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I

#main-----------------------------------------------------------------------

if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")

    addIdentityMat(matrix)
    gaussThuan(matrix)
    kq = gaussNghich(matrix)
    print("Nghiệm của hệ phương trình là: \n", kq)