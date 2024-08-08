# 101103104

# curl -X 'GET' \
#   'https://beta-product-aapi.kakao.com/GIFT/products/search?itemType=SHIPPING&productName=&sellerManagementCodes=&productIds=&brand=&giftBrand=&modelName=&manufacturer=&directBuying=&statuses=ON_SALE&categoryId=101111106&periodType=REGISTRATION_DATE&from=20140101000000&to=20240801235959&b2b=&displayable=&shoppingHowDisplayable=&stockQuantity=&sellerDiscount=&adminDiscount=&maxSaleQuantityEnabled=&isolatedAreaDeliverable=&booked=&maxPurchaseQuantityOfBuyer=&giftType=&suggestionNameExists=&eventNameExists=&size=100&approverName=&sellerId=&sellerName=&agencySellerId=&approveStatus=APPROVED&ctm=&slidingDiscount=&salePromotion=&productFee=&managedPrice=&priceRelatedPropertiesModify=&openApiRegistration=&bundleGroupAvailable=&deliveryMethodType=&isolatedAreaPickupAvailable=&pickupAvailableStoreType=&sameDayPickup=&pickupStoreChangeable=&optionChangeable=&giftPurchaseType=&displaySpace=&secretStore=&detailBuyingType=&giftPackaging=&customOrder=&advertisementReviewType=&advertisementReviewRequired=&advertisementReviewUploaded=&fixedDateGift=&approverSearchType=BRAND&cert=&valex=&showrooming=&monitoringStatuses=&monitoringChangedType=&prohibitionReasonType=&displayComparisonDiscountRate=&discountDisplayPolicy=&giftBrandIds=&fandom=&page=0&sortProperty=lastModifiedAt&sortType=desc&_t=1722495772708' \
#   -H 'accept: */*' \
#   -H 'x-user-type: MANAGER' \
#   -H 'Authorization: yon.du' \
#   | jq . > request-search.json

import json
import requests
import os
import time
from datetime import datetime
from datetime import timedelta
import sys

category_id = sys.argv[1]


# API URL
url = "https://beta-product-aapi.kakao.com/GIFT/products/search"

# API Header
headers = {
    "accept": "*/*",
    "x-user-type": "MANAGER",
    "Authorization": "yon.du",
}

# API Query - only fill in the necessary parameters

params = {
    "itemType": "SHIPPING",
    "productName": "",
    "sellerManagementCodes": "",
    "productIds": "",
    "brand": "",
    "giftBrand": "",
    "modelName": "",
    "manufacturer": "",
    "directBuying": "",
    "statuses": "ON_SALE",
    "categoryId": str(category_id),
    "periodType": "REGISTRATION_DATE",
    "from": "20140101000000",
    "to": "20240801235959",
    "b2b": "",
    "displayable": "",
    "shoppingHowDisplayable": "",
    "stockQuantity": "",
    "sellerDiscount": "",
    "adminDiscount": "",
    "maxSaleQuantityEnabled": "",
    "isolatedAreaDeliverable": "",
    "booked": "",
    "maxPurchaseQuantityOfBuyer": "",
    "giftType": "",
    "suggestionNameExists": "",
    "eventNameExists": "",
    "size": "2000",
    "approverName": "",
    "sellerId": "",
    "sellerName": "",
    "agencySellerId": "",
    "approveStatus": "APPROVED",
    "ctm": "",
    "slidingDiscount": "",
    "salePromotion": "",
    "productFee": "",
    "managedPrice": "",
    "priceRelatedPropertiesModify": "",
    "openApiRegistration": "",
    "bundleGroupAvailable": "",
    "deliveryMethodType": "",
    "isolatedAreaPickupAvailable": "",
    "pickupAvailableStoreType": "",
    "sameDayPickup": "",
    "pickupStoreChangeable": "",
    "optionChangeable": "",
    "giftPurchaseType": "",
    "displaySpace": "",
    "secretStore": "",
    "detailBuyingType": "",
    "giftPackaging": "",
    "customOrder": "",
    "advertisementReviewType": "",
    "advertisementReviewRequired": "",
    "advertisementReviewUploaded": "",
    "fixedDateGift": "",
    "approverSearchType": "BRAND",
    "cert": "",
    "valex": "",
    "showrooming": "",
    "monitoringStatuses": "",
    "monitoringChangedType": "",
    "prohibitionReasonType": "",
    "displayComparisonDiscountRate": "",
    "discountDisplayPolicy": "",
    "giftBrandIds": "",
    "fandom": "",
    "page": "0",
    "sortProperty": "lastModifiedAt",
    "sortType": "desc",
    "_t": "1722495772708",
}

# Create a directory to save the response
if not os.path.exists(str(category_id)):
    os.makedirs(str(category_id))

while True:

    # API Request
    response = requests.get(url, headers=headers, params=params)

    # API Response
    data = response.json()

    print(len(data["contents"]))



    json_filename = f"{category_id}/{params['page']}.json"

    # Save the response to a file
    with open(json_filename, "w") as f:
        # json.dump(data, f, ensure_ascii=True, indent=4)
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Saved to {json_filename}")

    if data["last"] is True:
        break

    # Update the 'page' parameter
    params["page"] = str(int(params["page"]) + 1)
