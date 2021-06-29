import requests
import json

def pelagoAPIRequest(productId):
    payload={"query": "query product($productId: String!) {\n product(productId: $productId){\n ... on Product {\n productId\n productName\n destinationId\nshortDescription\n cancellationType\n cancellationWindow\n minGroupSize\nopenDateTicket\n collectPhysicalTicket\n confirmationType\n voucherType\npriceRangeFrom\n priceRangeTo\n latitude\n longitude\n address\n__typename\n }\n ... on PelagoError {\n errorMessage\n code\n__typename\n }\n __typename\n }\n}","variables": {"productId": productId}}
    headers = {"Content-Type": "application/json"}
    r = requests.post("https://traveller-core.pelago.co/graphql", data=json.dumps(payload), headers=headers)
    prodDict=r.json()
    prodInfo=prodDict['data']['product']
    return prodInfo

def pelagoAPIRequestForReview(productId):
    payload = {"operationName":"productReviews","variables":{"productId":productId,"page":1,"pageSize":5},"query":"query productReviews($page: Int, $pageSize: Int, $productId: String!) {\n  productReviews(page: $page, pageSize: $pageSize, productId: $productId) {\n    ... on ReviewHistory {\n      reviews {\n        reviewId\n        rating\n        content\n        comment\n        status\n        activityDate\n        dateCreated\n        travellerType\n        customer {\n          firstName\n          lastName\n          __typename\n        }\n        __typename\n      }\n      reviewCount\n      __typename\n    }\n    ... on PelagoError {\n      errorMessage\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"}
    headers = {"Content-Type": "application/json"}
    r = requests.post("https://traveller-core.pelago.co/graphql", data=json.dumps(payload), headers=headers)
    reviewDict = r.json()
    reviewInfo=reviewDict['data']['productReviews']['reviews']
    return reviewInfo

def pelagoErrorMsgForProductInfo(ProductId):
    payload={"query": "query product($productId: String!) {\n product(productId: $productId){\n ... on Product {\n productId\n productName\n destinationId\nshortDescription\n cancellationType\n cancellationWindow\n minGroupSize\nopenDateTicket\n collectPhysicalTicket\n confirmationType\n voucherType\npriceRangeFrom\n priceRangeTo\n latitude\n longitude\n address\n__typename\n }\n ... on PelagoError {\n errorMessage\n code\n__typename\n }\n __typename\n }\n}","variables": {"productId": ProductId}}
    headers = {"Content-Type": "application/json"}
    r = requests.post("https://traveller-core.pelago.co/graphql", data=json.dumps(payload), headers=headers)
    print(r.json())
    product = r.json()
    productData = product['data']['product']['errorMessage']
    assert productData == str(ProductId) + " product not found"


def pelagoErrorMsgForReview(ProductId):
    payload = {"operationName": "productReviews", "variables": {"productId": ProductId, "page": 1, "pageSize": 5},
               "query": "query productReviews($page: Int, $pageSize: Int, $productId: String!) {\n  productReviews(page: $page, pageSize: $pageSize, productId: $productId) {\n    ... on ReviewHistory {\n      reviews {\n        reviewId\n        rating\n        content\n        comment\n        status\n        activityDate\n        dateCreated\n        travellerType\n        customer {\n          firstName\n          lastName\n          __typename\n        }\n        __typename\n      }\n      reviewCount\n      __typename\n    }\n    ... on PelagoError {\n      errorMessage\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"}
    headers = {"Content-Type": "application/json"}
    r = requests.post("https://traveller-core.pelago.co/graphql", data=json.dumps(payload), headers=headers)
    print(r.json())
    reviews = r.json()
    reviewData = reviews['data']['productReviews']['reviewCount']
    assert reviewData==0


#print(pelagoAPIRequestForReview('pkb3v'))