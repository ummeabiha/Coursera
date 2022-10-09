list=[]
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
       try:
         int_num= int(num)
         list.append(int_num)
       except:
         print("Invalid input")


print("Maximum is ",max(list))
print("Minimum is ",min(list))
