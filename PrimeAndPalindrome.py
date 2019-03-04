##############################
# Author: Shu'aib Solomons
# Date: 04/03/2019
# Description: Calculates n number of if number is prime and palindrome
##############################

def isPrime(num):
    if(num < 2):
        return False
    elif(num != 2 and num%2 == 0):
        return False
    else:
        return all (num % i for i in range(3, int(num**0.5)+1))

def isPalindrome(number):
    strNum = str(number)
    if(number<10):
        return False
    elif(strNum[0] != strNum[len(strNum)-1]):
        return False
    else:
        if(number%2 == 0):
            right = len(strNum)-1
            for i in range(len(strNum)):
                if(strNum[i]==strNum[right]):
                    right-=1
                    continue
                else:
                    return False
            return True
        else:
            right = len(strNum)-1
            for i in range(len(strNum)-1):
                if(strNum[i]==strNum[right]):
                    right-=1
                    continue
                else:
                    return False
            return True            
            


def nPrimeNumbers(n):
    prime = []
    count = 0
    i = 1
    while(count !=5):
        if(isPrime(i) == False):
            i +=1
            continue
        prime.append(i)
        i +=1
        count += 1
    return prime

def nPrimeNPalindrome(n):
    prime_pal = []
    count = 0
    i = 1
    while(count !=n):
        if isPrime(i) == False or isPalindrome(i) == False:
            i +=1
            continue
        prime_pal.append(i)
        i +=1
        count += 1
    return prime_pal
    

#print(nPrimeNumbers(5))
print(nPrimeNPalindrome(5))
