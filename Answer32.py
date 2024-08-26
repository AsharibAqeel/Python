import zlib

def compress_string(s):
    return zlib.compress(s.encode('utf-8'))

def decompress_string(compressed_data):

    return zlib.decompress(compressed_data).decode('utf-8')

original_string = "hello world!hello world!hello world!hello world!"

compressed_data = compress_string(original_string)
print("Compressed data:", compressed_data)

decompressed_string = decompress_string(compressed_data)
print("Decompressed string:", decompressed_string)

assert original_string == decompressed_string, "The decompressed string does not match the original string."
