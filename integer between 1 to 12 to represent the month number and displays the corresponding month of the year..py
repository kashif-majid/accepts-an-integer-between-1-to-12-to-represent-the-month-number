def month(i):
    a={1:"january",
       2:"february",
       3:"march",
       4:"april",
       5:"may",
       6:"june",
       7:"july",
       8:"august",
       9:"september",
       10:"october",
       11:"november",
       12:"december"}
    print(a[i])

i=1
while i==1:
    month_num=int(input("ENTER MONTH NUMBER BETWEEN 1 TO 12: "))
    month(month_num)

    i = int(input("\nIF U WANT TO CONTINUE PRESS 1 ELSE PRESS ANY KEY: "))