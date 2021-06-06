"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
tel_numbers_set = set()
for text in texts:
    tel_numbers_set.add(text[0])
    tel_numbers_set.add(text[1])
for call in calls:
    tel_numbers_set.add(call[0])
    tel_numbers_set.add(call[1])

print("There are {} different telephone numbers in the records.".format(
    len(tel_numbers_set)))

# Time Complexity for solution
#
# Both lists of texts and calls are scanned through once
# runtime = 2 * n
# 
# Adding a number to the set is in constant time
# However this happens n times
# runtime = 4 * n
#
# Get Length has a constant runtime = 1
# total runtime = 6 * n + 1
#
# Ans: Worst Case Runtime = O(n)