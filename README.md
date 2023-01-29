# dataExtractor
Automation script in Python that uses the Selenium library to automate the process of logging into a website and extracting data from it.

This script uses the webdriver module from the Selenium library to automate the process of logging into a website and extracting data from it.

The script creates a new instance of the Chrome browser and navigates to the login page of the website. It then finds the email and password fields on the page, enters the login credentials, and submits the login form.

Once the user is logged in, the script waits for the page to load and extracts the data from a specific element in the page by its id, in this case is 'data' and print the data.

The script then closes the browser.

You can use this script as a starting point and customize it to fit your specific needs, such as automating the process of filling out forms, clicking buttons, and navigating through different pages on a website.

Please keep in mind that automating the interaction with websites is against the terms of service of many websites and can be illegal, you should check the website policy and terms of service before automating any task.
