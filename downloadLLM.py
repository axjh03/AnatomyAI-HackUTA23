import gdown

# whole link
# https://drive.google.com/file/d/1UtXGktAaDMCgz4CyjhXVLJy4sz6_XIwx/view?usp=sharing

# File ID
file_id = "1c3gkBDnRk0PyonpY_3_6XoIQ90XmEmL0"

# Destination path to save the file
destination = "llama-2-7b-chat.ggmlv3.q4_0.bin"  # Replace 

# Download the file
gdown.download(f"https://drive.google.com/uc?id={file_id}", destination, quiet=False)
