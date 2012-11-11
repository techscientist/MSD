import scipy.io

def numerify (dataFile, userFile, songFile, outFile):
	"""
	Input: 
	dataFile = Name of the file that contains all the data.
		   	   Data should be of the form of triplets.
		   	   <userID, songID, songCount>
	userFile = Name of the file that contains all the user Id's
			   Should be of the form
			   <UserID>

	songFile = Name of the file that contains all the song Id's
			   Should be of the form
			   <SongId, SongIntID>
	outFile = Name of the file that would contain all the data in
			  csv format. The format of the file will be.
			  <UserIntId, SongIntId, songCount> 

	Output: Nothing.
	Side Effect: Creates a csv file containing
				 1. Integer Id's to long User Id's
				 2. Integer Id's to long song Id's
				 3. song count.
				 <userIntID, songIntID, songCount>
	"""

	uDict = userDict (userFile);
	sDict = songDict (songFile);
		
	out = open (outFile,"wb");
	
	for line in open (dataFile, "r"):
		user, song, songCount = line.strip ().split ("\t");
		out.write ("%d,%s,%s\n" %(uDict[user],sDict[song],songCount));

def userDict (userFile):	
	uDict = dict ();
	lineNumber = 1;
	for line in open(userFile):
		uID, = tuple(line.strip().split ("\t"));
		uDict[uID] = lineNumber;
		lineNumber = lineNumber + 1;
	return uDict;

def songDict (songFile):	
	sDict = dict ();
	for line in open(songFile):
		songID,songIntID = tuple(line.strip().split ());
		sDict[songID] =  songIntID;
	return sDict;
