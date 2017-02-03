# Binary CRC Exercise
# Assignment 1
# Brandon Knieriem
# Goals:
# 	Prompt the user for a valid binary value and check it.
# 	Calculate what kind of errors may have occurred.
# 	If there's an error, show where it occurred.
# 	If too many errors occurred and it can't be corrected, say so.
#IMPORTS########################################################

import sys

#FUNCTIONS######################################################
#Vets input based on length and values.
def enter_bin() :
	while True :
		bin_num = input("12 digit binary value or 'quit': ")
		if(bin_num == 'quit') : sys.exit()
		print("Input Value / Length:",bin_num, "/", len(bin_num))
		bin_list = list(bin_num)
		for x in bin_list :
			if(x != 1 or x != 0) :
				valid = False

		if( (len(bin_num)) != 12) :
			valid = False
		else :
			valid = True
			break

		print("Error: Invalid entry.")

	return bin_num
#-----------------------------------------------------------------
# d1, d2, d4, d5, d7. Checking c1.
def check_c1(bin_num, error_count) :
	eval_digits = [
	bin_num[2], bin_num[4], bin_num[6], bin_num[8], bin_num[10]]
	check = evaluate(eval_digits)
	is_valid = validate(check, bin_num[0])
	if(is_valid == False) :
		print("Error: C1.")
		error_count += 1

	return error_count
#-----------------------------------------------------------------
# d1, d3, d4, d6, d7. Checking c2.
def check_c2(bin_num, error_count) :
	eval_digits = [
	bin_num[2], bin_num[5], bin_num[6], bin_num[9], bin_num[10]]
	check = evaluate(eval_digits)
	is_valid = validate(check, bin_num[1])
	if(is_valid == False) :
		print("Error: C2.")
		error_count += 2

	return error_count
#-----------------------------------------------------------------
# d2, d3, d4, d8. Checking c4.
def check_c4(bin_num, error_count) :
	eval_digits = [bin_num[4], bin_num[5], bin_num[6], bin_num[8] ]
	check = evaluate(eval_digits)
	is_valid = validate(check, bin_num[3])
	if(is_valid == False) :
		print("Error: C4.")
		error_count += 4

	return error_count
#-----------------------------------------------------------------
# d5, d6, d7, d8. Checking c8.
def check_c8(bin_num, error_count) :
	eval_digits = [bin_num[8], bin_num[9], bin_num[10], bin_num[11] ]
	check = evaluate(eval_digits)
	is_valid = validate(check, bin_num[7])
	if(is_valid == False) :
		print("Error: C8.")
		error_count += 8

	return error_count
#-----------------------------------------------------------------
#Odd or even number of '1's? Even = True, Odd = False
def evaluate(eval_digits) :
	total = 0
	for i in eval_digits :
		if(i == '1') : total += 1
	if(total % 2 == 0) :
		return True
	if(total % 2 == 1) :
		return False
#-----------------------------------------------------------------
#Boolean check. True = even, False = odd. Used to verify c1.
def validate(check, c) :
	if check  == True and c == '0' :
		return True;
	elif check == False and c == '1' :
		return True;
	else :
		return False;
#-----------------------------------------------------------------
def error_handling(bin_num, error_count) :
	if(error_count == 0) :
		print("Success: No errors detected.")
		print_byte(bin_num)
	elif(error_count > 12) :
		print("Error: Unrecoverable binary value.")
	else :
		print("Error: Recoverable binary value.")
		#print("Position / Value:",
		#	error_count, "/", bin_num[error_count])
		bin_list = list(bin_num)

		if(bin_list[error_count] == '1') :
			bin_list[error_count] = 0
		else :
			bin_list[error_count] = 1
		print_byte(bin_list)
#-----------------------------------------------------------------
# Prints the original byte of data; with or without correction.
def print_byte(bin_num) :
	print(bin_num[2], bin_num[4], bin_num[5], bin_num[6],
	      bin_num[8], bin_num[9], bin_num[10], bin_num[11], sep="")
#MAIN#############################################################

print("\nASSIGNMENT 1: BINARY CRC\n")
# c1 = 0	c2 = 1		d1 = 2		c4 = 3		d2 = 4		d3 = 5
# d4 = 6	c8 = 7		d5 = 8		d6 = 9		d7 = 10		d8 = 11
while True :
	error_count = 0
	bin_num = enter_bin() 		# USER INPUT

	# Error Checking: Error_count refers to the erronous bit position.
	error_count = check_c1(bin_num, error_count)
	error_count = check_c2(bin_num, error_count)
	error_count = check_c4(bin_num, error_count)
	error_count = check_c8(bin_num, error_count)
	error_count -= 1 # Left adjusting for array values: 0 - 11
	error_handling(bin_num, error_count)