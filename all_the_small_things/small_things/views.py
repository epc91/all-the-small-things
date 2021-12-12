from django.shortcuts import render

# Create your views here.
def leap_year(year):
	is_leap = False
	if year % 4 == 0:
		is_leap = True
		if year % 100 == 0 and year % 400 == 0:
			is_leap = True
		else:
			is_leap = False
	else:
		is_leap = False
	return is_leap