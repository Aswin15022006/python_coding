word=input("enter the string")
a="aeiouAeiou"
ans=" "
for i in word:
    if(i not in a):
        ans=ans+i
print(ans)        
