# 1
hrs = input("Enter Hours:")
rte= input("Enter rate:")
hours=float(hrs)
rate=float(rte)

if hours>40:
    overtime_hrs= hours-40
    pay= (40*rate) + ((rate*1.5)* overtime_hrs)
    print("Pay:",pay)
else:
    pay = print("Pay:",hours * rate)
