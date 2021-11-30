from heapq import nsmallest

iterable_ex = [1,5,9,7,2,3,8]

print(f'List:     {iterable_ex}')
print(f'Min:      {min(iterable_ex)}')
print(f'Max:      {max(iterable_ex)}')
print(f'n Lowest: {nsmallest(3, iterable_ex)}')
print(f'Sorted:   {sorted(iterable_ex)}')
