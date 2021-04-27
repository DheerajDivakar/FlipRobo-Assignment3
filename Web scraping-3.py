#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Importing libs
#! pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(r'C:\Users\Dheeraj\Downloads\chromedriver_win32 (1)\chromedriver.exe')
url="https://www.amazon.in/"
driver.get(url)
    
    
    #Look for the class
search_box = driver.find_element_by_xpath("//input[@class='nav-input nav-progressive-attribute']")

a=input('enter the element')
    
    #Write what we be searched#
search_box.send_keys(a)

    #Submit the text
search_box.send_keys(Keys.RETURN)


# In[15]:


a


# In[16]:


brand=[]
rating=[]
no_ofrating=[]
price=[]
get_by=[]


# In[17]:


start=0
end=3
for page in range(start,end):#for loop for scrapping 3 page\n"
    brands=driver.find_elements_by_xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']")
    for i in brands:
         brand.append(i.text)
    rate=driver.find_elements_by_xpath("//i[@class='a-icon a-icon-star-small a-star-small-4 aok-align-bottom']")
    for i in rate:
         rating.append(i.text)
    nor=driver.find_elements_by_xpath("//span[@class='a-size-base']")
    for i in nor:
         no_ofrating.append(i.text)
    pri=driver.find_elements_by_xpath("//span[@class='a-price-whole']")
    for i in pri:
         price.append(i.text)
    get=driver.find_elements_by_xpath("//span[@class='a-text-bold']")
    for i in get:
         get_by.append(i.text)                                
    nxt_button=driver.find_elements_by_xpath("//li[@class='a-normal']/a")#scraping the list of buttons from the page\n",
    driver.get(nxt_button[page].get_attribute('href'))#getting the link from the list for next page\n",


# In[18]:


brand


# In[19]:


get_by


# In[20]:



no_ofrating


# In[21]:


import pandas as pd
df=pd.DataFrame({"Brand":brand[0:10],
                "rating":rating[0:10],
                "no of rating":no_ofrating[0:10],
                 "price":price[0:10],
                 "get it by":get_by[0:10]
                })


# # 3. Write a python program to access the search bar and search button on images.google.com and scrape 100 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’

# In[27]:


import selenium
import pandas as pd
from selenium import webdriver


# In[28]:


driver=webdriver.Chrome(r'C:\Users\Dheeraj\Downloads\chromedriver_win32 (1)\chromedriver.exe')


# In[29]:


url="https://images.google.com/?gws_rd=ssl"
driver.get(url)


# In[30]:



search_bar = driver.find_element_by_xpath('//*[@id=\"sbtc\"]/div/div[2]/input')   
search_bar.send_keys("fruits")       
search_button = driver.find_element_by_xpath('//*[@id=\"sbtc\"]/button')   
search_button.click()


# In[31]:



for i in range(500):
    driver.execute_script("window.scrollBy(0,10000)")


# In[32]:


images = driver.find_elements_by_xpath('//img[@class="rg_i Q4LuWd"]')


# In[33]:



img_urls = []
img_data = []
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            img_urls.append(source)
len(img_urls)


# In[34]:



for i in range(len(img_urls)):
    if i >= 100:
        break
        print("Downloading {0} of {1} images".format(i,100))
        response= requests.get(img_urls[i])
        file = open("H:/Flip ROBO/banana/img"+str(i)+".jpg\", \"wb")
        file.write(response.content)


# In[35]:



source


# In[36]:



url="https://images.google.com/?gws_rd=ssl"
driver.get(url)
from selenium.webdriver.common.keys import Keys
search_box = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")


    
    #Write what we be searched#
search_box.send_keys('machine learning')

    #Submit the text
search_box.send_keys(Keys.RETURN)


# In[37]:



machine=[]
ml=driver.find_elements_by_xpath("//img[@class='rg_i Q4LuWd']")
for i in ml:
    machine.append(i)


# In[38]:


machine


# # 4. Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”, “Secondary Camera”, “Display Size”, “Display Resolution”, “Processor”, “Processor Cores”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe and CSV

# In[39]:


url="https://www.flipkart.com/"
driver.get(url)


# In[40]:


from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
prod = input(" Enter the name of the mobile phone you want to search :")
time.sleep(3)
try:
    login_X_button = driver.find_element_by_xpath('//button[@class="_2KpZ6l _2doB4z\"]')                   
    login_X_button.click()
except NoSuchElementException:
    print("No Login page")
search_bar = driver.find_element_by_xpath('//*[@id=\"container\"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')    
search_bar.clear()              
search_bar.send_keys(prod)      
search_button = driver.find_element_by_xpath('//button[@class="L0Z3Pu\"]')   
search_button.click()


# In[41]:


flip_urls = []
urls = driver.find_elements_by_xpath('//a[@class=\"_1fQZEK\"]')
for url in urls:
    flip_urls.append(url.get_attribute("href"))


# In[42]:


len(flip_urls)


# In[43]:




flip_dict = {}
flip_dict["Brand"] = []
flip_dict["Smartphone"] = []
flip_dict["Colour"] = []
flip_dict["RAM"] = []
flip_dict["Storage(ROM)"] = []
flip_dict["Primary Camera"] = []
flip_dict["Secondary Camera"] = []
flip_dict["Display Size"] = []
flip_dict["Display Resolution"] = []
flip_dict["Processor"] = []
flip_dict["Processor Cores"] = []
flip_dict["Battery Capacity"] = []
flip_dict["Battery Type"] = []
flip_dict["Price"] = []
flip_dict["URL"] = []


# In[44]:


for url in flip_urls:
    driver.get(url)    
    print("Scraping URL = ", url)
    flip_dict['URL'].append(url)                                                         
    time.sleep(2)
