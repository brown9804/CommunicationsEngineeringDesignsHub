#Python3
# brown9804 Belinda Brown
#timna.brown@ucr.ac.cr
#                   Encryption & Decryption

#******************************************************************************
#******************************************************************************
# Frames result folder
R = ./results/
SRC = ./src_python/




#******************************************************************************
############ 						Run python script
#******************************************************************************
all: encryp_decryp

encryp_decryp:
	python3 $(SRC)TxtEncryp_Decryp.py

#******************************************************************************
############ 							CLEAN FOR ALL
#******************************************************************************


.PHONY: clean
clean:
	> $(R)encryption_results.txt
	> $(R)decryption_results.txt
	> $(R)Verified_Decryption.txt
