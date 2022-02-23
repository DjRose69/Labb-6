import timeit

#------------------------------------------------------------------------------------------

setup_code1 = '''
from songClass import artistList
artistList = artistList[0:1000]
from bubbleSort import bubbleSort'''

stmt_code1 = '''bubbleSort(artistList)'''

time1 = timeit.repeat(stmt=stmt_code1, setup=setup_code1, number=1, repeat=5)
print(f'\nTime taken to sort list through Bubble Sort: {min(time1)} seconds.')

#------------------------------------------------------------------------------------------

setup_code2 = '''
from songClass import artistList
artistList = artistList[0:1000000]
from mergeSort import mergeSort'''

stmt_code2 = '''mergeSort(artistList)'''

time2 = timeit.repeat(stmt=stmt_code2, setup=setup_code2, number=1, repeat=5)
print(f'\nTime taken to sort list through Merge Sort: {min(time2)} seconds.\n')

#------------------------------------------------------------------------------------------