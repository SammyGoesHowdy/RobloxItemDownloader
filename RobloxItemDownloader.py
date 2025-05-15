import json
import requests
import string
import os

print("""--------------------------------------------------------------------
                    ROBLOX Item Downloader
--------------------------------------------------------------------""")

AssetIds = ""
if os.path.isfile("FillThisWithItemIDS.txt"): 
	print("Found FillThisWithItemIDS.txt, reading item IDs...")
	ItemIDTXT = open("FillThisWithItemIDS.txt", "r")
	AssetIds = ItemIDTXT.read().split("\n")
	ItemIDTXT.close()
else:
	print("FillThisWithItemIDS.txt doesn't exist.")
	exit()

if os.path.isfile("ROBLOSECURITY.txt"): 
	roblosecTxt = open("ROBLOSECURITY.txt", "r")
	roblosecurity = roblosecTxt.read()

	if roblosecurity == "":
		input = input('Enter your .ROBLOSECURITY\n\nPlease do not publicly post this anywhere online. \nThis will be saved as "ROBLOSECURITY.txt" to prevent needing to do this again:')

		if input == "":
			print("No ROBLOSECURITY, exiting...")
			exit()
		# Remove the disclaimer to avoid any possible issues (will there even be any?)
		if input[:116] == "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_":
			roblosecurity = input[116:]
		else:
			roblosecurity = input

	roblosecTxt.close()
	# Save ROBLOSECURITY
	with open("ROBLOSECURITY.txt", "w") as f:
		f.write(roblosecurity)

else:
	input = input('Enter your .ROBLOSECURITY\n\nPlease do not publicly post this anywhere online. \nThis will be saved as "ROBLOSECURITY.txt" to prevent needing to do this again:')

	if input == "":
		print("No ROBLOSECURITY, exiting...")
		exit()
	# Remove the disclaimer to avoid any possible issues (will there even be any?)
	if input[:116] == "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_":
		roblosecurity = input[116:]
	else:
		roblosecurity = input

	# Save ROBLOSECURITY
	with open("ROBLOSECURITY.txt", "w") as f:
		f.write(roblosecurity)


for i in AssetIds:
	LVJson =  {
		"name": "Pal Hair",
		"description": "Yeah buddy! Pal Hair for the win.",
		"genre": 0,
		"assetType": 8,
		"creatorType": 1,
		"creatorId": 1,
		"creatorName": "ROBLOX",
		"isForSale": True,
		"priceInRobux": 0,
		"createdAt": "1/10/2017",
		"updatedAt": "1/10/2017",
	}

	url = "https://economy.roblox.com/v2/assets/" + str(i) + "/details"
	if url == "https://economy.roblox.com/v2/assets//details":
		print("No Item IDs were found. Did you fill in the FillThisWithItemIDS.txt file? \nPlease do so and try again.")
		exit()
	s = requests.session()
	s.cookies.set(".ROBLOSECURITY", roblosecurity)
	data = requests.get(url, cookies=s.cookies)

	print("Fetching data for Asset ID: " + str(i) + "...")

	creator = data.json()["Creator"]["Name"] 
	# Change "Roblox" to "ROBLOX" for accuracy's sake
	if creator == "Roblox":
		creator = "ROBLOX"

	# Get creator type
	creatorType = data.json()["Creator"]["CreatorType"] 
	if creatorType == "User":
		creatorType = 1
	elif creatorType == "Group":
		creatorType = 2

	# Get creation date
	creationYear = data.json()["Created"][:4]
	creationMonth = data.json()["Created"][5:7]
	creationDay = data.json()["Created"][8:10]

	# Get updated date
	updatedYear = data.json()["Updated"][:4]
	updatedMonth = data.json()["Updated"][5:7]
	updatedDay = data.json()["Updated"][8:10]

	# Fill JSON Metadata
	LVJson["name"] = data.json()["Name"]
	LVJson["description"] = data.json()["Description"]
	LVJson["assetType"] = data.json()["AssetTypeId"]
	LVJson["creatorType"] = creatorType
	LVJson["creatorId"] = data.json()["Creator"]["CreatorTargetId"]
	LVJson["creatorName"] = creator
	LVJson["isForSale"] = True
	LVJson["priceInRobux"] = data.json()["PriceInRobux"]
	LVJson["createdAt"] = creationMonth + "/" + creationDay + "/" + creationYear
	LVJson["updatedAt"] = updatedMonth + "/" + updatedDay + "/" + updatedYear

	print("Downloading Asset ID: " + str(i) + "...")
	# Asset delivery URL
	assetdeliveryUrl = "https://assetdelivery.roblox.com/v1/asset/?id=" + str(i)
	thumbnailApiUrl = "https://thumbnails.roblox.com/v1/assets/?assetIds="+str(i)+"&size=420x420&format=Png&isCircular=true"
	# Remove punctuation so the script doesnt shit itself
	filename = data.json()["Name"].translate(str.maketrans('', '', string.punctuation))
	RBXModel = requests.get(assetdeliveryUrl,cookies=s.cookies).content
	thumbnailUrl = requests.get(thumbnailApiUrl,cookies=s.cookies).json()["data"][0]["imageUrl"]
	thumbnail = requests.get(thumbnailUrl,cookies=s.cookies).content
	print(thumbnailUrl)

	folder = os.path.dirname(__file__) + "/items/"

	if not os.path.isdir(os.path.dirname(__file__) + "/items/"):
		# directory exists
		folder = os.makedirs(os.path.dirname(__file__) + "/items/")

	# Save RBXM
	print("Saving RBXM for: " + str(i) + "...")
	with open(os.path.dirname(__file__) + "/items/" + filename + ".rbxm", 'wb') as f:
		f.write(RBXModel)

	# Save Thumbnail
	print("Saving Thumbnail for: " + str(i) + "...")
	with open(os.path.dirname(__file__) + "/items/" + filename + ".png", 'wb') as f:
		f.write(thumbnail)	

	# Save JSON
	print("Saving JSON for: " + str(i) + "...")
	with open(os.path.dirname(__file__) + "/items/" + filename + ".json", "x") as f:
		f.write(json.dumps(LVJson, indent=4))

	print(data.json()["Name"] + " (ID:" + str(i) + ")... " + "Done!")
input("Done! Press enter to exit.")
