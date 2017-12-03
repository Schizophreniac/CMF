import os
import shutil

from sys import argv

base_path = argv[1]

def get_tracks_dict():
	""" Collects and returns a tracks dict in the folder. """
	tracks_dict = {}
	with os.scandir(base_path) as files:
		for track in files:
			if os.path.splitext(os.path.join(base_path, track.name))[1] == '.mp3':
				title_parts = list(map(lambda part: part.strip(), track.name.split('-')))
				if title_parts[0] in tracks_dict:
					tracks_dict[title_parts[0]].append(title_parts[1])
				else:
					tracks_dict[title_parts[0]] = [title_parts[1], ]
	return tracks_dict 


def create_folders_by_tracks_dict(tracks_dict):
	""" Creates folders which names are author's name. """
	os.chdir(base_path)
	for author in tracks_dict:
		author = author.strip()
		if not os.path.exists(author):
			os.mkdir(author)
		for track in tracks_dict[author]:
			shutil.move(author + ' - ' + track.strip(), author)


def main():
	tracks_dict = get_tracks_dict()
	print(tracks_dict)
	create_folders_by_tracks_dict(tracks_dict)


if __name__ == '__main__':
	main()