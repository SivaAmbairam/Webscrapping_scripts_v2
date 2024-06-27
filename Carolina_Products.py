import json

from module_package import *
import random
from DrissionPage import ChromiumPage, ChromiumOptions

def write_visited_log(url):
    output_dir = os.path.join('Output', 'temp')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, 'Visited_Carolina_urls.txt')
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'{url}\n')

def read_log_file():
    file_path = os.path.join('Output', 'temp', 'Visited_Carolina_urls.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as read_file:
            return read_file.read().split('\n')
    return []



def random_sleep(min_seconds=1, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)


if __name__ == '__main__':
    timestamp = datetime.now().date().strftime('%Y%m%d')
    file_name = Carolina_Products
    url = 'https://www.carolina.com/'
    # url = 'https://www.carolina.com/building-blocks-of-science-kits-grades-k-to-2/building-blocks-of-science-a-new-generation-discovering-plants/FAM_514001.pr'
    # url = 'https://www.carolina.com/human-genetics/how-do-polygenic-risk-scores-stack-up-kit/214828.pr'
    base_url = 'https://www.carolina.com'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'sib_cuid=f9bfa3f7-bb99-4d53-9b93-e31d2d79b617; _gcl_au=1.1.143815260.1713870676; _fbp=fb.1.1713870676303.1039358499; userty.core.p.89cc84=__2VySWQiOiIzOTMxY2I0YzcyNmZhMTcyMjhjY2JiYzkzZWZkOWEzZiJ9eyJ1c; hubspotutk=d1ce3404a88b213b8f3d1c5303da6434; lhnContact=0e841d9b-aa89-4142-bcd9-0c6a7f768fe4-24984-NXFAoQd; BVBRANDID=64921e2f-2bd3-4794-a737-3ebb4039539b; acceptCookieTermsCookie=; wp36423="WZXVWDDDDDDCTALMVZA-WZWT-XCVY-ITKC-ATBCHIBBUYIJDgNssDJHkhspgH_JhtDD"; _ga_QTJ7CYYKHD=GS1.1.1714720419.1.1.1714720423.0.0.0; _gid=GA1.2.1823798336.1719284576; __hssrc=1; lhnStorageType=cookie; BVImplmain_site=4902; lhnRefresh=cbf99534-f01a-41cd-a915-30fa111daf7e; lhnJWT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ2aXNpdG9yIiwiZG9tYWluIjoiIiwiZXhwIjoxNzE5NDcyMTg3LCJpYXQiOjE3MTkzODU3ODcsImlzcyI6eyJhcHAiOiJqc19zZGsiLCJjbGllbnQiOjI0OTg0LCJjbGllbnRfbGV2ZWwiOiJiYXNpYyIsImxobnhfZmVhdHVyZXMiOltdLCJ2aXNpdG9yX3RyYWNraW5nIjp0cnVlfSwianRpIjoiMGU4NDFkOWItYWE4OS00MTQyLWJjZDktMGM2YTdmNzY4ZmU0IiwicmVzb3VyY2UiOnsiaWQiOiIwZTg0MWQ5Yi1hYTg5LTQxNDItYmNkOS0wYzZhN2Y3NjhmZTQtMjQ5ODQtTlhGQW9RZCIsInR5cGUiOiJFbGl4aXIuTGhuRGIuTW9kZWwuQ29yZS5WaXNpdG9yIn19.LjOp2znrtB_VcNJjsZC2_hQ_c8yBn4glqBmeP-FmpyY; wisepops_visits=%5B%222024-06-26T15%3A32%3A54.117Z%22%2C%222024-06-26T15%3A29%3A21.633Z%22%2C%222024-06-26T15%3A27%3A24.129Z%22%2C%222024-06-26T15%3A09%3A15.828Z%22%2C%222024-06-26T15%3A00%3A36.576Z%22%2C%222024-06-26T15%3A00%3A28.949Z%22%2C%222024-06-26T15%3A00%3A21.906Z%22%2C%222024-06-26T13%3A27%3A20.407Z%22%2C%222024-06-26T08%3A21%3A34.106Z%22%2C%222024-06-26T08%3A21%3A13.849Z%22%5D; SSID=CQBw7R04AAAAAABQlydm2gKDDFCXJ2ZIAAAAAAAAAAAAAQZ9ZgDSFc7HAAPFchsAUJcnZj4AjTcBA_8VJwDfyHNmFQAeKwEDY9QlAFCXJ2Y-AIIxAQFsdCYAAQZ9ZgEA; SSSC=695.G7361018486023455450.72|51150.1798853:76574.2479203:78210.2520172:79757.2561535; serverRoute=CrBYX3eODFu9IG8Im21hqKaSV93jOTGy2F9c9drhHFPbpHQQXCT_!352584670!1719469569934-app1; CBSESSIONID=CrBYX3eODFu9IG8Im21hqKaSV93jOTGy2F9c9drhHFPbpHQQXCT_!352584670; BVBRANDSID=6c2b797d-fcdb-4f8b-9016-937a971e35ca; _hp2_ses_props.324705833=%7B%22r%22%3A%22https%3A%2F%2Fwww.carolina.com%2Fbuilding-blocks-of-science-kits-grades-k-to-2%2Fbuilding-blocks-of-science-a-new-generation-discovering-plants%2FFAM_514001.pr%22%2C%22ts%22%3A1719469572148%2C%22d%22%3A%22www.carolina.com%22%2C%22h%22%3A%22%2Fbuilding-blocks-of-science-kits-grades-k-to-2%2Fbuilding-blocks-of-science-a-new-generation-discovering-plants%2FFAM_514001.pr%22%7D; __hstc=5999596.d1ce3404a88b213b8f3d1c5303da6434.1713870678828.1719428534010.1719469578399.70; SSRT=lQd9ZgADAA; _gat_UA-159461-1=1; SSOD=AMkHAAAASAAxWEYA4QEAAFCXJ2akB31mAwCM6TgACgAAAANMK2Y2LXxmAABVWzQAAgAAAJCONGa5jjRmAACoqDcAAgAAAJCONGa5jjRmAAAAAA; _ga_2J2J1CBM0T=GS1.1.1719469561.94.1.1719469990.44.0.0; wisepops=%7B%22popups%22%3A%7B%22472246%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1719389190833%7D%2C%22492430%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1716199760335%2C%22cl%22%3A1%7D%2C%22495677%22%3A%7B%22dc%22%3A1%2C%22d%22%3A1717998220810%2C%22cl%22%3A1%7D%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A53%2C%22cid%22%3A%2248011%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; _ga=GA1.2.259678292.1713870676; wisepops_visitor=%7B%22JFEHQjxXN3%22%3A%225e155381-f6fa-4d54-9b1c-28e73243d7bf%22%7D; wisepops_session=%7B%22arrivalOnSite%22%3A%222024-06-27T06%3A26%3A12.181Z%22%2C%22mtime%22%3A1719469991005%2C%22pageviews%22%3A3%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22sticky%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3Anull%2C%22utm%22%3A%7B%7D%2C%22testIp%22%3Anull%7D; _uetsid=be8c60b0324b11ef8bd4e58a690e280d; _uetvid=3409c3a0016211efb8692f184a9b3ea5; _hp2_id.324705833=%7B%22userId%22%3A%221374166632732052%22%2C%22pageviewId%22%3A%225889596680827695%22%2C%22sessionId%22%3A%221536848784218781%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; datadome=3KEjgP5LA6Ow97t4hjC5oY2_F3JuiVBmB3yuV1BkP7OSaCNpyN5xl0a8ijzdl7Ew3ZaMT~DE34R_jMr65PKpK20txzPdkhchSLxqJs6ywz06X7JvNB025o74HAun7BhL; __hssc=5999596.3.1719469578399; userty.core.s.89cc84=__WQiOiI0OWQ3NGFmZjQ0NWQ2OWIyZDYwNWU0ZTMyNjc5ZWIwNCIsInN0IjoxNzE5NDY5NTc2OTQwLCJyZWFkeSI6dHJ1ZSwid3MiOiJ7XCJ3XCI6ODg3LFwiaFwiOjczMH0iLCJzZSI6MTcxOTQ3MTgwNzM0NywicHYiOjR9eyJza',
        'Host': 'www.carolina.com',
        'Referer': 'https://www.carolina.com/butterfly-kits/butterflies-in-the-classroom-kit-with-live-caterpillars/144014.pr',
        'Sec-Ch-Device-Memory': '8',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Arch': '"x86"',
        'Sec-Ch-Ua-Full-Version-List': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.114", "Google Chrome";v="126.0.6478.114"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Model': '""',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    soup = get_soup(url, headers)
    content = soup.find('li', class_='nav-item c-nav-menu-link').find_all('li', class_='row c-nav-menu-l1')
    for single_content in content:
        inner_content = single_content.find('div', class_='c-nav-menu-subnav col-12 col-lg-7')
        product_category = inner_content.find('h3', class_='d-none d-lg-block').text.strip()
        if inner_content.find('ul', class_='row'):
            all_urls = inner_content.find('ul', class_='row').find_all('li')
            for single_url in all_urls:
                product_sub_name = single_url.a.text.strip()
                main_url = f"{base_url}{single_url.a['href']}"
                print(f'main_url -----------> {main_url}')
                if main_url in read_log_file():
                    continue
                random_sleep(1, 10)
                inner_request = get_soup(main_url, headers)
                if inner_request is None:
                    continue
                if inner_request.find('div', class_='row px-1'):
                    inner_data = inner_request.find('div', class_='row px-1').find_all('a', class_='c-category-list')
                    for single_data in inner_data:
                        inner_url = f'{base_url}{single_data["href"]}'
                        inner_category = strip_it(single_data.find('h3', class_='c-category-title').text.strip())
                        sub_category = single_url.a.text.strip()
                        product_sub = f'{sub_category}-{inner_category}'
                        random_sleep(1, 10)
                        other_request = get_soup(inner_url, headers)
                        if other_request.find('div', class_='row px-1'):
                            inner_data = other_request.find('div', class_='row px-1').find_all('a', class_='c-category-list')
                            for single_datas in inner_data:
                                inner_process_url = f'{base_url}{single_datas["href"]}'
                                inner_categories = strip_it(single_datas.find('h3', class_='c-category-title').text.strip())
                                product_sub_category = f'{product_sub}-{inner_categories}'
                                inner_process_request = get_soup(inner_process_url, headers)
                                '''GET PAGINATION'''
                                if inner_process_request.find('ul',
                                                              class_='c-pagination pagination justify-content-start pagination-lg'):
                                    total_page = inner_process_request.find('ul',
                                                                            class_='c-pagination pagination justify-content-start pagination-lg').find_all(
                                        'li')[-2].text.strip()
                                    for i in range(0, int(total_page)):
                                        number = int(i) * int(60)
                                        page_link = f'{main_url}?Nf=product.cbsLowPrice%7CGT+0.0%7C%7Cproduct.startDate%7CLTEQ+1.71504E12%7C%7Cproduct.startDate%7CLTEQ+1.71504E12&No={number}&Nr=&'
                                        if page_link in read_log_file():
                                            continue
                                        random_sleep(1, 10)
                                        page_soup = get_soup(page_link, headers)
                                        if page_soup is None:
                                            continue
                                        inner_data = page_soup.find_all('div', class_='c-feature-product qv-model')
                                        for single_data in inner_data:
                                            product_url = f'{base_url}{single_data.find("a")["href"]}'
                                            print(product_url)
                                            random_sleep(1, 10)
                                            product_request = get_soup(product_url, headers)
                                            if product_request is None:
                                                continue
                                            content = product_request.find('script', type='application/ld+json')
                                            replace_content = str(content).replace(
                                                '<script type="application/ld+json">', '').replace('</script>', '')
                                            json_content = json.loads(replace_content)
                                            for inner_json in json_content['offers']:
                                                '''PRICE'''
                                                try:
                                                    product_price = f"$ {inner_json['price']}"
                                                except:
                                                    product_price = ''
                                                '''PRODUCT URL'''
                                                try:
                                                    product_url = inner_json['url']
                                                except:
                                                    product_url = ''
                                                '''PRODUCT NAME'''
                                                try:
                                                    product_name = inner_json['name']
                                                    if re.search('Pack of \\d+', str(product_name)):
                                                        product_quantity = re.search('Pack of \\d+', str(product_name)).group().replace(
                                                            'Pack of', '').strip()
                                                    else:
                                                        product_quantity = 1
                                                except:
                                                    product_name = json_content['name']
                                                    product_quantity = '1'
                                                '''PRODUCT DESC'''
                                                try:
                                                    desc = inner_json['description']
                                                    desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                                    product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                                except:
                                                    desc = json_content['description']
                                                    desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                                    product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                                '''IMAGE URL'''
                                                try:
                                                    image_url = inner_json['image']
                                                except:
                                                    image_url = json_content['image']
                                                '''PRODUCT ID'''
                                                try:
                                                    product_id = inner_json['sku']
                                                except:
                                                    product_id = json_content['sku']
                                                if product_id in read_log_file():
                                                    continue
                                                print('current datetime------>', datetime.now())
                                                dictionary = {
                                                    'Carolina_product_category': product_category,
                                                    'Carolina_product_sub_category': product_sub_category,
                                                    'Carolina_product_id': product_id,
                                                    'Carolina_product_name': product_name,
                                                    'Carolina_product_quantity': product_quantity,
                                                    'Carolina_product_price': product_price,
                                                    'Carolina_product_url': product_url,
                                                    'Carolina_image_url': image_url,
                                                    'Carolina_product_desc': product_desc
                                                }
                                                articles_df = pd.DataFrame([dictionary])
                                                articles_df.drop_duplicates(
                                                    subset=['Carolina_product_id', 'Carolina_product_name'], keep='first',
                                                    inplace=True)
                                                output_dir = 'Output'
                                                if not os.path.exists(output_dir):
                                                    os.makedirs(output_dir)
                                                file_path = os.path.join(output_dir, f'{file_name}.csv')
                                                if os.path.isfile(file_path):
                                                    articles_df.to_csv(file_path, index=False, header=False, mode='a')
                                                else:
                                                    articles_df.to_csv(file_path, index=False)

                                                write_visited_log(product_id)
                                        write_visited_log(page_link)
                                else:
                                    inner_data = inner_process_request.find_all('div', class_='c-feature-product qv-model')
                                    for single_data in inner_data:
                                        product_url = f'{base_url}{single_data.find('a')["href"]}'
                                        print(product_url)
                                        random_sleep(1, 10)
                                        product_request = get_soup(product_url, headers)
                                        if product_request is None:
                                            continue
                                        content = product_request.find('script', type='application/ld+json')
                                        replace_content = str(content).replace(
                                            '<script type="application/ld+json">', '').replace('</script>', '')
                                        json_content = json.loads(replace_content)
                                        for inner_json in json_content['offers']:
                                            '''PRICE'''
                                            try:
                                                product_price = f"$ {inner_json['price']}"
                                            except:
                                                product_price = ''
                                            '''PRODUCT URL'''
                                            try:
                                                product_url = inner_json['url']
                                            except:
                                                product_url = ''
                                            '''PRODUCT NAME'''
                                            try:
                                                product_name = inner_json['name']
                                                if re.search('Pack of \\d+', str(product_name)):
                                                    product_quantity = re.search('Pack of \\d+',
                                                                                 str(product_name)).group().replace(
                                                        'Pack of', '').strip()
                                                else:
                                                    product_quantity = 1
                                            except:
                                                product_name = json_content['name']
                                                product_quantity = '1'
                                            '''PRODUCT DESC'''
                                            try:
                                                desc = inner_json['description']
                                                desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                                product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                            except:
                                                desc = json_content['description']
                                                desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                                product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                            '''IMAGE URL'''
                                            try:
                                                image_url = inner_json['image']
                                            except:
                                                image_url = json_content['image']
                                            '''PRODUCT ID'''
                                            try:
                                                product_id = inner_json['sku']
                                            except:
                                                product_id = json_content['sku']
                                            if product_id in read_log_file():
                                                continue
                                            print('current datetime------>', datetime.now())
                                            dictionary = {
                                                'Carolina_product_category': product_category,
                                                'Carolina_product_sub_category': product_sub_category,
                                                'Carolina_product_id': product_id,
                                                'Carolina_product_name': product_name,
                                                'Carolina_product_quantity': product_quantity,
                                                'Carolina_product_price': product_price,
                                                'Carolina_product_url': product_url,
                                                'Carolina_image_url': image_url,
                                                'Carolina_product_desc': product_desc
                                            }
                                            articles_df = pd.DataFrame([dictionary])
                                            articles_df.drop_duplicates(
                                                subset=['Carolina_product_id', 'Carolina_product_name'], keep='first',
                                                inplace=True)
                                            output_dir = 'Output'
                                            if not os.path.exists(output_dir):
                                                os.makedirs(output_dir)
                                            file_path = os.path.join(output_dir, f'{file_name}.csv')
                                            if os.path.isfile(file_path):
                                                articles_df.to_csv(file_path, index=False, header=False, mode='a')
                                            else:
                                                articles_df.to_csv(file_path, index=False)

                                            write_visited_log(product_id)
                        else:
                            product_sub_category = product_sub
                            '''GET PAGINATION'''
                            if other_request.find('ul',
                                                  class_='c-pagination pagination justify-content-start pagination-lg'):
                                total_page = other_request.find('ul',
                                                                class_='c-pagination pagination justify-content-start pagination-lg').find_all(
                                    'li')[-2].text.strip()
                                for i in range(0, int(total_page)):
                                    number = int(i) * int(60)
                                    page_link = f'{main_url}?Nf=product.cbsLowPrice%7CGT+0.0%7C%7Cproduct.startDate%7CLTEQ+1.71504E12%7C%7Cproduct.startDate%7CLTEQ+1.71504E12&No={number}&Nr=&'
                                    if page_link in read_log_file():
                                        continue
                                    random_sleep(1, 10)
                                    page_soup = get_soup(page_link, headers)
                                    if page_soup is None:
                                        continue
                                    inner_data = page_soup.find_all('div', class_='c-feature-product qv-model')
                                    for single_data in inner_data:
                                        product_url = f'{base_url}{single_data.find("a")["href"]}'
                                        print(product_url)
                                        random_sleep(1, 10)
                                        product_request = get_soup(product_url, headers)
                                        if product_request is None:
                                            continue
                                        content = product_request.find('script', type='application/ld+json')
                                        replace_content = str(content).replace(
                                            '<script type="application/ld+json">', '').replace('</script>', '')
                                        json_content = json.loads(replace_content)
                                        for inner_json in json_content['offers']:
                                            '''PRICE'''
                                            try:
                                                product_price = f"$ {inner_json['price']}"
                                            except:
                                                product_price = ''
                                            '''PRODUCT URL'''
                                            try:
                                                product_url = inner_json['url']
                                            except:
                                                product_url = ''
                                            '''PRODUCT NAME'''
                                            try:
                                                product_name = inner_json['name']
                                                if re.search('Pack of \\d+', str(product_name)):
                                                    product_quantity = re.search('Pack of \\d+',
                                                                                 str(product_name)).group().replace(
                                                        'Pack of', '').strip()
                                                else:
                                                    product_quantity = 1
                                            except:
                                                product_name = json_content['name']
                                                product_quantity = '1'
                                            '''PRODUCT DESC'''
                                            try:
                                                desc = inner_json['description']
                                                desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                                product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                            except:
                                                desc = json_content['description']
                                                desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                                product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                            '''IMAGE URL'''
                                            try:
                                                image_url = inner_json['image']
                                            except:
                                                image_url = json_content['image']
                                            '''PRODUCT ID'''
                                            try:
                                                product_id = inner_json['sku']
                                            except:
                                                product_id = json_content['sku']
                                            if product_id in read_log_file():
                                                continue
                                            print('current datetime------>', datetime.now())
                                            dictionary = {
                                                'Carolina_product_category': product_category,
                                                'Carolina_product_sub_category': product_sub_category,
                                                'Carolina_product_id': product_id,
                                                'Carolina_product_name': product_name,
                                                'Carolina_product_quantity': product_quantity,
                                                'Carolina_product_price': product_price,
                                                'Carolina_product_url': product_url,
                                                'Carolina_image_url': image_url,
                                                'Carolina_product_desc': product_desc
                                            }
                                            articles_df = pd.DataFrame([dictionary])
                                            articles_df.drop_duplicates(
                                                subset=['Carolina_product_id', 'Carolina_product_name'], keep='first',
                                                inplace=True)
                                            output_dir = 'Output'
                                            if not os.path.exists(output_dir):
                                                os.makedirs(output_dir)
                                            file_path = os.path.join(output_dir, f'{file_name}.csv')
                                            if os.path.isfile(file_path):
                                                articles_df.to_csv(file_path, index=False, header=False, mode='a')
                                            else:
                                                articles_df.to_csv(file_path, index=False)

                                            write_visited_log(product_id)
                                    write_visited_log(page_link)
                            else:
                                inner_data = other_request.find_all('div', class_='c-feature-product qv-model')
                                for single_data in inner_data:
                                    product_url = f'{base_url}{single_data.find("a")["href"]}'
                                    print(product_url)
                                    random_sleep(1, 10)
                                    product_request = get_soup(product_url, headers)
                                    if product_request is None:
                                        continue
                                    content = product_request.find('script', type='application/ld+json')
                                    replace_content = str(content).replace(
                                        '<script type="application/ld+json">', '').replace('</script>', '')
                                    json_content = json.loads(replace_content)
                                    for inner_json in json_content['offers']:
                                        '''PRICE'''
                                        try:
                                            product_price = f"$ {inner_json['price']}"
                                        except:
                                            product_price = ''
                                        '''PRODUCT URL'''
                                        try:
                                            product_url = inner_json['url']
                                        except:
                                            product_url = ''
                                        '''PRODUCT NAME'''
                                        try:
                                            product_name = inner_json['name']
                                            if re.search('Pack of \\d+', str(product_name)):
                                                product_quantity = re.search('Pack of \\d+',
                                                                             str(product_name)).group().replace(
                                                    'Pack of', '').strip()
                                            else:
                                                product_quantity = 1
                                        except:
                                            product_name = json_content['name']
                                            product_quantity = '1'
                                        '''PRODUCT DESC'''
                                        try:
                                            desc = inner_json['description']
                                            desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                            product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                        except:
                                            desc = json_content['description']
                                            desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                            product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                        '''IMAGE URL'''
                                        try:
                                            image_url = inner_json['image']
                                        except:
                                            image_url = json_content['image']
                                        '''PRODUCT ID'''
                                        try:
                                            product_id = inner_json['sku']
                                        except:
                                            product_id = json_content['sku']
                                        if product_id in read_log_file():
                                            continue
                                        print('current datetime------>', datetime.now())
                                        dictionary = {
                                            'Carolina_product_category': product_category,
                                            'Carolina_product_sub_category': product_sub_category,
                                            'Carolina_product_id': product_id,
                                            'Carolina_product_name': product_name,
                                            'Carolina_product_quantity': product_quantity,
                                            'Carolina_product_price': product_price,
                                            'Carolina_product_url': product_url,
                                            'Carolina_image_url': image_url,
                                            'Carolina_product_desc': product_desc
                                        }
                                        articles_df = pd.DataFrame([dictionary])
                                        articles_df.drop_duplicates(subset=['Carolina_product_id', 'Carolina_product_name'],
                                                                    keep='first', inplace=True)
                                        output_dir = 'Output'
                                        if not os.path.exists(output_dir):
                                            os.makedirs(output_dir)
                                        file_path = os.path.join(output_dir, f'{file_name}.csv')
                                        if os.path.isfile(file_path):
                                            articles_df.to_csv(file_path, index=False, header=False, mode='a')
                                        else:
                                            articles_df.to_csv(file_path, index=False)

                                        write_visited_log(product_id)
                else:
                    product_sub_category = product_sub_name
                    '''GET PAGINATION'''
                    if inner_request.find('ul', class_='c-pagination pagination justify-content-start pagination-lg'):
                        total_page = inner_request.find('ul',
                                                        class_='c-pagination pagination justify-content-start pagination-lg').find_all(
                            'li')[-2].text.strip()
                        for i in range(0, int(total_page)):
                            number = int(i) * int(60)
                            page_link = f'{main_url}?Nf=product.cbsLowPrice%7CGT+0.0%7C%7Cproduct.startDate%7CLTEQ+1.71504E12%7C%7Cproduct.startDate%7CLTEQ+1.71504E12&No={number}&Nr=&'
                            if page_link in read_log_file():
                                continue
                            random_sleep(1, 10)
                            page_soup = get_soup(page_link, headers)
                            if page_soup is None:
                                continue
                            inner_data = page_soup.find_all('div', class_='c-feature-product qv-model')
                            for single_data in inner_data:
                                product_url = f'{base_url}{single_data.find("a")["href"]}'
                                print(product_url)
                                random_sleep(1, 10)
                                product_request = get_soup(product_url, headers)
                                if product_request is None:
                                    continue
                                content = product_request.find('script', type='application/ld+json')
                                replace_content = str(content).replace(
                                    '<script type="application/ld+json">', '').replace('</script>', '')
                                json_content = json.loads(replace_content)
                                for inner_json in json_content['offers']:
                                    '''PRICE'''
                                    try:
                                        product_price = f"$ {inner_json['price']}"
                                    except:
                                        product_price = ''
                                    '''PRODUCT URL'''
                                    try:
                                        product_url = inner_json['url']
                                    except:
                                        product_url = ''
                                    '''PRODUCT NAME'''
                                    try:
                                        product_name = inner_json['name']
                                        if re.search('Pack of \\d+', str(product_name)):
                                            product_quantity = re.search('Pack of \\d+',
                                                                         str(product_name)).group().replace(
                                                'Pack of', '').strip()
                                        else:
                                            product_quantity = 1
                                    except:
                                        product_name = json_content['name']
                                        product_quantity = '1'
                                    '''PRODUCT DESC'''
                                    try:
                                        desc = inner_json['description']
                                        desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                        product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                    except:
                                        desc = json_content['description']
                                        desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                        product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                    '''IMAGE URL'''
                                    try:
                                        image_url = inner_json['image']
                                    except:
                                        image_url = json_content['image']
                                    '''PRODUCT ID'''
                                    try:
                                        product_id = inner_json['sku']
                                    except:
                                        product_id = json_content['sku']
                                    if product_id in read_log_file():
                                        continue
                                    print('current datetime------>', datetime.now())
                                    dictionary = {
                                        'Carolina_product_category': product_category,
                                        'Carolina_product_sub_category': product_sub_category,
                                        'Carolina_product_id': product_id,
                                        'Carolina_product_name': product_name,
                                        'Carolina_product_quantity': product_quantity,
                                        'Carolina_product_price': product_price,
                                        'Carolina_product_url': product_url,
                                        'Carolina_image_url': image_url,
                                        'Carolina_product_desc': product_desc
                                    }
                                    articles_df = pd.DataFrame([dictionary])
                                    articles_df.drop_duplicates(subset=['Carolina_product_id', 'Carolina_product_name'],
                                                                keep='first',
                                                                inplace=True)
                                    output_dir = 'Output'
                                    if not os.path.exists(output_dir):
                                        os.makedirs(output_dir)
                                    file_path = os.path.join(output_dir, f'{file_name}.csv')
                                    if os.path.isfile(file_path):
                                        articles_df.to_csv(file_path, index=False, header=False, mode='a')
                                    else:
                                        articles_df.to_csv(file_path, index=False)

                                    write_visited_log(product_id)
                            write_visited_log(page_link)
                    else:
                        inner_data = inner_request.find_all('div', class_='c-feature-product qv-model')
                        for single_data in inner_data:
                            product_url = f'{base_url}{single_data.find("a")["href"]}'
                            print(product_url)
                            random_sleep(1, 10)
                            product_request = get_soup(product_url, headers)
                            if product_request is None:
                                continue
                            content = product_request.find('script', type='application/ld+json')
                            replace_content = str(content).replace(
                                '<script type="application/ld+json">', '').replace('</script>', '')
                            json_content = json.loads(replace_content)
                            for inner_json in json_content['offers']:
                                '''PRICE'''
                                try:
                                    product_price = f"$ {inner_json['price']}"
                                except:
                                    product_price = ''
                                '''PRODUCT URL'''
                                try:
                                    product_url = inner_json['url']
                                except:
                                    product_url = ''
                                '''PRODUCT NAME'''
                                try:
                                    product_name = inner_json['name']
                                    if re.search('Pack of \\d+', str(product_name)):
                                        product_quantity = re.search('Pack of \\d+', str(product_name)).group().replace(
                                            'Pack of', '').strip()
                                    else:
                                        product_quantity = 1
                                except:
                                    product_name = json_content['name']
                                    product_quantity = '1'
                                '''PRODUCT DESC'''
                                try:
                                    desc = inner_json['description']
                                    desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                    product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                except:
                                    desc = json_content['description']
                                    desc_soup = BeautifulSoup(desc, 'html.parser').text.strip()
                                    product_desc = BeautifulSoup(desc_soup, 'html.parser').text.strip()
                                '''IMAGE URL'''
                                try:
                                    image_url = inner_json['image']
                                except:
                                    image_url = json_content['image']
                                '''PRODUCT ID'''
                                try:
                                    product_id = inner_json['sku']
                                except:
                                    product_id = json_content['sku']
                                if product_id in read_log_file():
                                    continue
                                print('current datetime------>', datetime.now())
                                dictionary = {
                                    'Carolina_product_category': product_category,
                                    'Carolina_product_sub_category': product_sub_category,
                                    'Carolina_product_id': product_id,
                                    'Carolina_product_name': product_name,
                                    'Carolina_product_quantity': product_quantity,
                                    'Carolina_product_price': product_price,
                                    'Carolina_product_url': product_url,
                                    'Carolina_image_url': image_url,
                                    'Carolina_product_desc': product_desc
                                }
                                articles_df = pd.DataFrame([dictionary])
                                articles_df.drop_duplicates(subset=['Carolina_product_id', 'Carolina_product_name'],
                                                            keep='first', inplace=True)
                                output_dir = 'Output'
                                if not os.path.exists(output_dir):
                                    os.makedirs(output_dir)
                                file_path = os.path.join(output_dir, f'{file_name}.csv')
                                if os.path.isfile(file_path):
                                    articles_df.to_csv(file_path, index=False, header=False, mode='a')
                                else:
                                    articles_df.to_csv(file_path, index=False)

                                write_visited_log(product_id)
                write_visited_log(main_url)
