lease = '''Dear Dot, 
           This document validates that you are beholden to a monthly payment of rent for this house.
           Rent is to be paid by the first of every month.
           Fill in your signature to agree to these terms.  
            -------------
            Please Sign Here: 
'''

signature = 'I said "I don not know"'



#1/ new_lease = signature + lease --> obviously not since wrong order
new_lease = signature + lease
print("1st choice\n", new_lease, "\n")

#2/ new_lease = lease + signature --> yes?
new_lease = lease + signature
print("2nd choice\n", new_lease, "\n")

#3/ new_lease = f'{lease}{signature}' --> yes?
new_lease = f'{lease}{signature}'
print("3rd choice\n", new_lease, "\n")

#4/ recopied the whole thing --> yes and the name is on the same line as please sign here, but like why...?
new_lease = f'''Dear Dot, 
This document validates that you are beholden to a monthly payment of rent for this house.
Rent is to be paid by the first of every month.
Fill in your signature to agree to these terms.
-------------
Please Sign Here: {signature} 
'''
print("4th choice\n",new_lease, "\n")

#5/ new_lease = f'{lease}+{signature}' --> there is a plus sign so no?
new_lease = f'{lease}+{signature}'
print("5th choice\n",new_lease)
