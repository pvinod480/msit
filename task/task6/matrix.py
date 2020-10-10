class Matrix:
   
   def userInputMatrix(number_of_rows, number_of_columns,elements=0):
      mat = [[int(input("Enter elements")) for x in range (number_of_columns)] for y in range(number_of_rows)]
      print(mat)

   #same element Matrics--Matrix(2,3)
   def createMatrix(number_of_rows, number_of_columns,element=0):
      mat=[[element for i in range(number_of_columns)] for j in range(number_of_rows)]
      return mat

   def getShape(self):
       rows=len(matx)
       cols=len(matx[0])
       return rows,cols

   def compMatrix(m1,m2):
       if len(m1)==len(m2):
           if m1==m2:
               return True
           else:
               return False
   def isSquare(m1):
       if len(m1)==len(m1[0]):
           return True
       else:
           return False
         
   def isDiagonal(m):
      for row in range(len(m)):
         for col in range(len(m)):
            if row != col and m[row][col]!=0:
               return "Not Diagonal"
            else:
               continue
         return "Diagonal"
         

   def addMatrix(m1,m2,):
       results=[[m1[i][j] + m2[i][j]  for j in range(len(m1[0]))] for i in range(len(m1))] 
       for result in results:
           print(result)

   def mulMatrix(m1,m2,):
       results=[[[sum(m1[i][k] * m2[k][j] for i in range(len(m1)))]for j in range(len(m2[0]))]for k in range(len(m2))]
       for result in results:
           print(result)

   def transpose(m):
      results=[[m[i][j]  for i in range(len(m))] for j in range(len(m[0]))]
      for mat in results:
         print(mat)
      
   def removeRowColumn(m,row_number,column_number):

         del m[row_number]
         for col in m:
            del col[column_number]
         return(m)

m1=Matrix()
m1.createMatrix(3,3,2)
#print(m1.removeRowColumn(m1,1,1))
#print(m1)
m2=Matrix()
m2.createMatrix(3,2,2)
#print(isDiagonal(m1))
#print(isSqual(m1))

#add=addMatrix(m1,m2)
#mul=mulMatrix(m1,m2)
#print(compMatrix(m1,m2))
#transpose(m1)

#m2=getShape(m1)
#print(m2,type(m2))
#print(replaceElement(m1,1,1,5))

#m2=Matrix(3,2,2)
#print(m1)
print(m1==m2)
#m1[1,1]=10
#print(m1)
