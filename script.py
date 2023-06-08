from PIL import Image
import os  
import shutil

#boilerplate for pillow below
#img = Image.open("sheep.png")
#img.show()

wallpapers = []
wallpaper_dict = {}
wallpaper_tags = {}

# after dict variable below.

path = "./wallpaper/"
project_path="./"
image_extension = ".png"
image_extension_jpeg = ".jpg"

# functions below

def listing():
	for file in os.listdir(path):
		if file.endswith(image_extension):
			wallpapers.append(file)
			wallpaper_dict[file] = file.replace(image_extension,"")
		if file.endswith(image_extension_jpeg):
			wallpapers.append(file)
			wallpaper_dict[file] = file.replace(image_extension_jpeg,"")
			

def new_listing():
	wallpapers.pop()
	for file in os.listdir(path):
		if file.endswith(image_extension_jpeg):
			wallpapers.append(file)
			wallpaper_dict[file] = file.replace(image_extension_jpeg,"")
		if file.endswith(image_extension):
			wallpapers.append(file)
			wallpaper_dict[file] = file.replace(image_extension,"")
	

def tagReplace():
	add_path = add_path.replace("-tag", "")
	add_path = add_path.replace(" ", "")

def tagging():	
	if add_path.endswith("-tag"):
		tag_input=input("➡️ Enter Tag : ")
#		print("tagged.") #cmt later# 
#		print("tag is ", tag_input)
		add_path.replace("-tag","")
#		print(add_path)
		wallpaper_tags[add_path.replace("-tag","")] = tag_input
#		print(wallpaper_tags) 
	
#test path for new listing (jpeg) /home/spec/Pictures/nocos.jpg
#test path for new listing (jpeg) /home/spec/PyProjects/wallengine/test/archlinux.png

# interruption loop below

listing()	

def subfind():
	sub_str = walp_input
	input_file = [name for name in wallpapers if sub_str.replace("\t" and " ","") in name]
	try:
		for x in range(len(input_file)):
			suggest_file = input_file[x]
			print("⏳ Did you mean", suggest_file.replace(".jpg" and ".png",""), "?")
	except IndexError:
		print("❌ Wallpaper Not In Database")
		exit()	

#print(wallpapers) #comment this out later
#print(wallpaper_dict) #comment this out later

print("✅ Wallpapers Loaded.")

walp_input=input("➡️ Enter A Wallpaper Theme : ")

subfind()

if walp_input+".jpg" in wallpapers:
	print("✅ JPEG wallpaper in DB")
	print("✅ Opening File..")   
	img = Image.open(path+walp_input+".jpg")
	img.show()
	
elif walp_input+".png" in wallpapers:
#	print(input_file)
	print("✅ PNG wallpaper in DB")
	print("✅ Opening File..")   
	img = Image.open(path+walp_input+".png")
	img.show()

elif walp_input == "":
	("❌ Don't leave the input blank.")
	exit()

elif walp_input == "exit":
	exit()
	
elif walp_input == "listf":
	print("➡️", wallpapers)
	
elif walp_input == "delete":
	rm_input=input("➡️ File for Deletion : ")
	print("➡️", rm_input, "has been deleted")
	os.system("rm -rf "+path+rm_input)
	exit()
	

elif walp_input == "add":
	add_path=input("➡️ Path to new Image: ")
	if add_path.endswith("-tag"):
		tagging()
		add_path = add_path.replace("-tag", "")
		add_path = add_path.replace(" ", "")
	try:
		shutil.copy(add_path,path)
		new_listing()
		print("✅ File added")
	except IndexError:
		print("❌ No Such Path (if on linux or mac, refrain from using `~`)")
		exit()


	
# Commented Code is wrong.
#if walp_input in wallpapers or wallpaper_dict:
	#print("wallpaper in db")
	#print("✅ Opening File..")    
	#img = Image.open(path+walp_input)
	#img.show()
else:
	print("❌ Wallpaper Not In Database")
	
#looping below

while True:
	print("")
	walp_input=input("➡️ Enter A Wallpaper Theme : ")

	subfind()

	if walp_input+".jpg" in wallpapers:
		print("✅ JPEG wallpaper in DB")
		print("✅ Opening File..")   
		img = Image.open(path+walp_input+".jpg")
		img.show()
				
	elif walp_input+".png" in wallpapers:
#		print(input_file)
		print("✅ PNG wallpaper in DB")
		print("✅ Opening File..")   
		img = Image.open(path+walp_input+".png")
		img.show()
			
	elif walp_input == "":
		print("❌ Don't leave the input blank.")
		exit()
	
	elif walp_input == "exit":
		exit()
		
	elif walp_input == "delete":
		rm_input=input("➡️ File for Deletion : ")
		print("➡️", rm_input, "has been deleted")
		os.system("rm -rf "+path+rm_input)
		exit()
	
	
	elif walp_input == "listf":
		print(wallpapers)
		
#	elif walp_input == "listf -dev":
#		listfdev()
		
	elif walp_input == "add":
		add_path=input("➡️ Path to new Image: ")
		if add_path.endswith("-tag"):
			tagging()
			add_path = add_path.replace("-tag", "")
			add_path = add_path.replace(" ", "")
		try:
			shutil.copy(add_path,path)
			new_listing()
			print("✅ File added")
		except IndexError:
			print("❌ No Such Path (if on linux or mac, refrain from using `~` instead try `/home/`)")
			exit()

	# Commented Code is wrong.
	#if walp_input in wallpapers or wallpaper_dict:
		#print("wallpaper in db")
		#print("✅ Opening File..")    
		#img = Image.open(path+walp_input)
		#img.show()
	else:
		print("❌ Wallpaper Not In Database")	
