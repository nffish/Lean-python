import qrcode

# pip install qrcode
# version: v 1-40 (v-1)*4+21
# error_correction 容错系数 L7 M15 Q25 H30
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.ERROR_CORRECT_M,
    box_size=4,
    border=4,

)
qr.add_data('http://wwww.google.com')
qr.make(fit=True)  # 编译数据
img = qr.make_image(fill_color='white', back_color='red')
img.save('qrcode_color.png')
