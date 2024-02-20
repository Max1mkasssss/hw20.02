import secrets
import string

symbols = string.ascii_letters + string.digits
hash_val = ''.join(secrets.choice(symbols) for i in range(10))


with open('data.py', 'a') as a:

    data_list = []

    for i in range(5): 
        data = input("Enter your data >>> ")
        data_list.append(data)

    a.write(hash_val + str(' = ') + str(data_list) + '\n')
    print('Your hash >>> '+ hash_val)


q = input(str('Do you want to see your data? (yes/no) >>> '))

if q == 'yes': 
    with open('data.py', 'r') as a:
        hash_to_find = input("Enter your hash >>> ")
        found = False
        for line in a:
            if line.startswith(hash_to_find):
                data_list = eval(line.split('=')[1])
                print(f"Data for hash: {data_list}")
                found = True
                break
        if not found:
            print("Hash not found in file.")
else: 
    print('Bye')
    
