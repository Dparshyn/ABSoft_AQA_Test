from selenium import webdriver


def animal_request():
    driver = webdriver.Opera()
    driver.get("https://random.dog/woof.json")
    elemdog = driver.find_element_by_tag_name("pre")
    random_dog = elemdog.text.split('"')[-2]
    driver.get("https://randomfox.ca/floof/")
    elemfox = driver.find_element_by_tag_name("pre")
    random_fox = elemfox.text.split('"')[3].replace('\/', '/')
    return '\n'.join([random_dog, random_fox])
