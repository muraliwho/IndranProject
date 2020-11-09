collectData = False
result = ""
fullResult = ""

file1 = open ( r"C:\dev\IM\BMO Bank of Montreal Online Banking.html", "r")
# file1 = open ( r"C:\dev\IM\test.txt", "r")
l = file1.readlines()

for s in l:
    fullResult = fullResult + s
    if (s.find("Transaction Date") > 0):
        collectData = True
    if ( collectData == True and s.find("$") > 0 ) :
        x1 = s.find("<td")
        x2 = s.find("</td>", x1)
        result = result + s[x1:(x2-x1)]
        # result = result + s
file1.close()
print (result)

file2 = open ( r"C:\dev\IM\BMO Bank of Montreal Online Banking-new.html", "w")
file2.write(fullResult)
file2.close()

