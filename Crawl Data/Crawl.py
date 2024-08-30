from bs4 import *
import requests
import os

site = str(os.getcwd()) + "\\[FolderDownload]\\"

def folder_create(images, folder_name):
	try:
		if not os.path.exists(folder_name):
			os.makedirs(folder_name)
	except:
		print("Folder Exist!")
		folder_create()
	download_images(images, folder_name)
	print(folder_name)

def download_images(images, folder_name):
	count = 0
	print(f"Total {len(images)} Image! ")
	if len(images) != 0:
		for i, image in enumerate(images):
			try:
				image_link = image["data-src"]
			except:
				try:
					image_link = image["data-srcset"]
				except:
					try:
						image_link = image["data-fallback-src"]
					except:
						try:
							image_link = image["src"]
						except:
							pass
			try:
				r = requests.get(image_link).content
				try:

					r = str(r, 'utf-8')

				except UnicodeDecodeError:

					with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
						f.write(r)

					count += 1
			except:
				pass
		if count == len(images):
			print("Success!")
			
		else:
			print(f"Download {count} of {len(images)}")


def main(link, num):
	r = requests.get(link)
	soup = BeautifulSoup(r.text, 'html.parser')
	article = soup.select("") # tag contain element
	arr = link.split('/')
	name = arr[len(arr) -2]
	name = name.replace('\n', '') + '_' + str(x)
	name = site + name
	path = os.path.join(site, name)  
	print(path)
	folder_create(article, path)


f = open("result.txt", "r")
for x in range(1, 1):
    print(x)
    main(f.readline(), x)
f.close()
