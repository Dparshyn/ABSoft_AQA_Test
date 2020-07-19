from selenium import webdriver


def animal_request():
    link = []
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://random.dog/woof.json")
    elemdog = driver.find_element_by_tag_name("pre")
    random_dog = elemdog.text.split('"')[-2]
    link.append(random_dog)
    driver.get("https://randomfox.ca/floof/")
    elemfox = driver.find_element_by_tag_name("pre")
    random_fox = elemfox.text.split('"')[3].replace('\/', '/')
    link.append(random_fox)
    return link