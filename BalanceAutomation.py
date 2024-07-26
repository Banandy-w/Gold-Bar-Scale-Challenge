#Given a balance scale and 9 gold bars of the same size and look. You don’t know the exact weight of each bar,
#but you know they all weigh the same, except for one fake bar. It weighs less than others. You need to find the fake
#gold bar by only bars and balance scales.
#You can only place gold bars on scale plates (bowls) and find which scale weighs more or less


#Task Requirements:
#Create the test automation project using any preferred language to perform
#a. clicks on buttons (“Weigh”, “Reset”) DONE
#b. Getting the measurement results (field between the 'bowls') DONE
#c. filling out the bowls grids with bar numbers (0 to 8)
#d. getting a list of weighing
#e. Clicking on the gold bar number at the bottom of the website and checking for the alert message
#f. Code the algorithm solution that finds the fake bar

# Solution
# Given N bars. Put N/2 bars on each side of the scale. If the scales are balanced and N is odd, the odd bar out fake.
# The lighter scale will have the fake bar. Reset the scale
# Split the bars from the lighter scale between the scale
# The lighter scale will have the fake bar. 
# Repeat the splitting and weighting of the lighter scale until there is only 1 bar on each scale

#Pseudo Code
#1. Open website
#2. Find the Max index of bars, N
#3. For N/2 times, Insert numbers 0 to N/2 into left bowl grid
#4. For N/2 times, Insert numbers N/2 to N into right bowl grid
#5. Press weigh button 
#6. Get the results. Store the lighter bowl results. This is the new N
#7. Press reset
#8. Repeat from step3 with new N
#9. Find fake bar X
#10. Press button X
#11. Expect Alert message, verify
#12. Get list of weightings and output.



from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from POM import BalancePage,Locators

print("Log: Openning Page")
driver = webdriver.Firefox()
page = BalancePage(driver)
page.open_page('http://sdetchallenge.fetch.com/')
print("Log: Page Openned")



