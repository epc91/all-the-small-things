from django.shortcuts import render
from datetime import date

def leap_year_view(request):
	# GET

	# Get today
	today = date.today().strftime("%d/%m/%Y")
	actual_year = int(today.split('/')[-1])

	# Get if year is leap
	leap = leap_year(actual_year)

	# Data to client side
	context = {
		'actual_year': actual_year,
		'is_leap': leap
	}
	return render(request, 'small_things/leap-year.html', context)

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