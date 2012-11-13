#!/usr/bin/python

def Evaluate (M, Y, k):
	P = {}
	AP = {}

	#Precision at k
	for index in range(k):
		users_to_songs = {}
		'''for user in M.keys():
			temp_list = []
			for song in songs:
				total = 0;
				for i in range(index):
					total += M[user][Y[user][i]]
				total = total / index
				temp_list.append (total)
			users_to_songs[user] = temp_list'''
		temp_list = []
		for user in M.keys():
			total = 0;
			for i in range(index):
				total += M[user][Y[user][i]]
			total = total / index
			temp_list.append (total)
		P[index] = temp_list

	#Average Precision at each recall point
	for user in M.keys():
		positive = sum (M[user])
		if positive < k:
			nu = positive
		else 
			nu = k

		'''temp_list = []
		for song in songs:
			total = 0
			for i in index (k):
				total += (P[i][user][song] * M[user][Y[user][i]])
			total = total / nu
			temp_list.append (total)'''
		total = 0
		for i in index (k):
			total += (P[i][user][song] * M[user][Y[user][i]])
		total = total / nu
		AP[user] = total
	
	#MAP
	no_of_users = len (M.keys())
	total = 0
	for i in range(no_of_users):
		total += AP[i]
	MAP = total / no_of_users
	
	print "MAP is: " + str(MAP)
