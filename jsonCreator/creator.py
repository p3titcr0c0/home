import json

print("\n-- Solana airwave .json collection creator --\n")
sure = input("TEMPLATE const matches your collection (y or n): ")
if (sure == "y" or sure == "yes"):
	nbr = input("How many NFT in your collection ? ")
	print('\nStart :') if nbr.isnumeric() else (print("\n[Err] : must be integer"),exit(0))

	if (int(nbr)<1):
		print("\n[Err] : the number of objects in the collection < 1"),exit(0)

	TEMPLATE = {
  "name": "---DO NOT CHANGED---",
  "symbol": "??? CHANGEABLE ???",
  "description": "??? CHANGEABLE ???",
  "seller_fee_basis_points": "??? CHANGEABLE ???",
  "image": "0.png",
  "attributes": [
   {
      "trait_type": "??? CHANGEABLE ???",
      "value": "??? CHANGEABLE ???"
    },
   {
      "trait_type": "??? CHANGEABLE ???",
      "value": "??? CHANGEABLE ???"
    }
  ],
  "collection": {
     "name": "Mon super nft",
     "family": "??? CHANGEABLE ???"
  },
  "properties": {
    "files": [
      {
        "uri": "image.png",
        "type": "image/png"
      }
    ],
    "category": "image",
    "creators": [
      {
        "address": "??? CHANGEABLE ???",
        "share": 100
      }
    ]
  }
}

	for i in range(int(nbr)):
		with open("collection/"+str(i)+".json", 'w') as json_file:
			TEMPLATE['name'] = (TEMPLATE['collection']['name']+" n"+str(i))
			json.dump(TEMPLATE, json_file)
		print("[OK] "+str(i)+".json")

	print("[OK] 'collection/' contains your "+nbr+" json")

else :
	print("\n[Err] : check 'template.json'")