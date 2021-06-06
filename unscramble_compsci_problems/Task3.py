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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# 1. Get the entries where calls are made from Bangalore
bangalore_calls = []
for call in calls:
    if '(080)' in call[0]:
        bangalore_calls.append(call)

# 2. Get the area codes of the receiver based on starting character
receiver_area_codes = set()
for call in bangalore_calls:
    if call[1][0] == '(':
        end_index = call[1].index(')')
        receiver_area_codes.add(call[1][1:end_index])
    elif call[1][0] in '789':
        receiver_area_codes.add(call[1][:4])
    else:
        receiver_area_codes.add(call[1][:3])

# 3. Sort and print for Part A
codes_sorted = sorted(receiver_area_codes)
print('The numbers called by people in Bangalore have codes:')
for code in codes_sorted:
    print(code)

# 4. Get count of calls made from Bangalore to Bangalore
to_bangalore_calls = []
for call in bangalore_calls:
    if '(080)' in call[1]:
        to_bangalore_calls.append(call)

print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    len(to_bangalore_calls)  * 100 / len(bangalore_calls)))

# Time Complexity for solution
#
# 1. List is scanned once and appended into another list
# runtime = n
#
# 2. New list is scanned once and inserted into a set
# runtime = n
#
# 3. List is sorted (n.log(n)) and then scanned through to print
# runtime = n.log(n) + n
#
# 4. List is scanned through and appended into a list
# runtime = n
#
# total runtime = n.log(n) + 4.n
# we can drop 4.n for very large values of n
#
# Ans: Worst Case Runtime = O(n.log(n))