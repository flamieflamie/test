import math
import copy

def count_good_numbers(digits_num):
    sequence = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    i = 0
    j = 0
    summ = 0
    for discharge in range (3, digits_num + 1):
        sequence_temp = copy.deepcopy(sequence)
        for i in range(len(sequence_temp)): #sequences for every amount of digits
            for j in range(0, i+1):
                summ = summ + sequence_temp[j]
                sequence[i] = summ
            summ = 0
        for i in range(len(sequence)):
            sequence[i] = sequence [i] + 1
    result = sum(sequence)
    return result

def main():    
    print ('Please, input the amount of digits (from 3 to 100) :')
    digits = int(input ())
    print (count_good_numbers(digits))

if __name__ == '__main__':
    main()
