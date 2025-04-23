"""
You want to be safe online and use different passwords 
for different websites. However, you are forgetful at times 
and want to make a program that can match which password belongs 
to which website without storing the actual password!
This can be done via something called hashing.
"""

from hashlib import sha256

def hash_password(password):
    """
    Hash a password using SHA256 and return the hex digest.
    """
    return sha256(password.encode()).hexdigest()

# stored logins dictionary with hashed passwords
store_logins = {
    'hina@gmail.com': hash_password('abcd1234'),
    'code_in_placer@cip.org': hash_password('efgh567'),
    'studentportal.edu': hash_password('jklm8901')
}

def login(email, store_logins, password_to_check):
    """
    Returns True if the hash of password_to_check matches the stored hash for the email.
    """
    if email not in store_logins:
        return False
    return store_logins[email] == hash_password(password_to_check)


def main():
    print(login('hina@gmail.com', store_logins, 'abcd1234'))
    print(login('hina@gmail.com',store_logins, 'password'))
    
    print(login('code_in_placer@cip.org', store_logins,'cookies'))
    print(login('code_in_placer@cip.org', store_logins,'efgh567'))

    print(login('studentportal.edu', store_logins,'password'))
    print(login('studentportal.edu', store_logins,'amsnd12233@'))

if __name__ == '__main__':
    main()