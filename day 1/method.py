def move(time,speed):
	print("i am moving"  + str(speed)  + " kmph" + " at" + str(time))
	time = time + 1
	speed = speed-1 
	print("i am moving"  + str(speed)  +  " kmph"  +  " at"  +  str(time))

move(10,5)
print("____________")
move(2,10)	
print("____________")
move(3,11)
