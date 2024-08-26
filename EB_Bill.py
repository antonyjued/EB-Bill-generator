units=int(input("Enter Units : "))
if(units<300):
	units=units-100
	bill=(units*1.5)+20
elif(units>=300 and units<500):
	units=units-100
	bill=((units*0.5)*2)+((units*0.5)*3)+30
elif(units>=500 and units<800):
	units=units-100
	bill=((units*0.25)*2)+((units*0.75)*3)+30
elif(units>=800):
	units=units-100
	bill=(int(units*0.1439)*3.5)+(int(units*0.4289)*4.6)+(int(units*0.4289)*6.6)+50
	
print("Bill for Pay : ",bill)
	