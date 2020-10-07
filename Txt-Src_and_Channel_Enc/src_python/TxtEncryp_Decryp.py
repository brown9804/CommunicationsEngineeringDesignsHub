# @brown9804 Belinda Brown
# timna.brown@ucr.ac.cr
# Python3
# Text decryption algorithm

#******************************************************
#               PACKAGES
#******************************************************
import sys
from time import sleep

#******************************************************
#               DEFINITIONS
#******************************************************
def ProgressBar(value, max, label):
	bar_size = 40 #progress bar size
	sys.stdout.write('\r')
	bar = ""
	bar = '*' * int(bar_size * value)
	bar = bar + '-' * int(bar_size * (1-value))
	sys.stdout.write(f"{label.ljust(10)} | [{bar:{bar_size}s}] {round((value*100),2)}% \n")
	sys.stdout.flush()
	sleep(0.05)

##########
##########                  ENCRYP FILE
def filetxt_encrip(file_input, num_x,sys_x,vocalm_x, alf_x,writefile_x):
	file_x = open(file_input, "r")    ### OPEN
	text_x= file_x.read()
	counter_x = 0
	j_x = 0
	l_x = len(text_x)
	print("\nThe file has " + str(l_x) + " characters\n")
	write_file = open(writefile_x, "w")    #### OPEN
	for i_x in text_x:
		counter_x += 30
		if i_x in num_x: # numbers - alfm
			value_x = abs(round(((l_x-counter_x)%len(alf_x))%(len(alf_x)+l_x+len(alf_x))))
			if value_x >= len(num_x):
				charac_x = i_x
				write_file.write(charac_x)
			else:
				charac_x = alf_x[abs(round(((l_x-counter_x)%len(alf_x))%(len(alf_x)+l_x+len(alf_x))))]
				write_file.write(charac_x)
#**********************************************************************
		elif i_x in sys_x: # symbols - vocals
			value_x = abs(round(((l_x-counter_x)%len(vocalm_x))%(len(alf_x)+l_x+len(vocalm_x))))
			if value_x >= len(vocalm_x):
				charac_x = i_x
				write_file.write(charac_x)
			else:
				charac_x = vocalm_x[abs(round(((l_x-counter_x)%len(vocalm_x))%(len(alf_x)+l_x+len(vocalm_x))))]
				write_file.write(charac_x)
#**********************************************************************
		elif i_x in alf_x: # alf - sym
			value_x = abs(round(((l_x-counter_x)%len(sys_x))%(len(alf_x)+l_x+len(sys_x))))
			if value_x >= len(sys_x):
				charac_x = i_x
				write_file.write(charac_x)
			else:
				charac_x = sys_x[abs(round(((l_x-counter_x)%len(sys_x))%(len(alf_x)+l_x+len(sys_x))))]
				write_file.write(charac_x)
#**********************************************************************
		elif i_x in vocalm_x: # vocals - num_x
			value_x = abs(round(((l_x-counter_x)%len(num_x))%(len(alf_x)+l_x+len(num_x))))
			if value_x >= len(vocalm_x):
				charac_x = i_x
				write_file.write(charac_x)
			else:
				charac_x = num_x[abs(round(((l_x-counter_x)%len(num_x))%(len(alf_x)+l_x+len(num_x))))]
				write_file.write(charac_x)
	#**********************************************************************
		else:
			charac_x = " "
			write_file.write(charac_x)
		j_x +=1
		ProgressBar(j_x/l_x, l_x, "Progress -> File Encrytion ")
	print("Your message is encrypted\n")
	file_x.close()     ### CLOSE
	write_file.close()   ### CLOSE
	return



##########
##########                  ENCRYP
def manualentry_encryp(messg,numm,sysm,vocalm, alfm, writefile, path_console):
	input_msg = open(path_console, "w") #### OPEN
	input_msg.write(messg)
	# Close opend file
	input_msg.close() 				#### CLOSE
	lenghtm = len(messg)
	counter = 0
	j = 0
	print("\nThe message has " + str(lenghtm)+ " characters\n")
	filex = open(writefile, "w")    ### OPEN
	for i in messg:
		counter += 30
		if i in numm: # numbers - alfm
			value = abs(round(((lenghtm-counter)%len(alfm))%(len(alfm)+lenghtm+len(alfm))))
			if value >= len(numm):
				charac = i
				filex.write(charac)
			else:
				charac = alfm[abs(round(((lenghtm-counter)%len(alfm))%(len(alfm)+lenghtm+len(alfm))))]
				filex.write(charac)
