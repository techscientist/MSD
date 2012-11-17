import reader

def main ():
	# Fill the following variables appropriately.
	usersFile = "../Data/kaggle_users.txt"
	songsFile = "../Data/kaggle_songs.txt"
	historyFile = "../Data/kaggle_visible_evaluation_triplets.txt"
	compressedHistoryFile = "../Data/kaggle_data.csv"

	
	users = reader.readUsers (usersFile)
	songs = reader.readSongs (songsFile) 

	reader.compressHistory (users, songs, historyFile, compressedHistoryFile,"\t");
	history = reader.readHistory (compressedHistoryFile);
	print history;
if __name__ == "__main__":
	main ();
