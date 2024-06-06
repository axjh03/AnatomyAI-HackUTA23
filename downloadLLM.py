import gdown

# whole link
# https://drive.google.com/file/d/1UtXGktAaDMCgz4CyjhXVLJy4sz6_XIwx/view?usp=sharing

# File ID
file_id = "1UtXGktAaDMCgz4CyjhXVLJy4sz6_XIwx"

# Destination path to save the file
destination = "llama-2-7b-chat.ggmlv3.q8_0.bin"  # Replace 

# Download the file
gdown.download(f"https://drive.google.com/uc?id={file_id}", destination, quiet=False)
