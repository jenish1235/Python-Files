# get user email address
email = input("What is Your email address ==> ").strip()

# slice out user name 
user = email[:email.index("@")]

# slice domain name    
domain = email[email.index("@") + 1:]

# format message
output = f"your Username is {user} and your domain is {domain}"
# display output message
print(output)