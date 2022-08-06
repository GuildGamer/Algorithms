import math

def sort(array: list):
    # if the length of the array is 1, return array
    if len(array) == 1:
        return array

    else:
        # get the length of the first half of the array
        length = len(array)
        n1 = int(length/2) + (length % 2 > 0)

        print(n1)
        
        L = []
        R = []

        # divide the array intp 2
        for i in range(n1):
            L.append(array[i])
            j = i + 1
        
        for i in range(j, length):
            R.append(array[i])

        #sort recuesively if the length of the array is greater than 2
        if len(array) > 2:
            L = sort(L)
            R = sort(R)

        i = 0
        j = 0

        # new list to hold sorted array i.e A[p..k-1]
        n_list  = []

        for k in range(len(array)):
            
            if L[i] <= R[j]:
                n_list.append(L[i])

                # makes sure the last added element to the sorted array is ignored in... 
                # ...the next comparison iteration
                L[i] = math.inf

                # prevents loop from calling array element out of range
                if (i + 1) < len(L):
                    i += 1

            else:
                n_list.append(R[j])
                R[j] = math.inf

                if (j + 1) < len(R):
                    j += 1

        print(n_list)
        return n_list


if __name__ == "__main__":
    arr = eval(input("Array to sort: "))

    sorted = sort(arr)