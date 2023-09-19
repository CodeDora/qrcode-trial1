import tkinter as tk #gerekli packs
import qrcode

def generate_qr_code():
    url = entry.get()  # Kullanıcının girdiği URL'yi al
    if url:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save("qr_code.png")  # QR kodu dosyaya kaydet
        qr_img.show()  # QR kodunu ekranda göster



# Ana pencereyi oluştur
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("800x400")  # Pencere boyutunu 800x400 olarak ayarla

# URL giriş kutusu oluştur
entry_label = tk.Label(window, text="Link:")
entry_label.pack(pady=10)  # Boşluk ekleyerek büyüklüğü artır
entry = tk.Entry(window, width=60)
entry.pack(pady=10)  # Boşluk ekleyerek büyüklüğü artır

# "Dönüştür" düğmesi oluştur
generate_button = tk.Button(window, text="Dönüştür", command=generate_qr_code, width=20, height=2)
generate_button.pack()
# Pencereyi çalıştır
window.mainloop()
