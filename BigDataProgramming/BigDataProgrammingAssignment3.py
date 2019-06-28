import numpy as np

recheck = False
prog = False

while (recheck == False):
    while (prog == False):
        Exercise = int(input("Which exercise number would you like to check?"))
        if (Exercise > 0 and Exercise < 11):
            if (Exercise == 1):
                print("Exercise 1 :- How to replace items that satisfy a condition with another value in numpy array?")
                my_array = []
                a = int(input("Size of array:"))
                for i in range(a):
                    my_array.append(int(input("Element : ")))
                my_array = np.array(my_array)
                print(np.floor(my_array))
                inp = int(input("With what value would you like to replace your odd number values of the array?"))
                print("After replacing all odd number values in the array with -1, the new array is : ")
                print (np.where((my_array%2)==1, inp, my_array))
                
                a = False
                while (a==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        a = True
                    elif (check == 'n' or check == 'N' or check == 'no' or check == 'NO'):
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        a = False
            
            elif (Exercise == 2):
                print("Exercise 2 :- How to reshape an array?")
                number = False
                while (number == False):
                    a = int(input("How many elements should be there in the 1D array.\n (NOTE: Please select an even number)"))
                    num = a%2
                    if (num == 0):
                        array = np.arange(a)
                        print("1D array : \n", array)
                        number = True
                    else:
                        print ("Please select an even number.")
                        number = False
                print("Reshape of an original 1D array. Order is (Row, Column)")
                row = int(input("Row: "))
                column = int(a/row)
                print("Column: ", column)
                # shape array with 5 rows and 2 columns 
                array = np.arange(a).reshape(row, column)
                print("\narray reshaped with ",row," rows and ",column," columns : \n", array)
                
                b = False
                while (b==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        b = True
                    else:
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        b = False
            
            elif (Exercise == 3):
                print("Exercise 3 :- How to generate custom sequence in numpy without hardcoding?")
                my_array = []
                a = int(input("Size of array:"))
                for i in range(a):
                    my_array.append(int(input("Element : ")))
                my_array = np.array(my_array)
                b = []
                b = np.repeat(my_array, a)
                print("Repeatition of all values of array in Repeat form: ",b)
                c = []
                c = np.tile(my_array, a)
                print("Repeatition of all values of an array in Tile form: ",c)
                d = []
                d = np.concatenate((b,c), axis =0)
                print ("Custom Sequence: ",d)
                
                b = False
                while (b==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        b = True
                    else:
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        b = False
            
            elif (Exercise == 4):
                print("Exercise 4 :- How to get the common items between two python numpy arrays?")
                my_array1 = []
                a = int(input("Size of 1st array:"))
                print ("Element:\n")
                for i in range(a):
                    my_array1.append(int(input("\t")))
                my_array1 = np.array(my_array1)
                
                my_array2 = []
                b = int(input("Size of 2nd array:"))
                print ("Element:\n")
                for i in range(b):
                    my_array2.append(int(input("\t")))
                my_array2 = np.array(my_array2)
                
                common = []
                common = np.intersect1d(my_array1,my_array2)            
                print("Common items: ",common)
                
                c = False
                while (b==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        c = True
                    else:
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        c = False
                
            elif (Exercise == 5):
                print("Exercise 5 :- How to get the positions where elements of two arrays match?")
                my_array1 = []
                a = int(input("Size of 1st array:"))
                print ("Element:\n")
                for i in range(a):
                    my_array1.append(int(input("\t")))
                my_array1 = np.array(my_array1)
                
                my_array2 = []
                b = int(input("Size of 2nd array:"))
                print ("Element:\n")
                for i in range(b):
                    my_array2.append(int(input("\t")))
                my_array2 = np.array(my_array2)
                
                match = (my_array1 == my_array2)
                print("Index of common items: ",np.where(match==True))
                
                d = False
                while (d==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        d = True
                    else:
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        d = False
            
            elif (Exercise == 6):
                print("Exercise 6 :- How to create a 2D array containing random floats between 5 and 10?")
                my_array = []
                number = int(input("Size of an array"))
                lower = float(input("Lower Limit of array items :"))
                upper = float(input("Upper Limit of array items :"))
                for i in range (number):
                    numb = np.random.uniform(lower, upper)
                    my_array.append(numb)
                my_array = np.array(my_array)
                print("1D array : \n", my_array)
                
                print("Reshape of an original 1D array. Order is (Row, Column)")
                
                b = False
                while (b == False):
                    row = int(input("Row: "))
                    rem = number%row
                    if (rem == 0):
                        column = int(number/row)
                        b =True
                    else:
                        print ("2D array can't be created. Please give row count which is completely divisible by length of array.")
                        b = False
                
                print("Column: ", column)
                # shape array with 5 rows and 2 columns
                my_array = my_array.reshape(row, column) 
                print("\narray reshaped with ",row," rows and ",column," columns : \n", my_array)
                
                c = False
                while (c==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        c = True
                    else:
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        c = False

            elif (Exercise == 7):
                print("Exercise 7 :- How to limit the number of items printed in output of numpy array to 6?")
                my_array = []
                a = int(input("Size of array:"))
                for i in range(a):
                    my_array.append(int(input("Element : ")))
                #limit = int(input("Enter the threshold value of an array: "))
                my_array = np.array(my_array)
                np.set_printoptions(threshold=6)
                print(np.floor(my_array))
                
                b = False
                while (b==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        b = True
                    else:
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        b = False
            
            elif (Exercise == 8):
                print("Execise 8 :- How to pretty print a numpy array by suppressing the scientific notation like (1e10)?")
                my_array = []
                np.random.seed(100)
                row = int(input("Number of rows : "))
                column = int(input("Number of columns : "))
                random_array = np.random.random([row,column])
                print("Random array is : \n",random_array)
                random_array = random_array/1e3
                print ("Random array after division : \n", random_array)
                pres = int(input("Precision Value : "))
                np.set_printoptions(precision = pres, suppress=True)
                print ("Array after providing the precision value and suppression : \n", random_array)
                
                a = False
                while (a==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        a = True
                    else:
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        a = False
            
            elif (Exercise == 9):
                print("Exercise 9 :- How to swap two columns in a 2D numpy array?")
                my_array = np.arange(9).reshape(3, 3)
                print("Original array:")
                print(my_array)
                print("Which two columns would you like to swap? (NOTE: Column index starts with '0'.)")
                a = int(input())
                b = int(input())
                my_array[:,[a, b]] = my_array[:,[b, a]]
                print("\nAfter swapping of columns, our new array is : ")
                print(my_array)
                
                c = False
                while (c==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        c = True
                    else:
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        c = False

            elif (Exercise == 10):
                print("Exercise 10 :- How to swap two rows in a 2D numpy array?")
                my_array = np.arange(9).reshape(3, 3)
                print("Original array:")
                print(my_array)
                print("Which two rows would you like to swap? (NOTE: Column index starts with '0'.)")
                a = int(input())
                b = int(input())
                my_array[[a, b],:] = my_array[[b, a],:]
                print("\nAfter swapping of rows, our new array is : ")
                print(my_array)
                
                c = False
                while (c==False):
                    check = input("Would you like to check other exercise? (y/n)")
                    if (check == 'y' or check == 'Y' or check == 'yes' or check == 'YES'):
                        recheck = False
                        prog = False
                        c = True
                    else:
                        print("Please enter correct input")
                        recheck = True
                        prog = True
                        c = False

        else:
            print("Entered exercise number does not exist. Please enter the value between 1 and 10.")
            prog = False

