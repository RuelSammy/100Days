#Handle exceptions for file not found.
try:
	file1 = open("Myfolder/abc.txt")

except:
	print("file not found")
