## Belinda Brown
## Github @brown9804
## timna.brown@ucr.ac.cr

#!/usr/bin/
# -*- coding: utf-8 -*-

#######################################################
#                     1
#######################################################
def get_Data(input):
	import cv2
	from PIL import Image
	##### Read each image
	image_open = cv2.imread(input)
	img_gray = cv2.cvtColor(image_open, cv2.COLOR_BGR2GRAY, 0)
	return img_gray

#######################################################
#                     2
#######################################################
def binary_inv_threshold(image,result_folder):
	import cv2
	import time
	import os
	# Threshold.
	# first_value -> Set values equal to or above 220 to 0.
	# second_value ->  values below 220 to 255.
	th, bin_img = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY_INV);
	os_t = time.time()
	cv2.imwrite( str(result_folder) + 'RGBtoBINARY%s.jpg'%os_t, bin_img)
	print("\n")
	print("**********************************************")
	print("		RGB -> BINARY IMAGE  			Stage	")
	print("**********************************************")
	print('\n'+ str(result_folder) + 'RGBtoBINARY%s.jpg'%os_t+ '--> DONE \n')
	print("\n-----------------------------------------------")
	print("RGB -> BINARY IMAGE  ------->      DONE ")
	print("-----------------------------------------------\n")
	return bin_img

#######################################################
#                     3
#######################################################
def analize_source_data(dataBase):
	## Data storage
	complete_BinData = []
	pixel_high = []
	pixel_low = []
	## Data counters
	total_bits_counter = 0
	high_bits_counter = 0
	low_bits_counter = 0
	for vector in dataBase:
		for pixel in vector:
			total_bits_counter = total_bits_counter + 1
			if (pixel == 255): #### WHITE
				pixel = 0 ### Pix on low
				complete_BinData.append(pixel)
				pixel_high.append(pixel)
				##### Counter
				high_bits_counter = high_bits_counter + 1

			else:
				pixel = 1 ## Pix on high
				complete_BinData.append(pixel)
				pixel_low.append(pixel)
				##### Counter
				low_bits_counter = low_bits_counter + 1

	return complete_BinData, pixel_high, pixel_low, total_bits_counter, low_bits_counter, high_bits_counter

#######################################################
#                     4
#######################################################
def packaging(completeData, n):
	pkg_arr_arr = []
	pkg_arr_arr = [completeData[bit:bit+n] for bit in range(0, len(completeData), n)]
	# print(len(pkg_arr_arr)) # rows
	# print(len(pkg_arr_arr[0])) # columns
	return pkg_arr_arr

#######################################################
#                     5
#######################################################
def creating_G(data_packages, num_bit):
	import random
	import numpy as np
	# # Generator matrix
	big_matrix = []
	num_col = 0
	high = 1
	low = 0
	seq =  [0,0, 1, 1, 0, 0, 0 ]
	final_Gmx = []
	# step 1
	for i in range(0, num_bit-1): # 6x6
		for x in range(0, num_bit-1):
			index = random.randint(0, 1)
			big_matrix.append(index)
	print("Before Rows:     \n", big_matrix)
	print("\n")
	final_Gmx = [big_matrix[bit:bit+num_bit-1] for bit in range(0, len(big_matrix), num_bit-1)]
	print("As matrix Generator:				\n", final_Gmx)
	print("\n")

	### Parid verification by Rows
	parid =  0
	for rows in final_Gmx: # 6x6
		# print(rows)
		for i in range(0, num_bit - 1):
			parid = parid + rows[i]
			# print(parid)
		if (parid % 2 == 0):
			rows.append(0)
		else:
			rows.append(1)
		parid =  0
		i = 0
		print("\nPrinting Row by Row: ", rows)

	### Parid verification by Columns
	result_sum_col = []
	# print(type(final_Gmx)) # list of vector
	# print(final_Gmx[0][1])
	for j in range(0, num_bit): ### vector  [7 positions ]
		ii = 0
		parid_cols =  0
		for ii in range(0, num_bit-1):
			parid_cols = parid_cols + final_Gmx[ii][j]
		if (parid_cols % 2 == 0):
			result_sum_col.append(0)
		else:
			result_sum_col.append(1)
		# print(result_sum_col)

	final_Gmx.append(result_sum_col)
	print("\n")
	for x in final_Gmx:
		print("\nFinal Generator Matrix: ", x)
	#### Creating identity
	identity = []
	identity = np.identity(7)
	print("\nIdentity Matrix:\n", identity)
	# print("\nIdentity type", type(identity))
	# print("\nGmatrix final type", type(final_Gmx))
	##### Need to append final_Gmx with the identity
	G_matrix = []
	G_matrix = np.concatenate((final_Gmx, identity), axis=1, out=None)
	print("\nFinal Gmatrix:	\n", G_matrix)
	return G_matrix

