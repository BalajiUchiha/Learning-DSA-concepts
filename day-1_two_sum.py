target=10
nums=[1,5,3,7,9]
seen={}
j=0;
for i in nums:
    difference=target-i;
    if(difference in seen):
        print(seen[difference],j)
    seen[i]=j;
    j=j+1;

