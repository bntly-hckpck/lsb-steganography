from PIL import Image

# convert text to binary
def bit_conversion(text):
    binary_list = [] # empty list for binaries
    
    for character in text:
        
        ascii_value = ord(character) # ASCII value of the character
        binary_string = format(ascii_value, '08b') # ASCII conversion into 8-bit binary
        binary_list.append(binary_string) # add the resulting string to the binary list 
    
    final_string = ''.join(binary_list) # merge all the strings into one final string
    return final_string # return the final string

def encode_message(input_path, secret_message, output_path):

    image = Image.open(input_path) # open the input image
    rgba_image = image.convert('RGBA') # convert to rgba format
    pixels = list(rgba_image.getdata()) # get all of the pixels data

    bit_capacity = len(pixels) * 3 # total hiding capacity (1 pixel = 3 bits), if message doesn't fit data gets corrupted
    encoded_message = bit_conversion(secret_message) + ('0' * 16) # creates encoded message, converts and adds 16 0 bits delimiter 

    bit_idx = 0 # initializing bit index

    for i in range(len(pixels)): # main loop, will iterate over every pixel of the image

        r, g, b, a = pixels[i] # extracts the rgba values of the current [i] pixel, but we'll be using only r, g and b
        
        if bit_idx < len(encoded_message): # if we still have bits to hide, proceed
            hidden_bit = encoded_message[bit_idx] # reads the current bit from the secret message
            r = (r & 0xFE) | int(hidden_bit) # & 0xFE zeroes out the LSB for space, | int(hidden_bit) merges new secret bit (str -> int) into cleared position                        
            bit_idx += 1 # moves to the next bit

        if bit_idx < len(encoded_message):
            hidden_bit = encoded_message[bit_idx]
            g = (g & 0xFE) | int(hidden_bit)
            bit_idx += 1

        if bit_idx < len(encoded_message):
            hidden_bit = encoded_message[bit_idx]
            b = (b & 0xFE) | int(hidden_bit)
            bit_idx += 1
        
        pixels[i] = (r, g, b,a) # assigns modified bits to [i] pos in pixels list, inserting hidden message

    encoded_image = Image.new('RGBA', rgba_image.size) # creating a new rgba image for the output
    encoded_image.putdata(pixels) # inserting every pixel into the new image
    encoded_image.save(output_path) # saving the new, encoded image, to the desired output path (see below)

# executing the program
if __name__ == '__main__':

    input_path = 'bentley.png' # here goes your image's input path
    secret_message = "this is my secret message" # here goes your secret message
    output_path = 'encoding_output.png' # here goes your desired image's output path

    encode_message(input_path, secret_message, output_path) # encoding
