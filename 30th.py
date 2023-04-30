pb1=499.00
pb2=855.00
pb3=645.00
print("Books Available :")
print("Book 1. Introduction to Python Programming : Rs {0}\nBook 2. Python Libraries Cookbook : Rs {1}\nBook 3. Data Science in Python : Rs {2}\n".format(pb1,pb2,pb3))
qb1=float(input("Quantity of Book1 : "))
qb2=float(input("Quantity of Book2 : "))
qb3=float(input("Quantity of Book3 : "))
amount=qb1*pb1+qb2*pb2+qb3*pb3
gst=12
delcharges=250.00
print("Taxes and additional charges - \n\tGST : {0}%\n\tDelivery Charges : Rs.{1}".format(gst,delcharges))
total_price=amount*gst/100+delcharges
print("Total Invoce Amount : {0}".format(total_price))


