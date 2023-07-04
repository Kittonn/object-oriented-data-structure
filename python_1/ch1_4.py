print(' ***Function Odd List***')

nums = [int(i) for i in input('Enter list numbers : ').split()]

print('Input list : ', nums)

odd_list = [i for i in nums if i % 2 != 0]

print('Output list : ', odd_list)
