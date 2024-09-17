import qrcode

try:
    input_data = input("Enter a URL or text: ")

    img = qrcode.make(input_data)

    img.save("instagramni.png")
    print("QR code saved as 'instagramni.png'")
except Exception as e:
    print(f"An error occurred: {e}")
