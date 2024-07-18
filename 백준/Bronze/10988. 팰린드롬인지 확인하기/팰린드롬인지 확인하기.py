palindrome = list(input().strip())

for i in range(len(palindrome)//2):
    if palindrome[i] != palindrome[-i-1]:
        print(0)
        break
else:
    print(1)