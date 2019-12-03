import pandas as pd
import numpy as np

def matchMaker(product):

    the_category = []

    dict_categories = {
    'Charity':['charity', 'donate'],
    'Skincare':['serum','oil','gel','foundation', 'cream', 'body yoghurt', 'no7', 'soap','skincare', 'skin-care', 'skin care'],
    'Haircare':["pantene","aussie","herbal","shoulders","shampoo","conditioner","tressemme,'ABBP haircare', 'hair-care', 'hair care'"],
    'Makeup':['Eyeshadow','foundation', 'cosmetics', 'eyeshadow', 'makeup', 'make-up', 'soap & glory', 'lipstick'],
    'Recipe':['recipe'],
    'Food':['vitamin','soup','sweetclems','pudding','shreddies','kinder', 'yoghurt','bananas','apples','eggs','bread','walkers','chocolate','biscuits', 'chicken', 'crisps', 'sweets', 'cake', 'cadbury', 'pizza', 'walnut', 'snack', 'roast', 'potatoes', 'turkey', 'platter', 'cheese'],
    'Drink':['milk', 'coca-cola', 'pepsi', 'beer', 'wine', 'tea', 'coffee', 'drink', 'fizz', 'prosecco', 'Kopparberg'],
    'Homecare':['bleach','febreze', 'fragrance'],
    'Apps Games':[],
    'Baby':['maternity', 'toilet trainer', 'potty', 'nappies'],
    'Books':['dummies', 'harry potter', 'maths', 'science', 'history', 'potter'],
    'Car & Motorbike':['car care', 'deicer'],
    'CDs & Vinyl':[],
    'Classical Music':[],
    'Clothing':['glasses','sunglasses','beanie','cotton','boxer shorts','shirt', 'dress', 'sleepsuit','socks','sleepsuits', 'cap'],
    'Computers Accessories':['usb', 'cable', 'bluetooth', 'sandisk'],
    'Christmas Decorations':['christmas', 'tins', 'advent calendars'],
    'Digital Music ':[],
    'DIY & Tools':['drill', 'screws', 'tool kit'],
    'DVD & Blu-ray':['series 1','series 2','series 3','series 4','series 5','series 6','series 7','series 8','series 9', 'series 10','season 1','season 2','season 3','season 4','season 5','season 6','season 7','season 8','season 9', 'season 10'],
    'Electronics & Photo':['plug','vacuum cleaner','dash cam','charger','gadget','wireless','tv', 'camera', 'headphones', 'iphone', 'laptopn', 'smartphone', 'samsung', 'microsoft'],
    'Fashion':[],
    'Garden & Outdoors':['gazebo','bbq', 'garden', 'hose', 'flower'],
    'Gift Cards':['gift card'],
    'Handmade':[],
    'Health & Personal Care':[],
    'Home & Business Services':[],
    'Home & Kitchen':['microwave','container','floor brush','sofa','bed', 'shower', 'stainless', 'pan', 'pillow', 'lantern', 'candle', 'glass'],
    'Industrial & Scientific':[],
    'Jewellery':['rings', 'necklace'],
    'Kindle Store':[],
    'Large Appliances':['fridge','dishwasher','washing machine', 'cooker'],
    'Lighting':['spotlight', 'lamp', 'led', 'light'],
    'Luggage':['suitcase', 'backpack', 'rucksack', 'handbag'],
    'Luxury Beauty':[],
    'Musical Instruments & DJ':['guitar', 'piano', 'drum'],
    'PC & Video Games':['xbox', 'ps4', 'nintendo'],
    'Pet Supplies':['dog','cat','fish', 'hamster', 'mouse', 'pet'],
    'Prime Video':[],
    'Shoes':['sandals','shoes', 'trainers', 'sneakers', 'high heels', 'high tops', 'slippers'],
    'Software':[],
    'Sports & Outdoors':['wrist guards','waterproof','sports','football', 'basketball','sport', 'tennis', 'cricket', 'rugby', 'bowling'],
    'Stationery & Office Supplies':['ink','ruler', 'pen', 'pencil', 'pritt stick', 'glue', 'tape'],
    'Toys & Games':['kids','vatos', 'disney', 'car', 'frozen 2', 'unicorn'],
    'VHS':[],
    'Watches':['watch', 'casio'],
    'Cleaning product':['floor cleaner'],
    'Our brands':['febreze', 'air wick'],
    'Competitors':['ambi pur','glade'],
    'Competion': ['competition', 'winner', 'chance'],
    'Visit Instore': ['store', 'range'],
    }

    for category, list_definitions in dict_categories.items():
        for definition in list_definitions:


            if isinstance(product, float):
                the_category.append(category)
                break

            if definition in product.lower():
                the_category.append(category)
                break


    if len(the_category) == 0:
        category = ''
    else:
        category = the_category[0]

    return category

df = pd.read_csv('data/haircare_combined.csv', encoding='UTF-8')

list_products = df['post'].tolist()

list_categories  = []

for product in list_products:
    category = matchMaker(product)
    list_categories.append(category)

df['category'] = list_categories

print (len(list_categories))
filled = [ x for x in list_categories if x is not '']
print (len(filled))

df.to_csv('data/haircare_combined_categories.csv')
