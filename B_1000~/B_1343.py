data=list((input().split('.')))

for i in range(len(data)):
   if len(data[i])%4==2:
      a="AAAA"*(len(data[i])//4)  # 4로 나눈 몫만큼
      b="B"*(len(data[i])%4)      # 4로 나눈 나머지 만큼
      data[i]=a+b
   elif len(data[i])%4==0:
      a="AAAA"*(len(data[i])//4)  # 4로 나눈 몫만큼
      data[i]=a 
   else:
      data=[-1]
      break

result=data[0]

for i in data[1:]:
   i='.'+i
   result+=i

print(result)