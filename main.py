from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome ()
driver.get('https://secure.devpost.com/users/login?ref=top-nav-login')

# Select the id box
id_box = driver.find_element(By.ID,"user_email")

# Send id information
id_box.send_keys('Xiaos7093@wrdsb.ca')                       #SUB EMAIL OUT

# Find password box
pass_box = driver.find_element(By.ID,'user_password')
# Send password
pass_box.send_keys('*****MYPASSWORD*****')                   #SUB THIS OUT WITH PASSWORD FOR VIDEO DEMO
# Find Sign-In button
login_button = driver.find_element(By.ID,'submit-form')
login_button.click()

time.sleep(0.5)

driver.find_element(By.ID,'global-nav-screen-name').click()
driver.find_element(By.LINK_TEXT,'Portfolio').click()

time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR,'[alt="Untitled"]').click()
driver.find_element(By.LINK_TEXT,'Continue your submission').click()


project_Name = driver.find_element(By.ID,"participants_manage_project_overview_title")
project_Name.send_keys('Demo: Once')                                                      #FOR OUR ACTUAL DEVPOST MAKE THE NAME JUST "ONCE"

project_Pitch = driver.find_element(By.ID,"participants_manage_project_overview_tagline")
project_Pitch.send_keys('For those who value their time.')
driver.find_element(By.NAME,'button').click()
project_Story = driver.find_element(By.ID,"software_description")
project_Story.send_keys('              WWhat inspired us mainly was the pure joy of VACATION! Why even waste your brain power on small things? We all know that we have better stuff to do. Such as staying on our calculators and constantly calculating our grades before application. Once is an extension that lets you pre-setup actions for a website and automate it forever. For example, buying pizza. We built it using mainly python, html, CSS and JavaScript. There were many challenges such as switching between windows and OS, learning how to automate and your average coding problems. We are proud that we managed to learn something completely new and a product works for the most part. We plan on making it more polished, saving profiles and also gathering data from many websites from users to pre-make forms for such. Quality of life plus digital design remake is also a step. We just wish to create something that is small, simple, easy, free and cuts down on tedious tasks. We all know that we indeed have enough of those in life. Although it is shown that this form is made using our extension, it is just an example of what it can do. The main use is for those pesky and tedious attendant forms. Like who could ever remember...')

built_with = driver.find_element(By.ID,"s2id_autogen1")
built_with.send_keys('Python, HTML, CSS, JavaScript,Selenium,')

try_out = driver.find_element(By.ID, "software_urls_attributes_0_url")
try_out.send_keys("iosjgoaijgodsjg")                                 #SUB OUT WITH ACTUAL GIT REPO


video_Demo = driver.find_element(By.ID,"software_video_url")
video_Demo.send_keys('https://www.youtube.com/watch?v=xvFZjo5PgG0') #SUB THIS OUT WITH ACTUAL VIDEO

time.sleep(0.5)

driver.find_element(By.NAME,'button').click()

time.sleep(0.5)
tech_Exp = driver.find_element(By.ID,"participants_submission_requirements_submission_field_values_attributes_2_value")
tech_Exp.send_keys('It was quite amazing. Learned a lot from this experience. Although it would have been nice to work together IRL but unfortunately we were unable to make that happen.')
driver.find_element(By.NAME,'button').click()
driver.find_element(By.ID,'participants_manage_finalization_accepts_terms').click()
time.sleep(0.5)
driver.find_element(By.NAME,'button').click()
time.sleep(500)
