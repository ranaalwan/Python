#get age in all time units


#input age

print( " if you want your aga in all time units " .center(60,'¤'))
age=int(input(' what\'s Your Age? ').strip())



month= age*12
week = month*4
days = age*365
hour = days*24
minutes = hour*60
seconds = minutes*60

print('You lived for:')
print(f"{month} Month" )
print(f"{week:,} Week" )
print(f"{days:,} Days")
print(f"{minutes:,} Minutes")
print(f"{seconds:,} Seconds")