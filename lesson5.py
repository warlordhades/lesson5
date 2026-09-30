#creating 2D list/matrix/Nested List-> list inside a list

list1=[[3,4,5],[6,7,8], [10,11,12], [13,14,15]]
print(list1)

#index numbers -> position numbers each for row and
# column starting with @

print(list1[1] [2])

#accessing 8

rows = len(list1) #number of rows
print(rows)

cols = len(list1[0]) #number of columns
print(cols)

#nested loops -> loop in a loop
for r_n in range(0,rows):
    for c_n in range(0,cols):
        print(list1[r_n][c_n], end=" ")
    print("\n") #to print in new line after each row

#    print(list1.shape) #this will give error because list is not a numpy array

number_rows = int(input("Enter the number of rows - " ))
number_columns = int(input("Enter the number of columns - "))

for i in range(number_rows):
    tem=[]
    for j in range(number_columns):
        x= int(input("Enter your element - "))
        tem. append (x)
    matrix.append(tem)
print(matrix)
