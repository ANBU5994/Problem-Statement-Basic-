'''Today task for coding 
1.A washing machine works on the principle of Fuzzy System, the weight of clothes put 
inside it for washing is uncertain but based on weight measured by sensors and the water 
level chosen, it decides total time needed. 
For low level water, the time estimate is 25 minutes, where approximately weight is 
between 2000 grams or any nonzero positive number below that.
For medium level water, the time estimate is 35 minutes, where approximately weight is 
between 2001 grams and 4000 grams.
For high level water, the time estimate is 45 minutes, where approximately weight is 
above 4000 grams. Assume the capacity of machine is maximum 7000 grams. 
When the weight is zero, time needed is 
0
minutes. 
If the weight exceeds maximum weight limit, then, print “OVERLOADED”, and for all 
negative weights, the output is “INVALID INPUT”.
Sample Input-1: 2000, L
Sample Output-1: Time Estimated: 25 minutes
Input should be in the form of integer value. 
Output must have the following format: Time Estimated: NN Minutesc'''

A=input().strip()
parts= A.split(',')
if len(parts)!=2:
    print('invalid')
else:
    try:
        n=int(parts[0])
        value=(parts[1])

        if n<0:
            print("invalid value")
        elif n==0:
            print("time estimate is zero")
        elif n>7000:
            print("exceeds the value")

        if  value == 'L' and n<=2000 :
            print("estimate time is 25 Minutes")
        elif value== 'M' and  2001 <= n <= 4000 :
            print("estimate time is 35 Minutes")
        elif value== 'H' and  4001 >= n  :
            print("estimate time is 45 Minutes")
        else:
            print("invalid")

    except:
        print("invalid")