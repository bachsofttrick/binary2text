i_want_to_input_binary_string = False
while True:
    print("Type a string to convert: ")
    input_string = input()
    byte_array = input_string.encode('utf-8')

    # Converting the byte_array into a binary 
    # integer
    binary_int = int.from_bytes(byte_array, byteorder="big")

    # Formats bytes in byte_array as 8-bit binary strings
    # padding for length consistency then joins 
    binary_string = ''.join(format(byte, '08b') for byte in byte_array)

    # Split a binary string into fixed-length chunks
    binary_string_split = ' '.join(binary_string[i:i+8] for i in range(0, len(binary_string), 8))

    # Print the converted binary characters
    print("Binary: " + binary_string_split)

    # If i_want_to_input_binary_string is set, type in a binary string
    # to convert
    # Remove spaces and join binary strings into a single string
    if i_want_to_input_binary_string:
        print("Type a binary string to convert (with spaces): ")
        binary_string = input()
    binary_string = binary_string.replace(" ", "")

    # Divides binary string into 8-bit chunks
    # converts each to integer (string should be interpreted as a binary number)
    # constructs bytes object from integers.
    utf8_result = bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
    print("UTF-8 hex: ", utf8_result.hex())
    print("UTF-8 decoded: ", utf8_result.decode('utf-8'))
    print()
