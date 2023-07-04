print('*** Converting hh.mm.ss to seconds ***')

time = [int(i) for i in input('Enter hh mm ss : ').split()]

second = time[0] * 3600 + time[1] * 60 + time[2]
formatted_seconds = '{:,}'.format(second)

formatted_time = "{:02d}:{:02d}:{:02d}".format(time[0], time[1], time[2])

if (time[1] > 59 or time[1] < 0):
  print(f'mm({time[1]}) is invalid!')
elif (time[2] > 59 or time[2] < 0):
  print(f'ss({time[2]}) is invalid!')
else:
  print(f'{formatted_time} = {formatted_seconds} seconds')
