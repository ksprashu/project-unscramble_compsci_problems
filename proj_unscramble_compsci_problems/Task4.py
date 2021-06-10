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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# 1. Collect list of outgoing and incoming numbers
outgoing_calls = set([call[0] for call in calls])
incoming_calls = set([call[1] for call in calls])
outgoing_texts = set([text[0] for text in texts])
incoming_texts = set([text[1] for text in texts])

#2. find outgoing_calls that are not present in any other set
telemarketers = outgoing_calls - incoming_calls - outgoing_texts - incoming_texts
telemarketers_sorted = sorted(telemarketers)

print("These numbers could be telemarketers: ")
for number in telemarketers_sorted:
    print(number)

# Time Complexity for solution
#
# 1. List is scanned 4 times and appended into another list
# runtime = 4.n
#
# 2. Set Difference is computed 3 times and then sorted
# Runtime for set difference is O(len(s))
# runtime = n.log(n) + 3.n
#
# List is scanned through to print
# runtime = n
#
# total runtime = n.log(n) + 8.n
# we can drop 8.n for very large values of n
#
# Ans: Worst Case Runtime = O(n.log(n))
