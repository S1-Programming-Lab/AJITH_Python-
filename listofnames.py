Astr=input("enter the string \n")
char=input("enter the character \n")
print("given string :\n",Astr)
print("givewn character :\n",char)
res=0
for i in range(len(Astr)):
    if(Astr[i]==char):
        res=res+1
        print(""number of time character is present in string:\n",res)
