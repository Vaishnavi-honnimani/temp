temperature=float(input("Enter temperature C:"))

if temperature <20:
    status="cold"
elif temperature <=30:
    status="normal"
else:
    status="Hot"

fahrenheit=(temperature*9/5)+32       

print(f"temperature:{temperature}C")
print(f"status:{status}")
print(f"Temperature in Fahrenheit:{fahrenheit}F")