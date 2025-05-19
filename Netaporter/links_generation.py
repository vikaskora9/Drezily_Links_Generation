from copy import deepcopy
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json

response = requests.get(
    'https://www.net-a-porter.com/api/nap/search/resources/store/nap_us/productview/byCategory?attrs=true&category=%2Fclothing%2Fpants&locale=en_US&pageNumber=1&pageSize=60',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Application-Name': 'Blue lobster',
        "Application-Version": '4.793.0',
        'label': 'getCategoryBySeoPath',
        'priority': 'u=1, i',
        'referer': 'https://www.net-a-porter.com/en-us/shop/clothing/pants/',
        'sec-ch-ua': '"Chromium";v="130", "Not;A=Brand";v="99", "Microsoft Edge";v="130"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-ibm-client-id': '95f14cbd-793e-46ec-9f76-6fac2fbb6683'
    })
# print(response.text)
with open('pants_resp.txt', 'w') as f:
    f.write(response.text)
exit()
final_df = pd.DataFrame(
    columns=['Product_Category', 'Category', 'Subcategory1', 'Subcategory2', 'Subcategory3', 'Url', 'Attr_Name',
             'Attr_Value'])

attr_lst = {
    "resourceId": "/search/resources/store/NAP_IN/productview/byCategory?attrs=true&category=%2Fclothing%2Fcoats-and-jackets&locale=en_US&pageNumber=2&pageSize=60",
    "pageNumber": 2,
    "pageSize": 60,
    "orderBy": [
        {
            "labelEN": "Recommended",
            "label": "Recommended",
            "key": "5",
            "selected": "True"
        },
        {
            "labelEN": "New In",
            "label": "New In",
            "key": "10"
        },
        {
            "labelEN": "Price High to Low",
            "label": "Price High to Low",
            "key": "9"
        },
        {
            "labelEN": "Price Low to High",
            "label": "Price Low to High",
            "key": "8"
        }
    ],
    "recordSetStartNumber": 60,
    "resourceName": "productview",
    "recordSetTotal": 1364,
    "version": 1.7,
    "products": [
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/31840166392300153/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "SAINTLAURENT",
            "productId": "3074457345623012800",
            "modelId": "3074457345623012727",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345623012800",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "517741Y399W1000",
                    "price": {
                        "sellingPrice": {
                            "amount": 306000,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 306000,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "31840166392300153",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/31840166392300153/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Tube satin-trimmed grain de poudre wool blazer",
            "nameEN": "Tube satin-trimmed grain de poudre wool blazer",
            "type": "ProductColour",
            "mfPartNumber": "517741Y399W1000",
            "designerName": "SAINT LAURENT",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 306000,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 306000,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Tube satin-trimmed grain de poudre wool blazer",
            "partNumber": "31840166392300153",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "HS24",
                            "label": "HS24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "28",
                            "label": "28"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "SAINTLAURENT",
                            "label": "SAINT LAURENT"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power RTW",
                            "label": "Power RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "SAINT LAURENT",
            "seo": {
                "seoURLKeyword": "/saint-laurent/clothing/blazers/tube-satin-trimmed-grain-de-poudre-wool-blazer/31840166392300153"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597343786893/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "BARBOUR",
            "productId": "3074457345628300791",
            "modelId": "3074457345628300696",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Navy",
                    "visible": "True",
                    "productId": "3074457345628300791",
                    "labelEN": "Navy",
                    "label": "Navy",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "LWX1397BK71bk71",
                    "badges": [
                        {
                            "label": "20% OFF AT CHECKOUT",
                            "type": "MERCHANDISING",
                            "key": "BADGE_FP_PROMO_AUTOAPPLY"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 76800,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 76800,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597343786893",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597343786893/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Reighton corduroy-trimmed waxed-cotton jacket",
            "nameEN": "Reighton corduroy-trimmed waxed-cotton jacket",
            "type": "ProductColour",
            "mfPartNumber": "LWX1397BK71bk71",
            "designerName": "BARBOUR",
            "badges": [
                {
                    "label": "20% OFF AT CHECKOUT",
                    "type": "MERCHANDISING",
                    "key": "BADGE_FP_PROMO_AUTOAPPLY"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-1911",
                "labelEN": "Sport",
                "label": "Sport",
                "categoryId": "3074457345616676672",
                "child": {
                    "identifier": "NAP-1911-1916",
                    "labelEN": "Outdoor",
                    "label": "Outdoor",
                    "categoryId": "3074457345616676734",
                    "child": {
                        "identifier": "NAP-1911-1916-2001",
                        "labelEN": "Outerwear",
                        "label": "Outerwear",
                        "categoryId": "3074457345616677027"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 76800,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 76800,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597343786893",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Navy",
                            "label": "Navy"
                        },
                        {
                            "identifier": "Navy",
                            "label": "Navy"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Lingerie & Sporter",
                            "label": "Lingerie & Sporter"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "BARBOUR",
                            "label": "BARBOUR"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "BARBOUR",
            "seo": {
                "seoURLKeyword": "/barbour/sport/outerwear/reighton-corduroy-trimmed-waxed-cotton-jacket/1647597343786893"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "8",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597352892638/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345628753187",
            "modelId": "3074457345628753171",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628753187",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "251-WRO0167-FB0351Black",
                    "badges": [
                        {
                            "label": "EXCLUSIVE",
                            "type": "MERCHANDISING",
                            "key": "BADGE_EXCLUSIVE"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 140700,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 140700,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597352892638",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597352892638/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Scarf-detailed quilted recycled-shell jacket",
            "nameEN": "Scarf-detailed quilted recycled-shell jacket",
            "type": "ProductColour",
            "mfPartNumber": "251-WRO0167-FB0351Black",
            "designerName": "TOTEME",
            "badges": [
                {
                    "label": "EXCLUSIVE",
                    "type": "MERCHANDISING",
                    "key": "BADGE_EXCLUSIVE"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-78",
                        "labelEN": "Short",
                        "label": "Short",
                        "categoryId": "3074457345616677114"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 140700,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 140700,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597352892638",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "28",
                            "label": "28"
                        },
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/short/scarf-detailed-quilted-recycled-shell-jacket/1647597352892638"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "1",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597340634476/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "THEROW",
            "productId": "3074457345628115272",
            "modelId": "3074457345628115170",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628115272",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "8243-W3177BLK",
                    "price": {
                        "sellingPrice": {
                            "amount": 491600,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 491600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597340634476",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597340634476/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Fletcher wool blazer",
            "nameEN": "Fletcher wool blazer",
            "type": "ProductColour",
            "mfPartNumber": "8243-W3177BLK",
            "designerName": "THE ROW",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 491600,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 491600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597340634476",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "00",
                            "label": "00"
                        },
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "THEROW",
                            "label": "THE ROW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power RTW",
                            "label": "Power RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "THE ROW",
            "seo": {
                "seoURLKeyword": "/the-row/clothing/blazers/fletcher-wool-blazer/1647597340634476"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597354681294/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "VERONICADEPIANTE",
            "productId": "3074457345628829689",
            "modelId": "3074457345628829674",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628829689",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "VDPGP2027BLACK",
                    "badges": [
                        {
                            "label": "LOW STOCK",
                            "type": "STOCK",
                            "key": "BADGE_LOW_STOCK"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 291600,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 291600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597354681294",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597354681294/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Maeve cropped grain de poudre wool jacket",
            "nameEN": "Maeve cropped grain de poudre wool jacket",
            "type": "ProductColour",
            "mfPartNumber": "VDPGP2027BLACK",
            "designerName": "VERONICA DE PIANTE",
            "badges": [
                {
                    "label": "LOW STOCK",
                    "type": "STOCK",
                    "key": "BADGE_LOW_STOCK"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-89",
                        "labelEN": "Smart",
                        "label": "Smart",
                        "categoryId": "3074457345616677125"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 291600,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 291600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597354681294",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "VERONICADEPIANTE",
                            "label": "VERONICA DE PIANTE"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "VERONICA DE PIANTE",
            "seo": {
                "seoURLKeyword": "/veronica-de-piante/clothing/smart/maeve-cropped-grain-de-poudre-wool-jacket/1647597354681294"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "4",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597335450347/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "THEROW",
            "productId": "3074457345627727778",
            "modelId": "3074457345627727692",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345627727778",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "8142-W3062BLK",
                    "badges": [
                        {
                            "label": "RUNWAY",
                            "type": "MERCHANDISING",
                            "key": "BADGE_RUNWAY"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 420300,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 420300,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597335450347",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597335450347/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Hooded shell coat",
            "nameEN": "Hooded shell coat",
            "type": "ProductColour",
            "mfPartNumber": "8142-W3062BLK",
            "designerName": "THE ROW",
            "badges": [
                {
                    "label": "RUNWAY",
                    "type": "MERCHANDISING",
                    "key": "BADGE_RUNWAY"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-2775",
                        "labelEN": "Knee Length",
                        "label": "Knee Length",
                        "categoryId": "3074457345616677112"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 420300,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 420300,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597335450347",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "FW24",
                            "label": "FW24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "XS/S",
                            "label": "XS/S"
                        },
                        {
                            "identifier": "M/L",
                            "label": "M/L"
                        },
                        {
                            "identifier": "XL/XXL",
                            "label": "XL/XXL"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "THEROW",
                            "label": "THE ROW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power Designer",
                            "label": "Power Designer"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "THE ROW",
            "seo": {
                "seoURLKeyword": "/the-row/clothing/knee-length/hooded-shell-coat/1647597335450347"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597344851816/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "SALON1884",
            "productId": "3074457345628394700",
            "modelId": "3074457345628394681",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628394700",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "31470536BLACK (SILVER HARDWARE)",
                    "price": {
                        "sellingPrice": {
                            "amount": 995900,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 995900,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597344851816",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597344851816/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Marcelle belted shearling jacket",
            "nameEN": "Marcelle belted shearling jacket",
            "type": "ProductColour",
            "mfPartNumber": "31470536BLACK (SILVER HARDWARE)",
            "designerName": "SALON 1884",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-78",
                        "labelEN": "Short",
                        "label": "Short",
                        "categoryId": "3074457345616677114"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 995900,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 995900,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597344851816",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "SALON1884",
                            "label": "SALON 1884"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "SALON 1884",
            "seo": {
                "seoURLKeyword": "/salon-1884/clothing/short/marcelle-belted-shearling-jacket/1647597344851816"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "5",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597352892718/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345628753186",
            "modelId": "3074457345628753171",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "White",
                    "visible": "True",
                    "productId": "3074457345628753186",
                    "labelEN": "White",
                    "label": "White",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "251-WRO0167-FB0351Winter White",
                    "badges": [
                        {
                            "label": "EXCLUSIVE",
                            "type": "MERCHANDISING",
                            "key": "BADGE_EXCLUSIVE"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 140700,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 140700,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597352892718",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597352892718/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Scarf-detailed quilted recycled-shell jacket",
            "nameEN": "Scarf-detailed quilted recycled-shell jacket",
            "type": "ProductColour",
            "mfPartNumber": "251-WRO0167-FB0351Winter White",
            "designerName": "TOTEME",
            "badges": [
                {
                    "label": "EXCLUSIVE",
                    "type": "MERCHANDISING",
                    "key": "BADGE_EXCLUSIVE"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-78",
                        "labelEN": "Short",
                        "label": "Short",
                        "categoryId": "3074457345616677114"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 140700,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 140700,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597352892718",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "White",
                            "label": "White"
                        },
                        {
                            "identifier": "White",
                            "label": "White"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "28",
                            "label": "28"
                        },
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/short/scarf-detailed-quilted-recycled-shell-jacket/1647597352892718"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "42",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597340340077/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345628098170",
            "modelId": "3074457345628098168",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Camel",
                    "visible": "True",
                    "productId": "3074457345628098170",
                    "labelEN": "Camel",
                    "label": "Camel",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "244-WRO0131-FB0292CAMEL 033",
                    "price": {
                        "sellingPrice": {
                            "amount": 202300,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 202300,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597340340077",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597340340077/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Draped fringed wool-blend bouclé coat",
            "nameEN": "Draped fringed wool-blend bouclé coat",
            "type": "ProductColour",
            "mfPartNumber": "244-WRO0131-FB0292CAMEL 033",
            "designerName": "TOTEME",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 202300,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 202300,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597340340077",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Camel",
                            "label": "Camel"
                        },
                        {
                            "identifier": "Camel",
                            "label": "Camel"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "28",
                            "label": "28"
                        },
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/long/draped-fringed-wool-blend-boucle-coat/1647597340340077"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597340634474/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "THEROW",
            "productId": "3074457345628115274",
            "modelId": "3074457345628115172",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628115274",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "8293-W3181BLK",
                    "badges": [
                        {
                            "label": "LOW STOCK",
                            "type": "STOCK",
                            "key": "BADGE_LOW_STOCK"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 391800,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 391800,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597340634474",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597340634474/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Holbrook grain de poudre wool blazer",
            "nameEN": "Holbrook grain de poudre wool blazer",
            "type": "ProductColour",
            "mfPartNumber": "8293-W3181BLK",
            "designerName": "THE ROW",
            "badges": [
                {
                    "label": "LOW STOCK",
                    "type": "STOCK",
                    "key": "BADGE_LOW_STOCK"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 391800,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 391800,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597340634474",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "00",
                            "label": "00"
                        },
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power RTW",
                            "label": "Power RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "THEROW",
                            "label": "THE ROW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "THE ROW",
            "seo": {
                "seoURLKeyword": "/the-row/clothing/blazers/holbrook-grain-de-poudre-wool-blazer/1647597340634474"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "2",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597310507840/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "SELFPORTRAIT",
            "productId": "3074457345626277177",
            "modelId": "3074457345626277171",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "White",
                    "visible": "True",
                    "productId": "3074457345626277177",
                    "labelEN": "White",
                    "label": "White",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "PF23-933J-W.White",
                    "badges": [
                        {
                            "label": "EXCLUSIVE",
                            "type": "MERCHANDISING",
                            "key": "BADGE_EXCLUSIVE"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 112101,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 112200,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597310507840",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597310507840/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Cropped embellished satin-trimmed metallic bouclé-tweed blazer",
            "nameEN": "Cropped embellished satin-trimmed metallic bouclé-tweed blazer",
            "type": "ProductColour",
            "mfPartNumber": "PF23-933J-W.White",
            "designerName": "SELF-PORTRAIT",
            "badges": [
                {
                    "label": "EXCLUSIVE",
                    "type": "MERCHANDISING",
                    "key": "BADGE_EXCLUSIVE"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 112101,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 112200,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597310507840",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "White",
                            "label": "White"
                        },
                        {
                            "identifier": "White",
                            "label": "White"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "Continuity",
                            "label": "Continuity"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "SELFPORTRAIT",
                            "label": "SELF-PORTRAIT"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Contemporary RTW",
                            "label": "Contemporary RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "SELF-PORTRAIT",
            "seo": {
                "seoURLKeyword": "/self-portrait/clothing/blazers/cropped-embellished-satin-trimmed-metallic-boucle-tweed-blazer/1647597310507840"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597355286522/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "BRUNELLOCUCINELLI",
            "productId": "3074457345628848373",
            "modelId": "3074457345628848244",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Brown",
                    "visible": "True",
                    "productId": "3074457345628848373",
                    "labelEN": "Brown",
                    "label": "Brown",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "M0PCL208XC7495",
                    "badges": [
                        {
                            "label": "LOW STOCK",
                            "type": "STOCK",
                            "key": "BADGE_LOW_STOCK"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 645600,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 645600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597355286522",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597355286522/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Suede blazer",
            "nameEN": "Suede blazer",
            "type": "ProductColour",
            "mfPartNumber": "M0PCL208XC7495",
            "designerName": "BRUNELLO CUCINELLI",
            "badges": [
                {
                    "label": "LOW STOCK",
                    "type": "STOCK",
                    "key": "BADGE_LOW_STOCK"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 645600,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 645600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597355286522",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Brown",
                            "label": "Brown"
                        },
                        {
                            "identifier": "Brown",
                            "label": "Brown"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "BRUNELLOCUCINELLI",
                            "label": "BRUNELLO CUCINELLI"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Established Designer",
                            "label": "Established Designer"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "BRUNELLO CUCINELLI",
            "seo": {
                "seoURLKeyword": "/brunello-cucinelli/clothing/blazers/suede-blazer/1647597355286522"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "6",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597350558308/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "SELFPORTRAIT",
            "productId": "3074457345628648858",
            "modelId": "3074457345628648682",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Cream",
                    "visible": "True",
                    "productId": "3074457345628648858",
                    "labelEN": "Cream",
                    "label": "Cream",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "RS25-164J-CCREAM",
                    "badges": [
                        {
                            "label": "20% OFF AT CHECKOUT",
                            "type": "MERCHANDISING",
                            "key": "BADGE_FP_PROMO_AUTOAPPLY"
                        },
                        {
                            "label": "TRENDING NOW",
                            "type": "MERCHANDISING",
                            "key": "BADGE_TRENDING_NOW"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 95500,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 95500,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597350558308",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597350558308/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Cropped faux pearl-embellished sequined tweed jacket",
            "nameEN": "Cropped faux pearl-embellished sequined tweed jacket",
            "type": "ProductColour",
            "mfPartNumber": "RS25-164J-CCREAM",
            "designerName": "SELF-PORTRAIT",
            "badges": [
                {
                    "label": "20% OFF AT CHECKOUT",
                    "type": "MERCHANDISING",
                    "key": "BADGE_FP_PROMO_AUTOAPPLY"
                },
                {
                    "label": "TRENDING NOW",
                    "type": "MERCHANDISING",
                    "key": "BADGE_TRENDING_NOW"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 95500,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 95500,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597350558308",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Cream",
                            "label": "Cream"
                        },
                        {
                            "identifier": "Cream",
                            "label": "Cream"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Contemporary RTW",
                            "label": "Contemporary RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "SELFPORTRAIT",
                            "label": "SELF-PORTRAIT"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "SELF-PORTRAIT",
            "seo": {
                "seoURLKeyword": "/self-portrait/clothing/casual-jackets/cropped-faux-pearl-embellished-sequined-tweed-jacket/1647597350558308"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "4",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597325563744/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "MONCLER",
            "productId": "3074457345627098703",
            "modelId": "3074457345627098680",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Beige",
                    "visible": "True",
                    "productId": "3074457345627098703",
                    "labelEN": "Beige",
                    "label": "Beige",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "1A00068 - 595ZZ200",
                    "price": {
                        "sellingPrice": {
                            "amount": 172200,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 172200,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597325563744",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597325563744/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Argenno hooded belted appliquéd quilted shell down coat",
            "nameEN": "Argenno hooded belted appliquéd quilted shell down coat",
            "type": "ProductColour",
            "mfPartNumber": "1A00068 - 595ZZ200",
            "designerName": "MONCLER",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 172200,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 172200,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597325563744",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Beige",
                            "label": "Beige"
                        },
                        {
                            "identifier": "Beige",
                            "label": "Beige"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "HS24",
                            "label": "HS24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "00",
                            "label": "00"
                        },
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "1",
                            "label": "1"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "3",
                            "label": "3"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "5",
                            "label": "5"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "7",
                            "label": "7"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "9",
                            "label": "9"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "11",
                            "label": "11"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "13",
                            "label": "13"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "MONCLER",
                            "label": "MONCLER"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "MONCLER",
            "seo": {
                "seoURLKeyword": "/moncler/clothing/long/argenno-hooded-belted-appliqued-quilted-shell-down-coat/1647597325563744"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "1",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597352504996/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "BRUNELLOCUCINELLI",
            "productId": "3074457345628732212",
            "modelId": "3074457345628732179",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Dark gray",
                    "visible": "True",
                    "productId": "3074457345628732212",
                    "labelEN": "Dark gray",
                    "label": "Dark gray",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "M038P9703C006",
                    "price": {
                        "sellingPrice": {
                            "amount": 894400,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 894400,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597352504996",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597352504996/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Hooded faux fur-trimmed quilted wool down coat",
            "nameEN": "Hooded faux fur-trimmed quilted wool down coat",
            "type": "ProductColour",
            "mfPartNumber": "M038P9703C006",
            "designerName": "BRUNELLO CUCINELLI",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 894400,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 894400,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597352504996",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Dark gray",
                            "label": "Dark gray"
                        },
                        {
                            "identifier": "Dark gray",
                            "label": "Dark gray"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "BRUNELLOCUCINELLI",
                            "label": "BRUNELLO CUCINELLI"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "BRUNELLO CUCINELLI",
            "seo": {
                "seoURLKeyword": "/brunello-cucinelli/clothing/long/hooded-faux-fur-trimmed-quilted-wool-down-coat/1647597352504996"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "10",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597338909825/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "MONCLER",
            "productId": "3074457345628004738",
            "modelId": "3074457345628004693",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628004738",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "1C00026 595FE999",
                    "price": {
                        "sellingPrice": {
                            "amount": 258300,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 258300,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597338909825",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597338909825/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Boulogne reversible hooded quilted down coat",
            "nameEN": "Boulogne reversible hooded quilted down coat",
            "type": "ProductColour",
            "mfPartNumber": "1C00026 595FE999",
            "designerName": "MONCLER",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-2775",
                        "labelEN": "Knee Length",
                        "label": "Knee Length",
                        "categoryId": "3074457345616677112"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 258300,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 258300,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597338909825",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "FW24",
                            "label": "FW24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "00",
                            "label": "00"
                        },
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "1",
                            "label": "1"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "3",
                            "label": "3"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "5",
                            "label": "5"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "7",
                            "label": "7"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "9",
                            "label": "9"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "11",
                            "label": "11"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "13",
                            "label": "13"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "MONCLER",
                            "label": "MONCLER"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "MONCLER",
            "seo": {
                "seoURLKeyword": "/moncler/clothing/knee-length/boulogne-reversible-hooded-quilted-down-coat/1647597338909825"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597345911113/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "LOROPIANA",
            "productId": "3074457345628462729",
            "modelId": "3074457345628462670",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Cream",
                    "visible": "True",
                    "productId": "3074457345628462729",
                    "labelEN": "Cream",
                    "label": "Cream",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "FAO3220A0C7",
                    "badges": [
                        {
                            "label": "EXCLUSIVE",
                            "type": "MERCHANDISING",
                            "key": "BADGE_EXCLUSIVE"
                        },
                        {
                            "label": "LOW STOCK",
                            "type": "STOCK",
                            "key": "BADGE_LOW_STOCK"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 764800,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 764800,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597345911113",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597345911113/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Belted cashmere cardigan",
            "nameEN": "Belted cashmere cardigan",
            "type": "ProductColour",
            "mfPartNumber": "FAO3220A0C7",
            "designerName": "LORO PIANA",
            "badges": [
                {
                    "label": "EXCLUSIVE",
                    "type": "MERCHANDISING",
                    "key": "BADGE_EXCLUSIVE"
                },
                {
                    "label": "LOW STOCK",
                    "type": "STOCK",
                    "key": "BADGE_LOW_STOCK"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-78",
                        "labelEN": "Short",
                        "label": "Short",
                        "categoryId": "3074457345616677114"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 764800,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 764800,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597345911113",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Cream",
                            "label": "Cream"
                        },
                        {
                            "identifier": "Cream",
                            "label": "Cream"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "xx small",
                            "label": "xx small"
                        },
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Established Designer",
                            "label": "Established Designer"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "LOROPIANA",
                            "label": "LORO PIANA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "LORO PIANA",
            "seo": {
                "seoURLKeyword": "/loro-piana/clothing/short/belted-cashmere-cardigan/1647597345911113"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "2",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597347034735/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "ACNESTUDIOS",
            "productId": "3074457345628499734",
            "modelId": "3074457345628499688",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Camel",
                    "visible": "True",
                    "productId": "3074457345628499734",
                    "labelEN": "Camel",
                    "label": "Camel",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "AH0302-DFJ",
                    "price": {
                        "sellingPrice": {
                            "amount": 142500,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 142500,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597347034735",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597347034735/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Twill blazer",
            "nameEN": "Twill blazer",
            "type": "ProductColour",
            "mfPartNumber": "AH0302-DFJ",
            "designerName": "ACNE STUDIOS",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 142500,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 142500,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597347034735",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Camel",
                            "label": "Camel"
                        },
                        {
                            "identifier": "Camel",
                            "label": "Camel"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        },
                        {
                            "identifier": "54",
                            "label": "54"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "ACNESTUDIOS",
                            "label": "ACNE STUDIOS"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "ACNE STUDIOS",
            "seo": {
                "seoURLKeyword": "/acne-studios/clothing/blazers/twill-blazer/1647597347034735"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "41",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597340340087/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345628098171",
            "modelId": "3074457345628098168",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628098171",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "244-WRO0131-FB0292BLACK 100",
                    "price": {
                        "sellingPrice": {
                            "amount": 202300,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 202300,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597340340087",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597340340087/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Draped fringed wool-blend bouclé jacket",
            "nameEN": "Draped fringed wool-blend bouclé jacket",
            "type": "ProductColour",
            "mfPartNumber": "244-WRO0131-FB0292BLACK 100",
            "designerName": "TOTEME",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 202300,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 202300,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597340340087",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "28",
                            "label": "28"
                        },
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/long/draped-fringed-wool-blend-boucle-jacket/1647597340340087"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "16",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597355972301/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345628879169",
            "modelId": "3074457345628879168",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628879169",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "214-120-604.BLACK 100",
                    "badges": [
                        {
                            "label": "EXCLUSIVE",
                            "type": "MERCHANDISING",
                            "key": "BADGE_EXCLUSIVE"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 427400,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 427400,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597355972301",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597355972301/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Leather-trimmed shearling jacket",
            "nameEN": "Leather-trimmed shearling jacket",
            "type": "ProductColour",
            "mfPartNumber": "214-120-604.BLACK 100",
            "designerName": "TOTEME",
            "badges": [
                {
                    "label": "EXCLUSIVE",
                    "type": "MERCHANDISING",
                    "key": "BADGE_EXCLUSIVE"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 427400,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 427400,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597355972301",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "XXS",
                            "label": "XXS"
                        },
                        {
                            "identifier": "XS/S",
                            "label": "XS/S"
                        },
                        {
                            "identifier": "M/L",
                            "label": "M/L"
                        },
                        {
                            "identifier": "XL",
                            "label": "XL"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Bridge",
                            "label": "Bridge"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/casual-jackets/leather-trimmed-shearling-jacket/1647597355972301"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597329802564/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "LOROPIANA",
            "productId": "3074457345627351191",
            "modelId": "3074457345627351175",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Dark green",
                    "visible": "True",
                    "productId": "3074457345627351191",
                    "labelEN": "Dark green",
                    "label": "Dark green",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "FAN346550LT",
                    "price": {
                        "sellingPrice": {
                            "amount": 375707,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 375800,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597329802564",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597329802564/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Raniya belted macramé-trimmed cotton-blend velvet jacket",
            "nameEN": "Raniya belted macramé-trimmed cotton-blend velvet jacket",
            "type": "ProductColour",
            "mfPartNumber": "FAN346550LT",
            "designerName": "LORO PIANA",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 375707,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 375800,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597329802564",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Dark green",
                            "label": "Dark green"
                        },
                        {
                            "identifier": "Dark green",
                            "label": "Dark green"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "HS24",
                            "label": "HS24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "LOROPIANA",
                            "label": "LORO PIANA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "LORO PIANA",
            "seo": {
                "seoURLKeyword": "/loro-piana/clothing/blazers/raniya-belted-macrame-trimmed-cotton-blend-velvet-jacket/1647597329802564"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "12",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/45666037505083681/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345624131273",
            "modelId": "3074457345628833857",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Camel",
                    "visible": "True",
                    "productId": "3074457345624131273",
                    "labelEN": "Camel",
                    "label": "Camel",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "211-110-717CAMEL 835",
                    "price": {
                        "sellingPrice": {
                            "amount": 187747,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 187800,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "45666037505083681",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/45666037505083681/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "+ NET SUSTAIN Signature wool-blend coat",
            "nameEN": "+ NET SUSTAIN Signature wool-blend coat",
            "type": "ProductColour",
            "mfPartNumber": "211-110-717CAMEL 835",
            "designerName": "TOTEME",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 187747,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 187800,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Signature wool-blend coat",
            "partNumber": "45666037505083681",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Camel",
                            "label": "Camel"
                        },
                        {
                            "identifier": "Camel",
                            "label": "Camel"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/long/plus-net-sustain-signature-wool-blend-coat/45666037505083681"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "6",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/665933303132717/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "MAXMARA",
            "hasSiblings": "True",
            "productId": "3074457345617009299",
            "modelId": "3074457345617008676",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Camel",
                    "visible": "True",
                    "productId": "3074457345617009299",
                    "labelEN": "Camel",
                    "label": "Camel",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "MADAME01",
                    "price": {
                        "sellingPrice": {
                            "amount": 372457,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 372500,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "legacyId": "1146975",
                    "partNumber": "665933303132717",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/665933303132717/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Madame 101801 Icon double-breasted wool and cashmere-blend coat",
            "nameEN": "Madame 101801 Icon double-breasted wool and cashmere-blend coat",
            "type": "ProductColour",
            "mfPartNumber": "MADAME01",
            "designerName": "MAX MARA",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 372457,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 372500,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Madame 101801 Icon double-breasted wool and cashmere-blend coat",
            "legacyId": "1146975",
            "partNumber": "665933303132717",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Camel",
                            "label": "Camel"
                        },
                        {
                            "identifier": "Camel",
                            "label": "Camel"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "MAXMARA",
                            "label": "MAX MARA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "MAX MARA",
            "seo": {
                "seoURLKeyword": "/max-mara/clothing/long/madame-101801-icon-double-breasted-wool-and-cashmere-blend-coat/665933303132717"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597357891196/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "SAINTLAURENT",
            "hasSiblings": "True",
            "productId": "3074457345629005348",
            "modelId": "3074457345629005236",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Beige",
                    "visible": "True",
                    "productId": "3074457345629005348",
                    "labelEN": "Beige",
                    "label": "Beige",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "812414Y3A999610",
                    "price": {
                        "sellingPrice": {
                            "amount": 452000,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 452000,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597357891196",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597357891196/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Oversized belted cotton-twill trench coat",
            "nameEN": "Oversized belted cotton-twill trench coat",
            "type": "ProductColour",
            "mfPartNumber": "812414Y3A999610",
            "designerName": "SAINT LAURENT",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-80",
                        "labelEN": "Trench Coats",
                        "label": "Trench Coats",
                        "categoryId": "3074457345616677115"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 452000,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 452000,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597357891196",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Beige",
                            "label": "Beige"
                        },
                        {
                            "identifier": "Beige",
                            "label": "Beige"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "28",
                            "label": "28"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "SAINTLAURENT",
                            "label": "SAINT LAURENT"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power RTW",
                            "label": "Power RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "SAINT LAURENT",
            "seo": {
                "seoURLKeyword": "/saint-laurent/clothing/trench-coats/oversized-belted-cotton-twill-trench-coat/1647597357891196"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "2",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597348514976/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "LOEWE",
            "hasSiblings": "True",
            "productId": "3074457345628534698",
            "modelId": "3074457345628534679",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Ivory",
                    "visible": "True",
                    "productId": "3074457345628534698",
                    "labelEN": "Ivory",
                    "label": "Ivory",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "S359Y02XCS2110",
                    "badges": [
                        {
                            "label": "LOW STOCK",
                            "type": "STOCK",
                            "key": "BADGE_LOW_STOCK"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 484400,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 484400,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597348514976",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597348514976/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Shearling-trimmed cotton-blend shell jacket",
            "nameEN": "Shearling-trimmed cotton-blend shell jacket",
            "type": "ProductColour",
            "mfPartNumber": "S359Y02XCS2110",
            "designerName": "LOEWE",
            "badges": [
                {
                    "label": "LOW STOCK",
                    "type": "STOCK",
                    "key": "BADGE_LOW_STOCK"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 484400,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 484400,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597348514976",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Ivory",
                            "label": "Ivory"
                        },
                        {
                            "identifier": "Ivory",
                            "label": "Ivory"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "28",
                            "label": "28"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "LOEWE",
                            "label": "LOEWE"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power RTW",
                            "label": "Power RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "LOEWE",
            "seo": {
                "seoURLKeyword": "/loewe/clothing/casual-jackets/shearling-trimmed-cotton-blend-shell-jacket/1647597348514976"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597354437897/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "WARDROBENYC",
            "hasSiblings": "True",
            "productId": "3074457345628823694",
            "modelId": "3074457345627534676",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Charcoal",
                    "visible": "True",
                    "productId": "3074457345628823694",
                    "labelEN": "Charcoal",
                    "label": "Charcoal",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "W4060PCCHA",
                    "badges": [
                        {
                            "label": "LOW STOCK",
                            "type": "STOCK",
                            "key": "BADGE_LOW_STOCK"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 206100,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 206100,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597354437897",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597354437897/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Wool blazer",
            "nameEN": "Wool blazer",
            "type": "ProductColour",
            "mfPartNumber": "W4060PCCHA",
            "designerName": "WARDROBE.NYC",
            "badges": [
                {
                    "label": "LOW STOCK",
                    "type": "STOCK",
                    "key": "BADGE_LOW_STOCK"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 206100,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 206100,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597354437897",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Charcoal",
                            "label": "Charcoal"
                        },
                        {
                            "identifier": "Charcoal",
                            "label": "Charcoal"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "xx small",
                            "label": "xx small"
                        },
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "WARDROBENYC",
                            "label": "WARDROBE.NYC"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "WARDROBE.NYC",
            "seo": {
                "seoURLKeyword": "/wardrobenyc/clothing/blazers/wool-blazer/1647597354437897"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597350541504/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "BURBERRY",
            "productId": "3074457345628646795",
            "modelId": "3074457345628646711",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Forest green",
                    "visible": "True",
                    "productId": "3074457345628646795",
                    "labelEN": "Forest green",
                    "label": "Forest green",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "8104555C1764",
                    "price": {
                        "sellingPrice": {
                            "amount": 411800,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 411800,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597350541504",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597350541504/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Double-breasted belted cotton-gabardine trench coat",
            "nameEN": "Double-breasted belted cotton-gabardine trench coat",
            "type": "ProductColour",
            "mfPartNumber": "8104555C1764",
            "designerName": "BURBERRY",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-80",
                        "labelEN": "Trench Coats",
                        "label": "Trench Coats",
                        "categoryId": "3074457345616677115"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 411800,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 411800,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597350541504",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Forest green",
                            "label": "Forest green"
                        },
                        {
                            "identifier": "Forest green",
                            "label": "Forest green"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "BURBERRY",
                            "label": "BURBERRY"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "BURBERRY",
            "seo": {
                "seoURLKeyword": "/burberry/clothing/trench-coats/double-breasted-belted-cotton-gabardine-trench-coat/1647597350541504"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "3",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597349511528/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "GUESTINRESIDENCE",
            "hasSiblings": "True",
            "productId": "3074457345628579757",
            "modelId": "3074457345627140714",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Cream",
                    "visible": "True",
                    "productId": "3074457345628579757",
                    "labelEN": "Cream",
                    "label": "Cream",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "U20610JHCREAM",
                    "badges": [
                        {
                            "label": "20% OFF AT CHECKOUT",
                            "type": "MERCHANDISING",
                            "key": "BADGE_FP_PROMO_AUTOAPPLY"
                        },
                        {
                            "label": "EXCLUSIVE",
                            "type": "MERCHANDISING",
                            "key": "BADGE_EXCLUSIVE"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 170300,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 170300,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597349511528",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597349511528/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Grizzly belted brushed-cashmere coat",
            "nameEN": "Grizzly belted brushed-cashmere coat",
            "type": "ProductColour",
            "mfPartNumber": "U20610JHCREAM",
            "designerName": "GUEST IN RESIDENCE",
            "badges": [
                {
                    "label": "20% OFF AT CHECKOUT",
                    "type": "MERCHANDISING",
                    "key": "BADGE_FP_PROMO_AUTOAPPLY"
                },
                {
                    "label": "EXCLUSIVE",
                    "type": "MERCHANDISING",
                    "key": "BADGE_EXCLUSIVE"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 170300,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 170300,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597349511528",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Cream",
                            "label": "Cream"
                        },
                        {
                            "identifier": "Cream",
                            "label": "Cream"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Casual and Denim",
                            "label": "Casual and Denim"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "GUESTINRESIDENCE",
                            "label": "GUEST IN RESIDENCE"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "GUEST IN RESIDENCE",
            "seo": {
                "seoURLKeyword": "/guest-in-residence/clothing/long/grizzly-belted-brushed-cashmere-coat/1647597349511528"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597346625397/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "THANKYOUHAVEAGOODDAY",
            "productId": "3074457345628488690",
            "modelId": "3074457345628488678",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Blue",
                    "visible": "True",
                    "productId": "3074457345628488690",
                    "labelEN": "Blue",
                    "label": "Blue",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "CROSBY COATBLUE",
                    "badges": [
                        {
                            "label": "EXCLUSIVE",
                            "type": "MERCHANDISING",
                            "key": "BADGE_EXCLUSIVE"
                        },
                        {
                            "label": "NEW DESIGNER",
                            "type": "MERCHANDISING",
                            "key": "BADGE_NEW_DESIGNER"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 245800,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 245800,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597346625397",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597346625397/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Crosby  jacquard-trimmed wool coat",
            "nameEN": "Crosby  jacquard-trimmed wool coat",
            "type": "ProductColour",
            "mfPartNumber": "CROSBY COATBLUE",
            "designerName": "THANK YOU HAVE A GOOD DAY",
            "badges": [
                {
                    "label": "EXCLUSIVE",
                    "type": "MERCHANDISING",
                    "key": "BADGE_EXCLUSIVE"
                },
                {
                    "label": "NEW DESIGNER",
                    "type": "MERCHANDISING",
                    "key": "BADGE_NEW_DESIGNER"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 245800,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 245800,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597346625397",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Blue",
                            "label": "Blue"
                        },
                        {
                            "identifier": "Blue",
                            "label": "Blue"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "One size",
                            "label": "One size"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Contemporary RTW",
                            "label": "Contemporary RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Designed for Circularity",
                            "label": "Designed for Circularity"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "THANKYOUHAVEAGOODDAY",
                            "label": "THANK YOU HAVE A GOOD DAY"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "THANK YOU HAVE A GOOD DAY",
            "seo": {
                "seoURLKeyword": "/thank-you-have-a-good-day/clothing/long/crosby-jacquard-trimmed-wool-coat/1647597346625397"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597355461514/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "GUCCI",
            "productId": "3074457345628856207",
            "modelId": "3074457345628856177",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Dark gray",
                    "visible": "True",
                    "productId": "3074457345628856207",
                    "labelEN": "Dark gray",
                    "label": "Dark gray",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "803898ZAQW01179",
                    "badges": [
                        {
                            "label": "LOW STOCK",
                            "type": "STOCK",
                            "key": "BADGE_LOW_STOCK"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 519000,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 519000,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597355461514",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597355461514/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Belted wool and silk-blend coat",
            "nameEN": "Belted wool and silk-blend coat",
            "type": "ProductColour",
            "mfPartNumber": "803898ZAQW01179",
            "designerName": "GUCCI",
            "badges": [
                {
                    "label": "LOW STOCK",
                    "type": "STOCK",
                    "key": "BADGE_LOW_STOCK"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 519000,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 519000,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597355461514",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Dark gray",
                            "label": "Dark gray"
                        },
                        {
                            "identifier": "Dark gray",
                            "label": "Dark gray"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "GUCCI",
                            "label": "GUCCI"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power RTW",
                            "label": "Power RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "GUCCI",
            "seo": {
                "seoURLKeyword": "/gucci/clothing/long/belted-wool-and-silk-blend-coat/1647597355461514"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "2",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597317679912/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "MAXMARA",
            "hasSiblings": "True",
            "productId": "3074457345626648670",
            "modelId": "3074457345617766000",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Gray",
                    "visible": "True",
                    "productId": "3074457345626648670",
                    "labelEN": "Gray",
                    "label": "Gray",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "2421016052600001",
                    "price": {
                        "sellingPrice": {
                            "amount": 365756,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 365800,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597317679912",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597317679912/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Teddy Bear Icon oversized wool, alpaca and silk-blend coat",
            "nameEN": "Teddy Bear Icon oversized wool, alpaca and silk-blend coat",
            "type": "ProductColour",
            "mfPartNumber": "2421016052600001",
            "designerName": "MAX MARA",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 365756,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 365800,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597317679912",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Gray",
                            "label": "Gray"
                        },
                        {
                            "identifier": "Gray",
                            "label": "Gray"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "MAXMARA",
                            "label": "MAX MARA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "MAX MARA",
            "seo": {
                "seoURLKeyword": "/max-mara/clothing/long/teddy-bear-icon-oversized-wool-alpaca-and-silk-blend-coat/1647597317679912"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "7",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597355914677/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345628875669",
            "modelId": "3074457345628833857",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628875669",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "211-110-717.BLACK 001",
                    "price": {
                        "sellingPrice": {
                            "amount": 212300,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 212300,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597355914677",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597355914677/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Signature wool and cashmere-blend coat",
            "nameEN": "Signature wool and cashmere-blend coat",
            "type": "ProductColour",
            "mfPartNumber": "211-110-717.BLACK 001",
            "designerName": "TOTEME",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 212300,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 212300,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597355914677",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "FW24",
                            "label": "FW24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "xx small",
                            "label": "xx small"
                        },
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/long/signature-wool-and-cashmere-blend-coat/1647597355914677"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "2",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597347034733/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "ACNESTUDIOS",
            "productId": "3074457345628499713",
            "modelId": "3074457345628499670",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Brown",
                    "visible": "True",
                    "productId": "3074457345628499713",
                    "labelEN": "Brown",
                    "label": "Brown",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "A70186-AA3",
                    "price": {
                        "sellingPrice": {
                            "amount": 527200,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 527200,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597347034733",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597347034733/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Shearling jacket",
            "nameEN": "Shearling jacket",
            "type": "ProductColour",
            "mfPartNumber": "A70186-AA3",
            "designerName": "ACNE STUDIOS",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1370",
                        "labelEN": "Biker Jackets",
                        "label": "Biker Jackets",
                        "categoryId": "3074457345616677121"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 527200,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 527200,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597347034733",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Brown",
                            "label": "Brown"
                        },
                        {
                            "identifier": "Brown",
                            "label": "Brown"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        },
                        {
                            "identifier": "54",
                            "label": "54"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "ACNESTUDIOS",
                            "label": "ACNE STUDIOS"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "ACNE STUDIOS",
            "seo": {
                "seoURLKeyword": "/acne-studios/clothing/biker-jackets/shearling-jacket/1647597347034733"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "3",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/13452677153309983/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "MAXMARA",
            "productId": "3074457345621239693",
            "modelId": "3074457345617769371",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345621239693",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "1016032306 3MANUEL002",
                    "price": {
                        "sellingPrice": {
                            "amount": 300882,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 300900,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "legacyId": "1355020",
                    "partNumber": "13452677153309983",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/13452677153309983/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Manuela belted camel hair coat",
            "nameEN": "Manuela belted camel hair coat",
            "type": "ProductColour",
            "mfPartNumber": "1016032306 3MANUEL002",
            "designerName": "MAX MARA",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 300882,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 300900,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Manuela belted camel hair coat",
            "legacyId": "1355020",
            "partNumber": "13452677153309983",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "MAXMARA",
                            "label": "MAX MARA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "MAX MARA",
            "seo": {
                "seoURLKeyword": "/max-mara/clothing/long/manuela-belted-camel-hair-coat/13452677153309983"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597344765719/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "CHLO",
            "productId": "3074457345628387736",
            "modelId": "3074457345628387682",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Green",
                    "visible": "True",
                    "productId": "3074457345628387736",
                    "labelEN": "Green",
                    "label": "Green",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "CH24WMA091643G3",
                    "badges": [
                        {
                            "label": "RUNWAY",
                            "type": "MERCHANDISING",
                            "key": "BADGE_RUNWAY"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 1078400,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 1078400,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597344765719",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597344765719/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Oversized leather-trimmed checked wool-blend flannel coat",
            "nameEN": "Oversized leather-trimmed checked wool-blend flannel coat",
            "type": "ProductColour",
            "mfPartNumber": "CH24WMA091643G3",
            "designerName": "CHLOÉ",
            "badges": [
                {
                    "label": "RUNWAY",
                    "type": "MERCHANDISING",
                    "key": "BADGE_RUNWAY"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 1078400,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 1078400,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597344765719",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Green",
                            "label": "Green"
                        },
                        {
                            "identifier": "Green",
                            "label": "Green"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "FW24",
                            "label": "FW24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "28",
                            "label": "28"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power RTW",
                            "label": "Power RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "CHLO",
                            "label": "CHLOÉ"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "CHLOÉ",
            "seo": {
                "seoURLKeyword": "/chloe/clothing/long/oversized-leather-trimmed-checked-wool-blend-flannel-coat/1647597344765719"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597354681315/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "VERONICADEPIANTE",
            "productId": "3074457345628829687",
            "modelId": "3074457345628829672",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Green",
                    "visible": "True",
                    "productId": "3074457345628829687",
                    "labelEN": "Green",
                    "label": "Green",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "VDPGP1010PINE GREEN",
                    "price": {
                        "sellingPrice": {
                            "amount": 330600,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 330600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597354681315",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597354681315/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Manon grain de poudre wool and cashmere-blend coat",
            "nameEN": "Manon grain de poudre wool and cashmere-blend coat",
            "type": "ProductColour",
            "mfPartNumber": "VDPGP1010PINE GREEN",
            "designerName": "VERONICA DE PIANTE",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 330600,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 330600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597354681315",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Green",
                            "label": "Green"
                        },
                        {
                            "identifier": "Green",
                            "label": "Green"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "SS25",
                            "label": "SS25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "VERONICADEPIANTE",
                            "label": "VERONICA DE PIANTE"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "VERONICA DE PIANTE",
            "seo": {
                "seoURLKeyword": "/veronica-de-piante/clothing/long/manon-grain-de-poudre-wool-and-cashmere-blend-coat/1647597354681315"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "5",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/13452677153309981/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "MAXMARA",
            "hasSiblings": "True",
            "productId": "3074457345621239724",
            "modelId": "3074457345625341670",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345621239724",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "2421016042600008",
                    "price": {
                        "sellingPrice": {
                            "amount": 353550,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 353600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "legacyId": "1352516",
                    "partNumber": "13452677153309981",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/13452677153309981/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Tedgirl double-breasted alpaca, wool and silk-blend coat",
            "nameEN": "Tedgirl double-breasted alpaca, wool and silk-blend coat",
            "type": "ProductColour",
            "mfPartNumber": "2421016042600008",
            "designerName": "MAX MARA",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 353550,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 353600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Tedgirl double-breasted alpaca, wool and silk-blend coat",
            "legacyId": "1352516",
            "partNumber": "13452677153309981",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "xx small",
                            "label": "xx small"
                        },
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "MAXMARA",
                            "label": "MAX MARA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "MAX MARA",
            "seo": {
                "seoURLKeyword": "/max-mara/clothing/long/tedgirl-double-breasted-alpaca-wool-and-silk-blend-coat/13452677153309981"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "3",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/13452677153309979/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "MAXMARA",
            "hasSiblings": "True",
            "productId": "3074457345621239722",
            "modelId": "3074457345625341670",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Ivory",
                    "visible": "True",
                    "productId": "3074457345621239722",
                    "labelEN": "Ivory",
                    "label": "Ivory",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "2421016042600001",
                    "price": {
                        "sellingPrice": {
                            "amount": 353550,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 353600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "legacyId": "1352514",
                    "partNumber": "13452677153309979",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/13452677153309979/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Tedgirl double-breasted alpaca, wool and silk-blend coat",
            "nameEN": "Tedgirl double-breasted alpaca, wool and silk-blend coat",
            "type": "ProductColour",
            "mfPartNumber": "2421016042600001",
            "designerName": "MAX MARA",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 353550,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 353600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Tedgirl double-breasted alpaca, wool and silk-blend coat",
            "legacyId": "1352514",
            "partNumber": "13452677153309979",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Ivory",
                            "label": "Ivory"
                        },
                        {
                            "identifier": "Ivory",
                            "label": "Ivory"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "xx small",
                            "label": "xx small"
                        },
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "MAXMARA",
                            "label": "MAX MARA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "MAX MARA",
            "seo": {
                "seoURLKeyword": "/max-mara/clothing/long/tedgirl-double-breasted-alpaca-wool-and-silk-blend-coat/13452677153309979"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "25",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597326342287/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "THEFRANKIESHOP",
            "hasSiblings": "True",
            "productId": "3074457345627164374",
            "modelId": "3074457345621935184",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Army green",
                    "visible": "True",
                    "productId": "3074457345627164374",
                    "labelEN": "Army green",
                    "label": "Army green",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "OJATED407*Moss Green",
                    "price": {
                        "sellingPrice": {
                            "amount": 36000,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 36000,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597326342287",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597326342287/{view}/w{width}.jpg"
                }
            ],
            "isUnlinked": "1",
            "shortDescription": "Quilted padded ripstop jacket",
            "nameEN": "Quilted padded ripstop jacket",
            "type": "ProductColour",
            "mfPartNumber": "OJATED407*Moss Green",
            "designerName": "THE FRANKIE SHOP",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 36000,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 36000,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597326342287",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Army green",
                            "label": "Army green"
                        },
                        {
                            "identifier": "Army green",
                            "label": "Army green"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "XS/S",
                            "label": "XS/S"
                        },
                        {
                            "identifier": "S/M",
                            "label": "S/M"
                        },
                        {
                            "identifier": "M/L",
                            "label": "M/L"
                        },
                        {
                            "identifier": "L/XL",
                            "label": "L/XL"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "THEFRANKIESHOP",
                            "label": "THE FRANKIE SHOP"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "THE FRANKIE SHOP",
            "seo": {
                "seoURLKeyword": "/the-frankie-shop/clothing/casual-jackets/quilted-padded-ripstop-jacket/1647597326342287"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "29",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597336602125/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345627824673",
            "modelId": "3074457345622643168",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345627824673",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "211-177-732BLACK 200",
                    "price": {
                        "sellingPrice": {
                            "amount": 77000,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 77000,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597336602125",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597336602125/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Quilted recycled-shell jacket",
            "nameEN": "Quilted recycled-shell jacket",
            "type": "ProductColour",
            "mfPartNumber": "211-177-732BLACK 200",
            "designerName": "TOTEME",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 77000,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 77000,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Quilted recycled shell jacket",
            "partNumber": "1647597336602125",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "xx small",
                            "label": "xx small"
                        },
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/casual-jackets/quilted-recycled-shell-jacket/1647597336602125"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "6",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597325144796/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "LOEWE",
            "productId": "3074457345627074739",
            "modelId": "3074457345627074689",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Blue",
                    "visible": "True",
                    "productId": "3074457345627074739",
                    "labelEN": "Blue",
                    "label": "Blue",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "S359Y50X592834",
                    "price": {
                        "sellingPrice": {
                            "amount": 206600,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 206600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597325144796",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597325144796/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Anagram appliquéd denim jacket",
            "nameEN": "Anagram appliquéd denim jacket",
            "type": "ProductColour",
            "mfPartNumber": "S359Y50X592834",
            "designerName": "LOEWE",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 206600,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 206600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597325144796",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Blue",
                            "label": "Blue"
                        },
                        {
                            "identifier": "Blue",
                            "label": "Blue"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "HS24",
                            "label": "HS24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "28",
                            "label": "28"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "LOEWE",
                            "label": "LOEWE"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power Designer",
                            "label": "Power Designer"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "LOEWE",
            "seo": {
                "seoURLKeyword": "/loewe/clothing/casual-jackets/anagram-appliqued-denim-jacket/1647597325144796"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "10",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597336331163/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "ALAA",
            "productId": "3074457345627793183",
            "modelId": "3074457345627793169",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Blue",
                    "visible": "True",
                    "productId": "3074457345627793183",
                    "labelEN": "Blue",
                    "label": "Blue",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "AA9V03826T535524",
                    "price": {
                        "sellingPrice": {
                            "amount": 195700,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 195700,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597336331163",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597336331163/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Paneled denim jacket",
            "nameEN": "Paneled denim jacket",
            "type": "ProductColour",
            "mfPartNumber": "AA9V03826T535524",
            "designerName": "ALAÏA",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 195700,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 195700,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597336331163",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Blue",
                            "label": "Blue"
                        },
                        {
                            "identifier": "Blue",
                            "label": "Blue"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "FW24",
                            "label": "FW24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "28",
                            "label": "28"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "ALAA",
                            "label": "ALAÏA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power Designer",
                            "label": "Power Designer"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "ALAÏA",
            "seo": {
                "seoURLKeyword": "/alaia/clothing/casual-jackets/paneled-denim-jacket/1647597336331163"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "20",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597344063795/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "THEFRANKIESHOP",
            "hasSiblings": "True",
            "productId": "3074457345628322173",
            "modelId": "3074457345628322171",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628322173",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "OJAAST100*BLACK",
                    "price": {
                        "sellingPrice": {
                            "amount": 55300,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 55300,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597344063795",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597344063795/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Astra shell bomber jacket",
            "nameEN": "Astra shell bomber jacket",
            "type": "ProductColour",
            "mfPartNumber": "OJAAST100*BLACK",
            "designerName": "THE FRANKIE SHOP",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 55300,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 55300,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597344063795",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "XXXS/XXS",
                            "label": "XXXS/XXS"
                        },
                        {
                            "identifier": "XXS/XS",
                            "label": "XXS/XS"
                        },
                        {
                            "identifier": "XS/S",
                            "label": "XS/S"
                        },
                        {
                            "identifier": "S/M",
                            "label": "S/M"
                        },
                        {
                            "identifier": "M/L",
                            "label": "M/L"
                        },
                        {
                            "identifier": "L/XL",
                            "label": "L/XL"
                        },
                        {
                            "identifier": "XL/XXL",
                            "label": "XL/XXL"
                        },
                        {
                            "identifier": "XS",
                            "label": "XS"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "THEFRANKIESHOP",
                            "label": "THE FRANKIE SHOP"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "THE FRANKIE SHOP",
            "seo": {
                "seoURLKeyword": "/the-frankie-shop/clothing/casual-jackets/astra-shell-bomber-jacket/1647597344063795"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597319516091/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "VERSACE",
            "productId": "3074457345626771689",
            "modelId": "3074457345626771672",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345626771689",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "1011413_1A083471B000",
                    "price": {
                        "sellingPrice": {
                            "amount": 762200,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 762200,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597319516091",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597319516091/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Icons leather blazer",
            "nameEN": "Icons leather blazer",
            "type": "ProductColour",
            "mfPartNumber": "1011413_1A083471B000",
            "designerName": "VERSACE",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 762200,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 762200,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597319516091",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "VERSACE",
                            "label": "VERSACE"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "VERSACE",
            "seo": {
                "seoURLKeyword": "/versace/clothing/blazers/icons-leather-blazer/1647597319516091"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "3",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597316014491/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "CORDOVA",
            "hasSiblings": "True",
            "productId": "3074457345626532253",
            "modelId": "3074457345626532196",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Gray",
                    "visible": "True",
                    "productId": "3074457345626532253",
                    "labelEN": "Gray",
                    "label": "Gray",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "24AMRIW09GRAY MELANGE",
                    "badges": [
                        {
                            "label": "20% OFF AT CHECKOUT",
                            "type": "MERCHANDISING",
                            "key": "BADGE_FP_PROMO_AUTOAPPLY"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 179600,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 179600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597316014491",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597316014491/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Aomori hooded quilted down ski jacket",
            "nameEN": "Aomori hooded quilted down ski jacket",
            "type": "ProductColour",
            "mfPartNumber": "24AMRIW09GRAY MELANGE",
            "designerName": "CORDOVA",
            "badges": [
                {
                    "label": "20% OFF AT CHECKOUT",
                    "type": "MERCHANDISING",
                    "key": "BADGE_FP_PROMO_AUTOAPPLY"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-1911",
                "labelEN": "Sport",
                "label": "Sport",
                "categoryId": "3074457345616676672",
                "child": {
                    "identifier": "NAP-1911-1919",
                    "labelEN": "Ski",
                    "label": "Ski",
                    "categoryId": "3074457345616676737",
                    "child": {
                        "identifier": "NAP-1911-1919-1940",
                        "labelEN": "Outerwear",
                        "label": "Outerwear",
                        "categoryId": "3074457345616677053"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 179600,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 179600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597316014491",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Gray",
                            "label": "Gray"
                        },
                        {
                            "identifier": "Gray",
                            "label": "Gray"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Casual and Denim",
                            "label": "Casual and Denim"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "CORDOVA",
                            "label": "CORDOVA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "CORDOVA",
            "seo": {
                "seoURLKeyword": "/cordova/sport/outerwear/aomori-hooded-quilted-down-ski-jacket/1647597316014491"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "38",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/43769801094967944/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345623935727",
            "modelId": "3074457345624950185",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345623935727",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "224-1018-201BLACK 200",
                    "price": {
                        "sellingPrice": {
                            "amount": 161000,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 161000,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "43769801094967944",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/43769801094967944/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Draped fringed wool-blend jacket",
            "nameEN": "Draped fringed wool-blend jacket",
            "type": "ProductColour",
            "mfPartNumber": "224-1018-201BLACK 200",
            "designerName": "TOTEME",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 161000,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 161000,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Draped fringed wool-blend jacket",
            "partNumber": "43769801094967944",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "28",
                            "label": "28"
                        },
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/casual-jackets/draped-fringed-wool-blend-jacket/43769801094967944"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "7",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597325109274/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "BURBERRY",
            "hasSiblings": "True",
            "productId": "3074457345627072683",
            "modelId": "3074457345627072672",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Neutral",
                    "visible": "True",
                    "productId": "3074457345627072683",
                    "labelEN": "Neutral",
                    "label": "Neutral",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "8079404A1366",
                    "price": {
                        "sellingPrice": {
                            "amount": 369000,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 369000,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597325109274",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597325109274/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Chelsea organic cotton-gabardine trench coat",
            "nameEN": "Chelsea organic cotton-gabardine trench coat",
            "type": "ProductColour",
            "mfPartNumber": "8079404A1366",
            "designerName": "BURBERRY",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-80",
                        "labelEN": "Trench Coats",
                        "label": "Trench Coats",
                        "categoryId": "3074457345616677115"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 369000,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 369000,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597325109274",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Neutral",
                            "label": "Neutral"
                        },
                        {
                            "identifier": "Neutral",
                            "label": "Neutral"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "BURBERRY",
                            "label": "BURBERRY"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "BURBERRY",
            "seo": {
                "seoURLKeyword": "/burberry/clothing/trench-coats/chelsea-organic-cotton-gabardine-trench-coat/1647597325109274"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "7",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597281449159/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "CORDOVA",
            "hasSiblings": "True",
            "productId": "3074457345624495313",
            "modelId": "3074457345624495225",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345624495313",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "23SMT08ONYX",
                    "badges": [
                        {
                            "label": "20% OFF AT CHECKOUT",
                            "type": "MERCHANDISING",
                            "key": "BADGE_FP_PROMO_AUTOAPPLY"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 268600,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 268600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597281449159",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597281449159/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Sommet hooded belted padded ski suit",
            "nameEN": "Sommet hooded belted padded ski suit",
            "type": "ProductColour",
            "mfPartNumber": "23SMT08ONYX",
            "designerName": "CORDOVA",
            "badges": [
                {
                    "label": "20% OFF AT CHECKOUT",
                    "type": "MERCHANDISING",
                    "key": "BADGE_FP_PROMO_AUTOAPPLY"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-1911",
                "labelEN": "Sport",
                "label": "Sport",
                "categoryId": "3074457345616676672",
                "child": {
                    "identifier": "NAP-1911-1919",
                    "labelEN": "Ski",
                    "label": "Ski",
                    "categoryId": "3074457345616676737",
                    "child": {
                        "identifier": "NAP-1911-1919-1944",
                        "labelEN": "Ski Suits",
                        "label": "Ski Suits",
                        "categoryId": "3074457345616677057"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 268600,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 268600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Sommet hooded belted padded ski suit",
            "partNumber": "1647597281449159",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "x small",
                            "label": "x small"
                        },
                        {
                            "identifier": "small",
                            "label": "small"
                        },
                        {
                            "identifier": "medium",
                            "label": "medium"
                        },
                        {
                            "identifier": "large",
                            "label": "large"
                        },
                        {
                            "identifier": "x large",
                            "label": "x large"
                        },
                        {
                            "identifier": "xx large",
                            "label": "xx large"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Casual and Denim",
                            "label": "Casual and Denim"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "CORDOVA",
                            "label": "CORDOVA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                }
            ],
            "designerNameEN": "CORDOVA",
            "seo": {
                "seoURLKeyword": "/cordova/sport/ski-suits/sommet-hooded-belted-padded-ski-suit/1647597281449159"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "7",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597306616375/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "STELLAMCCARTNEY",
            "productId": "3074457345626000683",
            "modelId": "3074457345626000671",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345626000683",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "6500943CU7041000",
                    "price": {
                        "sellingPrice": {
                            "amount": 235100,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 235100,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597306616375",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597306616375/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "+ NET SUSTAIN wool-blend twill blazer",
            "nameEN": "+ NET SUSTAIN wool-blend twill blazer",
            "type": "ProductColour",
            "mfPartNumber": "6500943CU7041000",
            "designerName": "STELLA MCCARTNEY",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 235100,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 235100,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597306616375",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "STELLAMCCARTNEY",
                            "label": "STELLA MCCARTNEY"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power RTW",
                            "label": "Power RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "STELLA MCCARTNEY",
            "seo": {
                "seoURLKeyword": "/stella-mccartney/clothing/blazers/plus-net-sustain-wool-blend-twill-blazer/1647597306616375"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597340546978/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "RALPHLAURENCOLLECTION",
            "productId": "3074457345628111762",
            "modelId": "3074457345628111674",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Tan",
                    "visible": "True",
                    "productId": "3074457345628111762",
                    "labelEN": "Tan",
                    "label": "Tan",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "290955056001ICON TAN",
                    "price": {
                        "sellingPrice": {
                            "amount": 383300,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 383300,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597340546978",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597340546978/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Niles belted double-breasted cotton-blend twill trench coat",
            "nameEN": "Niles belted double-breasted cotton-blend twill trench coat",
            "type": "ProductColour",
            "mfPartNumber": "290955056001ICON TAN",
            "designerName": "RALPH LAUREN COLLECTION",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-80",
                        "labelEN": "Trench Coats",
                        "label": "Trench Coats",
                        "categoryId": "3074457345616677115"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 383300,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 383300,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597340546978",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Tan",
                            "label": "Tan"
                        },
                        {
                            "identifier": "Tan",
                            "label": "Tan"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "FW24",
                            "label": "FW24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "00",
                            "label": "00"
                        },
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "RALPHLAURENCOLLECTION",
                            "label": "RALPH LAUREN COLLECTION"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "RALPH LAUREN COLLECTION",
            "seo": {
                "seoURLKeyword": "/ralph-lauren-collection/clothing/trench-coats/niles-belted-double-breasted-cotton-blend-twill-trench-coat/1647597340546978"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "51",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/25185454456195123/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "hasSiblings": "True",
            "productId": "3074457345622325678",
            "modelId": "3074457345624950185",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Dark gray",
                    "visible": "True",
                    "productId": "3074457345622325678",
                    "labelEN": "Dark gray",
                    "label": "Dark gray",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "244-WR0918-FB0292DARK GREY MELANGE 359",
                    "price": {
                        "sellingPrice": {
                            "amount": 161000,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 161000,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "legacyId": "1374392",
                    "partNumber": "25185454456195123",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/25185454456195123/{view}/w{width}.jpg"
                }
            ],
            "isUnlinked": "1",
            "shortDescription": "Draped fringed wool-blend jacket",
            "nameEN": "Draped fringed wool-blend jacket",
            "type": "ProductColour",
            "mfPartNumber": "244-WR0918-FB0292DARK GREY MELANGE 359",
            "designerName": "TOTEME",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 161000,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 161000,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Draped fringed wool-blend jacket",
            "legacyId": "1374392",
            "partNumber": "25185454456195123",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Dark gray",
                            "label": "Dark gray"
                        },
                        {
                            "identifier": "Dark gray",
                            "label": "Dark gray"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "NET_SUSTAIN",
                    "values": [
                        {
                            "identifier": "Lower Impact Materials",
                            "label": "Lower Impact Materials"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "NET SUSTAIN"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "28",
                            "label": "28"
                        },
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/casual-jackets/draped-fringed-wool-blend-jacket/25185454456195123"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "1",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597319516090/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "VERSACE",
            "productId": "3074457345626771696",
            "modelId": "3074457345626771677",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Beige",
                    "visible": "True",
                    "productId": "3074457345626771696",
                    "labelEN": "Beige",
                    "label": "Beige",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "1011711_1A017181KA50",
                    "price": {
                        "sellingPrice": {
                            "amount": 448800,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 448800,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597319516090",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597319516090/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Icons belted double-breasted cotton-gabardine trench coat",
            "nameEN": "Icons belted double-breasted cotton-gabardine trench coat",
            "type": "ProductColour",
            "mfPartNumber": "1011711_1A017181KA50",
            "designerName": "VERSACE",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-80",
                        "labelEN": "Trench Coats",
                        "label": "Trench Coats",
                        "categoryId": "3074457345616677115"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 448800,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 448800,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597319516090",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Beige",
                            "label": "Beige"
                        },
                        {
                            "identifier": "Beige",
                            "label": "Beige"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "VERSACE",
                            "label": "VERSACE"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "VERSACE",
            "seo": {
                "seoURLKeyword": "/versace/clothing/trench-coats/icons-belted-double-breasted-cotton-gabardine-trench-coat/1647597319516090"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597332692840/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "SAINTLAURENT",
            "productId": "3074457345627521752",
            "modelId": "3074457345627521684",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Ivory",
                    "visible": "True",
                    "productId": "3074457345627521752",
                    "labelEN": "Ivory",
                    "label": "Ivory",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "778548Y3I859277",
                    "price": {
                        "sellingPrice": {
                            "amount": 446500,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 446500,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597332692840",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597332692840/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Double-breasted belted cotton and wool-blend tweed jacket",
            "nameEN": "Double-breasted belted cotton and wool-blend tweed jacket",
            "type": "ProductColour",
            "mfPartNumber": "778548Y3I859277",
            "designerName": "SAINT LAURENT",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 446500,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 446500,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597332692840",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Ivory",
                            "label": "Ivory"
                        },
                        {
                            "identifier": "Ivory",
                            "label": "Ivory"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "HS24",
                            "label": "HS24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "28",
                            "label": "28"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "SAINTLAURENT",
                            "label": "SAINT LAURENT"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power RTW",
                            "label": "Power RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "SAINT LAURENT",
            "seo": {
                "seoURLKeyword": "/saint-laurent/clothing/blazers/double-breasted-belted-cotton-and-wool-blend-tweed-jacket/1647597332692840"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "1",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597335069226/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "GOLDBERGH",
            "hasSiblings": "True",
            "productId": "3074457345627701671",
            "modelId": "3074457345627701669",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345627701671",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "GBS16-17-224.9000",
                    "badges": [
                        {
                            "label": "20% OFF AT CHECKOUT",
                            "type": "MERCHANDISING",
                            "key": "BADGE_FP_PROMO_AUTOAPPLY"
                        }
                    ],
                    "price": {
                        "sellingPrice": {
                            "amount": 115828,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 115900,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597335069226",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597335069226/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Hida faux fur-trimmed hooded ski jacket",
            "nameEN": "Hida faux fur-trimmed hooded ski jacket",
            "type": "ProductColour",
            "mfPartNumber": "GBS16-17-224.9000",
            "designerName": "GOLDBERGH",
            "badges": [
                {
                    "label": "20% OFF AT CHECKOUT",
                    "type": "MERCHANDISING",
                    "key": "BADGE_FP_PROMO_AUTOAPPLY"
                }
            ],
            "masterCategory": {
                "identifier": "NAP-1911",
                "labelEN": "Sport",
                "label": "Sport",
                "categoryId": "3074457345616676672",
                "child": {
                    "identifier": "NAP-1911-1919",
                    "labelEN": "Ski",
                    "label": "Ski",
                    "categoryId": "3074457345616676737",
                    "child": {
                        "identifier": "NAP-1911-1919-1940",
                        "labelEN": "Outerwear",
                        "label": "Outerwear",
                        "categoryId": "3074457345616677053"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 115828,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 115900,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597335069226",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "GOLDBERGH",
                            "label": "GOLDBERGH"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Casual and Denim",
                            "label": "Casual and Denim"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "GOLDBERGH",
            "seo": {
                "seoURLKeyword": "/goldbergh/sport/outerwear/hida-faux-fur-trimmed-hooded-ski-jacket/1647597335069226"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "9",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597339494969/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "TOTEME",
            "productId": "3074457345628050736",
            "modelId": "3074457345628050677",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345628050736",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "243-WRO3318-FB0187001",
                    "price": {
                        "sellingPrice": {
                            "amount": 159900,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 159900,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597339494969",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597339494969/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Belted twill coat",
            "nameEN": "Belted twill coat",
            "type": "ProductColour",
            "mfPartNumber": "243-WRO3318-FB0187001",
            "designerName": "TOTEME",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-16",
                    "labelEN": "Coats",
                    "label": "Coats",
                    "categoryId": "3074457345616676745",
                    "child": {
                        "identifier": "NAP-3-16-77",
                        "labelEN": "Long",
                        "label": "Long",
                        "categoryId": "3074457345616677113"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 159900,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 159900,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597339494969",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "FW24",
                            "label": "FW24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "28",
                            "label": "28"
                        },
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "TOTEME",
                            "label": "TOTEME"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "TOTEME",
            "seo": {
                "seoURLKeyword": "/toteme/clothing/long/belted-twill-coat/1647597339494969"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "5",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597336321688/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "ALAA",
            "productId": "3074457345627792220",
            "modelId": "3074457345627792182",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Blue",
                    "visible": "True",
                    "productId": "3074457345627792220",
                    "labelEN": "Blue",
                    "label": "Blue",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "AA9V03066T587508",
                    "price": {
                        "sellingPrice": {
                            "amount": 154400,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 154400,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "segmentBadges": [
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_PLATINUM"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_SILVER"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_EIP_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_EIP"
                        },
                        {
                            "badges": [
                                {
                                    "sequence": 0,
                                    "label": "20% OFF AT CHECKOUT",
                                    "key": "SEGMENTED_BADGE_LOYALTY_APPLIED_AT_CHECKOUT"
                                }
                            ],
                            "segmentName": "LOS_GOLD"
                        }
                    ],
                    "partNumber": "1647597336321688",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597336321688/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Cropped denim hooded jacket",
            "nameEN": "Cropped denim hooded jacket",
            "type": "ProductColour",
            "mfPartNumber": "AA9V03066T587508",
            "designerName": "ALAÏA",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-90",
                        "labelEN": "Casual Jackets",
                        "label": "Casual Jackets",
                        "categoryId": "3074457345616677126"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 154400,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 154400,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597336321688",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Blue",
                            "label": "Blue"
                        },
                        {
                            "identifier": "Blue",
                            "label": "Blue"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "FW24",
                            "label": "FW24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "28",
                            "label": "28"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "ALAA",
                            "label": "ALAÏA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Power Designer",
                            "label": "Power Designer"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "ALAÏA",
            "seo": {
                "seoURLKeyword": "/alaia/clothing/casual-jackets/cropped-denim-hooded-jacket/1647597336321688"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597333105831/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "LOROPIANA",
            "productId": "3074457345627561213",
            "modelId": "3074457345627561171",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Cream",
                    "visible": "True",
                    "productId": "3074457345627561213",
                    "labelEN": "Cream",
                    "label": "Cream",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "FAN6963A0EO",
                    "price": {
                        "sellingPrice": {
                            "amount": 574681,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 574700,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597333105831",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597333105831/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Double-breasted silk-dupioni blazer",
            "nameEN": "Double-breasted silk-dupioni blazer",
            "type": "ProductColour",
            "mfPartNumber": "FAN6963A0EO",
            "designerName": "LORO PIANA",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1379",
                        "labelEN": "Blazers",
                        "label": "Blazers",
                        "categoryId": "3074457345616677123"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 574681,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 574700,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597333105831",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Cream",
                            "label": "Cream"
                        },
                        {
                            "identifier": "Cream",
                            "label": "Cream"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "HS24",
                            "label": "HS24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "LOROPIANA",
                            "label": "LORO PIANA"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "LORO PIANA",
            "seo": {
                "seoURLKeyword": "/loro-piana/clothing/blazers/double-breasted-silk-dupioni-blazer/1647597333105831"
            }
        },
        {
            "buyable": "False",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597319516087/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "VERSACE",
            "productId": "3074457345626771702",
            "modelId": "3074457345626771684",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345626771702",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "1010545_1A101181B000",
                    "price": {
                        "sellingPrice": {
                            "amount": 744400,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 744400,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597319516087",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597319516087/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Icons belted leather biker jacket",
            "nameEN": "Icons belted leather biker jacket",
            "type": "ProductColour",
            "mfPartNumber": "1010545_1A101181B000",
            "designerName": "VERSACE",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1370",
                        "labelEN": "Biker Jackets",
                        "label": "Biker Jackets",
                        "categoryId": "3074457345616677121"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 744400,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 744400,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597319516087",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "CR25",
                            "label": "CR25"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "50",
                            "label": "50"
                        },
                        {
                            "identifier": "52",
                            "label": "52"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "VERSACE",
                            "label": "VERSACE"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Luxury RTW",
                            "label": "Luxury RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "VERSACE",
            "seo": {
                "seoURLKeyword": "/versace/clothing/biker-jackets/icons-belted-leather-biker-jacket/1647597319516087"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "2",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597299243976/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "LULULEMON",
            "hasSiblings": "True",
            "productId": "3074457345625542683",
            "modelId": "3074457345628817181",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Black",
                    "visible": "True",
                    "productId": "3074457345625542683",
                    "labelEN": "Black",
                    "label": "Black",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "LW3GQ6S-0001Black",
                    "price": {
                        "sellingPrice": {
                            "amount": 16600,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 16600,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597299243976",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597299243976/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Define Luon® jacket",
            "nameEN": "Define Luon® jacket",
            "type": "ProductColour",
            "mfPartNumber": "LW3GQ6S-0001Black",
            "designerName": "LULULEMON",
            "masterCategory": {
                "identifier": "NAP-1911",
                "labelEN": "Sport",
                "label": "Sport",
                "categoryId": "3074457345616676672",
                "child": {
                    "identifier": "NAP-1911-1912",
                    "labelEN": "Après Sport",
                    "label": "Après Sport",
                    "categoryId": "3074457345616676730",
                    "child": {
                        "identifier": "NAP-1911-1912-1949",
                        "labelEN": "Jackets",
                        "label": "Jackets",
                        "categoryId": "3074457345616676982"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 16600,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 16600,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "name": "Define paneled Luon jacket",
            "partNumber": "1647597299243976",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Black",
                            "label": "Black"
                        },
                        {
                            "identifier": "Black",
                            "label": "Black"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "Continuity",
                            "label": "Continuity"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "00",
                            "label": "00"
                        },
                        {
                            "identifier": "0",
                            "label": "0"
                        },
                        {
                            "identifier": "2",
                            "label": "2"
                        },
                        {
                            "identifier": "4",
                            "label": "4"
                        },
                        {
                            "identifier": "6",
                            "label": "6"
                        },
                        {
                            "identifier": "8",
                            "label": "8"
                        },
                        {
                            "identifier": "10",
                            "label": "10"
                        },
                        {
                            "identifier": "12",
                            "label": "12"
                        },
                        {
                            "identifier": "14",
                            "label": "14"
                        },
                        {
                            "identifier": "16",
                            "label": "16"
                        },
                        {
                            "identifier": "18",
                            "label": "18"
                        },
                        {
                            "identifier": "20",
                            "label": "20"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "LULULEMON",
                            "label": "LULULEMON"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Casual and Denim",
                            "label": "Casual and Denim"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "LULULEMON",
            "seo": {
                "seoURLKeyword": "/lululemon/sport/jackets/define-luonr-jacket/1647597299243976"
            }
        },
        {
            "buyable": "False",
            "inv_local_94074": "1",
            "thumbnail": "/wcsstore/NAPCAS/variants/images/1647597337088737/in/w1000.jpg",
            "visible": "True",
            "designerIdentifier": "JILSANDER",
            "productId": "3074457345627867227",
            "modelId": "3074457345627867195",
            "productColours": [
                {
                    "buyable": "False",
                    "identifier": "Neutral",
                    "visible": "True",
                    "productId": "3074457345627867227",
                    "labelEN": "Neutral",
                    "label": "Neutral",
                    "type": "ProductColour",
                    "imageViews": [
                        "in",
                        "ou"
                    ],
                    "mfPartNumber": "J01FB0102110",
                    "price": {
                        "sellingPrice": {
                            "amount": 478200,
                            "divisor": 100
                        },
                        "rdSellingPrice": {
                            "amount": 478200,
                            "divisor": 100
                        },
                        "currency": {
                            "symbol": "$",
                            "label": "USD"
                        }
                    },
                    "partNumber": "1647597337088737",
                    "selected": "True",
                    "imageTemplate": "//www.net-a-porter.com/variants/images/1647597337088737/{view}/w{width}.jpg"
                }
            ],
            "shortDescription": "Belted woven vest",
            "nameEN": "Belted woven vest",
            "type": "ProductColour",
            "mfPartNumber": "J01FB0102110",
            "designerName": "JIL SANDER",
            "masterCategory": {
                "identifier": "NAP-3",
                "labelEN": "Clothing",
                "label": "Clothing",
                "categoryId": "3074457345616676673",
                "child": {
                    "identifier": "NAP-3-19",
                    "labelEN": "Jackets",
                    "label": "Jackets",
                    "categoryId": "3074457345616676747",
                    "child": {
                        "identifier": "NAP-3-19-1371",
                        "labelEN": "Vests and Gilets",
                        "label": "Vests and Gilets",
                        "categoryId": "3074457345616677122"
                    }
                }
            },
            "price": {
                "sellingPrice": {
                    "amount": 478200,
                    "divisor": 100
                },
                "rdSellingPrice": {
                    "amount": 478200,
                    "divisor": 100
                },
                "currency": {
                    "symbol": "$",
                    "label": "USD"
                }
            },
            "partNumber": "1647597337088737",
            "dynamic": "False",
            "attributes": [
                {
                    "identifier": "Brand Colour",
                    "values": [
                        {
                            "identifier": "Neutral",
                            "label": "Neutral"
                        },
                        {
                            "identifier": "Neutral",
                            "label": "Neutral"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Colour"
                },
                {
                    "identifier": "Sale Season",
                    "values": [
                        {
                            "identifier": "HS24",
                            "label": "HS24"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Sale Season"
                },
                {
                    "identifier": "Brand Size",
                    "values": [
                        {
                            "identifier": "30",
                            "label": "30"
                        },
                        {
                            "identifier": "32",
                            "label": "32"
                        },
                        {
                            "identifier": "34",
                            "label": "34"
                        },
                        {
                            "identifier": "36",
                            "label": "36"
                        },
                        {
                            "identifier": "38",
                            "label": "38"
                        },
                        {
                            "identifier": "40",
                            "label": "40"
                        },
                        {
                            "identifier": "42",
                            "label": "42"
                        },
                        {
                            "identifier": "44",
                            "label": "44"
                        },
                        {
                            "identifier": "46",
                            "label": "46"
                        },
                        {
                            "identifier": "48",
                            "label": "48"
                        },
                        {
                            "identifier": "28",
                            "label": "28"
                        }
                    ],
                    "usage": "Defining",
                    "label": "Brand Size"
                },
                {
                    "identifier": "Brand",
                    "values": [
                        {
                            "identifier": "JILSANDER",
                            "label": "JIL SANDER"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Designer"
                },
                {
                    "identifier": "Department",
                    "values": [
                        {
                            "identifier": "Designer Studio RTW",
                            "label": "Designer Studio RTW"
                        }
                    ],
                    "usage": "Descriptive",
                    "label": "Department"
                }
            ],
            "designerNameEN": "JIL SANDER",
            "seo": {
                "seoURLKeyword": "/jil-sander/clothing/vests-and-gilets/belted-woven-vest/1647597337088737"
            }
        }
    ],
    "facets": [
        {
            "entry": [
                {
                    "identifier": "APAC__Clothing",
                    "children": [
                        {
                            "identifier": "APAC__Coats_And_Jackets_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Belted_Coats_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 139,
                                    "count": 139,
                                    "label": "Belted Coats",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/belted-coats"
                                    },
                                    "categoryId": "3074457345616748276"
                                },
                                {
                                    "identifier": "APAC__Blazers_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 296,
                                    "count": 296,
                                    "label": "Blazers",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/blazers"
                                    },
                                    "categoryId": "3074457345616748275"
                                },
                                {
                                    "identifier": "APAC__Bomber_And_Track_Jackets_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 76,
                                    "count": 76,
                                    "label": "Bomber And Track Jackets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/bomber-and-track-jackets"
                                    },
                                    "categoryId": "3074457345616756330"
                                },
                                {
                                    "identifier": "APAC__Capes_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 26,
                                    "count": 26,
                                    "label": "Capes",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/capes"
                                    },
                                    "categoryId": "3074457345616756326"
                                },
                                {
                                    "identifier": "APAC__Casual_Jackets_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 482,
                                    "count": 482,
                                    "label": "Casual Jackets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/casual-jackets"
                                    },
                                    "categoryId": "3074457345616758171"
                                },
                                {
                                    "identifier": "APAC__Denim_Jackets_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 77,
                                    "count": 77,
                                    "label": "Denim Jackets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/denim-jackets"
                                    },
                                    "categoryId": "3074457345616748272"
                                },
                                {
                                    "identifier": "APAC__Faux_Fur_And_Shearling_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 97,
                                    "count": 97,
                                    "label": "Faux Fur And Shearling",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/faux-fur-and-shearling"
                                    },
                                    "categoryId": "3074457345616756335"
                                },
                                {
                                    "identifier": "APAC__Leather_Jackets_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 116,
                                    "count": 116,
                                    "label": "Leather Jackets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/leather-jackets"
                                    },
                                    "categoryId": "3074457345616756307"
                                },
                                {
                                    "identifier": "APAC__Long_Coats_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 128,
                                    "count": 128,
                                    "label": "Long Coats",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/long-coats"
                                    },
                                    "categoryId": "3074457345616758174"
                                },
                                {
                                    "identifier": "APAC__Quilted_And_Puffer_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 339,
                                    "count": 339,
                                    "label": "Quilted And Puffer",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/quilted-and-puffer"
                                    },
                                    "categoryId": "3074457345616756338"
                                },
                                {
                                    "identifier": "APAC__Shirt_And_Utility_Jackets_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 114,
                                    "count": 114,
                                    "label": "Shirt And Utility Jackets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/shirt-and-utility-jackets"
                                    },
                                    "categoryId": "3074457345616756310"
                                },
                                {
                                    "identifier": "APAC__Sportswear_Jackets_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 197,
                                    "count": 197,
                                    "label": "Sportswear Jackets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/sportswear-jackets"
                                    },
                                    "categoryId": "3074457345616751218"
                                },
                                {
                                    "identifier": "APAC__Trench_Coats_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 59,
                                    "count": 59,
                                    "label": "Trench Coats",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/trench-coats"
                                    },
                                    "categoryId": "3074457345616756343"
                                },
                                {
                                    "identifier": "APAC__Vests_And_Gilets_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 76,
                                    "count": 76,
                                    "label": "Vests And Gilets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/vests-and-gilets"
                                    },
                                    "categoryId": "3074457345616756346"
                                },
                                {
                                    "identifier": "APAC__Wool_Coats_COATS_AND_JACKETS_CLOTHING",
                                    "numberOfVisibleProducts": 362,
                                    "count": 362,
                                    "label": "Wool Coats",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/coats-and-jackets/wool-coats"
                                    },
                                    "categoryId": "3074457345616749274"
                                }
                            ],
                            "numberOfVisibleProducts": 1364,
                            "count": 1364,
                            "label": "Coats and Jackets",
                            "seo": {
                                "seoURLKeyword": "/clothing/coats-and-jackets"
                            },
                            "categoryId": "3074457345616748262",
                            "selected": "True"
                        },
                        {
                            "identifier": "APAC__Denim_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Dresses_Denim_CLOTHING",
                                    "numberOfVisibleProducts": 26,
                                    "count": 26,
                                    "label": "Denim Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/denim/denim-dresses"
                                    },
                                    "categoryId": "3074457345616747237"
                                },
                                {
                                    "identifier": "APAC__Jackets_DENIM",
                                    "numberOfVisibleProducts": 77,
                                    "count": 77,
                                    "label": "Denim Jackets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/denim/denim-jackets"
                                    },
                                    "categoryId": "3074457345616747242"
                                },
                                {
                                    "identifier": "APAC__Jumpsuits_and_Playsuits_DENIM",
                                    "numberOfVisibleProducts": 10,
                                    "count": 10,
                                    "label": "Denim Jumpsuits and Playsuits",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/denim/denim-jumpsuits-and-playsuits"
                                    },
                                    "categoryId": "3074457345616747238"
                                },
                                {
                                    "identifier": "APAC__Denim_Pants_DENIM",
                                    "numberOfVisibleProducts": 530,
                                    "count": 530,
                                    "label": "Denim Pants",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/denim/denim-pants"
                                    },
                                    "categoryId": "3074457345616747239"
                                },
                                {
                                    "identifier": "APAC__Shorts_DENIM",
                                    "numberOfVisibleProducts": 25,
                                    "count": 25,
                                    "label": "Denim Shorts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/denim/denim-shorts"
                                    },
                                    "categoryId": "3074457345616747243"
                                },
                                {
                                    "identifier": "APAC__Skirts_DENIM",
                                    "numberOfVisibleProducts": 43,
                                    "count": 43,
                                    "label": "Denim Skirts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/denim/denim-skirts"
                                    },
                                    "categoryId": "3074457345616747240"
                                },
                                {
                                    "identifier": "APAC__Tops_DENIM",
                                    "numberOfVisibleProducts": 28,
                                    "count": 28,
                                    "label": "Denim Tops",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/denim/denim-tops"
                                    },
                                    "categoryId": "3074457345616747241"
                                }
                            ],
                            "numberOfVisibleProducts": 739,
                            "count": 739,
                            "label": "Denim",
                            "seo": {
                                "seoURLKeyword": "/clothing/denim"
                            },
                            "categoryId": "3074457345616747236"
                        },
                        {
                            "identifier": "APAC__Dresses_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Beach_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 112,
                                    "count": 112,
                                    "label": "Beach Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/beach-dresses"
                                    },
                                    "categoryId": "3074457345616750676"
                                },
                                {
                                    "identifier": "APAC__Bridal_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 74,
                                    "count": 74,
                                    "label": "Bridal Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/bridal-dresses"
                                    },
                                    "categoryId": "3074457345616750677"
                                },
                                {
                                    "identifier": "APAC__Day_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 664,
                                    "count": 664,
                                    "label": "Day Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/day-dresses"
                                    },
                                    "categoryId": "3074457345616750678"
                                },
                                {
                                    "identifier": "APAC__Embellished_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 339,
                                    "count": 339,
                                    "label": "Embellished Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/embellished-dresses"
                                    },
                                    "categoryId": "3074457345616750679"
                                },
                                {
                                    "identifier": "APAC__Evening_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 389,
                                    "count": 389,
                                    "label": "Evening Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/evening-dresses"
                                    },
                                    "categoryId": "3074457345616750681"
                                },
                                {
                                    "identifier": "APAC__Floral_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 217,
                                    "count": 217,
                                    "label": "Floral Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/floral-dresses"
                                    },
                                    "categoryId": "3074457345616750680"
                                },
                                {
                                    "identifier": "APAC__Gowns_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 314,
                                    "count": 314,
                                    "label": "Gowns",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/gowns"
                                    },
                                    "categoryId": "3074457345616690906"
                                },
                                {
                                    "identifier": "APAC__Kaftan_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 51,
                                    "count": 51,
                                    "label": "Kaftan Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/kaftan-dresses"
                                    },
                                    "categoryId": "3074457345616750682"
                                },
                                {
                                    "identifier": "APAC__Knit_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 264,
                                    "count": 264,
                                    "label": "Knit Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/knit-dresses"
                                    },
                                    "categoryId": "3074457345616750683"
                                },
                                {
                                    "identifier": "APAC__Maxi_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 451,
                                    "count": 451,
                                    "label": "Maxi Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/maxi-dresses"
                                    },
                                    "categoryId": "3074457345616690908"
                                },
                                {
                                    "identifier": "APAC__Midi_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 755,
                                    "count": 755,
                                    "label": "Midi Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/midi-dresses"
                                    },
                                    "categoryId": "3074457345616690910"
                                },
                                {
                                    "identifier": "APAC__Mini_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 482,
                                    "count": 482,
                                    "label": "Mini Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/mini-dresses"
                                    },
                                    "categoryId": "3074457345616690909"
                                },
                                {
                                    "identifier": "APAC__Modest_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 61,
                                    "count": 61,
                                    "label": "Modest Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/modest-dresses"
                                    },
                                    "categoryId": "3074457345616750684"
                                },
                                {
                                    "identifier": "APAC__Off_The_Shoulder_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 153,
                                    "count": 153,
                                    "label": "Off The Shoulder Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/off-the-shoulder-dresses"
                                    },
                                    "categoryId": "3074457345616750685"
                                },
                                {
                                    "identifier": "APAC__Party_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 525,
                                    "count": 525,
                                    "label": "Party Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/party-dresses"
                                    },
                                    "categoryId": "3074457345616750687"
                                },
                                {
                                    "identifier": "APAC__Shirt_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 140,
                                    "count": 140,
                                    "label": "Shirt Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/shirt-dresses"
                                    },
                                    "categoryId": "3074457345616750688"
                                },
                                {
                                    "identifier": "APAC__Slip_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 52,
                                    "count": 52,
                                    "label": "Slip Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/slip-dresses"
                                    },
                                    "categoryId": "3074457345616750690"
                                },
                                {
                                    "identifier": "APAC__Sun_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 233,
                                    "count": 233,
                                    "label": "Sun Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/sun-dresses"
                                    },
                                    "categoryId": "3074457345616750691"
                                },
                                {
                                    "identifier": "APAC__Wrap_Dresses_DRESSES_CLOTHING",
                                    "numberOfVisibleProducts": 45,
                                    "count": 45,
                                    "label": "Wrap Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/dresses/wrap-dresses"
                                    },
                                    "categoryId": "3074457345616750692"
                                }
                            ],
                            "numberOfVisibleProducts": 2042,
                            "count": 2042,
                            "label": "Dresses",
                            "seo": {
                                "seoURLKeyword": "/clothing/dresses"
                            },
                            "categoryId": "3074457345616690897"
                        },
                        {
                            "identifier": "APAC__Jeans_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Boyfriend_JEANS_CLOTHING",
                                    "numberOfVisibleProducts": 20,
                                    "count": 20,
                                    "label": "Boyfriend",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/jeans/boyfriend"
                                    },
                                    "categoryId": "3074457345616690916"
                                },
                                {
                                    "identifier": "APAC__Flared_JEANS_CLOTHING",
                                    "numberOfVisibleProducts": 59,
                                    "count": 59,
                                    "label": "Flared",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/jeans/flared"
                                    },
                                    "categoryId": "3074457345616690915"
                                },
                                {
                                    "identifier": "APAC__Skinny_Leg_JEANS_CLOTHING",
                                    "numberOfVisibleProducts": 14,
                                    "count": 14,
                                    "label": "Skinny Leg",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/jeans/skinny-leg"
                                    },
                                    "categoryId": "3074457345616690913"
                                },
                                {
                                    "identifier": "APAC__Slim_Leg_JEANS_CLOTHING",
                                    "numberOfVisibleProducts": 22,
                                    "count": 22,
                                    "label": "Slim Leg",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/jeans/slim-leg"
                                    },
                                    "categoryId": "3074457345616690912"
                                },
                                {
                                    "identifier": "APAC__Straight_Leg_JEANS_CLOTHING",
                                    "numberOfVisibleProducts": 214,
                                    "count": 214,
                                    "label": "Straight Leg",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/jeans/straight-leg"
                                    },
                                    "categoryId": "3074457345616690914"
                                },
                                {
                                    "identifier": "APAC__Tapered_JEANS_CLOTHING",
                                    "numberOfVisibleProducts": 17,
                                    "count": 17,
                                    "label": "Tapered",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/jeans/tapered"
                                    },
                                    "categoryId": "3074457345616706168"
                                },
                                {
                                    "identifier": "APAC__Wide_Leg_JEANS_CLOTHING",
                                    "numberOfVisibleProducts": 213,
                                    "count": 213,
                                    "label": "Wide Leg",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/jeans/wide-leg"
                                    },
                                    "categoryId": "3074457345616690911"
                                }
                            ],
                            "numberOfVisibleProducts": 529,
                            "count": 529,
                            "label": "Jeans",
                            "seo": {
                                "seoURLKeyword": "/clothing/jeans"
                            },
                            "categoryId": "3074457345616690899"
                        },
                        {
                            "identifier": "APAC__Jumpsuits_And_Playsuits_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Jumpsuits_JUMPSUITS_AND_PLAYSUITS_CLOTHING",
                                    "numberOfVisibleProducts": 96,
                                    "count": 96,
                                    "label": "Jumpsuits",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/jumpsuits-and-playsuits/jumpsuits"
                                    },
                                    "categoryId": "3074457345616690918"
                                },
                                {
                                    "identifier": "APAC__Playsuits_JUMPSUITS_AND_PLAYSUITS_CLOTHING",
                                    "numberOfVisibleProducts": 12,
                                    "count": 12,
                                    "label": "Playsuits",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/jumpsuits-and-playsuits/playsuits"
                                    },
                                    "categoryId": "3074457345616690917"
                                }
                            ],
                            "numberOfVisibleProducts": 106,
                            "count": 106,
                            "label": "Jumpsuits and Playsuits",
                            "seo": {
                                "seoURLKeyword": "/clothing/jumpsuits-and-playsuits"
                            },
                            "categoryId": "3074457345616690893"
                        },
                        {
                            "identifier": "APAC__Knitwear_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Cardigan_KNITWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 396,
                                    "count": 396,
                                    "label": "Cardigan",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/knitwear/cardigan"
                                    },
                                    "categoryId": "3074457345616690920"
                                },
                                {
                                    "identifier": "APAC__Cashmere_KNITWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 686,
                                    "count": 686,
                                    "label": "Cashmere",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/knitwear/cashmere"
                                    },
                                    "categoryId": "3074457345616756191"
                                },
                                {
                                    "identifier": "APAC__Polo_KNITWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 143,
                                    "count": 143,
                                    "label": "Polo",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/knitwear/knit-polo"
                                    },
                                    "categoryId": "3074457345616756192"
                                },
                                {
                                    "identifier": "APAC__Sweater_KNITWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 873,
                                    "count": 873,
                                    "label": "Sweater",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/knitwear/sweater"
                                    },
                                    "categoryId": "3074457345616690919"
                                },
                                {
                                    "identifier": "APAC__Turtleneck_KNITWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 236,
                                    "count": 236,
                                    "label": "Turtleneck",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/knitwear/turtleneck"
                                    },
                                    "categoryId": "3074457345616756193"
                                },
                                {
                                    "identifier": "APAC__Vest_KNITWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 55,
                                    "count": 55,
                                    "label": "Vest",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/knitwear/knit-vest"
                                    },
                                    "categoryId": "3074457345616756194"
                                }
                            ],
                            "numberOfVisibleProducts": 1364,
                            "count": 1364,
                            "label": "Knitwear",
                            "seo": {
                                "seoURLKeyword": "/clothing/knitwear"
                            },
                            "categoryId": "3074457345616690894"
                        },
                        {
                            "identifier": "APAC__Lingerie",
                            "children": [
                                {
                                    "identifier": "APAC__Bodysuits_LINGERIE",
                                    "numberOfVisibleProducts": 40,
                                    "count": 40,
                                    "label": "Bodysuits",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/bodysuits"
                                    },
                                    "categoryId": "3074457345616690999"
                                },
                                {
                                    "identifier": "APAC__Bras_LINGERIE",
                                    "numberOfVisibleProducts": 154,
                                    "count": 154,
                                    "label": "Bras",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/bras"
                                    },
                                    "categoryId": "3074457345616691002"
                                },
                                {
                                    "identifier": "APAC__Briefs_LINGERIE",
                                    "children": [
                                        {
                                            "identifier": "APAC__Briefs_BRIEFS_LINGERIE",
                                            "numberOfVisibleProducts": 50,
                                            "count": 50,
                                            "label": "Briefs",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/briefs/briefs"
                                            },
                                            "categoryId": "3074457345616691004"
                                        },
                                        {
                                            "identifier": "APAC__Thongs_BRIEFS_LINGERIE",
                                            "numberOfVisibleProducts": 38,
                                            "count": 38,
                                            "label": "Thongs",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/briefs/thongs"
                                            },
                                            "categoryId": "3074457345616691005"
                                        }
                                    ],
                                    "numberOfVisibleProducts": 88,
                                    "count": 88,
                                    "label": "Briefs",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/briefs"
                                    },
                                    "categoryId": "3074457345616690995"
                                },
                                {
                                    "identifier": "APAC__Camisoles_And_Chemises_LINGERIE",
                                    "children": [
                                        {
                                            "identifier": "APAC__Camisoles_CAMISOLES_AND_CHEMISES_LINGERIE",
                                            "numberOfVisibleProducts": 5,
                                            "count": 5,
                                            "label": "Camisoles",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/camisoles-and-chemises/camisoles"
                                            },
                                            "categoryId": "3074457345616691006"
                                        },
                                        {
                                            "identifier": "APAC__Chemises_CAMISOLES_AND_CHEMISES_LINGERIE",
                                            "numberOfVisibleProducts": 4,
                                            "count": 4,
                                            "label": "Chemises",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/camisoles-and-chemises/chemises"
                                            },
                                            "categoryId": "3074457345616691007"
                                        },
                                        {
                                            "identifier": "APAC__Slips_CAMISOLES_AND_CHEMISES_LINGERIE",
                                            "numberOfVisibleProducts": 1,
                                            "count": 1,
                                            "label": "Slips",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/camisoles-and-chemises/slips"
                                            },
                                            "categoryId": "3074457345616691008"
                                        }
                                    ],
                                    "numberOfVisibleProducts": 10,
                                    "count": 10,
                                    "label": "Camisoles and Chemises",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/camisoles-and-chemises"
                                    },
                                    "categoryId": "3074457345616690996"
                                },
                                {
                                    "identifier": "APAC__Hosiery_LINGERIE",
                                    "children": [
                                        {
                                            "identifier": "APAC__Socks_HOSIERY_LINGERIE",
                                            "numberOfVisibleProducts": 33,
                                            "count": 33,
                                            "label": "Socks",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/hosiery/socks"
                                            },
                                            "categoryId": "3074457345616691009"
                                        },
                                        {
                                            "identifier": "APAC__Stockings_HOSIERY_LINGERIE",
                                            "numberOfVisibleProducts": 3,
                                            "count": 3,
                                            "label": "Stockings",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/hosiery/stockings"
                                            },
                                            "categoryId": "3074457345616691010"
                                        },
                                        {
                                            "identifier": "APAC__Tights_HOSIERY_LINGERIE",
                                            "numberOfVisibleProducts": 16,
                                            "count": 16,
                                            "label": "Tights",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/hosiery/tights"
                                            },
                                            "categoryId": "3074457345616691011"
                                        }
                                    ],
                                    "numberOfVisibleProducts": 52,
                                    "count": 52,
                                    "label": "Hosiery",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/hosiery"
                                    },
                                    "categoryId": "3074457345616690997"
                                },
                                {
                                    "identifier": "APAC__Lingerie_Accessories_LINGERIE",
                                    "numberOfVisibleProducts": 3,
                                    "count": 3,
                                    "label": "Lingerie Accessories",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/lingerie-accessories"
                                    },
                                    "categoryId": "3074457345616691003"
                                },
                                {
                                    "identifier": "APAC__Matching_Separates_LINGERIE",
                                    "numberOfVisibleProducts": 77,
                                    "count": 77,
                                    "label": "Matching Separates",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/matching-separates"
                                    },
                                    "categoryId": "3074457345616701279"
                                },
                                {
                                    "identifier": "APAC__Robes_LINGERIE",
                                    "numberOfVisibleProducts": 29,
                                    "count": 29,
                                    "label": "Robes",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/robes"
                                    },
                                    "categoryId": "3074457345616691001"
                                },
                                {
                                    "identifier": "APAC__Shapewear_LINGERIE",
                                    "numberOfVisibleProducts": 106,
                                    "count": 106,
                                    "label": "Shapewear",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/shapewear"
                                    },
                                    "categoryId": "3074457345616691000"
                                },
                                {
                                    "identifier": "APAC__Sleepwear_LINGERIE",
                                    "children": [
                                        {
                                            "identifier": "APAC__Nightdresses_SLEEPWEAR_LINGERIE",
                                            "numberOfVisibleProducts": 20,
                                            "count": 20,
                                            "label": "Nightdresses",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/sleepwear/nightdresses"
                                            },
                                            "categoryId": "3074457345616691012"
                                        },
                                        {
                                            "identifier": "APAC__Pajamas_SLEEPWEAR_LINGERIE",
                                            "numberOfVisibleProducts": 59,
                                            "count": 59,
                                            "label": "Pajamas",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/lingerie/sleepwear/pajamas"
                                            },
                                            "categoryId": "3074457345616691013"
                                        }
                                    ],
                                    "numberOfVisibleProducts": 79,
                                    "count": 79,
                                    "label": "Sleepwear",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/lingerie/sleepwear"
                                    },
                                    "categoryId": "3074457345616690998"
                                }
                            ],
                            "numberOfVisibleProducts": 561,
                            "count": 561,
                            "label": "Lingerie",
                            "seo": {
                                "seoURLKeyword": "/clothing/lingerie"
                            },
                            "categoryId": "3074457345616690681"
                        },
                        {
                            "identifier": "APAC__Loungewear_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Bottoms_LOUNGEWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 168,
                                    "count": 168,
                                    "label": "Bottoms",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/loungewear/bottoms"
                                    },
                                    "categoryId": "3074457345616690925"
                                },
                                {
                                    "identifier": "APAC__Dresses_LOUNGEWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 8,
                                    "count": 8,
                                    "label": "Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/loungewear/dresses"
                                    },
                                    "categoryId": "3074457345616690921"
                                },
                                {
                                    "identifier": "APAC__Knitwear_LOUNGEWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 21,
                                    "count": 21,
                                    "label": "Knitwear",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/loungewear/knitwear"
                                    },
                                    "categoryId": "3074457345616690926"
                                },
                                {
                                    "identifier": "APAC__Sets_LOUNGEWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 19,
                                    "count": 19,
                                    "label": "Sets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/loungewear/sets"
                                    },
                                    "categoryId": "3074457345616690923"
                                },
                                {
                                    "identifier": "APAC__Tops_LOUNGEWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 128,
                                    "count": 128,
                                    "label": "Tops",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/loungewear/tops"
                                    },
                                    "categoryId": "3074457345616690922"
                                }
                            ],
                            "numberOfVisibleProducts": 337,
                            "count": 337,
                            "label": "Loungewear",
                            "seo": {
                                "seoURLKeyword": "/clothing/loungewear"
                            },
                            "categoryId": "3074457345616690891"
                        },
                        {
                            "identifier": "APAC__Matching_Separates__CLOTHING",
                            "numberOfVisibleProducts": 1297,
                            "count": 1297,
                            "label": "Matching Separates",
                            "seo": {
                                "seoURLKeyword": "/clothing/matching-separates"
                            },
                            "categoryId": "3074457345616701003"
                        },
                        {
                            "identifier": "APAC__Trousers_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Flared_TROUSERS_CLOTHING",
                                    "numberOfVisibleProducts": 115,
                                    "count": 115,
                                    "label": "Flared",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/pants/flared"
                                    },
                                    "categoryId": "3074457345616690961"
                                },
                                {
                                    "identifier": "APAC__Leggings_TROUSERS_CLOTHING",
                                    "numberOfVisibleProducts": 81,
                                    "count": 81,
                                    "label": "Leggings",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/pants/leggings"
                                    },
                                    "categoryId": "3074457345616690964"
                                },
                                {
                                    "identifier": "APAC__Skinny_Leg_TROUSERS_CLOTHING",
                                    "numberOfVisibleProducts": 20,
                                    "count": 20,
                                    "label": "Skinny Leg",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/pants/skinny-leg"
                                    },
                                    "categoryId": "3074457345616690966"
                                },
                                {
                                    "identifier": "APAC__Straight_Leg_TROUSERS_CLOTHING",
                                    "numberOfVisibleProducts": 289,
                                    "count": 289,
                                    "label": "Straight Leg",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/pants/straight-leg"
                                    },
                                    "categoryId": "3074457345616690963"
                                },
                                {
                                    "identifier": "APAC__Tapered_TROUSERS_CLOTHING",
                                    "numberOfVisibleProducts": 56,
                                    "count": 56,
                                    "label": "Tapered",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/pants/tapered"
                                    },
                                    "categoryId": "3074457345616690965"
                                },
                                {
                                    "identifier": "APAC__Track_Pants_TROUSERS_CLOTHING",
                                    "numberOfVisibleProducts": 134,
                                    "count": 134,
                                    "label": "Track Pants",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/pants/track-pants"
                                    },
                                    "categoryId": "3074457345616690962"
                                },
                                {
                                    "identifier": "APAC__Wide_Leg_TROUSERS_CLOTHING",
                                    "numberOfVisibleProducts": 359,
                                    "count": 359,
                                    "label": "Wide Leg",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/pants/wide-leg"
                                    },
                                    "categoryId": "3074457345616690960"
                                }
                            ],
                            "numberOfVisibleProducts": 1028,
                            "count": 1028,
                            "label": "Pants",
                            "seo": {
                                "seoURLKeyword": "/clothing/pants"
                            },
                            "categoryId": "3074457345616690892"
                        },
                        {
                            "identifier": "APAC__Shorts_CLOTHING",
                            "numberOfVisibleProducts": 174,
                            "count": 174,
                            "label": "Shorts",
                            "seo": {
                                "seoURLKeyword": "/clothing/shorts"
                            },
                            "categoryId": "3074457345616690903"
                        },
                        {
                            "identifier": "APAC__Skirts_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Knee_Length_Skirts_SKIRTS_CLOTHING",
                                    "numberOfVisibleProducts": 44,
                                    "count": 44,
                                    "label": "Knee Length Skirts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/skirts/knee-length-skirts"
                                    },
                                    "categoryId": "3074457345616690935"
                                },
                                {
                                    "identifier": "APAC__Maxi_Skirts_SKIRTS_CLOTHING",
                                    "numberOfVisibleProducts": 113,
                                    "count": 113,
                                    "label": "Maxi Skirts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/skirts/maxi-skirts"
                                    },
                                    "categoryId": "3074457345616690936"
                                },
                                {
                                    "identifier": "APAC__Midi_Skirts_SKIRTS_CLOTHING",
                                    "numberOfVisibleProducts": 269,
                                    "count": 269,
                                    "label": "Midi Skirts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/skirts/midi-skirts"
                                    },
                                    "categoryId": "3074457345616690937"
                                },
                                {
                                    "identifier": "APAC__Mini_Skirts_SKIRTS_CLOTHING",
                                    "numberOfVisibleProducts": 167,
                                    "count": 167,
                                    "label": "Mini Skirts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/skirts/mini-skirts"
                                    },
                                    "categoryId": "3074457345616690938"
                                }
                            ],
                            "numberOfVisibleProducts": 582,
                            "count": 582,
                            "label": "Skirts",
                            "seo": {
                                "seoURLKeyword": "/clothing/skirts"
                            },
                            "categoryId": "3074457345616690898"
                        },
                        {
                            "identifier": "APAC__Sport",
                            "children": [
                                {
                                    "identifier": "APAC__Dresses_SPORT",
                                    "numberOfVisibleProducts": 3,
                                    "count": 3,
                                    "label": "Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/dresses"
                                    },
                                    "categoryId": "3074457345616691080"
                                },
                                {
                                    "identifier": "APAC__Knitwear_SPORT",
                                    "numberOfVisibleProducts": 64,
                                    "count": 64,
                                    "label": "Knitwear",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/knitwear"
                                    },
                                    "categoryId": "3074457345616691087"
                                },
                                {
                                    "identifier": "APAC__Leggings_SPORT",
                                    "numberOfVisibleProducts": 45,
                                    "count": 45,
                                    "label": "Leggings",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/leggings"
                                    },
                                    "categoryId": "3074457345616691082"
                                },
                                {
                                    "identifier": "APAC__One-Piece_SPORT",
                                    "children": [
                                        {
                                            "identifier": "APAC__Bodysuits_And_Leotards_ONE-PIECE_SPORT",
                                            "numberOfVisibleProducts": 2,
                                            "count": 2,
                                            "label": "Bodysuits and Leotards",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/one-piece/bodysuits-and-leotards"
                                            },
                                            "categoryId": "3074457345616691088"
                                        },
                                        {
                                            "identifier": "APAC__Jumpsuits_ONE-PIECE_SPORT",
                                            "numberOfVisibleProducts": 2,
                                            "count": 2,
                                            "label": "Jumpsuits",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/one-piece/jumpsuits"
                                            },
                                            "categoryId": "3074457345616691089"
                                        },
                                        {
                                            "identifier": "APAC__Ski_Suits_ONE-PIECE_SPORT",
                                            "numberOfVisibleProducts": 33,
                                            "count": 33,
                                            "label": "Ski Suits",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/one-piece/ski-suits"
                                            },
                                            "categoryId": "3074457345616691090"
                                        }
                                    ],
                                    "numberOfVisibleProducts": 37,
                                    "count": 37,
                                    "label": "One-Piece",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/one-piece"
                                    },
                                    "categoryId": "3074457345616691076"
                                },
                                {
                                    "identifier": "APAC__Outerwear_SPORT",
                                    "numberOfVisibleProducts": 160,
                                    "count": 160,
                                    "label": "Outerwear",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/outerwear"
                                    },
                                    "categoryId": "3074457345616691086"
                                },
                                {
                                    "identifier": "APAC__Pants_SPORT",
                                    "children": [
                                        {
                                            "identifier": "APAC__Ski_Pants_And_Baselayer_PANTS_SPORT",
                                            "numberOfVisibleProducts": 66,
                                            "count": 66,
                                            "label": "Ski Pants and Baselayer",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/pants/ski-pants-and-baselayer"
                                            },
                                            "categoryId": "3074457345616691091"
                                        },
                                        {
                                            "identifier": "APAC__Track_Pants_PANTS_SPORT",
                                            "numberOfVisibleProducts": 44,
                                            "count": 44,
                                            "label": "Track Pants",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/pants/track-pants"
                                            },
                                            "categoryId": "3074457345616691092"
                                        }
                                    ],
                                    "numberOfVisibleProducts": 108,
                                    "count": 108,
                                    "label": "Pants",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/pants"
                                    },
                                    "categoryId": "3074457345616691077"
                                },
                                {
                                    "identifier": "APAC__Shorts_SPORT",
                                    "numberOfVisibleProducts": 14,
                                    "count": 14,
                                    "label": "Shorts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/shorts"
                                    },
                                    "categoryId": "3074457345616691081"
                                },
                                {
                                    "identifier": "APAC__Skirts_SPORT",
                                    "numberOfVisibleProducts": 6,
                                    "count": 6,
                                    "label": "Skirts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/skirts"
                                    },
                                    "categoryId": "3074457345616691083"
                                },
                                {
                                    "identifier": "APAC__Sports_Bras_SPORT",
                                    "numberOfVisibleProducts": 44,
                                    "count": 44,
                                    "label": "Sports Bras",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/sports-bras"
                                    },
                                    "categoryId": "3074457345616691097"
                                },
                                {
                                    "identifier": "APAC__Tops_SPORT",
                                    "children": [
                                        {
                                            "identifier": "APAC__Baselayer_TOPS_SPORT",
                                            "numberOfVisibleProducts": 41,
                                            "count": 41,
                                            "label": "Baselayer",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/tops/baselayer"
                                            },
                                            "categoryId": "3074457345616691096"
                                        },
                                        {
                                            "identifier": "APAC__Bodysuits_TOPS_SPORT",
                                            "numberOfVisibleProducts": 1,
                                            "count": 1,
                                            "label": "Bodysuits",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/tops/bodysuits"
                                            },
                                            "categoryId": "3074457345616691101"
                                        },
                                        {
                                            "identifier": "APAC__Long-Sleeve_Tops_TOPS_SPORT",
                                            "numberOfVisibleProducts": 31,
                                            "count": 31,
                                            "label": "Long-Sleeve Tops",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/tops/long-sleeve-tops"
                                            },
                                            "categoryId": "3074457345616691102"
                                        },
                                        {
                                            "identifier": "APAC__Sweatshirts_TOPS_SPORT",
                                            "numberOfVisibleProducts": 27,
                                            "count": 27,
                                            "label": "Sweatshirts",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/tops/sweatshirts"
                                            },
                                            "categoryId": "3074457345616691095"
                                        },
                                        {
                                            "identifier": "APAC__T-Shirts_TOPS_SPORT",
                                            "numberOfVisibleProducts": 32,
                                            "count": 32,
                                            "label": "T-Shirts",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/tops/t-shirts"
                                            },
                                            "categoryId": "3074457345616691099"
                                        },
                                        {
                                            "identifier": "APAC__Tank_Tops_TOPS_SPORT",
                                            "numberOfVisibleProducts": 21,
                                            "count": 21,
                                            "label": "Tank Tops",
                                            "seo": {
                                                "seoURLKeyword": "/clothing/sport/tops/tank-tops"
                                            },
                                            "categoryId": "3074457345616691100"
                                        }
                                    ],
                                    "numberOfVisibleProducts": 131,
                                    "count": 131,
                                    "label": "Tops",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/sport/tops"
                                    },
                                    "categoryId": "3074457345616691079"
                                }
                            ],
                            "numberOfVisibleProducts": 598,
                            "count": 598,
                            "label": "Sport",
                            "seo": {
                                "seoURLKeyword": "/clothing/sport"
                            },
                            "categoryId": "3074457345616690685"
                        },
                        {
                            "identifier": "APAC__Suits_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Jackets_SUITS_CLOTHING",
                                    "numberOfVisibleProducts": 137,
                                    "count": 137,
                                    "label": "Jackets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/suits/jackets"
                                    },
                                    "categoryId": "3074457345616690942"
                                },
                                {
                                    "identifier": "APAC__Pants_SUITS_CLOTHING",
                                    "numberOfVisibleProducts": 68,
                                    "count": 68,
                                    "label": "Pants",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/suits/pants"
                                    },
                                    "categoryId": "3074457345616690940"
                                },
                                {
                                    "identifier": "APAC__Shorts_SUITS_CLOTHING",
                                    "numberOfVisibleProducts": 5,
                                    "count": 5,
                                    "label": "Shorts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/suits/shorts"
                                    },
                                    "categoryId": "3074457345616690941"
                                },
                                {
                                    "identifier": "APAC__Skirts_SUITS_CLOTHING",
                                    "numberOfVisibleProducts": 15,
                                    "count": 15,
                                    "label": "Skirts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/suits/skirts"
                                    },
                                    "categoryId": "3074457345616690939"
                                }
                            ],
                            "numberOfVisibleProducts": 225,
                            "count": 225,
                            "label": "Suits",
                            "seo": {
                                "seoURLKeyword": "/clothing/suits"
                            },
                            "categoryId": "3074457345616690900"
                        },
                        {
                            "identifier": "APAC__Swimwear_And_Beachwear_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Beach_Dresses_SWIMWEAR_AND_BEACHWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 3,
                                    "count": 3,
                                    "label": "Beach Dresses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/swimwear-and-beachwear/beach-dresses"
                                    },
                                    "categoryId": "3074457345616690944"
                                },
                                {
                                    "identifier": "APAC__Bottoms_BIKINIS_SWIMWEAR_AND_BEACHWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 96,
                                    "count": 96,
                                    "label": "Bikini Bottoms",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/swimwear-and-beachwear/bikini-bottoms"
                                    },
                                    "categoryId": "3074457345616703669"
                                },
                                {
                                    "identifier": "APAC__Sets_BIKINIS_SWIMWEAR_AND_BEACHWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 96,
                                    "count": 96,
                                    "label": "Bikini Sets",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/swimwear-and-beachwear/bikini-sets"
                                    },
                                    "categoryId": "3074457345616690949"
                                },
                                {
                                    "identifier": "APAC__Tops_BIKINIS_SWIMWEAR_AND_BEACHWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 94,
                                    "count": 94,
                                    "label": "Bikini Tops",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/swimwear-and-beachwear/bikini-tops"
                                    },
                                    "categoryId": "3074457345616703668"
                                },
                                {
                                    "identifier": "APAC__Coverups_SWIMWEAR_AND_BEACHWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 127,
                                    "count": 127,
                                    "label": "Coverups",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/swimwear-and-beachwear/coverups"
                                    },
                                    "categoryId": "3074457345616690946"
                                },
                                {
                                    "identifier": "APAC__One-Piece_SWIMWEAR_AND_BEACHWEAR_CLOTHING",
                                    "numberOfVisibleProducts": 222,
                                    "count": 222,
                                    "label": "One-Piece",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/swimwear-and-beachwear/one-piece"
                                    },
                                    "categoryId": "3074457345616690945"
                                }
                            ],
                            "numberOfVisibleProducts": 624,
                            "count": 624,
                            "label": "Swimwear and Beachwear",
                            "seo": {
                                "seoURLKeyword": "/clothing/swimwear-and-beachwear"
                            },
                            "categoryId": "3074457345616690901"
                        },
                        {
                            "identifier": "APAC__Tops_CLOTHING",
                            "children": [
                                {
                                    "identifier": "APAC__Blouses_TOPS_CLOTHING",
                                    "numberOfVisibleProducts": 399,
                                    "count": 399,
                                    "label": "Blouses",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/tops/blouses"
                                    },
                                    "categoryId": "3074457345616690952"
                                },
                                {
                                    "identifier": "APAC__Bodysuits_TOPS_CLOTHING",
                                    "numberOfVisibleProducts": 131,
                                    "count": 131,
                                    "label": "Bodysuits",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/tops/bodysuits"
                                    },
                                    "categoryId": "3074457345616690951"
                                },
                                {
                                    "identifier": "APAC__Cropped_TOPS_CLOTHING",
                                    "numberOfVisibleProducts": 133,
                                    "count": 133,
                                    "label": "Cropped",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/tops/cropped"
                                    },
                                    "categoryId": "3074457345616690953"
                                },
                                {
                                    "identifier": "APAC__Shirts_TOPS_CLOTHING",
                                    "numberOfVisibleProducts": 416,
                                    "count": 416,
                                    "label": "Shirts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/tops/shirts"
                                    },
                                    "categoryId": "3074457345616690956"
                                },
                                {
                                    "identifier": "APAC__Sweatshirts_And_Hoodies_TOPS_CLOTHING",
                                    "numberOfVisibleProducts": 147,
                                    "count": 147,
                                    "label": "Sweatshirts and Hoodies",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/tops/sweatshirts-and-hoodies"
                                    },
                                    "categoryId": "3074457345616690954"
                                },
                                {
                                    "identifier": "APAC__T-Shirts_TOPS_CLOTHING",
                                    "numberOfVisibleProducts": 377,
                                    "count": 377,
                                    "label": "T-Shirts",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/tops/t-shirts"
                                    },
                                    "categoryId": "3074457345616690957"
                                },
                                {
                                    "identifier": "APAC__Tanks_And_Camis_TOPS_CLOTHING",
                                    "numberOfVisibleProducts": 294,
                                    "count": 294,
                                    "label": "Tanks and Camis",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/tops/tanks-and-camis"
                                    },
                                    "categoryId": "3074457345616690959"
                                },
                                {
                                    "identifier": "APAC__Turtleneck_TOPS_CLOTHING",
                                    "numberOfVisibleProducts": 83,
                                    "count": 83,
                                    "label": "Turtleneck",
                                    "seo": {
                                        "seoURLKeyword": "/clothing/tops/turtleneck"
                                    },
                                    "categoryId": "3074457345616690955"
                                }
                            ],
                            "numberOfVisibleProducts": 1858,
                            "count": 1858,
                            "label": "Tops",
                            "seo": {
                                "seoURLKeyword": "/clothing/tops"
                            },
                            "categoryId": "3074457345616690895"
                        }
                    ],
                    "numberOfVisibleProducts": 10089,
                    "count": 10089,
                    "label": "Clothing",
                    "seo": {
                        "seoURLKeyword": "/clothing"
                    },
                    "categoryId": "3074457345616690677"
                }
            ],
            "identifier": "CATEGORIES",
            "label": "Category"
        },
        {
            "entry": [
                {
                    "identifier": "Animal print",
                    "swatch": {
                        "URL": "https://media.yoox.biz/ytos/resources/THEOUTNET/images/colours/animal.jpg"
                    },
                    "count": 11,
                    "label": "Animal print",
                    "value": "ads_f11503_ntk_cs%3A%22Animal+print%22"
                },
                {
                    "identifier": "Black",
                    "swatch": {
                        "HEX": "000000"
                    },
                    "count": 452,
                    "label": "Black",
                    "value": "ads_f11503_ntk_cs%3A%22Black%22"
                },
                {
                    "identifier": "Blue",
                    "swatch": {
                        "HEX": "326FDA"
                    },
                    "count": 172,
                    "label": "Blue",
                    "value": "ads_f11503_ntk_cs%3A%22Blue%22"
                },
                {
                    "identifier": "Brown",
                    "swatch": {
                        "HEX": "7E4E38"
                    },
                    "count": 199,
                    "label": "Brown",
                    "value": "ads_f11503_ntk_cs%3A%22Brown%22"
                },
                {
                    "identifier": "Burgundy",
                    "swatch": {
                        "HEX": "953E47"
                    },
                    "count": 22,
                    "label": "Burgundy",
                    "value": "ads_f11503_ntk_cs%3A%22Burgundy%22"
                },
                {
                    "identifier": "Cream",
                    "swatch": {
                        "HEX": "ECEAC1"
                    },
                    "count": 35,
                    "label": "Cream",
                    "value": "ads_f11503_ntk_cs%3A%22Cream%22"
                },
                {
                    "identifier": "Ecru",
                    "swatch": {
                        "HEX": "DED4C8"
                    },
                    "count": 8,
                    "label": "Ecru",
                    "value": "ads_f11503_ntk_cs%3A%22Ecru%22"
                },
                {
                    "identifier": "Gold",
                    "swatch": {
                        "HEX": "AF812C"
                    },
                    "count": 1,
                    "label": "Gold",
                    "value": "ads_f11503_ntk_cs%3A%22Gold%22"
                },
                {
                    "identifier": "Gray",
                    "swatch": {
                        "HEX": "949494"
                    },
                    "count": 84,
                    "label": "Gray",
                    "value": "ads_f11503_ntk_cs%3A%22Gray%22"
                },
                {
                    "identifier": "Green",
                    "swatch": {
                        "HEX": "596750"
                    },
                    "count": 67,
                    "label": "Green",
                    "value": "ads_f11503_ntk_cs%3A%22Green%22"
                },
                {
                    "identifier": "Ivory",
                    "swatch": {
                        "HEX": "FFFFF0"
                    },
                    "count": 30,
                    "label": "Ivory",
                    "value": "ads_f11503_ntk_cs%3A%22Ivory%22"
                },
                {
                    "identifier": "Metallic",
                    "swatch": {
                        "URL": "https://media.yoox.biz/ytos/resources/THEOUTNET/images/colours/metallic.jpg"
                    },
                    "count": 2,
                    "label": "Metallic",
                    "value": "ads_f11503_ntk_cs%3A%22Metallic%22"
                },
                {
                    "identifier": "Multi",
                    "swatch": {
                        "URL": "https://media.yoox.biz/ytos/resources/THEOUTNET/images/colours/multi.jpg"
                    },
                    "count": 2,
                    "label": "Multi",
                    "value": "ads_f11503_ntk_cs%3A%22Multi%22"
                },
                {
                    "identifier": "Neutrals",
                    "swatch": {
                        "HEX": "E6C3AF"
                    },
                    "count": 93,
                    "label": "Neutrals",
                    "value": "ads_f11503_ntk_cs%3A%22Neutrals%22"
                },
                {
                    "identifier": "Off-white",
                    "swatch": {
                        "HEX": "FFFFFF"
                    },
                    "count": 22,
                    "label": "Off-white",
                    "value": "ads_f11503_ntk_cs%3A%22Off-white%22"
                },
                {
                    "identifier": "Orange",
                    "swatch": {
                        "HEX": "F08213"
                    },
                    "count": 4,
                    "label": "Orange",
                    "value": "ads_f11503_ntk_cs%3A%22Orange%22"
                },
                {
                    "identifier": "Pink",
                    "swatch": {
                        "HEX": "F058A3"
                    },
                    "count": 33,
                    "label": "Pink",
                    "value": "ads_f11503_ntk_cs%3A%22Pink%22"
                },
                {
                    "identifier": "Purple",
                    "swatch": {
                        "HEX": "803EAC"
                    },
                    "count": 10,
                    "label": "Purple",
                    "value": "ads_f11503_ntk_cs%3A%22Purple%22"
                },
                {
                    "identifier": "Red",
                    "swatch": {
                        "HEX": "F40002"
                    },
                    "count": 39,
                    "label": "Red",
                    "value": "ads_f11503_ntk_cs%3A%22Red%22"
                },
                {
                    "identifier": "Silver",
                    "swatch": {
                        "HEX": "C0C0C0"
                    },
                    "count": 8,
                    "label": "Silver",
                    "value": "ads_f11503_ntk_cs%3A%22Silver%22"
                },
                {
                    "identifier": "White",
                    "swatch": {
                        "HEX": "FFFFFF"
                    },
                    "count": 61,
                    "label": "White",
                    "value": "ads_f11503_ntk_cs%3A%22White%22"
                },
                {
                    "identifier": "Yellow",
                    "swatch": {
                        "HEX": "FFFF96"
                    },
                    "count": 9,
                    "label": "Yellow",
                    "value": "ads_f11503_ntk_cs%3A%22Yellow%22"
                }
            ],
            "identifier": "Filter Colour",
            "label": "Color"
        },
        {
            "entry": [
                {
                    "identifier": "16ARLINGTON",
                    "designerIdentifier": "16ARLINGTON",
                    "count": 1,
                    "label": "16ARLINGTON",
                    "value": "ads_f10003_ntk_cs%3A%2216ARLINGTON%22"
                },
                {
                    "identifier": "ACNESTUDIOS",
                    "designerIdentifier": "ACNESTUDIOS",
                    "count": 18,
                    "label": "ACNE STUDIOS",
                    "value": "ads_f10003_ntk_cs%3A%22ACNE+STUDIOS%22"
                },
                {
                    "identifier": "ADIDASBYSTELLAMCCARTNEY",
                    "designerIdentifier": "ADIDASBYSTELLAMCCARTNEY",
                    "count": 6,
                    "label": "ADIDAS BY STELLA MCCARTNEY",
                    "value": "ads_f10003_ntk_cs%3A%22ADIDAS+BY+STELLA+MCCARTNEY%22"
                },
                {
                    "identifier": "ADIDASORIGINALS",
                    "designerIdentifier": "ADIDASORIGINALS",
                    "count": 6,
                    "label": "ADIDAS ORIGINALS",
                    "value": "ads_f10003_ntk_cs%3A%22ADIDAS+ORIGINALS%22"
                },
                {
                    "identifier": "AGOLDE",
                    "designerIdentifier": "AGOLDE",
                    "count": 5,
                    "label": "AGOLDE",
                    "value": "ads_f10003_ntk_cs%3A%22AGOLDE%22"
                },
                {
                    "identifier": "ALAA",
                    "designerIdentifier": "ALAA",
                    "count": 14,
                    "label": "ALAÏA",
                    "value": "ads_f10003_ntk_cs%3A%22ALA%C3%8FA%22"
                },
                {
                    "identifier": "ALESSANDRARICH",
                    "designerIdentifier": "ALESSANDRARICH",
                    "count": 1,
                    "label": "ALESSANDRA RICH",
                    "value": "ads_f10003_ntk_cs%3A%22ALESSANDRA+RICH%22"
                },
                {
                    "identifier": "ALEXPERRY",
                    "designerIdentifier": "ALEXPERRY",
                    "count": 2,
                    "label": "ALEX PERRY",
                    "value": "ads_f10003_ntk_cs%3A%22ALEX+PERRY%22"
                },
                {
                    "identifier": "ALEXANDERMCQUEEN",
                    "designerIdentifier": "ALEXANDERMCQUEEN",
                    "count": 26,
                    "label": "ALEXANDER MCQUEEN",
                    "value": "ads_f10003_ntk_cs%3A%22ALEXANDER+MCQUEEN%22"
                },
                {
                    "identifier": "ALIXOFBOHEMIA",
                    "designerIdentifier": "ALIXOFBOHEMIA",
                    "count": 8,
                    "label": "ALIX OF BOHEMIA",
                    "value": "ads_f10003_ntk_cs%3A%22ALIX+OF+BOHEMIA%22"
                },
                {
                    "identifier": "ALOYOGA",
                    "designerIdentifier": "ALOYOGA",
                    "count": 2,
                    "label": "ALO YOGA",
                    "value": "ads_f10003_ntk_cs%3A%22ALO+YOGA%22"
                },
                {
                    "identifier": "ALTUZARRA",
                    "designerIdentifier": "ALTUZARRA",
                    "count": 2,
                    "label": "ALTUZARRA",
                    "value": "ads_f10003_ntk_cs%3A%22ALTUZARRA%22"
                },
                {
                    "identifier": "AMI",
                    "designerIdentifier": "AMI",
                    "count": 2,
                    "label": "AMI PARIS",
                    "value": "ads_f10003_ntk_cs%3A%22AMI+PARIS%22"
                },
                {
                    "identifier": "ANINEBING",
                    "designerIdentifier": "ANINEBING",
                    "count": 7,
                    "label": "ANINE BING",
                    "value": "ads_f10003_ntk_cs%3A%22ANINE+BING%22"
                },
                {
                    "identifier": "ANOTHERTOMORROW",
                    "designerIdentifier": "ANOTHERTOMORROW",
                    "count": 10,
                    "label": "ANOTHER TOMORROW",
                    "value": "ads_f10003_ntk_cs%3A%22ANOTHER+TOMORROW%22"
                },
                {
                    "identifier": "AZTECHMOUNTAIN",
                    "designerIdentifier": "AZTECHMOUNTAIN",
                    "count": 7,
                    "label": "AZTECH MOUNTAIN",
                    "value": "ads_f10003_ntk_cs%3A%22AZTECH+MOUNTAIN%22"
                },
                {
                    "identifier": "BSIDES",
                    "designerIdentifier": "BSIDES",
                    "count": 2,
                    "label": "B SIDES",
                    "value": "ads_f10003_ntk_cs%3A%22B+SIDES%22"
                },
                {
                    "identifier": "BALENCIAGA",
                    "designerIdentifier": "BALENCIAGA",
                    "count": 23,
                    "label": "BALENCIAGA",
                    "value": "ads_f10003_ntk_cs%3A%22BALENCIAGA%22"
                },
                {
                    "identifier": "BALLY",
                    "designerIdentifier": "BALLY",
                    "count": 6,
                    "label": "BALLY",
                    "value": "ads_f10003_ntk_cs%3A%22BALLY%22"
                },
                {
                    "identifier": "BALMAIN",
                    "designerIdentifier": "BALMAIN",
                    "count": 7,
                    "label": "BALMAIN",
                    "value": "ads_f10003_ntk_cs%3A%22BALMAIN%22"
                },
                {
                    "identifier": "BARBOUR",
                    "designerIdentifier": "BARBOUR",
                    "count": 20,
                    "label": "BARBOUR",
                    "value": "ads_f10003_ntk_cs%3A%22BARBOUR%22"
                },
                {
                    "identifier": "BERNADETTE",
                    "designerIdentifier": "BERNADETTE",
                    "count": 1,
                    "label": "BERNADETTE",
                    "value": "ads_f10003_ntk_cs%3A%22BERNADETTE%22"
                },
                {
                    "identifier": "BLAZMILANO",
                    "designerIdentifier": "BLAZMILANO",
                    "count": 12,
                    "label": "BLAZÉ MILANO",
                    "value": "ads_f10003_ntk_cs%3A%22BLAZ%C3%89+MILANO%22"
                },
                {
                    "identifier": "BODE",
                    "designerIdentifier": "BODE",
                    "count": 3,
                    "label": "BODE",
                    "value": "ads_f10003_ntk_cs%3A%22BODE%22"
                },
                {
                    "identifier": "BOGNER",
                    "designerIdentifier": "BOGNER",
                    "count": 13,
                    "label": "BOGNER",
                    "value": "ads_f10003_ntk_cs%3A%22BOGNER%22"
                },
                {
                    "identifier": "BOTTEGAVENETA",
                    "designerIdentifier": "BOTTEGAVENETA",
                    "count": 36,
                    "label": "BOTTEGA VENETA",
                    "value": "ads_f10003_ntk_cs%3A%22BOTTEGA+VENETA%22"
                },
                {
                    "identifier": "BRUNELLOCUCINELLI",
                    "designerIdentifier": "BRUNELLOCUCINELLI",
                    "count": 16,
                    "label": "BRUNELLO CUCINELLI",
                    "value": "ads_f10003_ntk_cs%3A%22BRUNELLO+CUCINELLI%22"
                },
                {
                    "identifier": "BURBERRY",
                    "designerIdentifier": "BURBERRY",
                    "count": 26,
                    "label": "BURBERRY",
                    "value": "ads_f10003_ntk_cs%3A%22BURBERRY%22"
                },
                {
                    "identifier": "CANADAGOOSE",
                    "designerIdentifier": "CANADAGOOSE",
                    "count": 5,
                    "label": "CANADA GOOSE",
                    "value": "ads_f10003_ntk_cs%3A%22CANADA+GOOSE%22"
                },
                {
                    "identifier": "CAROLINAHERRERA",
                    "designerIdentifier": "CAROLINAHERRERA",
                    "count": 1,
                    "label": "CAROLINA HERRERA",
                    "value": "ads_f10003_ntk_cs%3A%22CAROLINA+HERRERA%22"
                },
                {
                    "identifier": "CARVEN",
                    "designerIdentifier": "CARVEN",
                    "count": 3,
                    "label": "CARVEN",
                    "value": "ads_f10003_ntk_cs%3A%22CARVEN%22"
                },
                {
                    "identifier": "CHLO",
                    "designerIdentifier": "CHLO",
                    "count": 31,
                    "label": "CHLOÉ",
                    "value": "ads_f10003_ntk_cs%3A%22CHLO%C3%89%22"
                },
                {
                    "identifier": "CHRISTOPHERESBER",
                    "designerIdentifier": "CHRISTOPHERESBER",
                    "count": 1,
                    "label": "CHRISTOPHER ESBER",
                    "value": "ads_f10003_ntk_cs%3A%22CHRISTOPHER+ESBER%22"
                },
                {
                    "identifier": "CITIZENSOFHUMANITY",
                    "designerIdentifier": "CITIZENSOFHUMANITY",
                    "count": 3,
                    "label": "CITIZENS OF HUMANITY",
                    "value": "ads_f10003_ntk_cs%3A%22CITIZENS+OF+HUMANITY%22"
                },
                {
                    "identifier": "CORDOVA",
                    "designerIdentifier": "CORDOVA",
                    "count": 15,
                    "label": "CORDOVA",
                    "value": "ads_f10003_ntk_cs%3A%22CORDOVA%22"
                },
                {
                    "identifier": "COURRGES",
                    "designerIdentifier": "COURRGES",
                    "count": 2,
                    "label": "COURRÈGES",
                    "value": "ads_f10003_ntk_cs%3A%22COURR%C3%88GES%22"
                },
                {
                    "identifier": "DEIJISTUDIOS",
                    "designerIdentifier": "DEIJISTUDIOS",
                    "count": 1,
                    "label": "DEIJI STUDIOS",
                    "value": "ads_f10003_ntk_cs%3A%22DEIJI+STUDIOS%22"
                },
                {
                    "identifier": "DESTREE",
                    "designerIdentifier": "DESTREE",
                    "count": 9,
                    "label": "DESTREE",
                    "value": "ads_f10003_ntk_cs%3A%22DESTREE%22"
                },
                {
                    "identifier": "DIMAAYAD",
                    "designerIdentifier": "DIMAAYAD",
                    "count": 1,
                    "label": "DIMA AYAD",
                    "value": "ads_f10003_ntk_cs%3A%22DIMA+AYAD%22"
                },
                {
                    "identifier": "DODOBAROR",
                    "designerIdentifier": "DODOBAROR",
                    "count": 1,
                    "label": "DODO BAR OR",
                    "value": "ads_f10003_ntk_cs%3A%22DODO+BAR+OR%22"
                },
                {
                    "identifier": "DOLCEANDGABBANA",
                    "designerIdentifier": "DOLCEANDGABBANA",
                    "count": 23,
                    "label": "DOLCE&GABBANA",
                    "value": "ads_f10003_ntk_cs%3A%22DOLCE%26GABBANA%22"
                },
                {
                    "identifier": "DRIESVANNOTEN",
                    "designerIdentifier": "DRIESVANNOTEN",
                    "count": 12,
                    "label": "DRIES VAN NOTEN",
                    "value": "ads_f10003_ntk_cs%3A%22DRIES+VAN+NOTEN%22"
                },
                {
                    "identifier": "ERDEM",
                    "designerIdentifier": "ERDEM",
                    "count": 1,
                    "label": "ERDEM",
                    "value": "ads_f10003_ntk_cs%3A%22ERDEM%22"
                },
                {
                    "identifier": "ESSESTUDIOS",
                    "designerIdentifier": "ESSESTUDIOS",
                    "count": 2,
                    "label": "ESSE STUDIOS",
                    "value": "ads_f10003_ntk_cs%3A%22ESSE+STUDIOS%22"
                },
                {
                    "identifier": "ETRO",
                    "designerIdentifier": "ETRO",
                    "count": 4,
                    "label": "ETRO",
                    "value": "ads_f10003_ntk_cs%3A%22ETRO%22"
                },
                {
                    "identifier": "FAITHFULL",
                    "designerIdentifier": "FAITHFULL",
                    "count": 3,
                    "label": "FAITHFULL",
                    "value": "ads_f10003_ntk_cs%3A%22FAITHFULL%22"
                },
                {
                    "identifier": "FFORME",
                    "designerIdentifier": "FFORME",
                    "count": 1,
                    "label": "FFORME",
                    "value": "ads_f10003_ntk_cs%3A%22FFORME%22"
                },
                {
                    "identifier": "FORTELA",
                    "designerIdentifier": "FORTELA",
                    "count": 3,
                    "label": "FORTELA",
                    "value": "ads_f10003_ntk_cs%3A%22FORTELA%22"
                },
                {
                    "identifier": "FRAME",
                    "designerIdentifier": "FRAME",
                    "count": 10,
                    "label": "FRAME",
                    "value": "ads_f10003_ntk_cs%3A%22FRAME%22"
                },
                {
                    "identifier": "FUSALP",
                    "designerIdentifier": "FUSALP",
                    "count": 8,
                    "label": "FUSALP",
                    "value": "ads_f10003_ntk_cs%3A%22FUSALP%22"
                },
                {
                    "identifier": "GABRIELAHEARST",
                    "designerIdentifier": "GABRIELAHEARST",
                    "count": 6,
                    "label": "GABRIELA HEARST",
                    "value": "ads_f10003_ntk_cs%3A%22GABRIELA+HEARST%22"
                },
                {
                    "identifier": "GALVAN",
                    "designerIdentifier": "GALVAN",
                    "count": 1,
                    "label": "GALVAN",
                    "value": "ads_f10003_ntk_cs%3A%22GALVAN%22"
                },
                {
                    "identifier": "GANNI",
                    "designerIdentifier": "GANNI",
                    "count": 2,
                    "label": "GANNI",
                    "value": "ads_f10003_ntk_cs%3A%22GANNI%22"
                },
                {
                    "identifier": "GIVENCHY",
                    "designerIdentifier": "GIVENCHY",
                    "count": 2,
                    "label": "GIVENCHY",
                    "value": "ads_f10003_ntk_cs%3A%22GIVENCHY%22"
                },
                {
                    "identifier": "GOLDBERGH",
                    "designerIdentifier": "GOLDBERGH",
                    "count": 10,
                    "label": "GOLDBERGH",
                    "value": "ads_f10003_ntk_cs%3A%22GOLDBERGH%22"
                },
                {
                    "identifier": "GOLDENGOOSE",
                    "designerIdentifier": "GOLDENGOOSE",
                    "count": 5,
                    "label": "GOLDEN GOOSE",
                    "value": "ads_f10003_ntk_cs%3A%22GOLDEN+GOOSE%22"
                },
                {
                    "identifier": "GUCCI",
                    "designerIdentifier": "GUCCI",
                    "count": 47,
                    "label": "GUCCI",
                    "value": "ads_f10003_ntk_cs%3A%22GUCCI%22"
                },
                {
                    "identifier": "GUESTINRESIDENCE",
                    "designerIdentifier": "GUESTINRESIDENCE",
                    "count": 11,
                    "label": "GUEST IN RESIDENCE",
                    "value": "ads_f10003_ntk_cs%3A%22GUEST+IN+RESIDENCE%22"
                },
                {
                    "identifier": "ISABELMARANT",
                    "designerIdentifier": "ISABELMARANT",
                    "count": 11,
                    "label": "ISABEL MARANT",
                    "value": "ads_f10003_ntk_cs%3A%22ISABEL+MARANT%22"
                },
                {
                    "identifier": "JACQUEMUS",
                    "designerIdentifier": "JACQUEMUS",
                    "count": 1,
                    "label": "JACQUEMUS",
                    "value": "ads_f10003_ntk_cs%3A%22JACQUEMUS%22"
                },
                {
                    "identifier": "JEANPAULGAULTIER",
                    "designerIdentifier": "JEANPAULGAULTIER",
                    "count": 3,
                    "label": "JEAN PAUL GAULTIER",
                    "value": "ads_f10003_ntk_cs%3A%22JEAN+PAUL+GAULTIER%22"
                },
                {
                    "identifier": "JILSANDER",
                    "designerIdentifier": "JILSANDER",
                    "count": 9,
                    "label": "JIL SANDER",
                    "value": "ads_f10003_ntk_cs%3A%22JIL+SANDER%22"
                },
                {
                    "identifier": "JOSEPH",
                    "designerIdentifier": "JOSEPH",
                    "count": 6,
                    "label": "JOSEPH",
                    "value": "ads_f10003_ntk_cs%3A%22JOSEPH%22"
                },
                {
                    "identifier": "JWANDERSON",
                    "designerIdentifier": "JWANDERSON",
                    "count": 2,
                    "label": "JW ANDERSON",
                    "value": "ads_f10003_ntk_cs%3A%22JW+ANDERSON%22"
                },
                {
                    "identifier": "KALLMEYER",
                    "designerIdentifier": "KALLMEYER",
                    "count": 4,
                    "label": "KALLMEYER",
                    "value": "ads_f10003_ntk_cs%3A%22KALLMEYER%22"
                },
                {
                    "identifier": "KHAITE",
                    "designerIdentifier": "KHAITE",
                    "count": 21,
                    "label": "KHAITE",
                    "value": "ads_f10003_ntk_cs%3A%22KHAITE%22"
                },
                {
                    "identifier": "LADOUBLEJ",
                    "designerIdentifier": "LADOUBLEJ",
                    "count": 1,
                    "label": "LA DOUBLEJ",
                    "value": "ads_f10003_ntk_cs%3A%22LA+DOUBLEJ%22"
                },
                {
                    "identifier": "LALIGNE",
                    "designerIdentifier": "LALIGNE",
                    "count": 2,
                    "label": "LA LIGNE",
                    "value": "ads_f10003_ntk_cs%3A%22LA+LIGNE%22"
                },
                {
                    "identifier": "LEKASHA",
                    "designerIdentifier": "LEKASHA",
                    "count": 2,
                    "label": "LE KASHA",
                    "value": "ads_f10003_ntk_cs%3A%22LE+KASHA%22"
                },
                {
                    "identifier": "LEMAIRE",
                    "designerIdentifier": "LEMAIRE",
                    "count": 3,
                    "label": "LEMAIRE",
                    "value": "ads_f10003_ntk_cs%3A%22LEMAIRE%22"
                },
                {
                    "identifier": "LEMLEM",
                    "designerIdentifier": "LEMLEM",
                    "count": 1,
                    "label": "LEMLEM",
                    "value": "ads_f10003_ntk_cs%3A%22LEMLEM%22"
                },
                {
                    "identifier": "LESET",
                    "designerIdentifier": "LESET",
                    "count": 4,
                    "label": "LESET",
                    "value": "ads_f10003_ntk_cs%3A%22LESET%22"
                },
                {
                    "identifier": "LIBEROWE",
                    "designerIdentifier": "LIBEROWE",
                    "count": 14,
                    "label": "LIBEROWE",
                    "value": "ads_f10003_ntk_cs%3A%22LIBEROWE%22"
                },
                {
                    "identifier": "LOEWE",
                    "designerIdentifier": "LOEWE",
                    "count": 13,
                    "label": "LOEWE",
                    "value": "ads_f10003_ntk_cs%3A%22LOEWE%22"
                },
                {
                    "identifier": "LORETTACAPONI",
                    "designerIdentifier": "LORETTACAPONI",
                    "count": 1,
                    "label": "LORETTA CAPONI",
                    "value": "ads_f10003_ntk_cs%3A%22LORETTA+CAPONI%22"
                },
                {
                    "identifier": "LOROPIANA",
                    "designerIdentifier": "LOROPIANA",
                    "count": 57,
                    "label": "LORO PIANA",
                    "value": "ads_f10003_ntk_cs%3A%22LORO+PIANA%22"
                },
                {
                    "identifier": "LOULOU",
                    "designerIdentifier": "LOULOU",
                    "count": 8,
                    "label": "LOULOU DE SAISON",
                    "value": "ads_f10003_ntk_cs%3A%22LOULOU+DE+SAISON%22"
                },
                {
                    "identifier": "LULULEMON",
                    "designerIdentifier": "LULULEMON",
                    "count": 14,
                    "label": "LULULEMON",
                    "value": "ads_f10003_ntk_cs%3A%22LULULEMON%22"
                },
                {
                    "identifier": "MACKAGE",
                    "designerIdentifier": "MACKAGE",
                    "count": 8,
                    "label": "MACKAGE",
                    "value": "ads_f10003_ntk_cs%3A%22MACKAGE%22"
                },
                {
                    "identifier": "MAGDABUTRYM",
                    "designerIdentifier": "MAGDABUTRYM",
                    "count": 7,
                    "label": "MAGDA BUTRYM",
                    "value": "ads_f10003_ntk_cs%3A%22MAGDA+BUTRYM%22"
                },
                {
                    "identifier": "MARANTTOILE",
                    "designerIdentifier": "MARANTTOILE",
                    "count": 10,
                    "label": "MARANT ÉTOILE",
                    "value": "ads_f10003_ntk_cs%3A%22MARANT+%C3%89TOILE%22"
                },
                {
                    "identifier": "MARIAMCMANUS",
                    "designerIdentifier": "MARIAMCMANUS",
                    "count": 3,
                    "label": "MARIA MCMANUS",
                    "value": "ads_f10003_ntk_cs%3A%22MARIA+MCMANUS%22"
                },
                {
                    "identifier": "MARIEADAMLEENAERDT",
                    "designerIdentifier": "MARIEADAMLEENAERDT",
                    "count": 4,
                    "label": "MARIE ADAM-LEENAERDT",
                    "value": "ads_f10003_ntk_cs%3A%22MARIE+ADAM-LEENAERDT%22"
                },
                {
                    "identifier": "MARNI",
                    "designerIdentifier": "MARNI",
                    "count": 2,
                    "label": "MARNI",
                    "value": "ads_f10003_ntk_cs%3A%22MARNI%22"
                },
                {
                    "identifier": "MAXMARA",
                    "designerIdentifier": "MAXMARA",
                    "count": 19,
                    "label": "MAX MARA",
                    "value": "ads_f10003_ntk_cs%3A%22MAX+MARA%22"
                },
                {
                    "identifier": "MONCLER",
                    "designerIdentifier": "MONCLER",
                    "count": 103,
                    "label": "MONCLER",
                    "value": "ads_f10003_ntk_cs%3A%22MONCLER%22"
                },
                {
                    "identifier": "MONCLERGENIUS",
                    "designerIdentifier": "MONCLERGENIUS",
                    "count": 22,
                    "label": "MONCLER GENIUS",
                    "value": "ads_f10003_ntk_cs%3A%22MONCLER+GENIUS%22"
                },
                {
                    "identifier": "MONCLERGRENOBLE",
                    "designerIdentifier": "MONCLERGRENOBLE",
                    "count": 41,
                    "label": "MONCLER GRENOBLE",
                    "value": "ads_f10003_ntk_cs%3A%22MONCLER+GRENOBLE%22"
                },
                {
                    "identifier": "MOTHER",
                    "designerIdentifier": "MOTHER",
                    "count": 3,
                    "label": "MOTHER",
                    "value": "ads_f10003_ntk_cs%3A%22MOTHER%22"
                },
                {
                    "identifier": "NILILOTAN",
                    "designerIdentifier": "NILILOTAN",
                    "count": 16,
                    "label": "NILI LOTAN",
                    "value": "ads_f10003_ntk_cs%3A%22NILI+LOTAN%22"
                },
                {
                    "identifier": "NINARICCI",
                    "designerIdentifier": "NINARICCI",
                    "count": 1,
                    "label": "NINA RICCI",
                    "value": "ads_f10003_ntk_cs%3A%22NINA+RICCI%22"
                },
                {
                    "identifier": "NORMAKAMALI",
                    "designerIdentifier": "NORMAKAMALI",
                    "count": 2,
                    "label": "NORMA KAMALI",
                    "value": "ads_f10003_ntk_cs%3A%22NORMA+KAMALI%22"
                },
                {
                    "identifier": "NOURHAMMOUR",
                    "designerIdentifier": "NOURHAMMOUR",
                    "count": 17,
                    "label": "NOUR HAMMOUR",
                    "value": "ads_f10003_ntk_cs%3A%22NOUR+HAMMOUR%22"
                },
                {
                    "identifier": "ON",
                    "designerIdentifier": "ON",
                    "count": 3,
                    "label": "ON",
                    "value": "ads_f10003_ntk_cs%3A%22ON%22"
                },
                {
                    "identifier": "OURLEGACY",
                    "designerIdentifier": "OURLEGACY",
                    "count": 1,
                    "label": "OUR LEGACY",
                    "value": "ads_f10003_ntk_cs%3A%22OUR+LEGACY%22"
                },
                {
                    "identifier": "PAIGE",
                    "designerIdentifier": "PAIGE",
                    "count": 4,
                    "label": "PAIGE",
                    "value": "ads_f10003_ntk_cs%3A%22PAIGE%22"
                },
                {
                    "identifier": "PATOU",
                    "designerIdentifier": "PATOU",
                    "count": 5,
                    "label": "PATOU",
                    "value": "ads_f10003_ntk_cs%3A%22PATOU%22"
                },
                {
                    "identifier": "PERFECTMOMENT",
                    "designerIdentifier": "PERFECTMOMENT",
                    "count": 9,
                    "label": "PERFECT MOMENT",
                    "value": "ads_f10003_ntk_cs%3A%22PERFECT+MOMENT%22"
                },
                {
                    "identifier": "POLORALPHLAUREN",
                    "designerIdentifier": "POLORALPHLAUREN",
                    "count": 10,
                    "label": "POLO RALPH LAUREN",
                    "value": "ads_f10003_ntk_cs%3A%22POLO+RALPH+LAUREN%22"
                },
                {
                    "identifier": "PROENZASCHOULER",
                    "designerIdentifier": "PROENZASCHOULER",
                    "count": 4,
                    "label": "PROENZA SCHOULER",
                    "value": "ads_f10003_ntk_cs%3A%22PROENZA+SCHOULER%22"
                },
                {
                    "identifier": "PROENZASCHOULERWHITELABEL",
                    "designerIdentifier": "PROENZASCHOULERWHITELABEL",
                    "count": 2,
                    "label": "PROENZA SCHOULER WHITE LABEL",
                    "value": "ads_f10003_ntk_cs%3A%22PROENZA+SCHOULER+WHITE+LABEL%22"
                },
                {
                    "identifier": "PUCCI",
                    "designerIdentifier": "PUCCI",
                    "count": 2,
                    "label": "PUCCI",
                    "value": "ads_f10003_ntk_cs%3A%22PUCCI%22"
                },
                {
                    "identifier": "PURDEY",
                    "designerIdentifier": "PURDEY",
                    "count": 8,
                    "label": "PURDEY",
                    "value": "ads_f10003_ntk_cs%3A%22PURDEY%22"
                },
                {
                    "identifier": "R13",
                    "designerIdentifier": "R13",
                    "count": 3,
                    "label": "R13",
                    "value": "ads_f10003_ntk_cs%3A%22R13%22"
                },
                {
                    "identifier": "RALPHLAURENCOLLECTION",
                    "designerIdentifier": "RALPHLAURENCOLLECTION",
                    "count": 13,
                    "label": "RALPH LAUREN COLLECTION",
                    "value": "ads_f10003_ntk_cs%3A%22RALPH+LAUREN+COLLECTION%22"
                },
                {
                    "identifier": "RICKOWENS",
                    "designerIdentifier": "RICKOWENS",
                    "count": 15,
                    "label": "RICK OWENS",
                    "value": "ads_f10003_ntk_cs%3A%22RICK+OWENS%22"
                },
                {
                    "identifier": "RIXOLONDON",
                    "designerIdentifier": "RIXOLONDON",
                    "count": 3,
                    "label": "RIXO",
                    "value": "ads_f10003_ntk_cs%3A%22RIXO%22"
                },
                {
                    "identifier": "RUDSAK",
                    "designerIdentifier": "RUDSAK",
                    "count": 1,
                    "label": "RUDSAK",
                    "value": "ads_f10003_ntk_cs%3A%22RUDSAK%22"
                },
                {
                    "identifier": "RHE",
                    "designerIdentifier": "RHE",
                    "count": 4,
                    "label": "RÓHE",
                    "value": "ads_f10003_ntk_cs%3A%22R%C3%93HE%22"
                },
                {
                    "identifier": "SACAI",
                    "designerIdentifier": "SACAI",
                    "count": 14,
                    "label": "SACAI",
                    "value": "ads_f10003_ntk_cs%3A%22SACAI%22"
                },
                {
                    "identifier": "SAINTLAURENT",
                    "designerIdentifier": "SAINTLAURENT",
                    "count": 66,
                    "label": "SAINT LAURENT",
                    "value": "ads_f10003_ntk_cs%3A%22SAINT+LAURENT%22"
                },
                {
                    "identifier": "SALON1884",
                    "designerIdentifier": "SALON1884",
                    "count": 4,
                    "label": "SALON 1884",
                    "value": "ads_f10003_ntk_cs%3A%22SALON+1884%22"
                },
                {
                    "identifier": "SALONI",
                    "designerIdentifier": "SALONI",
                    "count": 1,
                    "label": "SALONI",
                    "value": "ads_f10003_ntk_cs%3A%22SALONI%22"
                },
                {
                    "identifier": "SASUPHI",
                    "designerIdentifier": "SASUPHI",
                    "count": 3,
                    "label": "SASUPHI",
                    "value": "ads_f10003_ntk_cs%3A%22SASUPHI%22"
                },
                {
                    "identifier": "SEA",
                    "designerIdentifier": "SEA",
                    "count": 4,
                    "label": "SEA",
                    "value": "ads_f10003_ntk_cs%3A%22SEA%22"
                },
                {
                    "identifier": "SELFPORTRAIT",
                    "designerIdentifier": "SELFPORTRAIT",
                    "count": 5,
                    "label": "SELF-PORTRAIT",
                    "value": "ads_f10003_ntk_cs%3A%22SELF-PORTRAIT%22"
                },
                {
                    "identifier": "SHUSHUTONG",
                    "designerIdentifier": "SHUSHUTONG",
                    "count": 3,
                    "label": "SHUSHU/TONG",
                    "value": "ads_f10003_ntk_cs%3A%22SHUSHU%2FTONG%22"
                },
                {
                    "identifier": "SIMKHAI",
                    "designerIdentifier": "SIMKHAI",
                    "count": 1,
                    "label": "SIMKHAI",
                    "value": "ads_f10003_ntk_cs%3A%22SIMKHAI%22"
                },
                {
                    "identifier": "SLVRLAKE",
                    "designerIdentifier": "SLVRLAKE",
                    "count": 2,
                    "label": "SLVRLAKE",
                    "value": "ads_f10003_ntk_cs%3A%22SLVRLAKE%22"
                },
                {
                    "identifier": "SPANX",
                    "designerIdentifier": "SPANX",
                    "count": 1,
                    "label": "SPANX",
                    "value": "ads_f10003_ntk_cs%3A%22SPANX%22"
                },
                {
                    "identifier": "SPORTYANDRICH",
                    "designerIdentifier": "SPORTYANDRICH",
                    "count": 4,
                    "label": "SPORTY & RICH",
                    "value": "ads_f10003_ntk_cs%3A%22SPORTY+%26+RICH%22"
                },
                {
                    "identifier": "STAUD",
                    "designerIdentifier": "STAUD",
                    "count": 2,
                    "label": "STAUD",
                    "value": "ads_f10003_ntk_cs%3A%22STAUD%22"
                },
                {
                    "identifier": "STELLAMCCARTNEY",
                    "designerIdentifier": "STELLAMCCARTNEY",
                    "count": 12,
                    "label": "STELLA MCCARTNEY",
                    "value": "ads_f10003_ntk_cs%3A%22STELLA+MCCARTNEY%22"
                },
                {
                    "identifier": "STOULS",
                    "designerIdentifier": "STOULS",
                    "count": 3,
                    "label": "STOULS",
                    "value": "ads_f10003_ntk_cs%3A%22STOULS%22"
                },
                {
                    "identifier": "SUZIEKONDI",
                    "designerIdentifier": "SUZIEKONDI",
                    "count": 1,
                    "label": "SUZIE KONDI",
                    "value": "ads_f10003_ntk_cs%3A%22SUZIE+KONDI%22"
                },
                {
                    "identifier": "THANKYOUHAVEAGOODDAY",
                    "designerIdentifier": "THANKYOUHAVEAGOODDAY",
                    "count": 2,
                    "label": "THANK YOU HAVE A GOOD DAY",
                    "value": "ads_f10003_ntk_cs%3A%22THANK+YOU+HAVE+A+GOOD+DAY%22"
                },
                {
                    "identifier": "38088",
                    "designerIdentifier": "38088",
                    "count": 3,
                    "label": "THE ATTICO",
                    "value": "ads_f10003_ntk_cs%3A%22THE+ATTICO%22"
                },
                {
                    "identifier": "THEELDERSTATESMAN",
                    "designerIdentifier": "THEELDERSTATESMAN",
                    "count": 1,
                    "label": "THE ELDER STATESMAN",
                    "value": "ads_f10003_ntk_cs%3A%22THE+ELDER+STATESMAN%22"
                },
                {
                    "identifier": "THEFRANKIESHOP",
                    "designerIdentifier": "THEFRANKIESHOP",
                    "count": 21,
                    "label": "THE FRANKIE SHOP",
                    "value": "ads_f10003_ntk_cs%3A%22THE+FRANKIE+SHOP%22"
                },
                {
                    "identifier": "THENORTHFACE",
                    "designerIdentifier": "THENORTHFACE",
                    "count": 9,
                    "label": "THE NORTH FACE",
                    "value": "ads_f10003_ntk_cs%3A%22THE+NORTH+FACE%22"
                },
                {
                    "identifier": "THEROW",
                    "designerIdentifier": "THEROW",
                    "count": 19,
                    "label": "THE ROW",
                    "value": "ads_f10003_ntk_cs%3A%22THE+ROW%22"
                },
                {
                    "identifier": "THEORY",
                    "designerIdentifier": "THEORY",
                    "count": 8,
                    "label": "THEORY",
                    "value": "ads_f10003_ntk_cs%3A%22THEORY%22"
                },
                {
                    "identifier": "THIERRYCOLSON",
                    "designerIdentifier": "THIERRYCOLSON",
                    "count": 1,
                    "label": "THIERRY COLSON",
                    "value": "ads_f10003_ntk_cs%3A%22THIERRY+COLSON%22"
                },
                {
                    "identifier": "THOMBROWNE",
                    "designerIdentifier": "THOMBROWNE",
                    "count": 5,
                    "label": "THOM BROWNE",
                    "value": "ads_f10003_ntk_cs%3A%22THOM+BROWNE%22"
                },
                {
                    "identifier": "TOMFORD",
                    "designerIdentifier": "TOMFORD",
                    "count": 7,
                    "label": "TOM FORD",
                    "value": "ads_f10003_ntk_cs%3A%22TOM+FORD%22"
                },
                {
                    "identifier": "TORYBURCH",
                    "designerIdentifier": "TORYBURCH",
                    "count": 1,
                    "label": "TORY BURCH",
                    "value": "ads_f10003_ntk_cs%3A%22TORY+BURCH%22"
                },
                {
                    "identifier": "TOTME",
                    "designerIdentifier": "TOTME",
                    "count": 34,
                    "label": "TOTEME",
                    "value": "ads_f10003_ntk_cs%3A%22TOTEME%22"
                },
                {
                    "identifier": "TOVE",
                    "designerIdentifier": "TOVE",
                    "count": 2,
                    "label": "TOVE",
                    "value": "ads_f10003_ntk_cs%3A%22TOVE%22"
                },
                {
                    "identifier": "ULLAJOHNSON",
                    "designerIdentifier": "ULLAJOHNSON",
                    "count": 4,
                    "label": "ULLA JOHNSON",
                    "value": "ads_f10003_ntk_cs%3A%22ULLA+JOHNSON%22"
                },
                {
                    "identifier": "VALENTINOGARAVANI",
                    "designerIdentifier": "VALENTINOGARAVANI",
                    "count": 15,
                    "label": "VALENTINO GARAVANI",
                    "value": "ads_f10003_ntk_cs%3A%22VALENTINO+GARAVANI%22"
                },
                {
                    "identifier": "VARLEY",
                    "designerIdentifier": "VARLEY",
                    "count": 12,
                    "label": "VARLEY",
                    "value": "ads_f10003_ntk_cs%3A%22VARLEY%22"
                },
                {
                    "identifier": "VERONICABEARD",
                    "designerIdentifier": "VERONICABEARD",
                    "count": 20,
                    "label": "VERONICA BEARD",
                    "value": "ads_f10003_ntk_cs%3A%22VERONICA+BEARD%22"
                },
                {
                    "identifier": "VERONICADEPIANTE",
                    "designerIdentifier": "VERONICADEPIANTE",
                    "count": 9,
                    "label": "VERONICA DE PIANTE",
                    "value": "ads_f10003_ntk_cs%3A%22VERONICA+DE+PIANTE%22"
                },
                {
                    "identifier": "VERSACE",
                    "designerIdentifier": "VERSACE",
                    "count": 7,
                    "label": "VERSACE",
                    "value": "ads_f10003_ntk_cs%3A%22VERSACE%22"
                },
                {
                    "identifier": "VICTORIABECKHAM",
                    "designerIdentifier": "VICTORIABECKHAM",
                    "count": 4,
                    "label": "VICTORIA BECKHAM",
                    "value": "ads_f10003_ntk_cs%3A%22VICTORIA+BECKHAM%22"
                },
                {
                    "identifier": "WARDROBENYC",
                    "designerIdentifier": "WARDROBENYC",
                    "count": 8,
                    "label": "WARDROBE.NYC",
                    "value": "ads_f10003_ntk_cs%3A%22WARDROBE.NYC%22"
                },
                {
                    "identifier": "WENORWEGIANS",
                    "designerIdentifier": "WENORWEGIANS",
                    "count": 1,
                    "label": "WE NORWEGIANS",
                    "value": "ads_f10003_ntk_cs%3A%22WE+NORWEGIANS%22"
                },
                {
                    "identifier": "YVESSALOMON",
                    "designerIdentifier": "YVESSALOMON",
                    "count": 15,
                    "label": "YVES SALOMON",
                    "value": "ads_f10003_ntk_cs%3A%22YVES+SALOMON%22"
                },
                {
                    "identifier": "TERNE",
                    "designerIdentifier": "TERNE",
                    "count": 2,
                    "label": "ÉTERNE",
                    "value": "ads_f10003_ntk_cs%3A%22%C3%89TERNE%22"
                }
            ],
            "identifier": "Brand",
            "label": "Designer"
        },
        {
            "entry": [
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.xxxs",
                    "count": 19,
                    "label": "XXXS",
                    "value": "ads_f15008_ntk_cs%3A%22XXXS%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.xxs",
                    "count": 268,
                    "label": "XXS",
                    "value": "ads_f15008_ntk_cs%3A%22XXS%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.xs",
                    "count": 804,
                    "label": "XS",
                    "value": "ads_f15008_ntk_cs%3A%22XS%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.s",
                    "count": 865,
                    "label": "S",
                    "value": "ads_f15008_ntk_cs%3A%22S%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.m",
                    "count": 936,
                    "label": "M",
                    "value": "ads_f15008_ntk_cs%3A%22M%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.l",
                    "count": 859,
                    "label": "L",
                    "value": "ads_f15008_ntk_cs%3A%22L%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.xl",
                    "count": 640,
                    "label": "XL",
                    "value": "ads_f15008_ntk_cs%3A%22XL%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.xxl",
                    "count": 294,
                    "label": "XXL",
                    "value": "ads_f15008_ntk_cs%3A%22XXL%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.xxxl",
                    "count": 99,
                    "label": "3XL",
                    "value": "ads_f15008_ntk_cs%3A%223XL%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.xxxxl",
                    "count": 10,
                    "label": "4XL",
                    "value": "ads_f15008_ntk_cs%3A%224XL%22"
                }
            ],
            "identifier": "SIZE_SCHEME_CLOTHING",
            "schemaLabel": "SML",
            "schemaIdentifier": "SIZE.SCHEMA.PUBLIC.NAP.CLOTHING.SML",
            "label": "Clothing Size",
            "selected": "True"
        },
        {
            "entry": [
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.30",
                    "count": 20,
                    "label": "FR 30",
                    "value": "ads_f20008_ntk_cs%3A%22FR+30%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.32",
                    "count": 269,
                    "label": "FR 32",
                    "value": "ads_f20008_ntk_cs%3A%22FR+32%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.34",
                    "count": 795,
                    "label": "FR 34",
                    "value": "ads_f20008_ntk_cs%3A%22FR+34%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.36",
                    "count": 833,
                    "label": "FR 36",
                    "value": "ads_f20008_ntk_cs%3A%22FR+36%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.38",
                    "count": 912,
                    "label": "FR 38",
                    "value": "ads_f20008_ntk_cs%3A%22FR+38%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.40",
                    "count": 817,
                    "label": "FR 40",
                    "value": "ads_f20008_ntk_cs%3A%22FR+40%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.42",
                    "count": 548,
                    "label": "FR 42",
                    "value": "ads_f20008_ntk_cs%3A%22FR+42%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.44",
                    "count": 246,
                    "label": "FR 44",
                    "value": "ads_f20008_ntk_cs%3A%22FR+44%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.46",
                    "count": 87,
                    "label": "FR 46",
                    "value": "ads_f20008_ntk_cs%3A%22FR+46%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.48",
                    "count": 10,
                    "label": "FR 48",
                    "value": "ads_f20008_ntk_cs%3A%22FR+48%22"
                }
            ],
            "identifier": "SIZE_SCHEME_CLOTHING",
            "schemaLabel": "FR",
            "schemaIdentifier": "SIZE.SCHEMA.PUBLIC.NAP.CLOTHING.FR",
            "label": "Clothing Size",
            "selected": "True"
        },
        {
            "entry": [
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.XXXS",
                    "count": 19,
                    "label": "XXXS",
                    "value": "ads_f10002_ntk_cs%3A%22XXXS%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.XXS",
                    "count": 267,
                    "label": "XXS",
                    "value": "ads_f10002_ntk_cs%3A%22XXS%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.XS",
                    "count": 653,
                    "label": "XS",
                    "value": "ads_f10002_ntk_cs%3A%22XS%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.S",
                    "count": 846,
                    "label": "S",
                    "value": "ads_f10002_ntk_cs%3A%22S%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.M",
                    "count": 753,
                    "label": "M",
                    "value": "ads_f10002_ntk_cs%3A%22M%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.L",
                    "count": 819,
                    "label": "L",
                    "value": "ads_f10002_ntk_cs%3A%22L%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.XL",
                    "count": 628,
                    "label": "XL",
                    "value": "ads_f10002_ntk_cs%3A%22XL%22"
                },
                {
                    "identifier": "SIZE.SCHEMA.VALUE_ID.XXL",
                    "count": 294,
                    "label": "XXL",
                    "value": "ads_f10002_ntk_cs%3A%22XXL%22"
                }
            ],
            "identifier": "SIZE_SCHEME",
            "schemaLabel": "Size",
            "schemaIdentifier": "SIZE.SCHEMA.PUBLIC.INTERNATIONAL",
            "label": ""
        },
        {
            "entry": [
                {
                    "lower": "*",
                    "upper": "250",
                    "count": 19,
                    "value": "price_USD_4000000000000001072%3A%28%7B*+250%7D+250%29"
                },
                {
                    "lower": "250",
                    "upper": "500",
                    "count": 57,
                    "value": "price_USD_4000000000000001072%3A%28%7B250+500%7D+500%29"
                },
                {
                    "lower": "500",
                    "upper": "1000",
                    "count": 172,
                    "value": "price_USD_4000000000000001072%3A%28%7B500+1000%7D+1000%29"
                },
                {
                    "lower": "1000",
                    "upper": "2000",
                    "count": 313,
                    "value": "price_USD_4000000000000001072%3A%28%7B1000+2000%7D+2000%29"
                },
                {
                    "lower": "2000",
                    "upper": "5000",
                    "count": 608,
                    "value": "price_USD_4000000000000001072%3A%28%7B2000+5000%7D+5000%29"
                },
                {
                    "lower": "5000",
                    "upper": "10000",
                    "count": 167,
                    "value": "price_USD_4000000000000001072%3A%28%7B5000+10000%7D+10000%29"
                },
                {
                    "lower": "10000",
                    "upper": "20000",
                    "count": 28,
                    "value": "price_USD_4000000000000001072%3A%28%7B10000+20000%7D+20000%29"
                },
                {
                    "lower": "20000",
                    "upper": "*",
                    "count": 0,
                    "value": "price_USD_4000000000000001072%3A%28%7B20000+*%7D%29"
                }
            ],
            "identifier": "price_USD_4000000000000001072",
            "lower": {
                "amount": 16600,
                "divisor": 100
            },
            "upper": {
                "amount": 1761800,
                "divisor": 100
            },
            "currency": {
                "symbol": "$",
                "label": "USD"
            },
            "label": "Price"
        }
    ],
    "recordSetCount": 60,
    "breadCrumbTrailEntryView": [
        {
            "label": "Clothing",
            "value": "3074457345616690677",
            "type_": "FACET_ENTRY_CATEGORY"
        },
        {
            "label": "Coats and Jackets",
            "value": "3074457345616748262",
            "type_": "FACET_ENTRY_CATEGORY"
        }
    ],
    "totalPages": 23,
    "selectedCategory": {
        "identifier": "APAC__Clothing",
        "count": 1364,
        "attributes": [
            {
                "identifier": "CAT_ATTR_PAGE_TYPE",
                "values": [
                    {
                        "identifier": "STANDARD",
                        "label": "Standard"
                    }
                ]
            }
        ],
        "label": "Clothing",
        "seo": {
            "seoURLKeyword": "/clothing"
        },
        "categoryId": "3074457345616690677",
        "child": {
            "identifier": "APAC__Coats_And_Jackets_CLOTHING",
            "attributes": [
                {
                    "identifier": "CAT_ATTR_PAGE_TYPE",
                    "values": [
                        {
                            "identifier": "STANDARD",
                            "label": "Standard"
                        }
                    ]
                }
            ],
            "label": "Coats and Jackets",
            "seo": {
                "seoURLKeyword": "/clothing/coats-and-jackets",
                "title": "Designer Coats and Jackets for Women | NET-A-PORTER",
                "metaDescription": "Shop designer Coats and Jackets for women at NET-A-PORTER, the ultimate destination for luxury women's fashion. Explore our curated Clothing selection from over 800 of the world's top luxury brands.",
                "metaKeyword": "Women's Luxury Coats and Jackets, Women's Designer Coats and Jackets, Designer Coats and Jackets for Women, Luxury Coats and Jackets for Women, Women's Designer Clothing, Women's Luxury Clothing"
            },
            "categoryId": "3074457345616748262"
        }
    },
    "recordSetComplete": "false"
}

print(attr_lst['facets'])
# exit()
for attr in attr_lst['facets'][1:]:
    try:
        for attr_value in attr['entry']:
            tmp_df = pd.DataFrame(data={'Product_Category': ['Clothing'],
                                        'Category': ['Women'],
                                        'Subcategory1': ['Western'],
                                        'Subcategory2': ['Outerwear'],
                                        'Subcategory3': ['Jackets and Coats'],
                                        'Attr_Name': [''],
                                        'Attr_Value': ['']})
            tmp_df['Attr_Name'] = attr['label']
            tmp_df['Attr_Value'] = attr_value['label']
            tmp_df['Url'] = f'https://www.net-a-porter.com/en-us/shop/clothing/coats-and-jackets?facet={attr_value["value"]}'
            final_df = final_df._append(tmp_df)
    except Exception as e:
        print(attr_value, e)
    finally:
        print('Error Ocurred')

    print(len(final_df))
final_df.to_csv('Netaporter_jackets_links_with_attrs.csv', index=False, index_label=False)
