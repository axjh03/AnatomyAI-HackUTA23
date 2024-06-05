import gdown

# whole link
# https://drive.google.com/file/d/1oE6xUUcM9suo9HL9E27zEi7vIO79viw2/view?usp=sharing

# File ID
file_id = "1oE6xUUcM9suo9HL9E27zEi7vIO79viw2"

# Destination path to save the file
destination = "llama-2-7b-chat.ggmlv3.q8_0.bin"  # Replace 

# Download the file
gdown.download(f"https://drive.google.com/uc?id={file_id}", destination, quiet=False)
