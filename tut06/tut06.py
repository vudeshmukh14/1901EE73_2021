import os
import shutil
import re          # making required imports

def regex_renamer():

	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))

	if (os.path.exists("corrected_srt")==False):   # checking if corrected_srt folder already exists or not
		os.mkdir("corrected_srt")                  # creating it if not

	# for Breaking Bad
	if webseries_num==1:
		# if Breaking Bad folder does not exists then creating it
		if os.path.exists(r"corrected_srt\Breaking Bad")==False:
			os.mkdir(r"corrected_srt\Breaking Bad")
		# if already exists then deleting all files from it
		else :
			for f in os.listdir(r"corrected_srt\Breaking Bad\\"):
				os.remove(os.path.join(r"corrected_srt\Breaking Bad\\", f))

		src=r"wrong_srt\Breaking Bad\\"
		dest=r"corrected_srt\Breaking Bad\\"
		for file_name in os.listdir(src):
			source=src+file_name
			destination=dest+file_name
			if os.path.isfile(source):
				shutil.copy(source, destination)  # copying all files from wrong_srt folder to corrected_srt

		for file_name in os.listdir(dest):
			numbers=re.findall(r"\d+", file_name) # extracting numbers from file_name
			episode=numbers[1].lstrip("0")
			season=numbers[0].lstrip("0")
			# making appropriate paddings
			while (len(season)<season_padding):
				season="0"+season
			while (len(episode)<episode_padding):
				episode="0"+episode
			
			words=re.findall(r"\w+", file_name)  # extracting words from file_name
			
			new_file_name=words[0]+" "+words[1]+" - "+"Season "+season+" Episode "+episode+"."+words[len(words)-1]
			
			os.rename(os.path.join(r"corrected_srt\Breaking Bad", file_name), os.path.join(r"corrected_srt\Breaking Bad", new_file_name))

	# for Game of Thrones
	elif webseries_num==2:
		# if Game of Thrones folder does not exists then creating it
		if os.path.exists(r"corrected_srt\Game of Thrones")==False:
			os.mkdir(r"corrected_srt\Game of Thrones")
		# if already exists then deleting all files from it
		else :
			for f in os.listdir(r"corrected_srt\Game of Thrones\\"):
				os.remove(os.path.join(r"corrected_srt\Game of Thrones\\", f))

		src=r"wrong_srt\Game of Thrones\\"
		dest=r"corrected_srt\Game of Thrones\\"
		for file_name in os.listdir(src):
			source=src+file_name
			destination=dest+file_name
			if os.path.isfile(source):
				shutil.copy(source, destination)  # copying all files from wrong_srt folder to corrected_srt

		for file_name in os.listdir(dest):
			numbers=re.findall(r"\d+", file_name) # extracting numbers from file_name
			episode=numbers[1].lstrip("0")
			season=numbers[0].lstrip("0")
			# making appropriate paddings
			while (len(season)<season_padding):
				season="0"+season
			while (len(episode)<episode_padding):
				episode="0"+episode

			words=re.findall(r"\w+", file_name)  # extracting words from file_name
			new_file_name=words[0]+" "+words[1]+" "+words[2]+" - "+"Season "+season+" Episode "+episode+" - "
			for word in words[4:]:
				if word=="WEB":
					break
				new_file_name=new_file_name+" "+word
			new_file_name=new_file_name+"."+words[len(words)-1]
			
			os.rename(os.path.join(r"corrected_srt\Game of Thrones", file_name), os.path.join(r"corrected_srt\Game of Thrones", new_file_name))

	# for Lucifer
	elif webseries_num==3:
		# if Lucifer folder does not exists then creating it
		if os.path.exists(r"corrected_srt\Lucifer")==False:
			os.mkdir(r"corrected_srt\Lucifer")
		# if already exists then deleting all files from it
		else :
			for f in os.listdir(r"corrected_srt\Lucifer\\"):
				os.remove(os.path.join(r"corrected_srt\Lucifer\\", f))

		src=r"wrong_srt\Lucifer\\"
		dest=r"corrected_srt\Lucifer\\"
		for file_name in os.listdir(src):
			source=src+file_name
			destination=dest+file_name
			if os.path.isfile(source):
				shutil.copy(source, destination)  # copying all files from wrong_srt folder to corrected_srt

		for file_name in os.listdir(dest):
			numbers=re.findall(r"\d+", file_name) # extracting numbers from file_name
			episode=numbers[1].lstrip("0")
			season=numbers[0].lstrip("0")
			# making appropriate paddings
			while (len(season)<season_padding):
				season="0"+season
			while (len(episode)<episode_padding):
				episode="0"+episode

			words=re.findall(r"[\w']+", file_name) # extracting words from file_name (also took care of "'")
			new_file_name=words[0]+" - "+"Season "+season+" Episode "+episode+" - "
			for word in words[2:]:
				if word=="HDTV":
					break
				new_file_name=new_file_name+" "+word
			new_file_name=new_file_name+"."+words[len(words)-1]
			
			os.rename(os.path.join(r"corrected_srt\Lucifer", file_name), os.path.join(r"corrected_srt\Lucifer", new_file_name))


regex_renamer()