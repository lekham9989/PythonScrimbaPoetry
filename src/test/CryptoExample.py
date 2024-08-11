# Project - crypto
# create a crypto machine that encrypts and decrypts messages

# If we got to message - message wii be a string, and if we encode, we need one dictionary with key as original string, value as encoded string and same for decoding. So, we need 2 dictionaries. we have to create keys, values. and we need input to crypto machine, a message and mode to encode or decode, then machine encodes or decodes and gives the result.

# Steps
def enigma_light():
    # create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    # autogenerate values string, by offsetting the keys string
    values = keys[-1] + keys[0:-1]
    # print(keys)
    # print(values)
    # create 2 dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))
    # OR create one and film it to get the other
    # dict_e = dict(zip(keys,values))
    # dict_d = {value,key for key,value in dict_e.itenms()}
    # input 'message' and mode for encode or decode
    msg = input('Enter a secret message:')
    mode = input('Enter you want to encode(e) or decode(d): ')
    # run encode or decode
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    # return result
    return new_msg.capitalize()

# clean and beautify the code
print(enigma_light())