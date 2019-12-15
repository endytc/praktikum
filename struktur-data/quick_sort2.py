def quickSort(alist,first=None,last=None):
   if first is None:
     first = 0
   if last is None:
     last = len(alist)-1

   if first<last:

       splitpoint = partition(alist,first,last)

       quickSort(alist,first,splitpoint-1)
       quickSort(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   while rightmark >= leftmark:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark >= leftmark:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [40,20,10,80,60,50,7,30,100]  
print("Before sort ",alist)
quickSort(alist)
print("After sort ",alist)