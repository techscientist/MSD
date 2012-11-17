import reader;

def main ():
	# Fill the following variables appropriately.
	usersFile = ""
	songsFile = ""
	historyFile = ""
	compressedHistoryFile = ""

	
	users = reader.readUsers (usersFile) 
	songs = reader.readSongs (songsFile) 

	reader.compressHistory (users, songs, historyFile, compressedHistoryFile);
	history = reader.readHistory (compressedHistoryFile);
