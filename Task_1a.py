for i in range(101):
	print (i+1)	#printing test case no. 
	N = input("")	#number of elements in list
	K = input("")	#number of places to shift
	array=[] 	#defining a blank list
	for i in range (N):	#taking input into the blank array
		if i>0:
			x=int(input(""))
			array.insert(i,x)
		else:
			 x=int(input("Enter Element "))
    			 array.insert(i,x)
    		i+=1
	temp = array[0:K]	#storing the sliced part of the original list
	del array[0:K]		#deleting the part to be left shifted
	output = array + temp	#placing the part to be left shifted at the back of the trimmed list
	print output		#printing out the left shifted list
