"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_duration = dict()
for call in calls:
    call_duration[call[0]] = call_duration.get(call[0], 0) + int(call[3])
    call_duration[call[1]] = call_duration.get(call[1], 0) + int(call[3])

# call_duration_sorted = sorted(
#     call_duration, key=lambda k: call_duration[k], reverse=True)
longest_call = max(call_duration, key=lambda k: call_duration[k])
print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(
    longest_call, call_duration[longest_call]))

# Time Complexity for solution
#
# The list is scanned through once
# runtime = n
#
# The dict is scanned for every item in the list and an insert is done
# This happens in constant time in the dictionary, but is done n times
# runtime = 2 * n
#
# Sorting is an n * log(n) operation in best case (python implements timsort)
# runtime = n * log(n)
# Note: worst case we can assume that there are no duplicates,
# hence all the numbers are in the dictionary
#
# Based on code review, updated longest_call to use max() in order to reduce
# time complexity from n.log(n) to n.
# 
# (new) runtime = n
#
# Look-up happens in constant time
# runtime = 2
#
# total runtime = 3.n + 2
# We can ignore the lower order terms
#
# Ans: Worst Case Runtime = O(n)
