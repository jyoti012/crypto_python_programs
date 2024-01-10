
import hashlib
import base64
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def find_mac_key():
  plain_text = "This is the message to Keccak-512 MAC!abc"
  mac = "6P9c8GDP31jtJ7dAW3E2YRKa+ntW3YQd+dL55bOMu4Qa8LhA0GF4LMZqtzWQlSDxqrn1gacjC3lIUurKUeWm8w=="
  target_mac_bytes = base64.b64decode(mac)

  for i in range(32, 127):  # Printable ASCII range
    for j in range(32, 127):
      for k in range(32, 127):
        modified_text = plain_text[:-3] + chr(i) + chr(j) + chr(k)
        encrypted_text = hashlib.sha3_512(
            modified_text.encode('utf-8')).digest()

        if encrypted_text == target_mac_bytes:
          return chr(i), chr(j), chr(k)

  return None


# Running the function and printing the result
key_chars = find_mac_key()
print(key_chars)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
