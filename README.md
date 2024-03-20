# Noble Candles

## FEATURES

![responsive](/media/readme/responsive.png)

## Description

This project designed and developed to create a useful experience for the users of Noble Candles. The users are given the possibility to explore and buy products.
All these functionalities can be accessed by any user with an account, considering that the owner have permissions for controlling the data. Noble Candles was developed using Python (Django), HTML, CSS and JavaScript by storing the data in a PostgreSQL database.

The fully deployed project can be accessed at [here](https://noble-candles-9ccec49c6b91.herokuapp.com/)

## The Header

At the header, you can find the logo with the name of the site and also the Navbar through that you can have an easy navigation to the site.
![header](/media/readme/header.png)
As non-loggged in user the header looks like this:
![header](/media/readme/header-no-login.png)
As loggged staff user the header looks like this:
![header](/media/readme/header-admin-login.png)

## Homepage

At homepage, the users can find a welcome content with a comment for the users and as a background image our beautiful candles.
![homepage](/media/readme/homepage.png)

## About us page

At this page, the user can find a few words for Noble Candles about the shop and who we are.
![about-us](/media/readme/about-us.png)

## Contact page

At this section the user can find the contact details, also the Google map that pin to the address.
![contact](/media/readme/contact.png)

## Contact form - Customer messages

At this section the Contact form make it simple for a customer to contact you if they need support or more information about your services.
![contact-form](/media/readme/messages/contact-form.png)
![contact-form](/media/readme/messages/customer-messages-1.png)
![contact-form](/media/readme/messages/customer-messages-2.png)
![contact-form](/media/readme/messages/customer-messages-3.png)
![contact-form](/media/readme/messages/customer-messages-4.png)
![contact-form](/media/readme/messages/customer-messages-5.png)
![contact-form](/media/readme/messages/customer-messages-6.png)

## Blog page

At this section the user can find articles and news for the site and the products.
![blog](/media/readme/blog/blog-1.png)
![blog](/media/readme/blog/blog-2.png)

## Products
Here the user can find all the products. There are two categories Candles and Christmas Candles. Also there is a search bar for easy navigation. Also we can see which products are out of stock.
![products](/media/readme/products-2.png)

## Product Detail

At this page the user can click the product that desire, the product details, the Quantity, the price and the description. Also has the choice to keep shopping or add to cart.Finally can see which products are in stock, out of stock and low in stock. 

![in stock](/media/readme/product-in-stock.png)
![out of stock](/media/readme/product-out-of-stock.png)
![low in stock](/media/readme/product-low-stock.png)

Also in this page we can see the reviews as well. Logged in users can add a review to a product they haven't reviewed yet. In this case an add review button is displayed, else a notification message that they have reviewed already this product. 
Logged in users can also edit/delete their review for a product.
![product reviews](/media/readme/product-details-reviews.png)

## Reviews management
For adding and editing reviews we have the following pages:
![add review](/media/readme/add-review.png)
![update review](/media/readme/update-review.png)


## Login page

At this page,the user can put username and password and log in if authentication is successful.If the user doesn't have an account there is a link to register. User should't be logged in order this page to appear.
![login](/media/readme/login.png)

## Register page

User can create an account, by inserting username, password and an email. User should't be logged in order this page to appear.
![register](/media/readme/register.png)

## 404 page

If the user see this 404 page, means that the page not found. The user need to try again.
![404](/media/readme/404.png)

## signout page

User can log out. User should be logged in order this page to appear.
![signout](/media/readme/signout.png)

## Cart

The user at this page can add products to the cart, there is the Qty, the price and the subtotal. The user can also remove or update the cart.
![cart](/media/readme/cart.png)

## Checkout

At this page the user can see all the details about the order, the delivery and the products before complete the order.
![checkout](/media/readme/checkout.png)

## profile page

At this page the user can see the profile page with all the details.
![profile](/media/readme/profile.png)

## product management

If you are logged in as an admin, you can create, delete, update products from the application without need to go to /admin.
![productmanagement1](/media/readme/product_details_admin.png)
![productmanagement2](/media/readme/edit_product.png)
![productmanagement3](/media/readme/add_product.png)

## Payments

This page is working through stripe payments. The owner can see which payments are succeeded or incomplete.
![payments](/media/readme/payments.png)

## Footer

 At the footer, you can find the Quick links, the social media links for Facebook, Instagram and Twitter the copyright for 2023 and the subscribe button for the newsletters .
![footer](/media/readme/footer.png)

## Tools used

- [Git](https://git-scm.com) - for version control.
- [Gitpod](https://www.gitpod.io) - online IDE.
- [GitHub](https://github.com) - for host repository.
- [Heroku](https://www.heroku.com) - for deploying the project
- [favicon](https://favicon.io) - for favicon
- [fontawsome](https://fontawesome.com) - for creating icons
- [Boostrap5](https://getbootstrap.com) - creating responsiveness
- [LucidChart](https://www.lucidchart.com/pages) - used for creating the Flowchart
- [Google maps](https://www.google.com) - used for creating the google map fr the contact details
- [Stripe](https://stripe.com/ie) used for creating the stripe payments

## Languages Used

- This tool is created using [Python](https://www.python.org) language.
- This tool is created using [SQL](https://en.wikipedia.org/wiki/SQL) language.
- This tool is created using [HTML](https://en.wikipedia.org/wiki/HTML) language.
- This tool is created using [CSS](https://en.wikipedia.org/wiki/CSS) language.
- This tool is created using [javascript](https://en.wikipedia.org/wiki/JavaScript) language.
- This tool is created using [JQuery](https://jquery.com) language.

[Git](https://git-scm.com) - for version control. For version control These commands were used for version control during project:

- git add . or git add -A: To add files before committing

- git commit -m: "type your message mentioning changes" - To commit changes to the local repository

- git push : To push all committed changes to the GitHub repository

## Libraries

![libraries](/media/readme/libraries.png)

## Validators testing

As advised by tutors, I validated Code Institute Python linter, html validator, css validator and Js validator

- HTML No errors were returned when passing through the official W3C validator
![html](/media/readme/validator.html.png)
- CSS No errors were found when passing through the official validator
![css](/media/readme/validator-css.png)
- JShint No errors were found when passing through the official validator
![js](/media/readme/validator-jshint.png)
![js](/media/readme/validator-jshint-2.png)
- Python No errors were found when passing through the official validator using pycodestyle. Due to pep8online.com still not being online,
  I used pycodestyle to check my python code. pycodestyle is a command line installed with pip. I ran the command "pycodestyle blog cart checkout customer_messages
  home noble_candles products profiles"
  which I took it from the suggestion in the [documentation](https://pycodestyle.pycqa.org/en/latest/intro.html#features)
![python](/media/readme/python-tests.png)

## Manual Testing

#### **1 - Deployment & Set up:**

|passed | **Access in a live url** I can use the site on any device.
|:---:|:---|
|&check;| Access the site via the deployed URL on the desktop.
|&check;| Access the site via the deployed URL on mobile.
|&check;| Access the site via the deployed URL on a tablet.
|&check;| All images and styles are as expected.

#### **2 - Viewing & Navigation:**

|passed | .**Clearly identity the site upon visiting** also **if the site is what I am looking for.**
|:---:|:---|
|&check;| The site is easy to navigate.

|passed | **View the list of products** so that I can **select some to add to the cart.**
|:---:|:---|
|&check;| The site has a list of products.
|&check;| The product list is ordered by default by ID.
|&check;| You can add to the cart a product in the product page direct.
|&check;| The list of products can be found by name ascending and descending.
|&check;| The list of products can be filtered by category.
|&check;| Add to cart button works as expected on all products & product details pages.
|&check;| Users can add more than one items to their cart.

|passed | **Individual product details** so that I can **identify the name of the product, price, description, rating and product image enabling me to compare how the product differs from other items.**
|:---:|:---|
|&check;| The site has a product details page.
|&check;| The product details page shows the product image.
|&check;| The product details page shows the product name.
|&check;| The product details page shows the description of the product.
|&check;| The product details page shows the product price.
|&check;| The product details page shows the rating of the product.
|&check;| The product details page shows the product description.
|&check;| The product details page shows the product rating.
|&check;| The product details page shows the product reviews.
|&check;| The product details page shows the add product review for logged user.
|&check;| The product details page shows the edit product review for logged user created the review.
|&check;| The product details page shows the delete product review for logged user created the review.
|&check;| The product details page shows the product quantity button.
|&check;| The product details page shows the product add to cart button.
|&check;| The product details page has a search bar for easiest navigation for the products.

|passed | **If something goes wrong on the site** fix any errors and continue with my purchase.
|:---:|:---|
|&check;| The site has a 404 page active when the URL is unknown.
|&check;| The site has a 500-page active when server error.
|&check;| Relevant feedback is displayed as a toast message when the user cannot act.

|passed | **View the total of my purchases** also view how much I am spending at any time in my order.
|:---:|:---|
|&check;| The site has a cart page.
|&check;| The cart preview shows the product image.
|&check;| The cart preview shows the product name.
|&check;| The cart preview shows the product price.
|&check;| The cart preview shows the current quantity in the cart.
|&check;| Cart preview shows when the product is added from any page.
|&check;| The cart page shows the product quantity, and the users can update their order quantity.
|&check;| The cart page/preview shows the cart total.
|&check;| The cart page shows the delivery cost and grand total.
|&check;| The cart page allows the users to completely remove an item from their cart and updates the cart total.
|&check;| When the quantity is updated in the user's cart, the cart total updates accurately.

|passed | **Contact with the owner** to ask questions about the products or the site.
|:---:|:---|
|&check;| The site has a contact page.
|&check;| Contact form cannot be submitted with required fields blank.
|&check;| Contact form cannot be presented with an invalid email address.
|&check;| Contact form submits a message to the database.
|&check;| Message can be read from the admin.
|&check;| Success message is shown to the user when a message is submitted.
|&check;| Message can be updated as done.
|&check;| Message can be deleted.

|passed | **Blog** to check out news and articles of the products or the site.
|:---:|:---|
|&check;| Blog has a button to the Navbar for easy navigation to the page.
|&check;| The page has articles and news for the site and the products.
|&check;| The page has a button to go back to the blog spots.

#### **3 - Register & User Accounts:**

|passed | **Register for an account** has my personal details, view my order history.
|:---:|:---|
|&check;| The site has a register page.
|&check;| User can not register with an email address that is already in use.
|&check;| User can successfully register for the site
|&check;| User can not register with a username that is already in use.
|&check;| User can not register with a password similar to their email address.
|&check;| User can not register with a too short password.
|&check;| Success message is displayed to the user if registration is successful.
|&check;| User sees message to verify their email.
|&check;| User can not login until they have verified their email.
|&check;| Verification email is sent to the user.
|&check;| Verification email contains a link to confirm the user's email.
|&check;| Once verified, user, can login with their username or email.

|passed | **Login or logout at any time** have access my personal account details.
|:---:|:---|
|&check;| Log in/out options are visible.
|&check;| Logged out, personal details is no longer visible.
|&check;| Logged in, the account options change to reveal a profile link.
|&check;| User receives a success message when they log in/out.

|passed | **Receive an email confirmation upon registration**. Confirm the registration process worked correctly.
|:---:|:---|
|&check;| Email sent upon registration asking for the user to verify their email address.

#### **4 - Searching:**

|passed | **Search the list of available products** To find the most suitable products to suit my needs.
|:---:|:---|
|&check;| Search bar is visible at the products page.
|&check;| Products can be searched by category.
|&check;| Products can be searched by key words.
|&check;| Search returns results based on the search term.
|&check;| Search matches product name and description.
|&check;| Number of products returned is displayed above the search results.

#### **5 - Purchasing & Checkout:**

|passed | **Select a quantity of a product**.
|:---:|:---|
|&check;| The Quantity can be selected on the product detail page.
|&check;| User can set the quantity selector to 1
|&check;| User can use the plus and minus buttons to select the quantity.
|&check;| User cannot add a quantity of 0 to the cart.
|&check;| User can see if the products are in stock.
|&check;| User can see if the products are low in stock.
|&check;| User can see if the products are out of stock.

|passed | **View items in my bag to be purchased** also I can identify the total ammount of my purchases before checkout.
|:---:|:---|
|&check;| The site has a shopping cart page.
|&check;| Cart page has a list of all the items in the user's cart.
|&check;| Cart page has a total ammount for all the user cart products.
|&check;| Cart page has the delivery fee and the delivery free 50 euro and over.
|&check;| Cart page has a button to proceed to checkout.
|&check;| Cart page has a button to remove products from the cart.
|&check;| Cart page has a button to continue shopping.

|passed | **Enter the payment info** so I can do the checkout quickly.
|:---:|:---|
|&check;| The site has a checkout page.
|&check;| The checkout page has a form to enter the user's payment details.
|&check;| The checkout page has a form to enter the user's shipping details.
|&check;| Payments are handled by Stripe.
|&check;| The checkout page has a button to complete the order.
|&check;| The checkout page has a button to cancel the order and return the user to the shopping cart.

|passed | **Securely submit the payment details** also make sure my financial info is safe.
|:---:|:---|
|&check;| Stripe payment system for the site is used.
|&check;| Stripe payment system for the site is PCI compliant.

#### **6 - Admin:**

|passed | **Add a product**.
|:---:|:---|
|&check;| Product can be added via the admin panel and is visible in the store.
|&check;| Added items had full functionality of pre-existing products.

|passed | **Edit a product**. Update the details of a product.
|:---:|:---|
|&check;| Product can be edited via the admin panel and is visible in the store.
|&check;| Quick edits can only be made from the front end by superusers.

|passed | **Delete a product**. Remove products that are no longer for sale.
|:---:|:---|
|&check;| Product can be deleted via the admin panel and is no longer visible in the store.
|&check;| Quick delete can only be made from the front end by superusers.

#### **7 - Social Media & Marketing:**

|passed | **Promotional emails**. Promote new products.
|:---:|:---|
|&check;| Mailchimp form is in the footerand is visible from all pages.
|&check;| Mailchimp form has a field to enter the email address.
|&check;| Mailchimp form has a button to do the submittion with the email address.
|&check;| Collected email addresses are stored in the mailchimp database.

|passed | **Social media page**. Promote my site and products.
|:---:|:---|
|&check;| Facebook page is set up.
|&check;| Facebook page is linked in the footer.

|passed | .**Increase the search engine ranking**. Increase the number of visitors to my site.
|:---:|:---|
|&check;| Each page has a meta description.
|&check;| Each page has a meta title.
|&check;| Each page has meta keywords.
|&check;| Site map done
|&check;| Robots.txt done

## Unfixed bugs

- In edit admin product the image is not displayed properly

## Unimplemented features

- Blog page : I would like to do more things at the blog page such as for the admin to
  insert, update and delete the blog spots.
- Staff users add more stock.  

## Deployment

- On [Heroku](https://www.heroku.com) dashboard, select "New" and click "Create new app"
- Create a unique app name
- Select your region
- Click "Create app"
- Go to the settings tab:
- Scroll down to the config vars section and select "Reveal Config Vars"
- Add necessary config vars
- In this case, in the key field enter "PORT" and the value field enter "8000"
- Click "Add"
- Scroll down to Buildpacks and click "Add buildpack"
- Add the necessary buildpacks.
- In this case, select "python" and click "Save changes"
- Then, select "node.js" and click "Save changes"
- Go to the Deploy tab:
- Select GitHub and confirm connection to GitHub account
- Search for the repository and click "Connect"
- Scroll down to the deploy options
- Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository
- In manual deploy, select which branch to deploy and click "Deploy Branch"
- Heroku will start building the app
- The link to the app can be found at the top of the page by clicking "Open app"
- The fully deployed project can be accessed at [here](https://noble-candles-9ccec49c6b91.herokuapp.com/)

## Confirmation email
Confirmation email sent example can be see ![here](/media/readme/confirmation-email.png)

## Flowchart

The Flowchart for my program was created using LucidChart and represents how the project works.
![flowchart](/media/readme/flowchart_new.png)

## Wireframes

- At the first wireframe you can see the central homepage within three sections the homepage, about and the contact page. At the top is the header with the logo, the Navbar and at the bottom the footer.
![wireframes 1](/media/readme/wireframe-homepage.jpg)
- At this wireframe you can see the products page with the search bar, also the header and the footer.
![wireframes 2](/media/readme/wireframe-products.jpg)
- At this wireframe you can see the product details page (image and description and the search bar) with the header and the footer too.
![wireframes 3](/media/readme/wireframe-product-detail.jpg)
- At this wireframe you can see the blog page with the header and the footer too.
![wireframes 4](/media/readme/wireframe-blog.jpg)
- At the last wireframe you can see the blog page but the individual blog with the header and the footer too.
![wireframes 5](/media/readme/wireframe-individual-blog.jpg)

## Facebook

The users here can find the Facebook business page for Noble Candles. <br>
The link for facebook can be found [here](https://www.facebook.com/people/Noble-Candles/pfbid02YxDjiW6oejUHAvS7nKjnw6Knabtew1Yri6vocVbd8Kfcbjn97kkSX6AjBX1nkoXvl)

![facebook](/media/readme/facebook-screenshot-1.png)
![facebook](/media/readme/facebook-screenshot-2.png)
![facebook](/media/readme/facebook-screenshot-3.png)

## E-commerce business model

Apart from Facebook, we use SEO as well to bring customers to our website. For subscribed users we use Mailchimp to send newletters with the latest offers and new products, in order to increase sales.

## Surface

- Color Scheme
  - #1c3a16
  - #3f5a36
  - #b8bbbc
  - #F5F5DC
  - beige
  - #3f5a36
  
- Fonts The fonts I used for the site are:
  - font-family: Gabriola, fantasy;
  - font-family: Palace script MT reg, sans;
  - font-family: Gabriola, sans-serif
  - font-family: Gabriola, sans;

## Agile Methodology

The project was developed by Agile methodology. The implementation progress was registered by [Jira](https://www.gira.com/en/en/country) The tasks were accomplished, there moved to Jira from to do, to in Progress, Tests and Done lists.
![jira1](/media/readme/jira1.png)
![jira2](/media/readme/jira2.png)
![jira3](/media/readme/jira3.png)

## Credits

- Content
  The content of the site is fictive. it's only for the project.
  
  - Media
  - [fontawsome](https://fontawesome.com/icons/facebook?f=brands&s=solid) - for the footer
  - [fontawsome](https://fontawesome.com/icons/instagram?f=brands&s=solid) - for the footer
  - [fontawsome](https://fontawesome.com/icons/twitter?f=brands&s=solid) - for the footer
  - [stackoverflow](https://stackoverflow.com)
  - [freepnging](https://freepngimg.com/png/26408-candles-transparent-background/icon)
  - [w3schools](https://www.w3schools.com)
  - [geeksforgeeks](https://www.geeksforgeeks.org)
  - [mailchimp](https://mailchimp.com) [here](https://us21.admin.mailchimp.com/audience/forms/dashboard)
  
## Acknowledgements
  
  I'd like to thank my mentor, Akshat Garg, for providing advices and feedback for this project. Also the tutors and the students for the comments to Slack.
