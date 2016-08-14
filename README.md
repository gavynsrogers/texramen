
**RAMEN**
-----

RAMEN (RAndoM ENcryption) is a simple text encryption program that, rather than using a password, generates a file full of metadata to reassemble the text. Without the meta file, the data is completely useless. As such, it can be secured physically on a hard drive, CD, phone, in the cloud, etc. The goal here was not to create the next big thing in cryptography; but instead to add another layer of protection on top of standard file encryption.

All it is is a python program that is under 200 lines of code. It's compatible with any Linux machine capable of running bash, Python 3 and the `touch` command. It is probably compatible with more shells than just bash but I haven't tested it with any. Cross-compatibility is in the cards.

**To install:**

Simply mark the file as executable (usually `chmod +x` and run it. It has no special dependencies outside of `touch` and `python3`.

Developed by [Gavyn Rogers](https://github.com/gavynsrogers)

gavyn.rogers97@gmail.com
