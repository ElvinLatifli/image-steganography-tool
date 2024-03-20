from stegano import lsb
from PIL import Image

def encode_with_LSB(carrier_img_path, message_img_path, output_img_path):
    carrier_img = Image.open(carrier_img_path)

    encoded_img = lsb.hide(carrier_img, message_img_path)

    encoded_img.save(output_img_path)

    return encoded_img

def decode_with_LSB(encoded_img_path):

    encoded_img = Image.open(encoded_img_path)


    decoded_img = lsb.reveal(encoded_img)

    decoded_img = Image.open(decoded_img)
    return decoded_img


carrier_img_path = "image1.png"
message_img_path = "image.png"
output_img_path = "encoded_image.png"


encoded_img = encode_with_LSB(carrier_img_path, message_img_path, output_img_path)
decoded_img = decode_with_LSB(output_img_path)