try:
    read_more = driver.find_element_by_xpath('//button[@class=\"_2KpZ6l _1FH0tX\"]')     
    read_more.click()
except NoSuchElementException:
        print("Exception Occured. Moving to next page")

try:
    brand = driver.find_element_by_xpath('//span[@class="B_NuCI"]')      
    flip_dict["Brand"].append(brand.text.split()[0])
except NoSuchElementException:
          flip_dict['Brand'].append('-')
 
try:
    price = driver.find_element_by_xpath('//div[@class=\"_30jeq3 _16Jk6d\"]')     
    flip_dict['Price'].append(price.text)
except NoSuchElementException:
       flip_dict['Price'].append('-')
   
try:
    name = driver.find_element_by_xpath('//div[@class=\"_3k-BhJ\"][1]/table/tbody/tr[3]/td[2]/ul/li')     
    flip_dict['Smartphone'].append(name.text)
except NoSuchElementException:
            flip_dict['Smartphone'].append('-')
    
try:
    color = driver.find_element_by_xpath('//div[@class=\"_3k-BhJ\"][1]/table/tbody/tr[4]/td[2]/ul/li')      
    flip_dict['Colour'].append(color.text)
except NoSuchElementException:
            flip_dict['Colour'].append('-')
     
try:
    disp_chk = driver.find_element_by_xpath('//div[@class=\"_3k-BhJ\"][2]/div')
    if disp_chk.text != "Display Features" : raise NoSuchElementException
    disp_size = driver.find_element_by_xpath('//div[@class=\"_3k-BhJ\"][2]/table[1]/tbody/tr[1]/td[2]/ul/li')  
    flip_dict['Display Size'].append(disp_size.text)
except NoSuchElementException:
    flip_dict['Display Resolution'].append('-')


# In[45]:


len(flip_dict["Brand"])


# In[46]:


flip_dict


# # Q5. 5.\tWrite a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

# In[47]:


driver.close()


# In[48]:


driver=webdriver.Chrome(r'C:\Users\Dheeraj\Downloads\chromedriver_win32 (1)\chromedriver.exe')


# In[49]:



driver.get("https://www.google.co.in/maps")
time.sleep(3)
    
city = input('Enter City Name : ')                                         
search = driver.find_element_by_id("searchboxinput")                     
search.clear()                                                             
time.sleep(2)
search.send_keys(city)                                                   
button = driver.find_element_by_id("searchbox-searchbutton")             
button.click()                                                          
time.sleep(3)
try:
    url_string = driver.current_url
    print("URL Extracted: ", url_string)
    lat_lng = re.findall(r'@(.*)data',url_string)
    if len(lat_lng):
        lat_lng_list = lat_lng[0].split(",")
        if len(lat_lng_list)>=2:
              lat = lat_lng_list[0]
              lng = lat_lng_list[1]
              print("Latitude = {}, Longitude = {}".format(lat, lng))
except Exception as e:
         print("Error: ", str(e))


# # Write a program to scrap details of all the funding deals for second quarter (i.e. July 20 – September 20) from trak.in

# In[56]:


driver=webdriver.Chrome(r'C:\Users\Dheeraj\Downloads\chromedriver_win32 (1)\chromedriver.exe')


# In[59]:



driver.get('https://trak.in/')


# In[60]:



button = driver.find_element_by_xpath('//li[@id=\"menu-item-51510\"]/a').get_attribute('href')
driver.get(button)


# In[62]:



fund_dict = {}
fund_dict['Date'] = []
fund_dict['Startup Name'] = []
fund_dict['Industry/Vertical'] = []
fund_dict['Sub-Vertical'] = []
fund_dict['Location'] = []
fund_dict['Investor'] = []
fund_dict['Investment Type'] = []
fund_dict['Amount(in USD)'] = []


# In[63]:


for i in range(48,51):
    driver.find_element_by_xpath('//div[@id=\"tablepress-{}_wrapper\"]/div/label/select/option[4]'.format(i)).click()
    dt = driver.find_elements_by_xpath('//table[@id=\"tablepress-{}\"]/tbody/tr/td[2]'.format(i))
    for d in dt:
        fund_dict['Date'].append(d.text)
    sn = driver.find_elements_by_xpath('//table[@id=\"tablepress-{}\"]/tbody/tr/td[3]'.format(i))
    for n in sn:
        fund_dict['Startup Name'].append(n.text)
    ind = driver.find_elements_by_xpath('//table[@id=\"tablepress-{}\"]/tbody/tr/td[4]'.format(i))
    for n in ind:
        fund_dict['Industry/Vertical'].append(n.text)
    sv = driver.find_elements_by_xpath('//table[@id=\"tablepress-{}\"]/tbody/tr/td[5]'.format(i))
    for s in sv:
        fund_dict['Sub-Vertical'].append(s.text)
    loc = driver.find_elements_by_xpath('//table[@id=\"tablepress-{}\"]/tbody/tr/td[6]'.format(i))
    for l in loc:
        fund_dict['Location'].append(l.text)
    inv = driver.find_elements_by_xpath('//table[@id=\"tablepress-{}\"]/tbody/tr/td[7]'.format(i))
    for n in inv:
        fund_dict['Investor'].append(n.text)
    invt = driver.find_elements_by_xpath('//table[@id=\"tablepress-{}\"]/tbody/tr/td[8]'.format(i))
    for n in invt:
        fund_dict['Investment Type'].append(n.text)
    amt = driver.find_elements_by_xpath('//table[@id=\"tablepress-{}\"]/tbody/tr/td[9]'.format(i))
    for a in amt:
        fund_dict['Amount(in USD)'].append(a.text)
   
    fund_df = pd.DataFrame(fund_dict)
    fund_df


# In[64]:



fund_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




