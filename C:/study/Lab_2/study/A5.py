a= int (input())
b= int (input())
result = "YES"*(a%b==0)+ "NO"*(a%b!=0)
print (result)