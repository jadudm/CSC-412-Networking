# Import hashlib library (md5 method is part of it)
import hashlib    

def md5(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_md5.update(chunk)
  return hash_md5.hexdigest()

# File to check
file_name = 'filename.exe'      
 
hash = md5(file_name)

# Correct original md5 goes here
print(hash)
#original_md5 = '5d41402abc4b2a76b9719d911017c592'  

# Open,close, read file and calculate MD5 on its contents 
with open(file_name) as file_to_check:
  # read contents of the file
  data = file_to_check.read()    
  # pipe contents of the file through
  md5_returned = hashlib.md5(data).hexdigest()

# Finally compare original MD5 with freshly calculated
if hash == md5_returned:
  print "MD5 verified."
else:
  print "MD5 verification failed!." 
print("FILENAME: {0}",format(file_name))
print("HASH: {0}".format(hash))
print("MD5_returned: {0}".format(md5_returned))

def md5(msg):
  m = hashlib.md5()
  m.update(msg)
  return m.hexdigest()

def decode(msg):
  return hashlib.md5(msg).hexdigest()
  
msg = "Hello world"
hash = (md5(msg))
md5_returned = decode(msg)
if hash == md5_returned:
  print "MD5 verified."
else:
  print "MD5 verification failed!."
print("MSG: {0}",format(msg))
print("ENCODED MSG: {0}".format(hash))
print("DECODED MSG: {0}".format(md5_returned))
