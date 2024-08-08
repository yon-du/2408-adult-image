from glob import glob
import json
import sys

category_id = sys.argv[1]

    # "contents": [
    #     {
    #         "saleChannel": "GIFT",
    #         "sellerId": 23503,
    #         "itemType": "SHIPPING",
    #         "id": "7636229",
    #         "imageUrl": "https://st.kakaocdn.net/thumb/B50x50.fjpg.q82/?fname=https%3A%2F%2Fst.kakaocdn.net%2Fproduct%2Fgift%2Fproduct%2Fkrh3fm8rqxr9-j3ulwcQvQ%2FNpaAqW4irYqUnWVPeuGewPjHSuGlWVDJQHNZi_3UwfY.jpg",

# load request-search-*.json and aggregate id and imageUrl



# load request-search-*.json and aggregate id and imageUrl
file_list = glob(f'{category_id}/*.json')

result = []
for file_name in file_list:
    with open(file_name, 'r') as f:
        data = json.load(f)
        for c in data['contents']:

            if c['minorPurchasable'] is False or \
                c["displayedSaleStatus"] != "판매중" or \
                    c["displayStatus"] != "전시함":
                continue

            # imageUrl sample: https://st.kakaocdn.net/thumb/B50x50.fjpg.q82/?fname=https%3A%2F%2Fst.kakaocdn.net%2Fproduct%2Fgift%2Fproduct%2Fy29ROOeKyyftcs8NxEgtAw%2FFZJb1rwWtzszkr6XXnloHOPAJzGxKEUo5kAa6UG3wi0
            # We need to parse the imageUrl to get the original image url
            imageUrl = c['imageUrl']
            imageUrl = imageUrl.split('fname=')[1]
            imageUrl = imageUrl.replace('%3A', ':').replace('%2F', '/')
            result.append({'id': c['id'], 'imageUrl': imageUrl})


# Save the result to a csv file

import csv

with open(f'{category_id}-aggregated.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'imageUrl'])
    writer.writeheader()
    for r in result:
        writer.writerow(r)
