# Binary CRC Exercise
# Assignment 1
# Brandon Knieriem
# Goals:
# 	Prompt the user for a valid binary value and check it.
# 	Calculate what kind of errors may have occurred.
# 	If there's an error, show where it occurred.
# 	If too many errors occurred and it can't be corrected, say so.

#FUNCTIONS######################################################
#Vets input based on length and values.
def enter_bin() :
	while True :
		bin_num = input("Enter an 12 digit binary value: ")
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
	print("Checking C1.")
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
	print("Checking C2.")
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
	print("Checking C4.")
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
	print("Checking C8.")
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
	print("Evaluating digits.")
	for i in eval_digits :
		if(i == '1') : total += 1
	#print("Total '1's:", total) # DEBUG
	if(total % 2 == 0) :
		print("There is an even number of '1's.") # DEBUG
		return True
	if(total % 2 == 1) :
		print ("There is an odd number of '1's.") # DEBUG
		return False
#-----------------------------------------------------------------
#Boolean check. True = even, False = odd. Used to verify c1.
def validate(check, c) :
	if check  == True and c == '0' :
		print("c value is valid.")
		return True;
	elif check == False and c == '1' :
		#print("Success: c value is valid.") # DEBUG
		return True;
	else :
		#print("Error: 'c' value is invalid.") # DEBUG
		return False;
#MAIN#############################################################
print("\nASSIGNMENT 1: BINARY MANIPULATION\n")
# c1 = 0	c2 = 1		d1 = 2		c4 = 3		d2 = 4		d3 = 5
# d4 = 6	c8 = 7		d5 = 8		d6 = 9		d7 = 10		d8 = 11

#bin_num = enter_bin() 		# USER INPUT

# TODO: Make this into a query loop when you're done debugging.
bin_num = "111111111111" 	# PRESET INPUT

error_count = 0

print("Input value in Binary:",bin_num)
dec_num = int(bin_num, 2)
print("Input value in Decimal:", dec_num)

# Error Checking: check returned as Even = True, Odd = False
error_count = check_c1(bin_num, error_count)
error_count = check_c2(bin_num, error_count)
error_count = check_c4(bin_num, error_count)
error_count = check_c8(bin_num, error_count)
print("Errors detected:", error_count)
if(error_count > 12) : "Error: Too many incorrect bits."