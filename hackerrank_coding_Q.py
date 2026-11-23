""" 


Contains only digits → invalid.

Contains only uppercase letters → invalid.

Contains only lowercase letters → invalid.

Contains any weak word from ["hello", "passowrd", "happy", "sad"] → invalid.

Otherwise → valid.
"""

def check_passwords(passwords):
    weak_words = ["hello", "passowrd", "happy", "sad"]
    result=[]
    
    for password in passwords:
        digits=0
        lowercase=0
        uppercase=0
        n=len(password)
        
        for char in password:
            if char.isdigit():
                digits+=1
            elif char.isalpha():
                if char.isupper():
                    uppercase+=1
                elif char.islower():
                    lowercase+=1
                    
        if digits==n or lowercase==n or uppercase==n:
            result.append(False)
            continue
        
        has_weak_word=False
        for weak_word in weak_words:
            if weak_word in password.lower():
                has_weak_word=True
                break
                
        result.append(not has_weak_word)
            
    print(result)
    return result
        
            


# Driver code
test_cases = [
    (["12345", "HELLO", "abc"], [False, False, False]),
    (["Abc123", "P@ss123"], [True, True]),
    (["Happy123", "sad@123"], [False, False]),
    (["ABC123", "abc@123"], [True, True]),
    (["123ABC", "Hello@123", "passowrd123"], [True, False, False])
]

count: int = 0

for passwords, expected in test_cases:
    actual = check_passwords(passwords)

    if actual == expected:
        count += 1

print(f"{count}/{len(test_cases)} PASSED")