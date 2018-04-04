import math
sequence = [2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
j = 0
summ = 0
for discharge in range (3, 10): #from 3 to 9 digits in the number
   for number in sequence: #sequences for every amount of digits
      for j in range(0, i+1):
         summ = summ + sequence[j]

      sequence[i] = summ
      i = i + 1
      summ = 0
   i = 0
   for number in sequence:
       sequence[i] = sequence [i] + 1
       i = i + 1
   print (discharge)
   print (sequence)
   i = 0

print (sum(sequence))
    
