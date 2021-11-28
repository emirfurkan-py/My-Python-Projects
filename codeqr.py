# python ile qrcode oluşturma
import qrcode
#qrcode boyutunu ayarlama
code=qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=50,
    border=5
)
#qrcode a adresi yükleme
code.add_data("https://github.com/emirfurki32")
code.make(fit=True)
#qrcode renklerini ayarlama ve png formatında kaydetme
image=code.make_image(fill_color="red",back_color="black")
image.save("vol2.png")
