def one_loop(n):
    ''' One loop, from 0 to n-1 '''
    count = 0
    for i in range(n):
        count += 1
    return count

def nested2(n):
    ''' Two nested loops from 0 to n-1 '''
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

def nested_ij(n):
    ''' Nested loops: outer i from 0 to n-1; inner from 0 to i-1 '''
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    return count

def nested_ijk(n):
    ''' Nested loops: outer i from 0 to n-1; middle j from 0 to i-1; inner k from 0 to j-1 '''
    count = 0
    for i in range(n):
        for j in range(i):
            for k in range(j):
                count += 1
    return count

def nested3(n):
    ''' Three nested loops from 0 to n-1 '''
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count

def binary_count(n, printflag = False):
    printflag and print( n , "-bit binary numbers, least significant bit first")
    A = np.zeros(n, 'int')
    count = 0
    i = 0
    while i < n:
        printflag and print(A)
        count += 1
        A[0] += 1
        i = 0
        while A[i] > 1:
            A[i] = 0
            i = i+1
            if i == n: break
            A[i] += 1
    return count

def n_count(n, printflag = False):
    printflag and print(f'{n}-tuples from [0..{n-1}].  Order matters, repetition allowed.')
    A = np.zeros(n, 'int')
    count = 0
    i = 0
    while i < n:
        printflag and print(A)
        count += 1
        A[0] += 1
        i = 0
        while A[i] >= n:
            A[i] = 0
            i = i+1
            if i == n: break
            A[i] += 1
    return count

def nondecr_count(n, printflag = False):
    printflag and print(f'Choose {n} from  [0..{n-1}] with repetition.  List as non-decreasing {n}- tuple.')
    A = np.zeros(n, 'int')
    count = 0
    i = 0
    while A[n-1] < n:
        printflag and print(A)
        count += 1
        A[0] += 1
        i = 0
        while i < n-1 and A[i] > A[i+1]:
            A[i] = 0
            i = i+1
            A[i] += 1
    return count

def i_count(n, printflag = False):
    printflag and print(f'{n}-tuples where the ith element is from  [0..{n}-i].  Order matters, repetition allowed.')
    A = np.zeros(n, 'int')
    count = 0
    i = 0
    while i < n:
        printflag and print(A)
        count += 1
        A[0] += 1
        i = 0
        while A[i] >= n-i:
            A[i] = 0
            i = i+1
            if i == n: break
            A[i] += 1
    return count

def incr_count(n, printflag = False):
    printflag and print(f'Choose {n} from  [0..{2*n-1}] without repetition.  List as increasing {n}- tuple.')
    A = np.arange(n)
    count = 0
    i = 0
    while A[n-1] < 2*n:
        printflag and print(A)
        count += 1
        A[0] += 1
        i = 0
        while i < n-1 and A[i] >= A[i+1]:
            A[i] = i
            i = i+1
            A[i] += 1
    return count


print(binary_count(20))
print(n_count(20))
print(nondecr_count(20))
print(i_count(20))
print(incr_count(20))