def indicatorDict (path):
	indicator = dict ();
	for line in open (path):
		user,song,_ = tuple (line.strip().split(","));
		if int(user) in indicator:
			indicator[int(user)].append (int(song));
		else:
			indicator[int(user)] = list ([int(song)]);
	return indicator; 
