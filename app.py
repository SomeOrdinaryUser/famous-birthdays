from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re

options = Options()
options.headless = True

# Change to your webdriver path
driver = webdriver.Firefox(
    executable_path=r"C:\\webdriver\\geckodriver.exe", options=options
)

# regex to match date. Example: january 29, december 14, june 4, etc.
myregex = re.compile(
    "january[1-9]+|february[1-9]+|march[1-9]+|april[1-9]+|may[1-9]+|june[1-9]+|july[1-9]+|august[1-9]+|october[1-9]+|november[1-9]+|december[1-9]+"
)

print("enter 'x' to exit this script anytime")


def get_famous_people():
    while True:

        user_bday = input(
            "Enter you're birthday or a birthday (example: January 11): "
        ).lower()
        if user_bday == "x":
            driver.quit()
            exit()
        else:
            user_bday = user_bday.split(" ")
            user_bday = "".join(user_bday)
            if re.match(myregex, user_bday):
                break
            else:
                print("unknown entry")
                continue

    url = "https://www.famousbirthdays.com/" + user_bday + ".html"
    driver.get(url)
    row = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[2]")
    string = ""
    for names in row:
        string += names.text
    contacts = re.sub(r"^\s*([0-9]+\s*)+$", "", string, flags=re.M)
    print(contacts)
    while True:
        log_or_not = input("log to text file? (y/n): ").lower()
        if log_or_not == "x":
            driver.quit()
            exit()
        if log_or_not == "y" or "Y":
            text_file = open("log.txt", "w")
            n = text_file.write(contacts)
            text_file.close()
        if log_or_not == "n":
            break
        else:
            print("unknown command.")
            continue
    while True:
        get_bio_or_not = input("get bio? (y/n): ").lower()
        if get_bio_or_not == "x":
            driver.quit()
            exit()
        if get_bio_or_not == "y":
            bio = input(
                "Enter famous person to get their biography: (example: elon musk) "
            ).lower()
            bio = bio.split(" ")
            bio = "-".join(bio)
            person_bio = driver.get(
                f"https://www.famousbirthdays.com/people/" + bio + ".html"
            )
            bio_text = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div[2]"
            ).text
            print(bio_text)
        if get_bio_or_not == "n":
            get_famous_people()
        else:
            print("unknown command.")
            continue


if __name__ == "__main__":
    get_famous_people()
