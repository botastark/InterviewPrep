#Projects
#P-5.32 Write a Python function that takes two three-dimensional numeric data
#sets and adds them componentwise.
def AddCompWise(data1, data2):

    result=data1
    for i in range(len(data1)):
        for j in range(len(data1[i])):
            result[i][j]=data1[i][j]+data2[i][j] 
    return result
data1 = [[22, 18, 709, 5, 33], [45, 32, 830, 120, 750], [4, 880, 45, 66, 61]]
data2 = [[33, 38, 719, 1, 33], [435, 332, 8340, 1520, 7550], [54, 8580, 545, 656, 561]]
print(AddCompWise(data1, data2))

#P-5.33 Write a Python program for a matrix class that can add and multiply twodimensional
#arrays of numbers, assuming the dimensions agree appropriately
#for the operation.
def MultCompWise(data1, data2):
    result=data1
    for i in range(len(data1)):
        result[i]=data1[i]*data2[i]
    return result
    
class matrix:
    def __init__(self,array):
        self._row=len(array)
        self._column=len(array[0])
        self._matrix=array
    def getrows(self,r):
        return self._matrix[r][:]
    
    def getcolumns(self,c):
        return [self._matrix[i][c] for i in range(len(data1))  ]
    
    def getsize(self):
        return self._row, self._column
    
def multiply(m1, m2):
    [r, c1]=m1.getsize()
    [r1,c]=m2.getsize()
    result=[ [0]*c for j in range(r) ]
    for i in range(r):
        for j in range(c):
            result[i][j]=sum(MultCompWise(m1.getrows(i),m2.getcolumns(j)))
    return result

m1=matrix([[1,2,3],[4,5,6]])
m2=matrix([[1,2,3,0],[4,5,6,1],[7,8,9,3]])

print(multiply(m1,m2))

#P-5.34 Write a program that can perform the Caesar cipher for English messages
#that include both upper- and lowercase characters.


#P-5.35 Implement a class, SubstitutionCipher, with a constructor that takes a
#string with the 26 uppercase letters in an arbitrary order and uses that for
#the forward mapping for encryption (akin to the self. forward string in
#our CaesarCipher class of Code Fragment 5.11). You should derive the
#backward mapping from the forward version.
#P-5.36 Redesign the CaesarCipher class as a subclass of the SubstitutionCipher
#from the previous problem.
#P-5.37 Design a RandomCipher class as a subclass of the SubstitutionCipher
#from Exercise P-5.35, so that each instance of the class relies on a random
#permutation of letters for its mapping.