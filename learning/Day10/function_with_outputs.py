# function with outputs
def format_name(f_name,l_name):
	formatted_f_name=f_name.title()	#title() converts the first letter into uppercase
	formatted_l_name=l_name.title()
	return f"{formatted_f_name} {formatted_l_name}"

formatted_full_name=format_name("aYUsh","NeuPaNE")
print(formatted_full_name)