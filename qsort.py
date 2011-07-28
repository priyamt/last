def qsort(a):
  if len(a)<=1:return a
  
  mid=a.pop(len(a)/2)
  less=[]
  great=[]
  for num in a:
    if num<=mid:less.append(num)
    else:great.append(num)
  sortedlist=[]
  if len(less)>0:
    sortedlist.extend(qsort(less))
  sortedlist.append(mid)
  if len(great)>0:
    sortedlist.extend(qsort(great))
  return sortedlist




print qsort(a=[1,5,32,74,13,45,23])
    
