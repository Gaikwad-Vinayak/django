from bs4 import BeautifulSoup
import requests
url='https://www.flipkart.com/moto-g70-lte-4-gb-ram-64-rom-11-inch-wi-fi-4g-tablet-modernist-teal/p/itmce2e58ddcfc16?pid=TABG9NNXJHBGU6WJ&lid=LSTTABG9NNXJHBGU6WJSVV6NQ&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_2154a61e-75a1-487d-bb56-4f63d4a78b10_3_Z1DO69MRGF0R_MC.TABG9NNXJHBGU6WJ&ppt=clp&ppn=electronics-big-savings-days-store&ssid=63rfdf9pz40000001642689864930&otracker=clp_pmu_v2_Wide%2BCollection_2_3.productCard.PMU_V2_Moto%2Bg70%2BLTE%2B4%2BGB%2BRAM%2B64%2BGB%2BROM%2B11%2BInch%2Bwith%2BWi-Fi%252B4G%2BTablet%2B%2528Modernist%2BTeal%2529_tablets-bbd21-sale-store_TABG9NNXJHBGU6WJ_neo%2Fmerchandising_1&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Wide%2BCollection_LIST_productCard_cc_2_NA_view-all&cid=TABG9NNXJHBGU6WJ'
res=requests.get(url)
html_containt=res.content
soup = BeautifulSoup(html_containt, 'html.parser')


print(soup.title.name)
