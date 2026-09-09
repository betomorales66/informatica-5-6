import qrcode

def main():
    song = "https://www.youtube.com/watch?v=P1jH1ekZuEI&list=RDP1jH1ekZuEI&start_radio=1"
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data("Some data")
    qr.make(fit=True)

    img = qr.make_image(fill_color="orange", black_color="dark-blue")
    img.save("my-qrcode.png")





if __name__=="__main__":
    main()
