
import timeit 

'''
Documentation:

SETUP is the code that needs to be executed BEFORE running the code snippet that
we wish to time, for example importing modules and such.

STMT is the code snippet that we WANT to measure the time of, and that is
what will be timed when using the timeit module.

NUMBER is the number of times the STMT code snippet will be executed.

What is printed by TIMEIT is the time amount taken by performing the STMT
code snippet by a decided NUMBER of times.
'''

#------------------------------------------------------------------------------------------

setup_code1 = '''
from songClass import artistList
artistList = artistList[0:1000000]
from linearSearch import linearSearch'''

stmt_code1 = '''linearSearch(artistList, 'Donny Hathaway')'''

time1 = timeit.repeat(stmt=stmt_code1, setup=setup_code1, number = 1, repeat=5)
print(f'\nLinear search time: {min(time1)} seconds.')

#------------------------------------------------------------------------------------------

setup_code2 = '''
from songClass import artistList
artistList = artistList[0:1000000]
artistList.sort()
from binarySearch import binarySearch'''

stmt_code2 = '''binarySearch(artistList, 'Donny Hathaway')'''

time2 = timeit.repeat(stmt=stmt_code2, setup=setup_code2, number = 1, repeat = 5)
print(f'\nBinary search time: {min(time2)} seconds.')

#------------------------------------------------------------------------------------------

setup_code3 = '''
from songClass import artistList
artistList = artistList[0:1000000]
artistDict = {}
for index in range(len(artistList)):
    artistDict[artistList[index]] = index'''

stmt_code3 = '''artistDict['Donny Hathaway']'''

time3 = timeit.repeat(stmt=stmt_code3, setup=setup_code3, number = 1, repeat = 5)
print(f'\nDictionary search time: {min(time3)} seconds.\n')

#------------------------------------------------------------------------------------------
