# Text system communication
The encryption and decryption algorithm is done in python. 
For the data compression method the huffman algorithm is implemented using the C & C++ languages.

In the ``src_python`` folder you can see the encryption and decryption algorithm, inside ``src_c++`` is the 
data compression method the huffman algorith and a basic compression by 
substitution, in ``input`` folder you can visualize the text files inputs and 
results in plain text format inside ``results`` folder.


## University of Costa Rica
## September, 2020


## Integrants
1. Brown Ramírez, Timna Belinda  B61254
2. Esquivel Molina, Brandon B52571


### Important
Change paths inside ``TxtEncryp_Decryp.py`` according with your machine.


## Instructions 
* To run the encryption and decryption mode you need to:

``
<LOCAL PATH>/Txt_SysCommu$ make 
``
* To run the simple compressor with the example input text in1.txt, do
``
$ make run_zip
``
You can compress a different file using:

``
./bin/main 0 <your_file_path>
``

the "0" indicates the threshold of occurrences of words to be substituted, 0 being the total substitution.

* To run the huffman encoding & decoding algorithm with the in1.txt example use:

``
$ make run_huffman
``

If you want to encode or decode a different file use:

``
$ ./src_c++/bin/hufman encode <your_file_path> <output_file_path>
``

``
$ ./src_c++/bin/hufman decode <your_file_path> <output_file_path>
``

