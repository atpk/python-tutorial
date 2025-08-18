import qrcode
from PIL import Image

# Generate QR with logo
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('your-url-here')  # Replace with your actual URL
qr.make()

qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img = qr_img.convert('RGB')

# Open and resize logo
logo = Image.open('path/to/image.file')
logo = logo.convert('RGBA')
logo_size = qr_img.size[0] // 5
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Create white square background
border_size = logo_size + 5  # Add small border each side
white_bg = Image.new('RGB', (border_size, border_size), 'white')

# Paste logo onto white background (centered)
logo_pos = ((border_size - logo_size) // 2, (border_size - logo_size) // 2)
white_bg.paste(logo, logo_pos, logo)

# Paste the logo+border onto QR code
qr_pos = ((qr_img.size[0] - border_size) // 2, (qr_img.size[1] - border_size) // 2)
qr_img.paste(white_bg, qr_pos)

qr_img.save('qr_with_logo.png')

# Display the result
from IPython.display import Image as IPImage, display
display(IPImage('qr_with_logo.png'))
