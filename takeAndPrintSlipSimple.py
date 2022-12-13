import os
import tempfile
extension = ".txt"
filename = tempfile.mktemp(extension)

name ="Customer Name = " + input("Enter Customer Name : ")
id ="Product ID = " +  (input("Enter product ID : "))
product ="Product Name = " +  input("Enter Product Name : ")
price ="Price = " + input("Enter Price : ")
signature = "--------------------------\nIssued by: M Zeeshan Zafar\n--------------------------"

text = name + "\n" + id + "\n" + product + "\n" + price + "\n" + signature
open(filename,'w').write(str(text))
os.startfile(filename,"print")