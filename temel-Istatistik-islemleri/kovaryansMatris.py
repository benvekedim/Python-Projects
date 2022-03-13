#Kovaryans Matrisi

def Ortalama(arr):
    return sum(arr) / len(arr)

def CovarianceValue(X,Y):
    '''
    cov_Value: X ile Y arasindaki kovaryans degeri
    cov_Value > 0 ise iki vektör doğru orantili
    cov_Value < 0 ie  iki vektör ters orantili
    cov_Value = 0 ise iki vektör arasinda herhangi bir lineer iliski yok

    '''

    diffOrt_X = [i - Ortalama(X) for i in  X ]
    diffOrt_Y = [j - Ortalama(Y) for j in  Y ]

    cov_Value = sum([i * j for i, j in zip(diffOrt_X,diffOrt_Y)]) / (len(X) - 1)

    return cov_Value

  
def CovarianceMatrix(X,Y):
    var_X = CovarianceValue(X,X)
    var_Y = CovarianceValue(Y,Y)
    cov_XY = CovarianceValue(X,Y)
    cov_YX = CovarianceValue(Y,X)

    return [[var_X,cov_XY],[cov_XY,var_Y]]

X = [6,5,3,1]
Y = [1,4,7,9]

print(CovarianceMatrix(X,Y))
