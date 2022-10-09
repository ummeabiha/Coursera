def computepay(h, r):
    if h > 40:
        overtime_hrs = h - 40
        pay = (40 * r) + ((r * 1.5) * overtime_hrs)
        return pay
    else:
        pay = h * r
        return pay


hrs = input("Enter Hours:")
rte = input("Enter rate:")
hours = float(hrs)
rate = float(rte)

p = computepay(hours, rate)
print("Pay", p)
