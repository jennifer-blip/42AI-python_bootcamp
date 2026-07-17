import sys
from pprint import pprint
from FileLoader import FileLoader
from HowManyMedalsByCountry import how_many_medals_by_country

if __name__ == "__main__":
	file=FileLoader()
	data=file.load('../athlete_events.csv')
	pprint("------Finland results------")
	pprint(how_many_medals_by_country(data, 'Finland'))
	pprint("------France results------")
	pprint(how_many_medals_by_country(data, 'France'))