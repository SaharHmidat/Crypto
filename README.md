# Crypto
The code do encryption & decryption for TEA algorithm for either CBC or ECB mode 
In main module asked user to enter Key and IV and the mode to run 
In image module based on mode make encryption or decryption then converts the  bytes back to an image format using the Image.frombytes() function and show the image in grey scale 
In CBC module make the encryption and decryption, first to guarantee that the length of the plaintext is more than the block size, it is padde to make sure that data input can be divided into blocks in equals size then convert the input data and IV into a list of 32 bit then do the encryption for each block and at the end convert it into byte string in decryption instead of make plaintext = lengthInput(plaintext) such as first in encryption, make the inversre by unlengthInput(decryptedData) at the end 
In ECB module, write the function convertToByteString,convertToListInt,lengthInput and unlengthInput that used in previous module and in ECb module then make encryption and decryption, same way in encryption and decryption but didn't use Xor such as CBC.
In TEA module write the same algorithm that provides in assignment for encryption and decryption.
