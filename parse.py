def parse_func(file_name):
	data = {}

	with open(file_name) as f:
		content = f.readlines()
	content = [x.strip() for x in content] 

	start_time = ""
	end_time = ""
	key = 0
	lyric = ""
	step = 1
	for i in content:
		if step == 1:
			key = int(i)
			step = 2
		elif step == 2:
			start_time = i[0:12]
			end_time = i[17:29]
			step = 3
		elif step == 3:
			if i[-1:] == "ª":
				for j in i:
					if (j != "â") and (j != "™") and (j != "ª"):
						lyric += j
				step = 4
			else:
				for j in i:
					if (j != "â") and (j != "™") and (j != "ª"):
						lyric += j
				step = 3
		elif step == 4:
			data[key] = ((start_time, end_time), lyric[1:-1])
			start_time = ""
			end_time = ""
			key = 0
			lyric = ""
			step = 1

	return data


if __name__ == '__main__':
	pass
	# data = parse_func("test.srt")

	# # print just a certain line, key is that line
	# print (data[1])

	# # print start time and end time 
	# print (data[1][0][0], data[1][0][1])

	# # print lyrics
	# print (data[1][1])