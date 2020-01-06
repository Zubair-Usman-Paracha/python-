def mergeSort (nlist):
    print ("[-] Sorting : ",nlist)

    if len(nlist) > 1 :
        divide = len(nlist)//2
        leftSide = nlist[:divide]
        rightSide = nlist[divide:]

        mergeSort(leftSide)
        mergeSort(rightSide)

        i=j=k=0

        while i < len(leftSide) and j < len(rightSide) :
            if leftSide [i] < rightSide [j]:
                nlist [k] = leftSide[i]
                i = i+1
            else :
                nlist [k] = rightSide [j]
                j= j+1
            k =k+1

        while i < len(leftSide):
            nlist[k] = leftSide [i]

            i = i+1
            k = k+1

        while j < len(rightSide):
            nlist [k] = rightSide[j]

            j = j+1
            k = k+1

    print ("[+] Merging : ",nlist)

nlist = [5,1,3,6,2,4]
mergeSort(nlist)
print ("[=] Merging is done : ",nlist)
         