#######################################################
#                     6
#######################################################
def pack_X_genM(pkgs, Gmatrix_ready, number_b):
	import numpy as np
	print("\nThe amount of rows from Binary Source:			", len(pkgs))
	print("\nThe amount of columns from Binary Source:			", len(pkgs[0]))
	print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
	print("\nThe amount of rows from G_matrix:			", len(Gmatrix_ready))
	print("\nThe amount of columns from G_matrix:			", len(Gmatrix_ready[0]))
	print("\n--------------*----------------\n")
	print("\nBinary Source ----> rowsXcolumns: 			" + str(len(pkgs)) + " X " +  str(len(pkgs[0])) )
	print("\nG_matrix ----> rowsXcolumns: 			" + str(len(Gmatrix_ready)) + " X " +  str(len(Gmatrix_ready[0])) )
	##### 186833 X 7 * 7x14
	##### 1 X 7 * 7x14
	##### .....
	bin_u_data = []
	u_data = np.zeros((len(pkgs),len(Gmatrix_ready[0]) ), dtype=int, order='C')
	u_data = [[sum(a*b for a,b in zip(pkgs_row,Gmatrix_ready_col)) for Gmatrix_ready_col in zip(*Gmatrix_ready)] for pkgs_row in pkgs]
	for row in u_data:
		for item in row:
			# print(item)
			if (int(item) % 2 == 0):
				even = 0
				bin_u_data.append(even)
			else:
				odd = 1
				bin_u_data.append(odd)
	bin_u_data = [bin_u_data[bitx:bitx + 2*number_b] for bitx in range(0, len(bin_u_data), 2*number_b)]
	print("\nBinary rows, expecting 186833:					", len(bin_u_data))
	print("\nResult of ---- Packages * Gmatrix = U .......	\n")
	verify0 = 0
	for x in bin_u_data:
		verify0 = verify0 + 1
		# print(x)
		# print(len(x)) # how many columns
	print("\nFinal verification, expecting 186833 rows:					", verify0)
	return bin_u_data # ready verified

#######################################################
#                     7
#######################################################
def noise(u_data, err_porcentage,n_bits_no):
	import random
	import numpy as np
	err_counter = 0
	#### 186833 x 14
	v_noise_unpack = []
	final_v  = []
	###### Verification
	noise_verify0 = 0
	high_cnt = 0
	low_cnt = 0
	static = 0
	# print(type(v_noise_unpack)) # verified numpy.ndarray
	for eachpack in u_data:
		# print(eachpack) # verify pack 14 bits
		# print(noise_verify0) # verified row number #186833
		noise_verify0 = noise_verify0 + 1  # 186833
		err_counter = err_counter + len(eachpack) #### threshold each time 14
		indexNoise = random.randint(0, len(eachpack) - 1)
		for bit_to_noise in eachpack:
			if (err_counter >= err_porcentage): # # # if more err
				if ( int(indexNoise) % 2 == 0): # if even
					# print(indexNoise) # need to be [0,.... or ..... 13] # verified
					err = 0
					v_noise_unpack.append(err) # verified
					low_cnt = low_cnt + 1 # v_noise_unpack
				else:	# take random pack and ~ as errs
					# print("0") # verified
					err_0 = 1
					v_noise_unpack.append(err_0)
					high_cnt = high_cnt + 1 # verifed
			else:
				static = static + 1
				v_noise_unpack.append(bit_to_noise) #

	print("\nNoise counter, expecting 186833:				 ", noise_verify0) # number of iterations # verified
	print("\nAmount of changed to HIGH:					", low_cnt)  #
	print("\nAmount of changed to LOW:					", high_cnt) #
	print("\nAmount of Static value:					", static) #

	##### ready ----> Sum of both = total
	###### Matrix expected -> 186833 x 14 -
	final_v = [v_noise_unpack[bitj:bitj + 2*n_bits_no] for bitj in range(0, len(v_noise_unpack), 2*n_bits_no)]
	# print("\n V matrix .......	\n", final_v)
	vHigh = 0
	vLow = 0
	vRow =  0
	for vv in final_v:
		# print(vv) # verifed
		# print(len(vv)) # verfied
		vRow = vRow + 1
		for v in vv:
			if v == 1:
				vHigh  = vHigh + 1
			else:
				vLow = vLow  + 1
	print("\n+++++++++&+++++++++\n")
	print("\nFinal Verification for Rows, expecting 186833:				 ", len(final_v))
	print("\nFinal HIGH verfication new, expecting " + str(high_cnt) + ":				", vHigh)
	print("\nFinal LOW verfication new, expecting " + str(low_cnt) + ":				", vLow)
	return final_v # ready verfied

