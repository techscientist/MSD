def user_history (dataFile):
	f = open (dataFile, "r");
	userHistory = dict();
	for line in f:
		user, song, _ = tuple (line.strip ().split (","));
		if user in userHistory:
			userHistory[user].append (song);
		else:
			userHistory[user] = list ([song]);
	return userHistory;

def popular_songs (dataFile, topCount = -1):
	f = open (dataFile,"r");
	song_popularity = dict();
	for line in f:
		_, song, _ = tuple (line.strip().split(","));
		if song in song_popularity:
			song_popularity[song] = song_popularity[song] + 1;
		else:
			song_popularity[song] = 1;
	f.close ();
	popularSongs = sorted (song_popularity, key = song_popularity.get, reverse = True);
	if topCount == -1:
		return popularSongs;
	else:
		return popularSongs[:topCount];

def getAllUsers (usersFile):
	f = open (usersFile);
	users = map (lambda line:line.strip(), f.readlines());
	users = [index + 1 for index,user in enumerate (users)];
	return users;

def recommendUsers (users, userHistory, popularSongs, nRecommendations):
	subFile = open ("../Data/submission.txt", "w");
	recommended_songs = dict ();
	for user in users:
		recommended_songs[user] = list();
		for song in popularSongs:
			if len (recommended_songs[user]) >= nRecommendations:
				break;
			else:
				if song not in userHistory[str(user)]:
					recommended_songs[user].append (song);
		for song in recommended_songs[user]:
			subFile.write ('%s,%s\n' %(str(user), song));

	subFile.close ();

def main ():
	filePath = "../Data/kaggle_data.csv";
	usersFile = "../Data/kaggle_users.txt";
	users = getAllUsers (usersFile);
	popularSongs = popular_songs (filePath);
	userHistory = user_history (filePath);
	recommendUsers (users, userHistory, popularSongs, 20);

if __name__ == "__main__":
	main ();