#**********************************************************************
		elif i in sysm: # symbols - vocals
			value = abs(round(((lenghtm-counter)%len(vocalm))%(len(alfm)+lenghtm+len(vocalm))))
			if value >= len(vocalm):
				charac = i
				filex.write(charac)
			else:
				charac = vocalm[abs(round(((lenghtm-counter)%len(vocalm))%(len(alfm)+lenghtm+len(vocalm))))]
				filex.write(charac)
#**********************************************************************
		elif i in alfm: # alf - sym
			value = abs(round(((lenghtm-counter)%len(sysm))%(len(alfm)+lenghtm+len(sysm))))
			if value >= len(sysm):
				charac = i
				filex.write(charac)
			else:
				charac = sysm[abs(round(((lenghtm-counter)%len(sysm))%(len(alfm)+lenghtm+len(sysm))))]
				filex.write(charac)
#**********************************************************************
		elif i in vocalm: # vocals - numm
			value = abs(round(((lenghtm-counter)%len(numm))%(len(alfm)+lenghtm+len(numm))))
			if value >= len(vocalm):
				charac = i
				filex.write(charac)
			else:
				charac = numm[abs(round(((lenghtm-counter)%len(numm))%(len(alfm)+lenghtm+len(numm))))]
				filex.write(charac)
	#**********************************************************************
		else:
			charac = " "
			filex.write(charac)
		j +=1
		# print((j)/lenght)
		ProgressBar(j/lenghtm, lenghtm, "Progress -> Message Encryption")
		# print("Charater encrypted!\n")
	print("Your message is encrypted\n")
	# print(encrypted)
	# Close opend file
	filex.close()    ### CLOSE
	return
##########
##########                  DECRYP
def decryp_file(decryp_message_d,numm_d,sysm_d,vocalm_d, alfm_d, save_in_file_d):
	file_d = open(decryp_message_d, "r")    #### OPEN
	text_d= file_d.read()
	lenghtm_d = len(text_d)
	counter_d = 0
	j_d = 0
	print("\nThe message has " + str(lenghtm_d)+ " characters\n")
	filex_d = open(save_in_file_d, "w")     ### OPEN
	for i_d in text_d:
		counter_d += 30
		if i_d in alfm_d: # numbers <- alfm
			value_d = abs(round(((lenghtm_d-counter_d)%len(alfm_d))%(len(alfm_d)+lenghtm_d+len(alfm_d))))
			if value_d >= len(numm_d):
				charac_d = i_d
				filex_d.write(charac_d)
			else:
				charac_d =  numm_d[abs(round(((lenghtm_d-counter_d)%len(alfm_d))%(len(alfm_d)+lenghtm_d+len(alfm_d))))]
				filex_d.write(charac_d)
#**********************************************************************
		elif i_d in vocalm_d: # symbols <- vocals
			value_d = abs(round(((lenghtm_d-counter_d)%len(vocalm_d))%(len(alfm_d)+lenghtm_d+len(vocalm_d))))
			if value_d >= len(vocalm_d):
				charac_d = i_d
				filex_d.write(charac_d)
			else:
				charac_d = sysm_d[abs(round(((lenghtm_d-counter_d)%len(vocalm_d))%(len(alfm_d)+lenghtm_d+len(vocalm_d))))]
				filex_d.write(charac_d)
#**********************************************************************
		elif i_d in sysm_d: # alf <- sym
			value_d = abs(round(((lenghtm_d-counter_d)%len(sysm_d))%(len(alfm_d)+lenghtm_d+len(sysm_d))))
			if value_d >= len(sysm_d):
				charac_d = i_d
				filex_d.write(charac_d)
			else:
				charac_d =  alfm_d[abs(round(((lenghtm_d-counter_d)%len(sysm_d))%(len(alfm_d)+lenghtm_d+len(sysm_d))))]
				filex_d.write(charac_d)
