User
from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
import os

class ImageEncryptionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Encryption")

        # Set the size of the GUI window
        window_width = 800
        window_height = 600
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        master.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

        # Get the path to the desktop directory
        self.desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        self.input_image_path = os.path.join(self.desktop_path, "images.jpeg")

        # Load the original image
        self.original_image = Image.open(self.input_image_path)
        self.original_image.thumbnail((400, 400))  # Resize the image for display
        self.original_image_tk = ImageTk.PhotoImage(self.original_image)

        # Create a frame to contain the original image
        self.original_frame = Frame(master)
        self.original_frame.pack()

        # Display the original image
        self.original_image_label = Label(self.original_frame, image=self.original_image_tk)
        self.original_image_label.pack()

        # Create frames to display encrypted and decrypted images
        self.encrypted_frame = Frame(master)
        self.encrypted_frame.pack(pady=20)
        self.decrypted_frame = Frame(master)
        self.decrypted_frame.pack(pady=20)

        # Create buttons for encryption and decryption
        self.encrypt_button = Button(master, text="Encrypt", command=self.encrypt_image, bg="green", fg="white")
        self.encrypt_button.pack(side="left", padx=10, pady=10)

        self.decrypt_button = Button(master, text="Decrypt", command=self.decrypt_image, bg="red", fg="white")
        self.decrypt_button.pack(side="right", padx=10, pady=10)

    def encrypt_image(self):
        # Encrypt the input image
        encrypted_image_path = self.encrypt_image_func(self.input_image_path)

        if encrypted_image_path:
            # Load the encrypted image
            encrypted_image = Image.open(encrypted_image_path)
            encrypted_image.thumbnail((400, 400))  # Resize the image for display
            encrypted_image_tk = ImageTk.PhotoImage(encrypted_image)

            # Display the encrypted image
            encrypted_image_label = Label(self.encrypted_frame, image=encrypted_image_tk)
            encrypted_image_label.image = encrypted_image_tk
            encrypted_image_label.pack()

    def decrypt_image(self):
        # Decrypt the encrypted image
        decrypted_image_path = self.decrypt_image_func(os.path.join(self.desktop_path, "encrypted_image.png"))

        if decrypted_image_path:
            # Load the decrypted image
            decrypted_image = Image.open(decrypted_image_path)
            decrypted_image.thumbnail((400, 400))  # Resize the image for display
            decrypted_image_tk = ImageTk.PhotoImage(decrypted_image)

            # Display the decrypted image
            decrypted_image_label = Label(self.decrypted_frame, image=decrypted_image_tk)
            decrypted_image_label.image = decrypted_image_tk
            decrypted_image_label.pack()

    def encrypt_image_func(self, image_path):
        # Check if the image file exists
        if not os.path.isfile(image_path):
            print(f"Error: Image file '{image_path}' not found.")
            return None

        # Open the image
        img = Image.open(image_path)
        width, height = img.size

        # Encrypt the image by swapping pixel values
        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                # Example of a basic mathematical operation (adding a constant value)
                new_pixel = tuple((p + 50) % 256 for p in pixel)
                img.putpixel((x, y), new_pixel)

        # Save the encrypted image
        encrypted_image_path = os.path.join(self.desktop_path, "encrypted_image.png")
        img.save(encrypted_image_path)
        return encrypted_image_path  # Return the path to the encrypted image

    def decrypt_image_func(self, encrypted_image_path):
        # Check if the encrypted image file exists
        if not os.path.isfile(encrypted_image_path):
            print(f"Error: Encrypted image file '{encrypted_image_path}' not found.")
            return None

        # Open the encrypted image
        img = Image.open(encrypted_image_path)
        width, height = img.size

        # Decrypt the image by reversing the encryption process
        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                # Example of reversing the mathematical operation
                original_pixel = tuple((p - 50) % 256 for p in pixel)
                img.putpixel((x, y), original_pixel)

        # Save the decrypted image
        decrypted_image_path = os.path.join(self.desktop_path, "decrypted_image.png")
        img.save(decrypted_image_path)
        return decrypted_image_path  # Return the path to the decrypted image

# Create and run the GUI
root = Tk()
app = ImageEncryptionGUI(root)
root.mainloop()