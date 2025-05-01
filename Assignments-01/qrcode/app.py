# This code generates a QR code and saves it as an image file. It also provides functionality to decode a QR code from an image file.
import qrcode

# this function generate a QR code and save an image file
def generate_qrcode():
    
    # data to be encode in the QR code
    data = "https://github.com/Tayyaba10"
    # create a QR code image from the data
    img = qrcode.make(data)
    
    img.save("C:/Users/tayya/OneDrive/Desktop/New folder/myqrcode.png")
    
# this function create another QR code from user input image file
def decode_qr():
    
    path = input("Enter the path of the QR code image: ")
    
    # create a QR code with the specified version, box size, and border
    qr = qrcode.QRCode(version = 1, box_size=10, border=5)
    
    # add data to the QR code
    qr.add_data(path)
    qr.make(fit=True)
    
    # create an image with custom colors
    img = qr.make_image(fill_color="red", back_color="white")
    # save the image
    img.save("C:/Users/tayya/OneDrive/Desktop/New folder/decode.png")
    
# main function to run the program
def main():
    
    # generate a initial Qr code
    generate_qrcode()
    print("QR code generated and saved as file.png")
    
    # provide menu options to the user
    choice = input("1. Generate another QR code\n2. Decode QR\n3. Exit\nEnter your choice: ")
    if choice == '1':
        generate_qrcode()
        
    elif choice == '2':
        decode_qr()
        
    elif choice == '3':
        print("Exiting...")
        
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()