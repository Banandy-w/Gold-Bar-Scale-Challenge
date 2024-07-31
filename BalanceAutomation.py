#Given a balance scale and 9 gold bars of the same size and look. You don’t know the exact weight of each bar,
#but you know they all weigh the same, except for one fake bar. It weighs less than others. You need to find the fake
#gold bar by only bars and balance scales.
#You can only place gold bars on scale plates (bowls) and find which scale weighs more or less


#Task Requirements:
#Create the test automation project using any preferred language to perform
#a. clicks on buttons (“Weigh”, “Reset”)                                                            DONE
#b. Getting the measurement results (field between the 'bowls')                                     DONE
#c. filling out the bowls grids with bar numbers (0 to 8)                                           DONE
#d. getting a list of weighing                                                                      DONE
#e. Clicking on the gold bar number at the bottom of the website and checking for the alert message DONE
#f. Code the algorithm solution that finds the fake bar                                             DONE

# Solution
# Given N bars. Put N/2 bars on each side of the scale. If the scales are balanced and N is odd, the odd bar out fake.
# The lighter scale will have the fake bar. Reset the scale
# Split the bars from the lighter scale between the scale
# The lighter scale will have the fake bar. 
# Repeat the splitting and weighting of the lighter scale until there is only 1 bar on each scale
# When there is only 1 bar on each scale left, the lighter scale from this result should be the fake


import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from POM import BalancePage,Locators

#Pseudo Code
#1. Open website
#2. Find the Max index of bars, N
#3. For N/2 times, Insert numbers 0 to N/2 into left bowl grid
#4. For N/2 times, Insert numbers N/2 to N into right bowl grid
#5. Press weigh button 
#6. Get the results. Store the lighter bowl results. This is the last N
#7. Press reset
#8. Repeat from step3 with last N
#9. Find fake bar X
#10. Press button X
#11. Expect Alert message, verify
#12. Get list of weightings and output.

def split_weigh(weighing):
    """Takes a string similar to '[0,1,2,3] > [4,5,6,7]' This function does not check for validity at the moment. 
    Returns a list of numbers with the lesser weight or '=' if the string is equal
    """
    if '>' in weighing:
        weight1, weight2 = weighing.split('>')
        weight2 = weight2.strip('[] ')
        last_weigh = [x for x in weight2.split(',')]
        #print(f"Log:Fake bar is one of the following numbers: {last_weigh}")
        return last_weigh
    
    elif '<' in weighing:
        weight1, weight2 = weighing.split('<')
        weight1 = weight1.strip('[] ')
        last_weigh = [x for x in weight1.split(',')]
        #print(f"Log:Fake bar is one of the following numbers: {last_weigh}")
        return last_weigh
    
    else:
        #print("Log: The weights are equal. Fake bar is the odd one out")
        return '='

# return = [x for x in weight2.split(',')] is the same as the following
#        last_weigh = []
#        for x in weight2.split(','):
#           last_weigh.append(x)
#         return last_weigh[]


#Open website
URL = 'http://sdetchallenge.fetch.com/'
print("Log: Openning Page " + URL)
driver = webdriver.Firefox()
page = BalancePage(driver)
page.open_page(URL)
print("Log: Page Openned")

#Find the Max index of bars
page.wait_for(Locators.GOLD_BUTTON_ARRAY)
goldbars_len = int(page.get_array_length())
goldbars_mid_index = math.floor(goldbars_len/2)
print("Log: Waiting for page to load")

#Fill each bowl with half of the gold bars and weigh them
#If the result is equal then the fake bar is the odd one out
print('Log: Filling Grids')
page.fill_grid('left',0,goldbars_mid_index)
page.fill_grid('right',goldbars_mid_index,goldbars_len-1)
page.click_weigh_button()

if(page.get_result() == '='):
    page.click_goldbar(goldbars_len-1)
    print(f'Log: The fake should be {goldbars_len-1}')
    driver.quit()

page.click_reset_button()
weighings = page.get_weighings()

# weighings = list of weighing results
# weighings[last_item] = latest weighing result
# split_weighings[weighings[last_item]] = List of numbers that should have the fake bar

#Repeat filling the grid until weighings[last_item] returns a comparison that only has 1 goldbar a side
#While the last item in split_weigh(weighings) is not equal to 1
while True:
    #Get refreshed weighings and last weighing should contain numbers from the lighter scale
    weighings = page.get_weighings()
    #Array[-1] returns last index of Array
    last_weighing = split_weigh(weighings[-1])

    #If we weighed only one result with another, then the value in the lighter scale should be the fake
    #This works b/c split_weigh method returns the a list of numbers from the lighter scale
    if(len(last_weighing) == 1):
        print(f'Log: The fake should be {last_weighing[0]}')
        page.click_goldbar(last_weighing[0])
        break
    
    #last_weighing is the new reference for what numbers to fill the scales
    goldbars_len = len(last_weighing)
    goldbars_mid_index = math.floor(goldbars_len/2)

    print('Log: Filling Grids')
    page.fill_grid('left',last_weighing[0], last_weighing[goldbars_mid_index])
    page.fill_grid('right',last_weighing[goldbars_mid_index], int(last_weighing[goldbars_len-1])+1)
    page.click_weigh_button()
    page.click_reset_button()

    
    
    
    




