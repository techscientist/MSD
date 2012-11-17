def readHistory (fileName, delimiter = ','):
	"""
	Parses a given file and returns the contents in a dictionary.
	Expected format of the file. Each line is of the form
	<UserId, SongId, SongCount> (for delimiter = ',')

	Input:
	fileName = Name of the history file.
	delimiter = (Optional) The delimiter character.

	Output:
	Dictionary with
		Key = user (in string)
		Value = list of songs and the songcounts listened by this user.
				Every element in the list is of the form
				<SongID, SongCount>

	Side Effect:
	None.

	"""
	
	File = open (fileName, "r");
	history = dict ();
	for line in File:
		user, song, song_count = tuple(line.strip().split(delimiter));
		if int(user) not in history:
			history[int(user)] = list([tuple([int(song), int(song_count)])]);
		else:
			history[int(user)].append(tuple([int(song), int(song_count)]));
	File.close();
	return history;

def readUsers (fileName):
	"""
	Parses a given file and returns the contents in a dictionary.
	Expected format of the file. Each line is of the form
	<UserId>

	Input:
	fileName = Name of the users file.

	Output:
	Dictionary with
		Key = user (in string)
		Value = user (in integer)

	Side Effect:
	None.

	"""
	File = open (fileName, "r");
	userID = 1;
	users = dict();
	for line in File:
		user = line.strip();
		if user not in users:
			users[user] = userID;
			userID = userID + 1;
	File.close ();
	return users;

def readSongs (fileName, delimiter = " "):
	"""
	Parses a given file and returns the contents in a dictionary.
	Expected format of the file. Each line is of the form
	<SongId index> (for delimiter = " ")

	Input:
	fileName = Name of the songs file.

	Output:
	Dictionary with
		Key = song (in string)
		Value = song (in integer)

	Side Effect:
	None.

	"""
	File = open (fileName, "r");
	songID = 1;
	songs = dict ();
	for line in File:
		song,_ = tuple(line.strip().split(delimiter));
		if song not in songs:
			songs[song] = songID;
			songID = songID + 1;
	File.close ();
	return songs;

def compressHistory (users, songs, inFileName, outFileName, indelim = " ", outdelim = ","):
	"""
	Parses a given file and creates a corresponding output file.
	Expected format of the input file
	<userId songId songCount> (for delimiter = " ")

	Expected format of the output file
	<userId,songId,songCount> (for delimiter = ",")

	Input:
		users = Dictionary containing Id as key and Numeric Id as value.
		songs = Dictionary containing Id as key and Numeric Id as value.
		inFileName = Name of the input file name
		outFileName = Name of the output file name
		indelim = Character used to delimit lines in input file.
		outdelim = Character used to delimit lines in output file.

	Output:
		None.

	Side Effect:
		Creates the file by the name given in outFileName.
	
	"""

	inFile = open (inFileName, "r");
	outFile = open (outFileName, "w");
	for line in inFile:
		user, song, songCount = tuple(line.strip().split (indelim));
		outstring = "%s" + outdelim + "%s" + outdelim + "%s\n";
		outFile.write (outstring %(str(users[user]), str(songs[song]), songCount));
	inFile.close ();
	outFile.close ();
