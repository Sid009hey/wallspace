from PIL import Image
import os  

#boilerplate for pillow below
#img = Image.open("sheep.png")
#img.show()

wallpapers = []
wallpaper_dict = {}

# after dict variable below.

path = "./wallpaper/"
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
	
listing()	


def subfind():
	sub_str = walp_input
	input_file = [name for name in wallpapers if sub_str in name]
	try:
		for x in range(len(input_file)):
			suggest_file = input_file[x]
			print("⏳ Perhaps You Meant", suggest_file)
	except IndexError:
		print("❌ Wallpaper Not In Database")
		exit()

#print(wallpapers) #comment this out later
#print(wallpaper_dict) #comment this out later

print("✅ Test 1 Passed.")

walp_input=input("Enter A Wallpaper Theme : ")

subfind()

if walp_input+".jpg" in wallpapers:
	print("JPEG wallpaper in db")
	print("✅ Test 2 Passed.")   
	img = Image.open(path+walp_input+".jpg")
	img.show()
	
elif walp_input+".png" in wallpapers:
#	print(input_file)
	print("PNG wallpaper in db")
	print("✅ Test 2 Passed.")   
	img = Image.open(path+walp_input+".png")
	img.show()

elif walp_input == "exit":
	exit()

# Commented Code is wrong.
#if walp_input in wallpapers or wallpaper_dict:
	#print("wallpaper in db")
	#print("✅ Test 2 Passed.")    
	#img = Image.open(path+walp_input)
	#img.show()
else:
	print("❌ Wallpaper Not In Database")
	
	
while True:
	print("")
	walp_input=input("Enter A Wallpaper Theme : ")

	subfind()

	if walp_input+".jpg" in wallpapers:
		print("JPEG wallpaper in db")
		print("✅ Test 2 Passed.")   
		img = Image.open(path+walp_input+".jpg")
		img.show()
		
	elif walp_input+".png" in wallpapers:
	#	print(input_file)
		print("PNG wallpaper in db")
		print("✅ Test 2 Passed.")   
		img = Image.open(path+walp_input+".png")
		img.show()
	
	elif walp_input == "exit":
		exit()


	# Commented Code is wrong.
	#if walp_input in wallpapers or wallpaper_dict:
		#print("wallpaper in db")
		#print("✅ Test 2 Passed.")    
		#img = Image.open(path+walp_input)
		#img.show()
	else:
		print("❌ Wallpaper Not In Database")
