from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData
import sys

if __name__ == "__main__":
	file=FileLoader()
	data=file.load('../athlete_events.csv')
	sp=SpatioTemporalData(data)
	print("----when Atlanta?-----")
	sp.when('atlanta')
	print("----when Athina?-----")
	sp.when('Athina')
	print("----when Paris?-----")
	sp.when('Paris')
	print("----where 2006?-----")
	sp.where(2006)
	print("----where 1896?-----")
	sp.where(1896)