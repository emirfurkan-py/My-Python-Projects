# Generating qrcode with python
import qrcode
#set qrcode size
code=qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=50,
    border=5
)
#uploading qrcode address
code.add_data("https://github.com/emirfurki32")
code.make(fit=True)
#set qrcode colors and save in png format
image=code.make_image(fill_color="red",back_color="black")
image.save("vol2.png")
