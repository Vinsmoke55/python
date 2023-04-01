# using multiple return inside a single function
def format_name(f_name,l_name):
	if f_name=="" or l_name=="":
		return "please provide the valid name" #after the return statement the function ends
	formatted_f_name=f_name.title()
	formatted_l_name=l_name.title()
	return f"{formatted_f_name} {formatted_l_name}"

formatted_full_name=format_name(input("what is your first name? "),input("What is your last name? "))
print(formatted_full_name)