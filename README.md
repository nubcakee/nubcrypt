# Nubcrypt - Noob File Encryption
Python data encryption tools

## Install
``pip install nubcrypt``

## Common Usages
```python
import nubcrypt a nbx

filetarget = "testfile.txt"
key = "secret key"

#encrypt a file
outfile = filetarget + ".nubx"
nbx.encrypt_file(filetarget, key, outfile)

#encrypt a bytes
nubx_bytes = nubcrypt.encrypt_string("encrypt this text".encode(), key)
```
