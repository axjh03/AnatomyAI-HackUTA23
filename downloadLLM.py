import requests

url = "https://cdn-lfs.huggingface.co/repos/30/e3/30e3aca7233f7337633262ff6d59dd98559ecd8982e7419b39752c8d0daae1ca/8daa9615cce30c259a9555b1cc250d461d1bc69980a274b44d7eda0be78076d8?response-content-disposition=attachment%3B+filename*%3DUTF-8%27%27llama-2-7b-chat.ggmlv3.q4_0.bin%3B+filename%3D%22llama-2-7b-chat.ggmlv3.q4_0.bin%22%3B&response-content-type=application%2Foctet-stream&Expires=1717963444&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcxNzk2MzQ0NH19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5odWdnaW5nZmFjZS5jby9yZXBvcy8zMC9lMy8zMGUzYWNhNzIzM2Y3MzM3NjMzMjYyZmY2ZDU5ZGQ5ODU1OWVjZDg5ODJlNzQxOWIzOTc1MmM4ZDBkYWFlMWNhLzhkYWE5NjE1Y2NlMzBjMjU5YTk1NTViMWNjMjUwZDQ2MWQxYmM2OTk4MGEyNzRiNDRkN2VkYTBiZTc4MDc2ZDg%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qJnJlc3BvbnNlLWNvbnRlbnQtdHlwZT0qIn1dfQ__&Signature=SyIt4jnVZLhKHXELakpuirrJy9HHG7ETsYGWP0u8KhmKD2sv8hY35khc0F7fOG6Gh9sdSqvebSzFz-RrqMw-ibcLmzqoRJ35ZKNE0JjMmk61APtW0DiMMD8bCwRHQs8T3IA-eIP4ybz06UD3NTVTTrKCGkPw8nZMImph-BFmx6fOO9JD9CrrQ7TBE-LOAbfsGzOF-nAXjPhGzYvtliIsATipqDkTgGKOcJx9PeQDyHBRaHHr5jrss20%7EUixaWRHAt6Og2JJUA7CK%7ElCEy7Jgo5--%7EqDZoyfXxhvV6zqsaZrs1aXxoCov-QBoz6hEN5yKPjpWJC9DYjMJn4kce3o9fQ__&Key-Pair-Id=KVTP0A1DKRTAX"

file_name = "llama-2-7b-chat.ggmlv3.q4_0.bin"

# Send GET request to the URL
response = requests.get(url, stream=True)

# Raise an exception in case of an HTTP error
response.raise_for_status()

# Write the content of the response to a file
with open(file_name, 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            file.write(chunk)
print("Downloading llm")
print(f"Downloaded 'llama-2-7b-chat.ggmlv3.q4_0.bin' successfully.")
