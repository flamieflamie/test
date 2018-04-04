import math
import copy
sequence = [2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
j = 0
summ = 0
print ('Please, input the amount of digits (from 3 to 100) :')
digits = int(input ())
for discharge in range (3, digits): #from 3 to 9 digits in the number
   sequence_temp = copy.deepcopy(sequence)
   for i in range(len(sequence_temp)): #sequences for every amount of digits
       for j in range(0, i+1):
         summ = summ + sequence_temp[j]
       sequence[i] = summ
       summ = 0
   for i in range(len(sequence)):
       sequence[i] = sequence [i] + 1
   print (discharge)
   print (sequence)

print (sum(sequence))
    