#######################################################
#            Sindrome   Stage
#######################################################
### # 186833x7       X      # 186833 x 14
def sindrome(Srcmatrix, Vmatrix, number_bits):
	Smatrix =  [] # sindrome
	sindrome1_counter = 0
	sindrome0_counter = 0
	assert_counter =  0
	# print("Srcmatrix rows", len(Srcmatrix))
	# print("Vmatrix rows", len(Vmatrix))
	for s_el, v_el in sorted(zip(Srcmatrix,Vmatrix)):
		# here we are in rows
		for i in range(0, 7):
			if (len(s_el) == len(v_el[:number_bits])): # if this range
					# print(s_el[i])
					# print(v_el[i])
					if s_el[i] != v_el[i]:
						if s_el[i] == 1:
							Smatrix.append("wrong_1")
							sindrome1_counter = sindrome1_counter +  1
						else:
							Smatrix.append("wrong_0")
							sindrome0_counter = sindrome0_counter +  1
					else:
						Smatrix.append(v_el[i])
						assert_counter = assert_counter + 1
			else: # if less items inside row - helps in tail condition
				Smatrix.append(v_el)
				assert_counter =  assert_counter + 1
	print("\nTotal of SINDROME 0 bit found:				", sindrome0_counter)
	print("\nTotal of SINDROME 1 bit found:				", sindrome1_counter)
	print("\nTotal of RIGHT bit found:				", assert_counter)
	# print("\nThe unpack sindrome matrix is:			\n", Smatrix)
	Smatrix_pack = [Smatrix[bits:bits + number_bits] for bits in range(0, len(Smatrix), number_bits)]
	print("\nAmount of pack rows in Sindrome matrix:				", len(Smatrix_pack))
	# print("\nPack Sindrome matrix \n", Smatrix_pack)
	# ver = 0
	# for row in Smatrix_pack:
	# 	print(row)
	# 	ver = ver + 1
	# print(ver)
	return Smatrix_pack, sindrome0_counter, sindrome1_counter, assert_counter


#######################################################
#            Fixing Error   Stage
#######################################################
### # 186833x7       X      # 186833 x 7
def fixing_err(Src_M, Sindrome_M, numbits, sin0c, sin1c, okCC):
	Received_M =  [] # sindrome
	fix0_counter = 0
	fix1_counter = 0
	ok_counter =  0
	# print(len(Src_M))
	# print(len(Sindrome_M))
	# print(type(Src_M))
	# print(type(Sindrome_M))
	for row in Sindrome_M:
		for item_s in row:
			if item_s == 'wrong_1':
				Received_M.append(0)
				fix1_counter = fix1_counter +  1
			elif item_s == 'wrong_0':
				Received_M.append(1)
				fix0_counter = fix0_counter +  1
			else:
				Received_M.append(item_s)
				ok_counter = ok_counter + 1
	print("\nTotal of fixed SINDROME 0 bit, expecting " + str(sin0c)  +  " :				" + str(fix0_counter))
	print("\nTotal of fixed SINDROME 1 bit, expecting " + str(sin1c)  +  " :				" + str(fix1_counter))
	print("\nTotal of RIGHT bit, expecting " + str(okCC) + " :				" + str(ok_counter))
	Received_M_pack = [Received_M[bitfin:bitfin + numbits] for bitfin in range(0, len(Received_M), numbits)]
	print("\nAmount of pack rows in Sindrome matrix:				", len(Received_M_pack))
	# print("\nThe final received data is:\n")
	# for final_row in Received_M_pack:
	# 	print(final_row)
	return Received_M_pack



#######################################################
#                     FINAL
#######################################################
def BINARY_RGB(gray_img, r_folder):
	import cv2
	import time
	import os
	reverted_rgb_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB)
	os_t = time.time()
	cv2.imwrite( str(r_folder) + 'BINARYtoRGB%s.jpg'%os_t, reverted_rgb_img)
	print("\n")
	print("**********************************************")
	print("		BINARY -> RGB IMAGE 		Stage	")
	print("**********************************************")
	print('\n'+ str(r_folder) + 'BINARYtoRGB%s.jpg'%os_t+ '--> DONE \n')
	print("\n-----------------------------------------------")
	print("BINARY -> RGB IMAGE  ------->      DONE ")
	print("-----------------------------------------------\n")
	return reverted_rgb_img
