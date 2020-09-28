from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

my_url = 'https://store.steampowered.com/search/?specials=1'
# grabs url
uClient = uReq(my_url)
# saves html source code to var
page_html = uClient.read()
# parsing
page_soup = soup(page_html, "html.parser")


drops = page_soup.findAll('div',{'class':'responsive_search_name_combined'})
# use drop as test
drop = drops[0]




# Sets up the five files
page_1 = open('Steam_sales_page_1.csv', 'w')
page_2 = open('Steam_sales_page_2.csv', 'w')
page_3 = open('Steam_sales_page_3.csv', 'w')
page_4 = open('Steam_sales_page_4.csv', 'w')
page_5 = open('Steam_sales_page_5.csv', 'w')
headers = [' Name ', ' Original Price ', ' Discount Percent ', ' Discount Price ']
output_writer = csv.DictWriter(page_1, fieldnames=headers)
output_writer2 = csv.DictWriter(page_2, fieldnames=headers)
output_writer3 = csv.DictWriter(page_3, fieldnames=headers)
output_writer4 = csv.DictWriter(page_4, fieldnames=headers)
output_writer5 = csv.DictWriter(page_5, fieldnames=headers)
output_writer.writeheader()
output_writer2.writeheader()
output_writer3.writeheader()
output_writer4.writeheader()
output_writer5.writeheader()


# for loop sorting data
amount = 0
for i in drops:
    # this sorts the names of the games
    names = ' ' + i.div.span.text + ' '
    discount = i.find('div',{'class':'col search_discount responsive_secondrow'})
    # this sorts the discounts
    if discount.text.strip() == '':
        dis = ' Discount hidden '
    else:
        dis = ' ' + discount.text.strip() + ' '
    price = i.find('div',{'class':'col search_price discounted responsive_secondrow'})
    # this sorts the orginal price and discount price
    if hasattr(price, 'text'):
        sub1 = price.text.replace('$', ' $', 2)
        sub2 = sub1.replace(' $', '$', 1)
        sub_list = sub2.split()
        original_price = ' ' + sub_list[0] + ' '
        discount_price = ' ' + sub_list[1] + ' '
    else:
        original_price = ' Price hidden '
        discount_price = ' Price hidden '
    amount += 1
    # adding the data to the files
    if amount <= 10:
        big_list = {' Name ': names, ' Original Price ': original_price, ' Discount Percent ': dis, ' Discount Price ': discount_price}
        page_1.write('\n..........................................................\n')
        output_writer.writerow(big_list)
    elif amount > 10 and amount <= 20:
        big_list = {' Name ': names, ' Original Price ': original_price, ' Discount Percent ': dis, ' Discount Price ': discount_price}
        page_2.write('\n..........................................................\n')
        output_writer2.writerow(big_list)
    elif amount > 20 and amount <= 30:
        big_list = {' Name ': names, ' Original Price ': original_price, ' Discount Percent ': dis, ' Discount Price ': discount_price}
        page_3.write('\n..........................................................\n')
        output_writer3.writerow(big_list)
    elif amount > 30 and amount <= 40:
        big_list = {' Name ': names, ' Original Price ': original_price, ' Discount Percent ': dis, ' Discount Price ': discount_price}
        page_4.write('\n..........................................................\n')
        output_writer4.writerow(big_list)
    elif amount > 40 and amount <= 50:
        big_list = {' Name ': names, ' Original Price ': original_price, ' Discount Percent ': dis, ' Discount Price ': discount_price}
        page_5.write('\n..........................................................\n')
        output_writer5.writerow(big_list)
# ends and closes the files
page_1.write('\nPage 1 of 5\n')
page_2.write('\nPage 2 of 5\n')
page_3.write('\nPage 3 of 5\n')
page_4.write('\nPage 4 of 5\n')
page_5.write('\nPage 5 of 5\n')
uClient.close()
page_1.close()
page_2.close()
page_3.close()
page_4.close()
page_5.close()
print('Done!')
