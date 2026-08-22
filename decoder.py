from PIL import Image

# transforming the bits into chars
def bits_to_char(bits):
    binary_chars = [] # empty list for binary chars

    for bit in bits: # for every bit in bits 
        binary_chars.append(str(bit)) # convert bit to string and add it to binary_chars

    byte_string = ''.join(binary_chars) # unify binary_chars, without spaces in between, in byte_string
    decimal = int(byte_string, 2) # convert byte_string to int, assigning it to decimal
    return chr(decimal) # convert decimal to char, return it

# decoding the message
def decode_message(image_path):
    image = Image.open(image_path) # open image from image_path
    rgb_image = image.convert('RGB') # convert image to RGB, preventing channel-related errors

    bits = [] # empty list for bits
    zero_counter = 0 # 0s counter (for terminator)

    for r, g, b in rgb_image.getdata(): # for every rgb pixel in image

        if zero_counter == 16: # before anything, if terminator (16 0s) is encountered, break out!
            break

        for channel in (r, g, b): # for every rgb channel
            bit = channel & 1 # desired bit is least significant bit (last one)

            if bit == 0: # if current bit is 0, check if we're near the terminator
                zero_counter += 1 # increment 0s counter by 1
            else:
                zero_counter = 0 # if bit is 1, reset 0s counter completely

            bits.append(bit) # add bit to bits list

    if zero_counter < 16: # if there are no 16 0s found, error
        return "error: no terminator found in this image"
        
    secret_message = '' # empty secret message string
    index = 0  # start at beginning

    while index < len(bits): # while index < bits length
        byte = bits[index : index + 8] # group next 8 bits together

        if len(byte) == 8: # if exactly 8 bits grouped
            secret_message += bits_to_char(byte) # convert bits to char and add it to secret message string
        
        index += 8 # increment index by 8, moving towards next byte

    return secret_message # at the end, return the completed secret message

# executing the program
if __name__ == '__main__':
     image_path = 'encoding_output.png' # here goes your encoded image
     secret_message = decode_message(image_path) # retrieving secret message, calling decode_message() with image_path
     print(f"the secret message is: '{secret_message}'") # print secret message  
