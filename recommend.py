import math;
import copy;

def user_history (dataFile, users):
	usersDict = dict ();
	for user in users:
		usersDict[user] = True;
	f = open (dataFile, "r");
	userHistory = dict();
	for line in f:
		user, song, _ = tuple (line.strip ().split (","));
		if int(user) in usersDict:
			if user in userHistory:
				userHistory[user].append (song);
			else:
				userHistory[user] = list ([song]);
	return userHistory;

def partial_user_history (userHistory, fraction):	
	for user in userHistory.keys ():
		songs = userHistory[user];
		songs = songs[0:int(math.floor(fraction * len (songs)))];
		userHistory[user] = songs;
	return userHistory;

def popularity (dataFile, users):
	usersDict = dict ();
	for user in users:
		usersDict[user] = True;
	f = open (dataFile,"r");
	song_popularity = dict();
	for line in f:
		user, song, _ = tuple (line.strip().split(","));
		if int(user) in usersDict:
			if song in song_popularity:
				song_popularity[song] = song_popularity[song] + 1;
			else:
				song_popularity[song] = 1;
	f.close ();
	popularSongs = sorted (song_popularity, key = song_popularity.get, reverse = True);
	return popularSongs;

def recommendUsers (users, userHistory, popularSongs, nRecommendations):
	recommended_songs = dict ();
	for user in users:
		recommended_songs[user] = list();
		for song in popularSongs:
			if len (recommended_songs[user]) >= nRecommendations:
				break;
			else:
				if song not in userHistory[str(user)]:
					recommended_songs[user].append (song);	
	return recommended_songs;
	
def getAllUsers (usersFile):
	f = open (usersFile);
	users = map (lambda line:line.strip(), f.readlines());
	users = [index + 1 for index,user in enumerate (users)];
	return users;

def difference (userHistory, partialUserHistory):
	differenceUserHistory = dict ();
	for user in userHistory.keys ():
		completeUH = userHistory[user];
		partialUH = partialUserHistory[user];
		diffUH = list(set(completeUH) - set(partialUH));
		differenceUserHistory[user] = diffUH;
	return differenceUserHistory;

def calculateError (diffHistory, recommendations):
	error = 0;
	for user in recommendations.keys ():
		for song in recommendations[user]:
			if str(user) in diffHistory.keys ():
				if song not in diffHistory[str(user)]:
					error = error + 1;
	return error;

def main ():
	usersFile = "../Data/kaggle_users.txt";
	dataFile = "../Data/kaggle_data.csv";
	users = getAllUsers (usersFile);
	fold_size = len (users)/10;
	print fold_size;
	allRecommendedSongs = dict();
	"""
	trainingUsers = users [:9*fold_size];
	testUsers = users [9*fold_size:];
	
	popularSongs = popularity (dataFile, trainingUsers);
	userHistory = user_history (dataFile, testUsers);
	partialUserHistory = partial_user_history (copy.deepcopy (userHistory), 0.5);
	recommended_songs = recommendUsers (testUsers, partialUserHistory, popularSongs, 20);
	allRecommendedSongs = dict (allRecommendedSongs.items() + recommended_songs.items ());
	"""
	for fold in range (10):
		testUsers = users [fold * fold_size: fold * fold_size + fold_size - 1];
		trainingUsers = [user for user in users if user not in testUsers];
		popularSongs = popularity (dataFile, trainingUsers);
		userHistory = user_history (dataFile, testUsers);
		partialUserHistory = partial_user_history (copy.deepcopy (userHistory), 0.5);
		differenceUserHistory = difference (userHistory, partialUserHistory);
		recommended_songs = recommendUsers (testUsers, partialUserHistory, popularSongs, 20);
		error = calculateError (differenceUserHistory, recommended_songs);
		allRecommendedSongs = dict (allRecommendedSongs.items() + recommended_songs.items ());
		print fold;
		print error;
	
	#print (allRecommendedSongs);
	
if __name__ == "__main__":
	main ();