#**********************************************************************
		elif i_d in numm_d: # vocals <- numm
			value_d = abs(round(((lenghtm_d-counter_d)%len(numm_d))%(len(alfm_d)+lenghtm_d+len(numm_d))))
			if value_d >= len(vocalm_d):
				charac_d = i_d
				filex_d.write(charac_d)
			else:
				charac_d = vocalm_d[abs(round(((lenghtm_d-counter_d)%len(numm_d))%(len(alfm_d)+lenghtm_d+len(numm_d))))]
				filex_d.write(charac_d)
#**********************************************************************
		else:
			charac_d = " "
			filex_d.write(charac_d)
		j_d +=1
		# print((j_d)/lenght_d)
		ProgressBar(j_d/lenghtm_d, lenghtm_d, "Progress -> Decryption")
		# print("Charater decrypted!\n")
	# Close save file
	filex_d.close()     ### CLOSE
	# Close input file
	file_d.close()     ### CLOSE
	print("Your message is decrypted\n...\n ")
	return

######
###### Verification
def verification_process(decoded_file,verify_script, Verified_file):
	##########   Verification ############
	decoded_result = open(decoded_file, "r")
	final_result_file = open(Verified_file, "w")      ######## OPEN EMPTY FILE
	file_decrip= open(verify_script, "r")       ######## OPEN MODEL
	for v in file_decrip: #If actual message -> EACH MODEL CHARAC
		if v in decoded_result:  # For decoded result
			final_result_file.write(v) # append in a vector
		else:
			final_result_file.write(v)
	decoded_result.close()
	file_decrip.close()      ### CLOSE
	final_result_file.close()        ### CLOSE
	print("Verification process -> DONE")
	return

##########
##########                  MENU
def menu():
	print("\n\n*****************************************\n")
	print("")
	print("				...... MENU ......\n")
	print("")
	print("\n\n*****************************************\n")
	print("\n")
	print("1.The encrypted result will be in the results folder and where the encryption_results.txt\n")
	print("2.The decrypted result will be in the results folder and where the Verified_Decryption.txt\n")
	print("\n\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	print("			....								")
	print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n")
	option = input("0. Quit\n1. Manual message to encrypt\n2. Take a data compression file for encrypted and decrypted  \n3. Decrypt the last message introduced \nChoose an option: .....    ")
	main(option)
	return option
##########
##########                  MAIN
def main(op):
	num = ["0","1","2","3","4","5","6","7","8","9"]
	sym = [":","!","@","$","?","¿","¡",",",".","+","-","_","#", "&","%", "/", "^", "*", "(",")"]
	vocal = ["a","e","i","o","u"]
	alf = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
	# print("Amount of num items:    ....      ", len(num))
	# print("Amount of symbol items:    ....      ", len(sym))
	# print("Amount of vocal items:    ....      ", len(vocal))
	# print("Amount of alf items:    ....      ", len(alf))
	data_compress_file = "/Users/belindabrown/Desktop/Txt_SysCommu/results/zip.txt"
	input_path = "/Users/belindabrown/Desktop/Txt_SysCommu/input/input_console.txt"
	path = "/Users/belindabrown/Desktop/Txt_SysCommu/results/encryption_results.txt"
	save_in_filex = "/Users/belindabrown/Desktop/Txt_SysCommu/results/decryption_results.txt"
	Verified_Decryption = "/Users/belindabrown/Desktop/Txt_SysCommu/results/Verified_Decryption.txt"
	if op == "1":
		message = input("\nEntry the message that you wanna encrypt... \n")
		manualentry_encryp(message,num,sym,vocal, alf,path, input_path)
		op = menu()
	if op == "2":
		filetxt_encrip(data_compress_file,num,sym,vocal, alf,path)
		decryp_file(path,num,sym,vocal, alf,save_in_filex)
		verification_process(save_in_filex,data_compress_file, Verified_Decryption)
		op = menu()
	if op == "3":
		decryp_file(path,num,sym,vocal, alf,save_in_filex, input_path, Verified_Decryption)
		op = menu()
	if op =="0":
		print(" \n******************\nEND ------")
		sys.exit()
	if op != ("0" or "1" or "2" or "3"):
		print("\nWrong value, please check\n")
		op = menu()
	return


#******************************************************
#               MAIN
#******************************************************
option_choose = menu()
main(option_choose)
