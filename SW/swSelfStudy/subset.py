#subset
'''
유한개의정수로이루어진집합이있을때,
이집합의부분집합중에서그집합의원소를모두더한값이0이되는경우가있는지를알아내보자.
예를들어,이라는집합이있을때, {−3,−2,5}는이집합의부분집합이면서총합이0이므로이경우의답은참이다.
{-7,-3,-2,5,8}
'''
import  sys
sys.stdin = open('input/subset', 'r')


def candidate():
    list =[0,1]
    return list

def find(a,k,subset,numSet):
    global answer
    global answerSum
    if a==k :
        temp=[]
        sum =0
        for i in range(k):
            if subset[i]==1:
                temp.append(numSet[i])
                sum+=numSet[i]
        answer.append(temp)
        if sum ==0 : answerSum = True
    elif a<k :
        nCandidate = candidate()
        for i in range(len(nCandidate)):
            subset.append(nCandidate[i])
            find(a+1,k,subset,numSet)
            subset.pop(-1)
    else : return

answer = []
numSet = [-7,-3,-2,5,8]
subset=[]
answerSum = False
find(0,len(numSet),subset,numSet)
print(len(answer),answerSum)




'''
voidmain(void){
int i,j;
int arr[]={-7,-3,-2,5,8};
int n =sizeof(arr)/sizeof(arr[0]);
// n:원소의개수 
int sum;
int ret = 0;
    for(i =1;i <(1<<(n));i++)// 1<<n: 부분집합의개수
    {
        sum =0;
        for(j =0;j <n;j++)// 원소의수만큼비트를비교함
        {   
            if(i &(1<<j))// i의j번째비트가1이면j번째원소출력
            {
                sum +=arr[j];
            }
        }
        if(sum ==0)
            {
                ret = 1;break;
            }
    }
printf("%s\n", ret ? "True": "False");
}
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
N = 3
K = 10
cnt =0
n = len(arr)
subSet =[]
for i in range(1<<n):
    temp = []
    for j in range(n):
        if i &(1<<j):
            temp.append(arr[j])
    subSet.append(temp)
'''

arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
subset =[]
for i in range(1<<n):   #전체 부분집합갯수
    temp =[]
    for j in range(n):
        if i &(1<<j): # i의 j번째 비트가 1인지 리턴
            temp.append(arr[j])
    subset.append(temp)