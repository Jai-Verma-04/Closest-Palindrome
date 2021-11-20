print("CLOSEST PALINDROME TO A NUMBER")

def main():
    try:
        num = int(input("Enter a Number: "))
        def ispalindrome(n):
                if str(n)[::-1]==str(n):
                   return True
        
        def ask_again():
            ask = input("Wanna play again?[Y/N] >>").lower()
            if ask == 'y':
                main()
            elif ask == 'n':
                exit()
            else:
                print("Invalid Choice")
                ask_again()
                
        def check(n):
            if n>10:
                if ispalindrome(n):
                    print('number', n, 'is already a palindrome')
                    ask_again()
                else:
                    upper, lower = n,n
                    while True:
                        upper+=1;lower-=1
                        
                        if ispalindrome(upper):
                            print("Closest Palindrome number = ",upper)
                            ask_again()
                        
                        elif ispalindrome(lower):
                            print("Closest Palindrome number = ",lower)
                            ask_again()
            elif n<10:
                print('Number should not be less than or equal to 10')
        check(num)
        
    except ValueError:
        print('Only Numbers are allowed')
        main()
main()
