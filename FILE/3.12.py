def dayUp(df):
	dayup=1.0
	for i in range(365):
		if i%7 not in [5,6,0]:
			dayup=dayup*(1+df)
	print("{:3f}.".format(dayup))

N=0.001
while(N<0.011):
    dayUp(N)
    N=N+0.001
