
# Beergate

## Code Institute Portfolio Project 4 - a Full Stack website using the Django framework and a database

Am I response image here

# Table of Contents

- [Scope](#scope)
- [Background](#background)
- [Audience](#audience--users)
- [User Stories](#user-stories)
    - [Admin user User Stories](#admin-user-user-stories)
    - [Unregistered user User Stories](#unregistered-user-user-stories)
    - [Registered user User Stories](#registered-user-user-stories)
- [Features](#features)
    - [Based](#base)
    - [Header and navbar](#header-and-navbar)
    - [Footer](#footer)
    - [Landing Page](#landing-page)
        - [Review cards](#review-cards)
        - [Pagination](#pagination)
        - [Sorting and filtering](#sorting-and-filtering)
    - [Review Page](#review-page)
    - [Add Review Page](#add-review-page)
    - [Update Review Page](#update-review-page)
    - [Delete Review Page](#delete-review-page)
    - [Search Results Page](#search-results-page)
    - [User Reviews Page](#user-reviews-page)
    - [AllAuth pages](#sign-in-sign-out-sign-up-and-reset-password-pages)
- [Function](#function)
    - [Reviews app](#reviews-app)
        - [Models](#reviews-models)
            - [Review](#review-class)
                - [Review class methods](#review-class-methods)
            - [Comment](#comment-class)
                - [Comment class methods](#comment-class-methods)
        - [Views](#reviews-views)
            - [Index Views](#index-views)
                - [Default View](#default-view)
                - [Sorting Views](#sorting-views)
                - [Filtering Views - type](#filtering-views---type)
                - [Filtering Views - colour](#filtering-views---colour)
                - [Filtering Views - served as](#filtering-views---servedas)
            - [Review View](#review-view)
            - [Search Results View](#search-results-view)
            - [User Reviews View](#user-reviews-view)
            - [Add Review View](#add-review-view)
            - [Update Review View](#update-review-view)
            - [Delete Review View](#delete-review-view)
            - [Voting Views](#review-upvote-and-review-downvote)
        - [Forms](#reviews-forms)
            - [Comment Form](#commentform)
            - [User Review Form](#userreviewform)
        - [URLs](#reviews-urls)
        - [Admin](#reviews-admin)    
    - [User app](#user-app)
        - [User Views](#user-views)
        - [User Forms](#user-forms)
        - [User URLs](#user-urls)
- [Deployment](#deployment)
- [Tasks](#tasks)
- [Future Work](#future-work)
- [Bugs](#bugs)
- [Development Choices](#development-choices)
- [Testing](#testing)
    - [Manual User Story testing](#manual-user-story-testing)
        - [Admin user User Story testing](#admin-user-user-story-testing)
        - [Generic user User Story testing](#generic-user-user-story-testing)
        - [Unregistered user User Story testing](#unregistered-user-user-story-testing)
        - [Registered user User Story testing](#registered-user-user-story-testing)
    - [Other Manual testing](#other-manual-testing)
    - [Validation testing](#validation-testing)
        - [HTML validation](#html-validation)
            - [Base template](#base-template)
            - [Index template](#index-template)
            - [Review template](#review-template)
            - [Search Results template](#search-results-template)
            - [User Reviews template](#user-reviews-template)
            - [Add Review template](#add-review-template)
            - [Update Review template](#update-review-template)
            - [Delete Review template](#delete-review-template)
            - [Account Sign-in template](#account-sign-in-template)
            - [Account Sign-out template](#account-sign-out-template)
            - [Account Sign-up template](#account-sign-up-template)
            - [Account Password Change template](#account-password-change-template)
        - [CSS validation](#css-validation)
        - [JS validation](#js-validation)
        - [Python validation](#python-validation)
            - [Beergate settings.py](#beergate-settingspy)
            - [Beergate urls.py](#beergate-urlspy)
            - [Reviews urls.py](#reviews-urlspy)
            - [Reviews admin.py](#reviews-adminpy)
            - [Reviews forms.py](#reviews-formspy)
            - [Reviews models.py](#reviews-modelspy)
            - [Reviews urls.py](#reviews-urlspy)
            - [Reviews views.py](#reviews-viewspy)
            - [User forms.py](#user-formspy)
            - [User view.py](#user-viewspy)
            - [User urls.py](#user-urlspy)
    - [Automated testing](#automated-testing)
- [Technologies](#technologies)
- [Other Notes](#other-notes)
- [Credits](#credits)

# Scope

The scope of this project is to create a website using the Python Django framework. The website will function as a social media and blogging site for people who like beer. 
<br><br>
The project will use the Django AllAuth library to allow users to create accounts and log in to the website. Once they have logged in, users will be able to post reviews of beers to help other users expand their tastes. Logged-in users will also be able to upvote and downvote these reviews, and post comments. Users will be able to update and delete their own reviews. 
<br><br>
The project will also feature several mechanisms for searching, sorting and filtering database entries.
<br><br>

# Background

This project is inspired by the Code Institute Whiskey Drop walkthrough project that was used to demonstrate the power and responsiveness of Bootstrap. Since I am more of a beer drinker than a whiskey drinker, I made my own variation that I called Beergate. [This is the repository](https://github.com/AdamBoley/bootstrap-experimentation), and [this is the deployed site on Github Pages](https://adamboley.github.io/bootstrap-experimentation/).
<br><br>
As a beer drinker, I enjoy exploring different beers, rather than sticking to the same brewers. The UK has a large community of small breweries who collectively produce a huge number of different beers. Given the large variety of different hops, malts and brewing techniques these breweries use, beers can differ greatly in colour and taste. 
<br><br>
Whilst this makes the UK a gold-mine for beer drinkers, it presents a problem for the breweries themselves. With so many beers and so much variety, the market is effectively saturated, making it difficult for small breweries to stand out and make their products widely known.
<br><br>
This is where this project comes in. If a user finds and drinks a good beer, they can use this project to write a review, recommending (or not) that beer to the wider beer-drinking community. Similarly, users who wish to expand their range of beers can use this project to find recommendations. 

# Audience / Users

This project is aimed at the large community of beer drinkers in the UK who want to read reviews of different beers so that they can find more beers that they may want to try. 

# User Stories

## Admin user User Stories

- As an Admin user I can...
    - Navigate to the admin sign-in page
    - Use the admin sign-in page to access the admin panel
    - View all beer reviews submitted by users
    - Filter and sort all beer reviews easily
    - Quickly approve any number of selected beer reviews so that they become visible on the site
    - Quickly disapprove any number of selected beer reviews so that they stop being visible on the site
    - Quickly delete any number of selected beer reviews
    - Fully edit a beer review, including rich text and images
    - View all comments submitted by users
    - Filter and sort all comments easily
    - Quickly approve any number of selected comments so that they become visible on their parent review page
    - Quickly disapprove any number of selected comments so that they stop being visible on their parent review page
    - Fully edit a comment, including rich text
    - View all extant users
    - Delete any number of extant users
    - View login attempts from dummy admin honeypot page

## Generic user User Stories 

These user stories apply to all users regardless of authentication status

- As a generic user I can ...
    - Immediately determine the purpose of the application when first visiting
    - Access the application from any web-enabled device and have a positive user experience
    - View all beer reviews
        - At the same, not be overwhelmed by reviews
    - Sort and filter all beer reviews so that I can see only the beer reviews that appeal to me
    - Have my sorting or filtering criteria reflected back to me so that I know which criteria I have applied
    - View any single beer review in its entirety so that I can read the content
    - Use a search function to search for beer reviews using keyword terms
        - If my search returned no results, have that reflected back to me
    
## Unregistered user User Stories

- As an unregistered user I can ...
    - Sign-up and create an account
    - Sign-in to that created account

## Registered user User Stories

- As a registered user I can ...
    - Sign in to a previously created account
    - Change the password for that account
    - Sign-out easily, when I am already signed-in
    - Have my sign-in status reflected back to me
    - Write a beer review easily
        - Apply rich text formatting to the content of my review
        - upload an image to my review
    - If signed in, easily access all of the reviews that I have written
        - If I have written no reviews, have that reflected back to me
    - Easily update any beer reviews that I have written
    - Easily delete any beer reviews that I have written
        - At the same time, ensure that I cannot accidentally delete any beer reviews
    - When viewing a single beer review, post a comment
        - when I have submitted a comment, have a confirmation message displayed to me indicating success
    - When viewing a single beer review, upvote it if I like it
    - When viewing a single beer review, downvote it if I do not like it

- Rejected user stories:
    - Be able to upvote comments
    - Be able to downvote comments


# Features

This section discusses the features and structure of the project's templates  and the design choices made

## Base

BeerGate uses a single base.html template to render every page. This provides a consistent user experience. The background image used is one of a tall glass of beer. A 50% opacity dark background has been applied over this image to darken it off. This is because the unmodified image is particularly bright and eye-catching.

## Header and Navbar

The navbar provides navigation to the other pages of BeerGate. The navbar was created using a standard Bootstrap navbar, so as to make it smoothly responsive on smaller screen sizes. Each list item in the navbar has been given the Bootstrap `btn` class to turn it into a button. Functionally, this has been used to apply a nice rounded border when the button is hovered over, and custom CSS has been written to turn the button white and keep the text black when this happens. This provides clear user feedback so that the user knows that they are about to click a button and be redirected to another page. 

If the user is signed out or has not yet created an account, their navigation options are limited. They may go back to the standard landing page view by clicking either the Reviews button or the bolded BeerGate icon. A user may created an account by clicking on the Sign Up button, or sign in to an existing account by clicking the Sign In button. 

The navbar list items change if the user is signed in. If signed in, the user may click on the Add a review button to be taken to a page where they may create and upload a beer review of their own. They may also click the My Reviews button to view all of the beer reviews that they have written. They may sign-out by clicking the sign-out button and finally they may change their password with the Change Password button. 

The navbar also informs the user whether or not they are signed in. If they are not signed in, text displays saying that. If they are signed in, different text displays saying that, and their username is displayed as well. 

The final part of the navbar is the search box. Using this, a user may search the database for reviews. These are displayed in a separate search results page. A search is triggered by pressing the Search button. The search function works independently of user sign-in status. 

Final navbar screenshot:

## Footer

The footer contains standard copyright information. 

Final footer screenshot:

## Landing page

The landing page is the first template rendered to the user when they visit the deployed project - [Beergate](https://beergate.herokuapp.com/). The navbar and footer are discussed separately below. The landing page is rendered from templates/index.html using the ReviewList view. The main content of the landing page are 4 'review cards', so called because each holds a link to a particular Review, and because each is created using a Bootstrap card. 

Final Landing page screenshot:

### Review cards

Each review card provides a brief overview snippet of a particular beer review. Each card provides quick information to a user that helps them decide which review to visit, such as the type and colour of the beer, when it was reviewed and the number of upvotes and downvotes. A user may click anywhere on the card to be directed to the associated review. I initially had only the name of the beer wrapped in the anchor element, however user testing on a mobile device indicated that it was sometimes difficult to tap the hyperlink. Modifying the template so that the entire card in within the anchor element allows a user with a mobile device to tap anywhere on the card to visit the review page.   

The review page is discussed in more detail [below](#review-page).

Single review card screenshot:

### Pagination

The landing page is set to display review cards in batches of 4. Further reviews are paginated, and these may be accessed by clicking or tapping on the Next button. Previous reviews may be accessed by clicking or tapping on the Previous button. This was implemented to save mobile users from having to endlessly scroll through reviews. 

Screenshot of pagination buttons

### Sorting and Filtering

Aside from the search function, I considered that it would be difficult to find particular records. Hence, I implemented some functionality that allows a user to sort and filter the records displayed on the landing page. By default, records are displayed in descending timestamp order, i.e. with the newest records first. A user may sort the records to display those with the highest number of upvotes first, and may also sort the records to display in ascending timestamp order, i.e with the oldest records first. 

A user may also filter the records by various properties. 

Firstly, they may filter by broad beer type - Ale, Stout and Lager. If any of these options are selected, only reviews of Ales, Stouts or Lagers will be displayed. 

Secondly, a user may filter by beer colour - Pale, Golden, Amber and Dark. If any of these options are selected, only reviews of Pale, Golden, Amber or Dark beers will be displayed. 

Finally, a user may filter by whether the beer, when reviewed, was served bottled or draught. This was included because a beer can taste different depending on whether it is drunk bottled or on draught, so it is perfectly possible to have two separate reviews of the same beer - one in which the beer was served bottled and another in which it was served on draught. In addition, if a user is looking to purchase bottles of beer from a supermarket, then reviews of draught beers would be unhelpful. Similarly, if the user is in a pub with draught beers, reviews of bottled beers would be unhelpful. 

Each of these sorting and filtering functions is rendered using its own view using the index template. 

Final screenshot of sorting and filtering bar:

## Review page

The review page is used to display a single beer review in its entirety. The review is held with a standard Bootstrap card. All the relevant fields in a record are displayed within this card, including the beer's name, keyword descriptors, content and scores. The output of the short_description method is also displayed. 

As with the navbar, the review page changes depending on the user's sign-in status. If signed in, a user may upvote and downvote that review by clicking on the thumbs-up and thumbs-down buttons. These buttons are mutually-exclusive - upvoting a review will cause an extant downvote to be removed. This particular feature was inspired by Reddit, which allows posts and comments to be upvoted or downvoted, not both. If the user is not signed-in, the upvote and downvote buttons are disabled and will instead just display the extant upvote and downvote totals. 

Below the upvote / downvote section is the comment section. If a review has no comments posted, the comments section will inform the user of this. If the user is signed-in, they may post a comment. I debated whether to make the comment submission field a rich text editor or a standard text field. Ultimately I went with a rich text editor because I wanted users to have the ability to add formatted comments. When a comment is submitted, it requires approval from an administrator, so a text box will display informing the user of that. 

Additionally, at the bottom of the card, there is a back button that directs the user back to the default landing page. This provides an alternative to the user's browser back button. If the the user is signed-in, and if the user is the author of that review, then they may update their review or delete it.

Final screenshot of upper review page:

Final screenshot of lower review page:

## Add Review page

The add_review page is rendered using the add_review template and the AddReviewView. 

The add_review page allows a user to write and submit a beer review of their own. This is done via a form. The user must enter all of the necessary information about the beer - the name, brewery, type, colour, alcohol content, a short description, their full review and then their score in each of 4 categories - aroma, appearance, taste and aftertaste. The user may also upload an image, though this is optional. If no image is uploaded, the review will display a placeholder image. The user may select whether the beer was served bottled or on draught. 

As with review comments, reviews are not automatically displayed, as they must be approved by an administrator. When submitted, a message will display informing the user of this. 

Final screenshot of upper add review page:

Final screenshot of lower add review page:

## Update Review page

The update_review page is rendered using the update_review template and the UpdateReviewView view. It functions similarly to the add_review template as the form uses the same form template and fields, except that the form fields are pre-populated with the extant records. A user may update any of the review's information, including the image. When submitted, the record is automatically disapproved, and a text box displays informing the user of this. 

Final screenshot of upper update review page:

Final screenshot of lower update review page:

## Delete Review page

The delete_review page is rendered using the delete_review template and the DeleteReviewView view. It is a simple template, and allows a user to delete a particular review. Rather than having a simple button to do this, I considered that placing the actual delete button inside a modal would be superior, to prevent a review being deleted by accident. In this way, a user must actively seek to delete a review. 

Final screenshot of delete review page:

## Search Results page

The search_results page is rendered using the search_results template and the SearchResultsView view. The page consists of a Bootstrap card which contains all of the reviews returned by the search query. Similarly to the landing page, the entirety of each search result is contained within an anchor element linking to the particular review. Due to the particular structure and intended look of this page, I had some difficulty making it responsive to smaller screen sizes. In particular, the images proved troublesome. To overcome this issue, I set the images to be hidden on these smaller screen sizes. As each search result is placed within an anchor element, the text within each search result card is given anchor element styling - namely a blue colour and underline text decoration. I removed this native styling for most of the text elements, but kept it for the beer name, with the intention being to mimic the Google search results page, where the clickable links have unmodified anchor element styling. 

The reasoning for placing the entirety of each search result within an anchor element is the same as that applied to the landing page - it aids tapping for mobile device users. 

Final screenshot of search results page:

## User Reviews page

The user_reviews page is rendered using the UserReviewsView. The design is intentionally very similar to that of the search_results page, including the lack of images on smaller screen sizes, as I view both pages as a means of listing some collection of reviews, though obviously the difference lies in *how* that collection is assembled - this is dicussed in more detail in the Function section. The only noticable difference is that the user_reviews page's search results do not display the author of the reviews. As the author of the review is the user themselves, I considered this to be redundant. 

The idea behind the implementation of this page is to allow a user to quickly see all of the reviews that they have written, so that they can update or delete them in one place, and also quickly see the number of upvotes and downvotes that other users have made against their reviews. The page also allows users to quickly visit each of their reviews to see the comments other users have posted. 

Final screenshot of user_reviews page:

## Sign In, Sign Out, Sign Up and Reset Password pages

These pages are modified versions of the standard AllAuth templates that can be copied over from the site-packages directory with the `cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates` command. A new app called 'user' was started to hold the views, forms and urls that control these templates, primarily to apply the Bootstrap `form-control` class that makes the input elements smooth and nice to use with user feedback. 

# Function

This section is discusses the code used in the project, and explains any particularly note-worthy or obscure features. 

## Reviews app

The Reviews app is where the bulk of the project's development took place, and holds most of the back-end code. 

### Reviews Models

BeerGate uses two data models - Review and Comment. A validation function called `validate_within_limits` has also been written to validation inputs for the Review model's aroma, appearance, taste and aftertaste fields. These are IntegerFields, but the values must be between 1 and 10

#### Review class

Review is the primary data model for BeerGate. As of the end of the project's development cycle, it contains 18 fields. The name, brewery, type, colour and keywords fields are all standard character fields. The image field is a CloudinaryField, as uploaded images are saved to the Cloudinary CDN. 

The content field is a TextField, but this was not always the case. As noted elsewhere, I initially used the django-summernote package to apply the Summernote Rich Text Editor, but this caused a fatal error that required the project to be restarted. When the project was restarted, I used the CK-editor package, which supplies a custom field type called RichTextField. When this package did not work on the deployed app, I switched to using the django-tinymce package in hopes of using the TinyMCE Rich Text Editor, which supplies a custom field type called HTMLField. Again, this did not work on the deployed app, so I went back to using the django-summernote package. Unlike the other two, the django-summernote package merely requires a widget called SummernoteWidget to be applied to a standard TextField in the corresponding forms file. 

A late addition to the Review model was the served_as field, which is an IntegerField. It operates similarly to the status field of the Django Blog walkthrough project, in that the served_as field takes values defined within an external global variable, which is in this case called SERVED_AS. The served_as field determines whether the beer was served bottled or on draught, as the same beer can taste differently depending on how it is served. 

The upvotes and downvotes fields are ManyToMany fields linked to the standard Django User model, since many users can upvote and downvote many reviews. I decided early on to include separate upvotes and downvotes fields since I am an avid user of Reddit, but I dislike Reddit's choice to combine upvotes and downvotes into a single number, as a user cannot see the total number of upvotes and downvotes. With separate upvote and downvote counts, both numbers can be displayed, so that users can see how many people agree with a review, and how many people disagree, so as to be as well-informed as possible.

The author field is a standard ForegignKey field linked to the Django User model. It has the `ondelete=models.CASCADE` instruction so that if a user is deleted from the database then all of that user's reviews are deleted as well. 

The timestamp field is standard DateTimeField with the `auto_now_add=True` instruction so that the exact date and time that a review was submitted is captured. 

The approved field is a BooleanField with a default value of False. This field palys a considerable role in the security and defensive programming of BeerGate. As discussed below, reviews that are not approved are not displayed to users, and must be manually approved by an administrator. This field ensures that malicious users cannot post inappropriate or offensive reviews.

The aroma, appearance, taste and aftertaste fields are standard IntegerFields, with validation being handled by the validate_within_limits function. These fields provide quick numerical scores of beers. These were added after I found [RateBeer](https://www.ratebeer.com/), and noted that said site allows numerical scores. I felt that using numerical scores along with class methods to do something with these would elevate the project. I am a member of CAMRA, and so I was able to find the criteria used by their judges in the Champion Beer of Britain competition.

Early versions of the Review model used a slug field with the SlugField type, which was used to generate custom URLs, much as like in the Django Blog walkthrough project. However, this proved to be an obstacle to mass-approval of reviews in the admin panel. As in the walkthrough project, the slug field was set to be pre-populated, but I discovered that this pre-population only occurred when each individual record was accessed. Should users collectively submit hundreds of reviews, an administrator would need to access each record to pre-populate the slug field, which would be a huge time-sink. When this was discovered, the slug field was removed and the project converted to use the primary_key of each Review instead. 

##### Review class methods

The Review model contains a number of methods. The first of these is a standard Meta class, which supplies the verbose name and ordering of the reviews. 

There is also a standard string method, the so-called 'magic method', which returns a text string containing the name of the beer and the author's name. 

The get_absolute_url method specifies the redirection URL, which is used when upvoting and downvoting reviews, as these reload the page. 

The description method returns a composite text string containing the beer's colour, type and brewery. This returns something like "A Golden Ale by Hogsback".

The short_description method returns the keywords field in a more user-friendly way, much like the magic string method. It returns something like "Described as Hoppy, zesty and bitter".

The review_upvotes and review_downvotes methods are quite simple and return total counts of the number of upvotes and downvotes applied to a review. These are injected into various templates as a measure of how highly or lowly rated a review is. 

The average_score method averages the values of the aroma, appearance, taste and aftertaste fields to provide a single overall score for a beer. 

#### Comment class

The Comment model is a secondary data model for BeerGate. It provides the functionality for users to comment on Reviews

The review field is a ForeignKey field that links a comment to a particular Review, much like the author field does for the Review model. It has the ondelete=models.CASCADE so that should a Review be deleted, all attached comments will be deleted as well. 

The author field is a ForeignKey field that functions identically to the author field of the Review model. 

The content field is a standard TextField. I have chosen to use the SummernoteWidget in the forms file to make this field into a RichTextEditor, so as to give commenting users the same rich text formatting options as they have when writing reviews. 

The timestamp and approved fields function identically to those fields of the same name in the Review model. 

The upvotes and downvotes fields function identically to those fields of the same name in the Review model. However, at the time of writing, I was unable to implement upvoting and downvoting of comments, as Reddit allows a user to do, primarily because the voting function for Reviews reloads the page, using the primary key of the review as the redirection URL. Nonetheless, I have decided to keep these fields in the model with a view to implementing such functionality at a later date. The total numbers of upvotes and downvotes are never displayed on the front-end, so a user will never know that the model contains those fields. 

##### Comment class methods

As with the Review model, the Comment model contains a Meta child class that supplies a verbose name and ordering. In contrast to the Review model, comments are ordered in ascending timestamp order, so that the oldest comments appear first. As in the walkthrough project, the intention is to mimic a conversation around the review and the beer. 

The Comment model also contains a magic string method that returns a string of text containing the author and the content of the comment. It returns something like "Robert said: Nice review!"

### Reviews Views

#### Index views

I have written a large number of views that render various versions of the the landing page using the index.html template. Each of these uses the generic Django ListView and in all cases the model is the Review model with pagination set to 4. 

The justification for these various index views is [here](#ordering) 

##### Default view

The default view is called ReviewList, and the queryset filters the Review to include only those that have their approved field set to True, and orders these in descending timestamp order, so that the newest reviews are displayed first. 

##### Sorting views

There are two other views which apply different sorting instructions. 

ReviewListMostUpvotes uses the annotate method to get the total number of upvotes for each Review, and then orders Reviews by this number. This allows users to view the most highly rated reviews first. The annotate method works similarly to the review_upvotes method of the Review model, in that it counts the number of upvotes and returns this count so that it can be used by other methods. 

ReviewListOldest is nearly identical to the default ReviewList view, except that it orders Reviews in ascending timestamp order, so that the oldest reviews are displayed first. 

##### Filtering views - type

The ReviewListAleType, ReviewListStoutType and ReviewListLagerType function similarly to the default ReviewList view, filtering out those reviews that are not approved and ordering by descending timestamp order. These views also filter by the Review model type field. 

ReviewListAleType filters out beers that do not have Ale as their type

ReviewListStoutType filters out beers that do not have Stout as their type

ReviewListLagerType filters out beers that do not have Lager as their type

##### Filtering views - colour

These views are called ReviewListPaleColour, ReviewListGoldenColour, ReviewListAmberColour and ReviewListDarkColour. These function similarly to the default ReviewList view, filtering out those reviews that are not approved and ordering by descending timestamp order. These views also filter by the Review model colour field. 

ReviewListPaleColour filters out beers that do not have Pale as their colour

ReviewListGoldenColour filters out beers that do not have Golden as their colour

ReviewListAmberColour filters out beers that do not have Amber as their colour

ReviewListDarkColour filters out beers that do not have Dark as their colour

##### Filtering views - served_as

These views are called ReviewListBottled and ReviewListDraught These function similarly to the default ReviewList view, filtering out those reviews that are not approved and ordering by descending timestamp order. These views also filter by the Review model served_as field.

ReviewListBottled filters out beers that do not have 1 (meaning bottled, since served_as is an IntegerField) as the served_as value

ReviewListDraught filters out beers that do not have 2 (meaning draught, since served_as is an IntegerField) as the served_as value

#### Review view

The view that renders the entirety of a single review using the review.html page is called BeerReviewSingle. 

This view holds two methods - a get method and a post method. These are little different from the PostDetail view of the walkthrough project, except that in each method I have chosen to explictly define a variable called context to hold the object that holds the various key - value pairs that can be used in the template. I consider that this is a more pythonic way of doing things, and I generally prefer explict variable declarations anyway. 

The get method defines a queryset containing all approved Reviews, and then retrieves a specific review using the `get_object_or_404` method, using the review's primary key, pk. It also retrives that review's comments, and defines two variables - upvotes and downvotes, both set to False. If the user is signed-in and has previous upvoted or downvoted that review, then either the upvoted or the downvoted variable is set to True. The specific review is then rendered in the return statement using the render keyword, the review.html template and the context variable. 

The post method functions similarly, except that it has additional code to handle the submission of the CommentForm. If the submitted CommentForm is valid, the user and the current review are attached to the comment submission, so that the comment 'belongs' to that particular user and that review. In the context, commented is set to True, which triggers some templating language code to display a submission confirmation textbox to the user. 

#### Search Results view

The SearchResultsView view renders the search_results page using the search_results.html page. The object_list, which holds the reviews that are displayed, is constructed using the get_queryset method, which retrieves the search term used in the navbar's search box input element as a variable called query. The object_list is then constructed using a standard filter method that uses [Q Objects](https://docs.djangoproject.com/en/4.0/topics/db/queries/#complex-lookups-with-q-objects) to chain filters together. The code in this view was written using [this tutorial](https://learndjango.com/tutorials/django-search-tutorial), authored by known Django expert Will Vincent. The object_list is the returned for use within the template using templating language.  

#### User Reviews view

The UserReviewsView view renders the user_reviews page using the user_reviews.html template. It is relatively simple, using get method to construct a queryset consisting of all reviews belonging to a particular user that have been approved. As in BeerReviewSingle, a context variable has been explictly defined outside of the return statement that is then called in that return statement. 

#### Add Review view

The AddReviewView view renders the add_review page using the add_review.html template. This is, if you will, the meat of the project, as it allows a user to upload a beer review using a form. The form itself is rendered using the form_class variable set to the imported UserReviewForm. In previous versions of the project, as in the walkthrough project, a get method was used to render this form. Using the form_class variable reduces the amount of code required considerably, and thereby reduces complexity. The UserReviewForm is discussed in more detail [here](#userreviewform).

Form submission is handled using the post method. This functions similarly to the code that handles comment submission in the BeerReviewSingle view, essentially checking if the submitted form is valid, and the attaching the user ID if so, so that the review 'belongs' to that particular user. A context variable is then defined and a return statement renders the template again, this time with the reviewed key set to True, which triggers some templating language to display a textbox informing the user that their review has been submitted and is awaiting approval. 

#### Update Review view

The UpdateReviewView view renders the update_review page using the update_review.html template. This a necessary companion to the AddReviewView, as it allows a user to update their reviews. As with the AddReviewView, a form_class variable specifies that the UserReviewForm is to be used. The view uses 3 methods - a get method, a post method and a form_valid method. These methods are necessary because I wanted this view to automatically disapprove reviews when they are updated. As discussed in the [bugs section](#bugs), this is a prudent security measure and part of the defensive programming employed in BeerGate. I found that without these methods, when the form is submitted, the review instantly and automatically holds the updated information. This is a vulnerability that a malicious user could exploit, first by submitting a seemingly-genuine review, getting it approved and then updating it with malicious/inappropriate/offensive content. 

Full credit for the design of these methods goes to [this Reddit question](https://www.reddit.com/r/django/comments/8jkh5t/updateview_creates_new_items_in_the_db_instead_of/), where the author appears to have had a similar issue, and they answer their own question. I confess that I do not fully understand what these methods are doing, but my understanding is as follows:

The get method retrieves the particular review that is being updated and the form that is being used. The post method handles the submission of the form containing the updated information. I have added a line of code that sets the updated review to be disapproved inside the IF statement block. The form_valid method then saves the updated information to the database. The return statement that renders a context is my own work, which sets the updated flag to True. This in turn triggers some templating language code in the template that informs that user that their updated review is awaiting reapproval. 

#### Delete Review view

The DeleteReviewView view renders the delete_review page using the delete_review.html template. This view uses the generic Django DeleteView which allows easy deletion of records. Once the review has been deleted, the success_url variable redirects the user back to the landing page. 

#### Review Upvote and Review Downvote

The ReviewUpvote and ReviewDownvote views handle upvoting and downvoting of reviews. They are essentially identical, and the core code borrows heavily from the walkthrough project's PostLike view. I have made my own additions inside the ELSE blocks of the post methods which make upvotes and downvotes mutually exclusive - that is, a user may either upvote or downvote a review, not both, and if a user has previously upvoted a review, then downvoting it will remove the extant upvote, and vice versa. Once a vote has been applied, the user is redirected back to the review they were voting on. 

### Reviews Forms

The forms file contains two form classes - CommentForm and UserReviewForm. As is the case in the walkthrough project, these forms are explicitly defined because I wanted to specifically control which fields were displayed. In addition, I wanted to apply the Bootstrap `form-control` class to makes the forms nicer to use. I was able to use the widgets variable to apply the `form-control` class. Later on, the widgets variable helped get the django-summernote Rich Text Editor working by way of the SummernoteWidget. I was also able to use the labels variable to modify the labels of the form input elements. 

#### CommentForm

The CommentForm class is quite simple - it sets that the only field to be displayed is the content field, which is made into a Rich Text Editor by way of the SummernoteWidget. The label is also modified to 'Your comment' 

#### UserReviewForm

The UserReviewForm class appears to be more complex, but is functionally similar to the CommentForm. It restricts the fields that are displayed and applies the `form-control` class to those fields, with the exception of the content field, which is turned into a Rich Text Editor using the SummernoteWidget. The widget object also allowed me to add the placeholder attribute to several fields which meant that I could add assistive placeholder text.  

### Reviews URLS

The urls file holds the urlpatterns for the reviews app. Most of the paths apply to the previously-mentioned sorting and filtering views that render various versions of the landing page. After these comes the add_review, search and user_review pages. Lastly come the paths which render the review pages and the pages for updating and deleting records, as well as the upvote and downvote paths. As previously mentioned, reviews are not listed by their slug but instead by their primary key, so for paths that deal with specific records, `<int:pk>` is used instead of `<slug:slug>` as in the walkthrough project.   

I learned early on in development that paths that take in arguments are considered more general, and must hence be placed below more specific paths. Prior to learning this, an error would occur whenever I tried to naviagte to the add_review page. Thankfully Tutor Support were able to teach me this. As it turned out, I had all of the pieces in place, and the ordering of the urlpatterns was the only barrier. 

### Reviews Admin

The admin file controls the layout of, and actions available in, the Django admin panel. Functionally, it is little different to the admin file of the walkthrough project. There are two classes - BeerReviewAdmin and CommentAdmin - thanks to my going back to using the django-summernote package, both admin classes extend the SummernoteModelAdmin class. 

Both admin classes are also similar in construction, as both have the same control variables - list_filter, list_display, search_fields, actions and summernote_fields. The list_display control variable within both classes has been given terms that allow an administator to quickly see the pertinent meta-data of a review - beer name, beer type, colour, brewery, timestamp, approval status, and the author. 

Both admin classes have the same two methods - approve_beer_review / approve_comment and disapprove_beer_review / disapprove_comment. The approve methods are used for mass approval of all selected reviews whilst the disapprove methods are used for mass disapproval (i.e. mass withdrawal) of all selected reviews. 

## User app

The user app was started purely to achieve better control over the rendering of the signin.html, signout.html, signup.html and password_change.html templates. Primarily, the goal was to apply the Bootstrap `form-control` class to the forms. After doing this with the CommentForm and UserReviewForm in the reviews app, this proved quite easy, however in order to use the custom forms, I had to create custom views. 

It should be noted that I created forms and views for all of the AllAuth functions, not just signing in, signing out, signing up and changing passwords. After doing so, I tested these and noted that only those named functions worked out-of-the-box. The others, such as resetting a password, required an email service. After speaking with my Mentor about this, he suggested keeping the views and forms and then removing the paths from the urls.py file, thus disabling them and ensuring that they could not be accessed accidentally. Getting this functionality working will be something to work on in the future after project submission.  

### User Views

As noted above, the only views in user/views.py that are in active used by BeerGate are UserSignInView, UserSignUpView and UserPasswordChangeView. There is no custom view for the user signout functionality because while that template has a form, it only consists of a submit button and hence has no need of the `form-control` class. 

The active views are very simple, only using the form_class and template_name variables to designate the form and template to be used. The UserSignInView extends the AllAuth LoginView, the UserSignUpView extends the SignupView and the UserPasswordChangeView extends the PasswordChangeView. 

### User Forms

As with the views, only the UserSignInForm, UserSignupForm and UserPasswordChangeForm are actively used by BeerGate, with the others dormant until their corresponding views can be put into use. 

Initially I tried using the widgets method shown in reviews/forms.py to apply the `form-control` class to forms, but this failed. I then found [this Medium article](https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56) (as a Medium article, access might be restricted), which suggested using an `__init__` method within each form class to apply the `form-control` class. 

The UserSignupForm and UserChangePasswordForm use a for loop to apply a `form-control` widget to each form field. However, this approach failed with the UserLoginForm, since this form has a 'remember me' checkbox, which, when given the `form-control` class, becomes an input field that cannot accept any input. To overcome this, I used another technique from that article to apply the `form-control` class to only the username and password input elements. This itself proved difficult, since the name of the username field is unhelpfully called 'login' rather than 'username', as might be expected. 

### User URLS

As noted above, the user/urls.py file's urlpatterns list only contains 3 paths. These are for the signin, signup and password_change pages. In the future, as I get the remaining AllAuth functionality working, corresponding paths will be added to allow these templates to be accessed. 






# Design Choices

I intend to use the background image used in the first Beergate project, that of a tall glass of beer with a dark background, which is then given some opacity to darken it off. This will apply to all pages for a uniform user experience. 
<br><br>
Given the dark background, each beer review post shall be held in a Bootstrap card with a light colour - white, off-white or light grey. 

# Database Models

As a Full Stack project that uses Django, this project uses models to create the database tables. These are below, and include the column headers, examples of what might be in that column and other relevant notes.

## Beer

The Beer model is used to create a table that holds all of the data to make a beer review post. 

| Column Header      | Example             | Other notes                                                      |
| -------------------|---------------------|------------------------------------------------------------------|
| name               | Golden Champion     | Unique(?), CharField, primary key?                               |
| brewery            | Hogsback            | CharField, One to Many since one brewery can make multiple beers |
| type               | Lager / Stout / Ale | CharField                                                        |
| colour             | Amber / Pale / Dark | CharField                                                        |
| alcohol_content    | 4 / 5.5             | DecimalField(max_digits=3, decimal_places=1)                     |
| image              | an image            | Cloudinary image                                                 |
| slug               | golden-champion     | SlugField, generated from name to create unique URLs             |
| content            | This beer is a beer | TextField, forms main content of post                            |
| keywords           | Hoppy / Malty       | CharField                                                        |
| hops               | American / Indian   | CharField, the hops used in the beer                             |
| upvotes            | 112                 | ManyToManyField, since many users can upvote many posts          |
| downvotes          | 21                  | ManyToManyField, since many users can downvote many posts        |
| author             | John Smith          | ForeignKey, from User table, on delete cascade                   |
| created_on         | 32nd of January     | DateTimeField                                                    |
| approved           | boolean yes/no      | BooleanField, I approve as admin superuser                       |
| aroma              | 8                   | IntegerField, with validation to accept values between 1 and 10  |
| appearance         | 5                   | IntegerField, with validation to accept values between 1 and 10  |
| taste              | 10                  | IntegerField, with validation to accept values between 1 and 10  |
| aftertaste         | 4                   | IntegerField, with validation to accept values between 1 and 10  |
| Aroma              |                     | The smell of the beer - does it smell good or bad                |
| Appearance         |                     | Colour, clarity, head and visual carbonation                     |
| Taste              |                     | How does it taste - is it overly bitter, too weak or just right? |
| Aftertaste         |                     | How the taste lingers in the mouth                               |


The Beer model will have a Meta class that orders reviews by created_on in descending order, so that the newest reviews are displayed first

The Beer model will also have a magic string method to return the name of the beer, and two methods that deal with the numbers of upvotes and downvotes, one for each. These methods will return a count of these numbers so that they can be displayed. 

### Discussion


## Comment

The Comment model is used to create a table that holds all of the information to display a comment on a beer review post. 

| Column Header      | Example             | Other notes                                                      |
| -------------------|---------------------|------------------------------------------------------------------|
| post               | Guinness            | ForeignKey(Beer), on delete cascade                              |
| author             | Bob Smith           | ForeignKey(User), on delete cascade                              |
| body               | I agree with this   | TextField                                                        |
| created_on         | 33rd of February    | DateTimeField                                                    |
| upvotes            | 54                  | ManyToManyField, since many users can upvote many comments       |
| downvotes          | 67                  | ManyToManyField, since many users can downvote many comments     |

The Comment model will have a Meta class that orders comments by created_on in ascending order, so that the oldest comments are displayed first. 

The Comment model will also have a magic string method to return the comment itself followed by the name of the commenter. The Comment model will also have two other methods that deal with the numbers of upvotes and downvotes, one for each. These methods will return a count of these numbers so that they can be displayed.

### Discussion

The post and author fields will both be Foreign Keys, and will have on_delete=models.CASCADE. This means that the comment will be removed if the parent review is deleted, or if the author's account is deleted. As above, this is intended as a defensive measure, so comments made by malicious users are deleted if that malicious user's account is deleted. 
<br>
<br>
The Meta class that orders comments by created_on date so that the oldest comments are displated first is intended to simulate a conversation, so that other users can follow any discussion in the comments of a post. 

# Deployment

This project was deployed to Heroku early on, as per the Django Blog walkthrough project. This proved to be a valuable lesson, since I deployed my Project 3 to Heroku quite late, which caused much stress. As a bonus, early deployment allowed me to view the project on my mobile device when not developing the project, allowing me to note bugs and areas where improvements were needed. 

## Project set up

Given that this is a Django project, a number of terminal commands must be run before any real development work can begin:

Install Django v3 and the Gunicorn web-server: <br>
`pip3 install 'django<3' gunicorn`

Install libraries necessary for working with PostgresQL:<br>
`pip3 install dj_database_url psycopg2`

Install libraries needed for Cloudinary:<br>
`pip3 install dj3_cloudinary_storage`

Create a requirements.txt file:<br>
`pip3 freeze --local > requirements.txt`

Create a new Django Project:<br>
`django-admin startproject beergate .`

Create a new Django app for the beer reviews: <br>
`python3 manage.py startapp reviews`

Then add 'reviews' to beergate/settings.py

Now migrate the changes made by starting the beergate project and the reviews app to the database:<br>
`python3 manage.py migrate`

Check that Django and all other libraries have been installed by running the project locally:<br>
`python3 manage.py runserver`

Create a new Heroku app and add on the heroku-postgres module. Copy the DATABASE_URL config var

Create an env.py file. At the top, import os and create an os environment variable called DATABASE_URL and assign it the value from Heroku as a string
Then add a second os environment variable called SECRET_KEY and assign it a random value
Add this to the Heroku config vars

Add a conditional import to settings.py to import env.py
Update the DATBASES variable in settings.py to use the heroku DATABASE_URL config var

Then migrate the changes again:
`python3 manage.py migrate`

Add Port 8000 to Heroku config vars

### Cloudinary

Create a Cloudinary account, copy API environment variable

Add CLOUDINARY_URL environment variable to env.py and paste in
Add same to Heroku config vars

Add DISABLE_COLLECTSTATIC to Heroku config vars as well, with a value of 1

Add static file storage and media file storage to settings.py
Add local host and heroku app name to ALLOWED_HOSTS
Add the TEMPLATES_DIR to settings.py

Create media, static and templates directories at top-level of the repository

Create a Procfile

### Models

Create Models in reviews/models.py

Prepare migrations:
`python3 manage.py makemigrations`

Load models into database and create tables:
`python3 manage.py migrate`

### Superuser and Django admin panel set up

Create a superuser:
`python3 manage.py createsuperuser`

Run a development server to access the Django admin panel:
`python3 manage.py runserver`

Append `/admin/` to the URL

Login to Django admin backend using superuser credentials

(solve problem relating to automatic upgrade to Django v4.1 - see bugs section)

Update admin.py to allow superusers to create beer reviws in the Django admin panel

Install Summernote to allow rich text in admin panel:
`pip3 install django-summernote`

Add summernote to requirements.txt:
`pip3 freeze --local > requirements.txt`

Add summernote to INSTALLED_APPS in settings.py

Update urls.py, then admin.py

Migrate again:
`python3 manage.py migrate`

### Views

Views and URLs created as per walkthrough videos. Beer review posts not displaying. 

Problem may lie in views.py, where reviews are filtered by approved=True. May need to update model to use the Draft / Published IntegerField system of the Django Blog. 

Views created successfully and above problem solved - see bugs section. 

### Single beer review page

Create BeerReviewSingle view that contains a get method and a return render

Create a template to display the review - beer_review_single.html

Create a path in urls.py 

### AllAuth

Install AllAuth:
`pip3 install django-allauth`

Update requirements.txt:
`pip3 freeze --local > requirements.txt`

In beergate/urls - add a path for the allauth urls. 

In settings.py - add allauth, allauth.account and allauth.socialaccount to INSTALLED_APPS. Add SITE_ID=1, LOGIN_REDIRECT_URL='/' and LOGOUT_REDIRECT_URL='/'

Run migrations:
`python3 manage.py migrate`

Port in templating language for authenticated users to navbar

Go to Register page, create account

Go to Login page, login using that account

Now modify allauth templates:

Determine version of Python:
`ls ../.pip-modules/lib` - python v3.8

Copy allauth templates to templates folder:
`cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates`

In account/login.html, account/logout.html and account/signup.html, replace `{% extends "account/base.html" %}` with `{% extends "base.html" %}`
Visit the login page to check that these pages are extending base.html properly

### Commenting

Install Crispy Forms:
`pip3 install django-crispy-forms`

Add Crispy Forms to settings.py INSTALLED_APPS

Create a forms.py in reviews

Import the Comment class (and the BeerReview Class, for later)

### Creating a user submitted beer review form

Create a beer review form class in forms.py

Create a new view in views.py

Problem - 404 error when accessing user_review page

Tutor support solution - Uninstall Django 4.1, downgrade to Django 3.2, reorder urls in urls.py so that the user_review path is above the beer_review_single path


## Development process

Now that Django has been set up:

I need to change up the process that is used in the Walkthrough

Users should be able to make posts

This will require appropriation of the code for leaving a comment

I foresee two methods by which a user could make a post:
- Hide the form where a user makes a post behind a button on the index page. When the user clicks this button, the form is revealed and the user may write their post
- Provide a button with an anchor link that takes the user to a separate page where the post is written - USE THIS APPROACH
    - This is a separation of concerns matter - the index page is displaying posts, the single_review page is for viewing a post and the make_a_post page is for writing a post.

# Tasks

Done:
- implement upvotes / downvotes feature for Beer Reviews - done 
- Implement a Summernote content field or other rich text editor for user-generated posts - done using CKeditor
- Look into an error displayed when creating a new account. Account appeared to be created successfully (I was able to log in with it), but got a Django error page with Error 111 Connection Refused - No longer a problem
- If a user attempts to submit a duplicate review - i.e same author and same beer name, an error is thrown. Need something to handle this - done thanks to move to display by primary key
- It does appear that when uploading a post from the site that a slug is not automatically generated - no longer an issue as slug removed
- Find fix to the problem on images not uploading - use cloudinary image upload(https://cloudinary.com/documentation/django_image_and_video_upload) - fixed and documented
- implement functionality to allow users to update, and delete their posts - both done, full CRUD functionality
- For the admin backend, add a disapprove method, so that several previously-approved reviews can be made inactive at the same time, much like several unapproved reviews can be approved at the same time.
- implement an exclusivity feature - if a user upvotes, remove their downvote, if user downvotes, remove their upvote so that they cannot do both at the same time

- Style AllAuth forms with Bootstrap - done
    - Steps:
        - Start new app called 'user'
        - add 'user' to beergate/settings.py INSTALLED_APPS
        - In that, add a forms.py and a urls.py
        - in forms.py, import the AllAuth LoginForm and SignupForm
        - create custom UserLoginForm and UserSignupForm classes, and use them to extend the LoginForm and SignupForm respectively
        - in settings.py, override standard AllAuth forms using the ACCOUNT_FORMS variable
        - Per [this Medium article](https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56), add code to apply widgets to form fields that add the Bootstrap CSS form-control class
        - Import these custom forms into user/views.py
        - Create UserLoginView and UserSignupView, which extend the AllAuth LoginView and SignupView
        - assign these views the relevant form_class and template_name, being sure to prefix the template with account/, since the templates are located in the account directory
        - create paths in user/urls.py, importing the necessary views

- Style additional AllAuth forms with Bootstrap - done
    - email
    - password_reset_from_key
    - password_reset
    - password_set
    - plus AllAuth templates without forms

- Implement modal for delete_review.html so that a user must manually confirm deletion - done
- [Implement a search bar function](https://learndjango.com/tutorials/django-search-tutorial) - done
- add `logged in as: {{ user.username }}` to base.html somewhere, so the user can confirm that they are logged in
- Implement functionality to allow a user to see their own reviews - done
- use `{% block title %}{% endblock %}` control statements to provide custom titles for html pages - done
- Find a way to list all of a particular user's posts for easy access - done
- Background image not displaying on deployed site - done, documented in bugs section
- Review generic placeholder image - done, new image will much greater resolution used which is better for the review.html page
- Provide a consistent aspect ratio for post images - done by sizing the image-container element using bootstrap classes
- Not all cards displaying on mobile devices - done by reworking html structure and css rules
- Fix bug related to UpdateReviewView creating a new record - done
- Implement Django HoneyPot - done
- Add settings.py booleans to enhance security - done
- Apply bootstrap to search results and user reviews page - done
- Larger, bolder, more prominent font on navbar - done
- CKeditor rich text field not displaying on deployed site, including mobile devices- done by implementing Summernote

- For a user-written beer review form:
    - need a completed BeerReviewForm in forms.py - done
    - need a new view in views.py - done
    - need a context in the return render of the view - done
    - need a template and front-end links to that - done
    - need a path in urls.py for that template - done
    - Add some functionality to handle an improperly completed form. Apply this to the comment form as well (for example if a user tries to submit an empty form). 
    - update admin.py with an approve beer review action - done

- Offer an option of ordering reviews by the number of upvotes - use a dropdown menu or some type of selector (in navbar?) Then render different index views based on that selection

- Implement functionality to broadly sort reviews by type and colour
    - use index.html and ListView
    - expand navbar dropdown menu
    - dropdown divider to separate different sorting parameters
    - use filter in view
    - sort by type - ale, stout, lager
    - sort by colour - pale, amber, dark
    - principle is to sort by broad characteristics
    - each needs its own view for sorting on index template
    - for readme - Martin is not a beer drinker, so the search bar is less useful due to lack of familiarity with terms, so dropdown menu provides clearer sort function
    All Done

- Update data model to allow a user to select whether a beer is bottled, draught, etc, and then filter results by this - expand navbar filtering - done
    - Update data model to include a 'served_as' IntegerField - done
    - Above Review model, designate a global SERVED_AS variable = `(0, 'draught'), (1, 'bottled'))` - done
    - In IntegerField, use choices=SERVED_AS, default of 0 - done
    - https://stackoverflow.com/questions/5924988/radio-buttons-in-django-forms for more
    - and https://stackoverflow.com/questions/27321692/override-a-django-generic-class-based-view-widget/27322032#27322032
    - in widgets - 'served_as': forms.RadioSelect - done
    All Done

- Remove unused AllAuth URLS in urls.py, keep views and templates - done
- add more content to index cards to better reflect any sorting that has been applied - done
- comment disapproval method not working due to spelling error - done
- Navbar fails to render properly on horizontal tablets - screen widths 992 to 1400px / lg to xxl breakpoints - done
- review reviews/admin.py to see if more terms need to be added to the control variables - done
- Footer - done
- In BeerReviewSingle view, UserReviewsView view and AddReviewView, explicitly define a context variable to hold the object in the return statement, then call context in that return. Do same with template_name variable - done
- add return of average_score method to index card, next to upvotes/downvotes - done
- Fix issue of floated card content becoming misaligned at smaller screen sizes - done







Rejected:
- add update and delete buttons to user_reviews so that a user does not have to access each record individually - not possible, since the entire search result card is itself an anchor element, it cannot have other anchor elements as children
- In UserReviewForm, apply bootstrap to RadioSelect widget with name, class, etc - rejected as unnecessary, since the extant radio buttons are clear enough





In progress:
- Review and update Bootstrap card structure for non-AllAuth templates:
    - base / navbar - logged-in note for collapsed navbars
    - index
    - review 
        - main image is rather large so reduce size - done
        - centre comment rich-text field - more difficult
    - add_review - try to centre the rich-text editor box
    - update_review - increase width, use same layout as add_review - done
    - delete_review - add link to update the review - done
    - user_reviews - in progress
    - search_results - in progress
- Style AllAuth templates - sign-in, sign-up, login, logout, email, password, etc - 

Modify sorting to use a checkbox group like GW - https://stackoverflow.com/questions/31145498/how-to-submit-checklist-in-django-with-get




Note regarding search_results and user_reviews:
The mobile view displays at 576px
However, horizontal phones will use the >576px width
vertical phones top out at about 412px, so apply cols and offsets to satisfy this, and note these observations fully
The major exception is the Surface Duo, which is a hybrid tablet/phone

To do:

- Allow the superuser (user ID = 1) to update and delete all posts as well as users, so that the admin does not have to use the admin panel
    - related, allow the superuser to quickly access the admin panel from the front-end
    - update method auto-disapproves, so admin panel access would be required anyway
    - This renders the justification moot
    - However, could use an AdminUpdateReview view that does not use the methods, and hence does not auto-disapprove the review



- Place My Reviews, Sign-out and Change Password behind a Account actions dropdown menu to make navbar less busy

- add more content to search results and user reviews pages in the same vein as index

- update data model with a OPTIONAL field for where a beer may be purchased. 'If you bought this beer online, where did you buy it from?' - encourages traffic to brewery websites
    - From a user perspective, this is easy to do on a PC with multiple tabs, but less easy to do with a mobile device

- move sorting menu from navbar to its own navbar only on the index page - perhaps use a def get method to render a custom context that informs/reminds the user of the criteria they are filtering/sorting by. 

- Create a view to order by return of average_score 

- Implement a random 'surprise me' feature

- decreased number of cards on index page to 3 so that background image is less obscured
- capitalise the type and colour field somewhere so that the filtering views do not miss any reviews.  Can filter() use a list?
- look into displaying the total number of comments on the search_results and user_reviews pages using a similar thing to BeerReviewSingle
- display review meta-data inline on larger screens
- base.html meta tags
- update image field label in add_review and update_review to explictly make it optional
- Remove Hops field from Review - this is not always available on bottled beers and certainly not for draught beers
- Add a request to users to upvote or downvote reviews - "this helps push good reviews up the rankings"
- look into pagination for search_results and user_reviews pages
- User_reviews does not filter out unapproved reviews
- After submitting a User Review Form, add a link to submit a new review to the success text box
- ensure all templating language is properly indented
- remove all extraneous / commented-out code
- Harmonise login, log out, signup to sign-in, sign-out and sign-up - will require changing login.html and logout.html template names. 
- Implement tests from Django-Experimentation repo
- add class and method docstrings
- Modify Reviews so that they have realistic content, not just Lorem Ipsum bulk text
- Use the checking thing to check if a user is the post's author - if so, remove/disable the upvote button, or trigger it automatically. 
    - adding an upvote automatically is difficult, since the add_review function does not allow an upvote to be assigned during the upload/save process
    - disabling the upvote/downvote buttons is relatively simple - use the checker statement employed elsewhere


Summernote editor:
- continue tweaking settings, possibly apply different settings for the comment editor. 
- remove `'disableDragAndDrop': True` and test what uploading images and videos through the editor does

Readme:
- Soundly note change to new repository thanks to summernote editor
- Testing section for exhaustive manual testing
- Note removal of AllAuth Urls, and retention of views, forms and template for future work
- Remove need for scrolling after upvote / downvote page reload - https://stackoverflow.com/questions/64456417/django-redirect-view-after-liking-without-scrolling
- Add additional classes to forms.py widgets to control input element widths
- Find and apply a favicon
- Add screenshots of all pages to Readme
- Upload wireframes to readme
- Rework documentation
- add line-breaks for clearer structure

# Future Work

Future work:
- implement upvotes / downvotes feature for Comments
- mimic an excerpt on the index cards with `{{ review.content|slice:":100" }}` to show the first 100 characters - fancy formatting in those first 100 characters could prove problematic, but test this first
- Extend User model to include a profile picture and other information - display this on the navbar and below each beer review
- Add higher-level AllAuth functionality - social media sign in, password complexity, confirmation emails, etc
- Modify UserSignUpForm in user/forms.py to include additional first_name and last_name fields - https://www.youtube.com/watch?v=d9aCpxQfnOg @ 4.57




# Bugs

When trying to deploy an initial blank version of the project to Heroku, I ran into an error, with Heroku being unable to build a wheel for backports.zoneinfo

Some Googling revealed that the problem could be to do with the version of Python that Heroku uses, and that a possible fix could be to add a runtime.txt file to the repository to specify the exact version of Python that should be used. Said file was added with `python-3.8.13`.

In the end, I noted that this was extraneous, since INSTALLED_APPS was missing a comma. Once added, Heroku was able to build and deploy the app properly


After creating a superuser to access the Django backend, I ran into a 403 error when trying to login using that superuser via the admin login page. 

Some Googling found [this StackOverflow page](https://stackoverflow.com/questions/70285834/forbidden-403-csrf-verification-failed-request-aborted-reason-given-for-fail/70326426#70326426). Though this should apply only to Django v4.x.x , where I specifically installed Django v3, as per the walkthrough videos. 

Running the command `python3 -m django --version`, obtained from [this StackOverflow page](https://stackoverflow.com/questions/6468397/how-to-check-django-version), to check the version of Django installed, I found that the project was using Django v4. The Django documentation says that Django v4.1 was released on 3/8/22, about 4 days before I tried to access the backend. I can only conclude that Django upgraded from v3 to v4.1 automatically. 

To solve the error, I found [this StackOverflow page](https://stackoverflow.com/questions/29573163/django-admin-login-suddenly-demanding-csrf-token), which provided a line of code that must be added to settings.py:

CSRF_TRUSTED_ORIGINS = ['https://*.YOUR_DOMAIN.COM'], replacing YOUR_DOMAIN.COM with the URL of the Gitpod workspace I was using, prefixed with `8000-` to account for the development server. 

This worked, and allowed me to login to the Django backend without issue. The code above appears to override the need to provide a CSRF token when performing actions from this workspace. This may present a vulnerability, as a CSRF token is Django's way of protecting sites against malicious users, and the code in settings.py overrides that. I asked my Mentor, and his response was....



When attempting to render an BeerReview database entry, I initially could not get a Bootstrap card holding the various fields to display. I thought that this may have been a problem with my views. Where the Django Blog uses a status field to mark a post as either draft or published, I am merely using an approved field, and then filtering posts to display by the boolean value in the approved field. Removing this stipulation did not work. 

I then viewed the index.html page in the Dev Tools and found that the card was not even rendering, and that the code was stopping at the Templating Language For Loop. I had been using for `beer_review in beer_review_list`. I then consulted the [Django documentation on class-based views](https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/), and found that their example code uses `for publisher in object_list`. I followed their pattern and changed `beer_review_list` to `object_list`. This worked, and the index page displayed the test beer review that I had made in the database. 

For later - `object_list` may be customised by adding `context_object_name = ` to the class in views.py, and assigning beer_reviews. i.e `context_object_name = beer_reviews`, and then using `for beer_review in beer_reviews` in the Templating Language. From [this video](https://www.youtube.com/watch?v=llbtoQTt4qw)

Some minor bugs were encountered when implementing the functionality to view a single beer review. These turned out to be syntax errors and were easily identified and rectified when Django displayed the error pages. 


11/8/22:
When adding the code to allow a user to post a comment on a beer_review_single page, I encountered a ValueError - Cannot assign "`<username>`": "Comment.author" must be a "User" instance.

The offending code was in the views.py file, and had been:
`comment_form.instance.author = request.user.username`, per the walkthrough video on adding comments

Some Googling revealed that another developer had encountered a similar issue when using Django, who asked [this question](https://groups.google.com/g/django-users/c/cKd3t7yQzFo). An answer recommended using `author=request.user` that instance, which I thought might apply to my code. I removed `.username` from the code and I was then able to submit a comment as expected. A check of the Django admin panel showed that the comments had been submitted successfully, and were awaiting approval. Once approved, only the comments' created_on fields were displaying properly. A check of the code revealed that I had been ported over the HTML code from the walkthrough project without changing the fields to reflect those of my models. Since my Comment model and the walkthrough's Comment model share a created_on field, only this was displaying initially. Once the fields had been updated, the comment displayed properly. 

Given that I was using code that is largely identical to that of the walkthrough project, I can only assume that this is an artefact of the upgrade to Django v4.1


12/8/22:
When adding a form that would allow users to post beer reviews, I encountered a 404 error where the user_review.html page could not be located, despite being present. Tutor support were eventually able to find the problem - the UserReview url path had to be above the BeerReviewSingle path, per the [URL dispatcher documentation](https://docs.djangoproject.com/en/4.1/topics/http/urls/). Once this had been implemented, the page displayed as expected. However, the form did not display. This proved easy to diagnose - in views.py I had `"user_review": UserReviewForm()` in the dictionary of the return render, whereas I was using `user_review_form` in the templating language of `user_review.html`. Changing the view code to `user_review_form` caused the form entry fields to be displayed as expected. A quick test using a beer called Surrey Nirvana from the Hogsback brewery confirmed that the form was working and had been submitted to the backend. Logging in as the superuser allowed me to approve this entry, and it was then displayed as expected. Formatting remains an issue, but this should be easily corrected. 

One issue remains - on the front-end form, per the model, there is an image field. An image can be selected using a standard image upload interface, but this does not appear to be passed into the admin backend, as the image name there defaults to the placeholder image. 

It is also worth noting that the slug is not generated until the review is accessed for approval. This could cause problems if reviews are blanket approved without accessing them - this requires testing to be fully sure. 

It should also be noted that during the Tutor support session, I was advised to downgrade to Django 3.2. As a result, the CSRF token fix mentioned above was removed, on the assumption that it would no longer be necessary. The bug and the solution have been documented should the problem arise again. 

18/8/22:
After designing and implementing the functionality to allow a user to submit a review, a bug was noted that did not allow more than one review to exist in the admin area without being reviewed. The reason is that a review's slug is generated in-situ when viewed in the admin area, and the slug is used to generate urls. The slug field in models is set to be unique, the reasoning being that urls should be unique. I reason that even an empty slug field, is considered by the admin as being valid, so therefore there cannot be more than 1 review with an empty slug field, and an empty slug field is by itself unique. 
Two solutions present themselves:
- make slug fields non-unique, allowing more than one review to exist with an empty slug review
    - this opens up potential errors with redirection to other-than-intended beer_review_single pages, should two beer reviews have the same slug
    - the odds of this are low - why would a user submit two reviews of the same beer?
    - This would also prevent mass-approval of reviews, as these reviews would have the same empty slug field
- remove the slug field, and load beer_review_single pages by primary key instead
    - each beer review has a unique primary key

Ultimately I went with the second solution, though this did require some major reworking of the project so that reviews were loaded by their primary key instead of their slug. 

18/8/22 (again):
When I decided to implement the solution to the bug above, I decided to remove the slug field from the Review Model. When migrating this change, an error occured with django summernote needing to make a migration as well. Why summernote needed to do so I cannot say, but this presented a major obstacle that i was unable to find a work-around for. Ultimately, I decided to restart the project using a fresh repository, workspace, database and Heroku app. This repository - Project Beergate - should be viewed as a continuation of the old project - [Beergate](#https://github.com/AdamBoley/Beergate). Whilst annoying, I took the opportunity to redesign parts of the project, changing some Model and field names for increased clarity and ease-of-use, and using the Django CKeditor library instead of Summernote to provide rich text fields. Commit #4, made at 14.27 on 18/8/22, added many files and changes that might normally have been added over several commits. This is because these files were merely copied over from the old project, with those changes as described above. The changes are:
- BeerReview changed to Review, and within that model:
    - created_on field changed to timestamp
    - beer_name changed to name
    - alcohol_content changed to alcohol
    - references to such changed in views and templates

Within Comment(unchanged):
- beer_review changed to review
- created_on changed to timestamp
- references to such changed in views and templates


19/8/22:
When designing the user review form that allows users to submit their own beer reviews, and implementing the backend code to handle this, I noted that the form was not uploading images that had been attached in the image field. A Django blog walkthrough video on Youtube suggested using an ImageField, and then storing images directly in the repository. Whilst I considered that this might be an acceptable work-around, I concluded that it would not for extensibility reasons. Many users uploading many images would bloat that directory. I then found [Cloudinary's documentation on image uploading](https://cloudinary.com/documentation/django_image_and_video_upload). I determined that I already had most of the pieces in place, though their code snippets pre-suppose the use of function-based views. Merely adding `{% load cloudinary %}` to the HTML file, and adding `request.FILES` to the post method of the AddReviewView view was sufficient to get this working. A database entry with name `image upload test` is testament to this - this entry's image was uploaded using the form, not via the admin backend, though I have disapproved it since the image is poorly-sized. 

19/8/22:
After implementing the functionality to update and delete posts, I was researching ways to limit only the user of a post to edit or delete it. In doing so, I came across a potential vulnerability - a logged in user may duplicate their tab and then using that second tab, navigate to the user_review, update_review and delete_review pages. If they then log out using the first tab and refresh the second tab, that second tab remains on those pages, effectively giving a logged-out user continued access to functionality that only logged in users should have. Fortunately, I already had `{% if user.is_authenticated %}` control statements in these pages, so that if a user tries the above work-around, the content will not display. It is possible that a user might do this accidentally, so I added text and links to the login page if the user is not authenticated. This is also intended to tweak-off a malicious user. 

A similar issue was noted when adding the Jinja templating language code that only allows a user to update or delete a review if they are the author of it. Determining if a user owns a review, and is therefore eligible to update or delete it was simple - I merely added `{% if user.id == review.author.id %}` control statements to the pages. To fix the vulnerability, I added this control statement to the update_review and delete_review files as well, with some text and a link back to the homepage. 

21/8/22:
When I implemented the upvote and downvote features, they were independent of each other. This allowed a user to both upvote and downvote a beer review, which is plainly non-sensical. To rectify this, I considered removing the views and urls that control upvoting and downvoting, and replacing them with a single view for both actions. I then realised that I could simply modify the existing views so that if a user's upvote is added and if a downvote by that same user exists, then the downvote is removed, and vice-versa - if a user's downvote is added and an upvote by that same user exists, then the upvote is removed. These modifications proved remarkably easy to implement - requiring a single IF conditional within the extant ELSE block. Simple testing confirmed that the modifications worked as intended - a vote was extant, clicking the button for the opposite vote removed the extant vote when the opposite vote was added.

26/8/22:
When I added the AllAuth functionality for resetting passwords and adding email addresses, testing revealed that these functions did not work, with a Django error page being generated. [This video](https://www.youtube.com/watch?v=d9aCpxQfnOg) was found. However, pending guidance on if this level of AllAuth functionality was necessary, links to these pages were removed from the navbar. 

28/8/22 - 29/8/22:
A noted bug with uploaded images was that they were neither centered nor had a uniform size. This was eventually solved by using the max-height and max-width CSS style rules. 
Further investigation on different viewport sizes proved that this had been the wrong approach - I had been fighting against Bootstap, rather than using it. I solved this by implementing a container and row arrangement within each Review card within which to place the images. This proved effective, as it centered and sized the images appropriately for all viewport sizes.

29/8/22:
Until this point, the background image for the application and the placeholder image had been served from the local repository. When DEBUG = True and running a local development server, this worked fine. However, with DEBUG = False and viewing the deployed app on Heroku, the background image and placeholder image failed to display. I noted from the Django Blog walkthrough videos that Django is designed to serve images via a CDN, not locally. At this point, I realised that Cloudinary is a CDN, and hence that I could use it to serve my background and placeholder images for the deployed app. When Debug was turned off and the app was deployed, the background and placeholder images displayed as expected. 

31/8/22 - 1/9/22:
The main background image caused problems when the app was viewed on mobile devices, with all of the first review and most of the second hidden. I determined that this was due to the main background image being applied to the `<main>` element in base.html. When changed to apply to the body element, the navbar moved. I determined that this was because the ruleset included the display: flex and align-items: center style rules which govern the layout of each page. Separating the ruleset out so that the display rules were applied to the `main` element and the background image style rules were applied to the `body` element solved this problem. I also removed the previously-applied `opaque-overlay` class selector, instead folding the style rules contained therein into the `main` selector. These changes solved the problem, allowing all of the reviews to be displayed on mobile devices with a fully-darkened background image as intended. 

3/9/22:
When I initially implemented the UpdateReviewView to enable a user to update their own Reviews on the front-end, it occurred to me that a malicious user could exploit the fact that when a review is updated, it is not automatically disapproved. In order to do so, a malicious user would need to pose as a normal user and submit a seemingly-genuine beer review that would likely be approved without issue. Then, said malicious user could simply update their review with their malicious content, and it would be unlikely that an administrator would see this in order to remove it. I ran this past both my Mentor and an experienced software developer friend of mine, and both agreed that this was a potential vulnerability. 

An initial solution involved using a post method inside the UpdateReviewView, however I noted that this actually had the effect of creating a new record with the updated content. For a time I considered that this was an acceptable solution - since the new record would be automatically disapproved, any malicious content would not be visible and could be safely removed by an administrator. However, this new record also did not have an image attached, which would require an image to be added by the administrator. If the user was replacing the image, this would have been problematic. 

I spent a long time searching for a solution, and I found several StackOverflow questions that point to the creation of a duplicate record when using the generic UpdateView being a common issue. I eventually found [this Reddit post](https://www.reddit.com/r/django/comments/8jkh5t/updateview_creates_new_items_in_the_db_instead_of/), in which the author answers their own question. The author's use-case appears to be slightly different from mine, but it is sufficiently similar that I was able to appropriate most of their code. With a few adjustments, notably adding `user_update_form.instance.approved = False` and altering the return statement to render the `update_review.html` page with the Updated flag set to True, I was able to update a record and then see the confirmation message. When I went to the index page, I noted that the record I had updated was absent. I then checked the admin panel and noted that the record had been automatically unapproved. When I accessed that record, I noted that the update I had made appeared. When I approved the record and visited the index page, the record was visible. When I clicked on the card to visit the detail page, the updated content was visible. This was immensely satisfying. Best of all, since the record is being updated, the image remains unchanged and does not default to the placeholder. 

8/9/22:
Whilst using the deployed app using the Chrome browser of my Android mobile device, I noted with some alarm that the CK-Editor rich text fields for the add_review page and the add-comment section of the review page was not displaying. Further investigation revealed that this bug extended to the deployed version on my PC as well, indicating that the problem lay with the deployed site. 

Since this problem only existed on the deployed version of the app, fixing it required many commits with debug turned off, and then redeploying on Heroku. The commit history of this project from 8/9/22 to 9/9/22 has many small commits that were tweaking various settings and code

During the attempts the fix this bug, it was noted that the CK editor does not display on the local version either - this is only an issue when Debug is off

Per [this StackOverflow question](https://stackoverflow.com/questions/71814013/djangos-ckeditor-not-appearing-in-admin-panel), I inspected the form, and noted that the actual textarea input element has visibilty: hidden. However, if visibility: hidden is unchecked in the Chrome developer tools, a standard textarea element appears, not a full rich text editor

I tried many fixes, including:
`<script>CKEDITOR.replace('editor1');</script>`

`{{ form.text | safe }}`

`{{ form.as_p | safe }}`

Halfway through this attempt at fixing the bugs I had met with no success, so I switched to using the TinyMCE rich text editor. Attempts at implementing this proved as fruitless as before.  

From the developer tools, I see that the TinyMCE editor textarea is not displaying properly because the JS file that controls it cannot be located and hence loaded. This is not a problem with Debug turned on in local development. 

When the collectstatic command is run, the static files are copied/moved to the value set in the STATICFILES_STORAGE setting in settings.py. This happens to be Cloudinary. I had thought that CLoudinary could only be used to store uploaded images, but it seems that it can serve as a repository for *any* file, and then serve them.
I solutions to this:
1 - copy the JS file code into a file in the local static folder, then set the TINYMCE_JS_URL to that location
2 - Use Cloudinary to store and serve the JS file

I note that I have run the collectstatic command several times - it probably took so long to execute because instead of locally copying/moving the files, they were being uploaded to Cloudinary. Hence, Cloudinary is storing JS files that control the SummerNote, CKeditor and TinyMCE Rich Text Editors. It is possible that 2 different RTEs could be used

Cloudinary is also storing, and presumably serving, the CSS file. This is proved by disabling STATICFILES_STORAGE - without it, the CSS file fails to load on the deployed version

Verdict 9/9/22:
Ultimately, implementing a Rich Text Editor using either the CK Editor or the TinyMCE proved too difficult to get working in production. I note that [RateBeer](https://www.ratebeer.com/) does not use an RTE. Reviews posted by users are short and simple, without fancy formatting. 

Update 11/9/22:
I remembered that the Django Blog walkthrough project uses the Django Summernote editor. Whilst I wanted for this project to move away from the walkthrough project as much as possible, so as to make it as much of my own work as possible, I note that the Summernote editor worked and was easy to implement. This proved true for this projet as well - I was able to implement it in about 2 hours of work, compared to the 2 days I had previous spent fruitlessly trying to make the CK Editor and TinyMCE editor work. That said, several commits were necessary, as the deployed app initially failed to load with an H10 error. Those commits removed remnant code written for the previously-named rich text editors and reworked the settings and forms files. 

Whilst the note about [RateBeer](https://www.ratebeer.com/) above still stands, the implementation of the Summernote editor is as much about me proving to myself that I could do it as it is about providing a good user experience. It should go without saying that I am very pleased to have done so. Credit goes to [this article](https://djangocentral.com/integrating-summernote-in-django/) and the [Django Summernote documentation](https://github.com/summernote/django-summernote)

18/9/22:
Fix spelling error bug in reviews/admin.py causing the mass comment disapprove method to not display

Whilst testing responsiveness to smaller screen sizes, I noted that the navbar nav-items became misaligned at between the LG and XXL breakpoints (992px to 1400px), before collapsing behind the burger icon at less than 992px. I changed the navbar collapse breakpoint to XXL to stop this happening. I should note however that this was only an issue when signed-in, due to the greater number of nav-item links. 

I added the 'served_as' field to the admin list_filter and list_display control variables

I also noted that the review field of the admin comments page was displaying the output of the Review model magic string method. Since the magic string method appears to be used only here, I modified the output of said method to return only the name of the review. This made the the admin comments page clearer 

I personally like to add footers containing copyright information to my projects where possible, a basic footer element was added along with accompanying CSS. 

Whilst the return render method used in the walkthrough videos is perfectly functional, I personally do not find it overly clear, especially since it is placed over multiple lines and contains a object. I have since learned that the object is called a context. I found it clearer and more pythonic to explicitly declare the context object as a value of a variable called context, and also to declare the HTML template file to be used as the value of a variable called template_name. I then called the context and template_name variables in the return render method with the request. I feel that this made the return statement clearer, since it occupied a single line.  

On smaller screen sizes, I noted that the supplementary beer review information - author, timestamp, brewery, etc - became misaligned on smaller screen sizes. I solved this by removing the float classes I had previously applied, as I considered that it would be very possible for authors, beers and breweries to have long names, and for the keywords field to have many words as well. I also reduced the pagination number to 3 so that only 3 reviews display per page. This has created a cleaner, less busy landing page. 

I noted that the user_reviews and search_results pages were quite bare, so I added the same supplementary information that had been added to the index page - type, colour, brewery, etc. I had also planned to insert quick links to the update_review and delete_review pages, so that a user could quickly update and delete these reviews from the search_results and user_reviews pages. Whilst technically possible, it disrupted my styling and element placement, presumably because each search result card rendered on those pages is contained within an anchor element. I could have removed this parent anchor element, but chose not to because it makes tapping on a mobile device much easier. 

# Development Choices

When formatting the admin panel, I decided to allow filtering by 5 categories - approved, created_on, brewery, type and author. Filtering by approved allows a superuser to see reviews that have not yet been approved. Filtering by created_on allows superusers to see what reviews have been posted in the last periods of time. Filtering by brewery and type allows superusers to see reviews of beers brewed by certain breweries and of beers of a certain type. Filtering by author allows superusers to see posts by certain users, which may allow them to find users who are particularly prolific. 

19/8/22:
To create the functionality that allows users to update posts, major changes were made to the views.py file, per [this series of django tutorials](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)

UserReview was renamed to AddReviewView, and was changed to use the CreateView generic view, which allowed me to remove the get method (currently commented out)

A new view called UpdateReviewView was created, using the generic UpdateView. Get and post methods exist in this view, but are commented out. The get method is probably unnecessary, but the post method may be necessary, but it currently creates a duplicate record. 

25/8/22:
When implementing the modal for the delete_review page, I found that when the close button was placed outside of the form that it was mis-aligned with the button to confirm the deletion. Rather than try to manual align the buttons with custom CSS that might produce unexpected results for different viewports, I solved this problem by placing the button within the form element. This does not appear to have any unintended side-effects. 

26/8/22:
When implementing the functionality to allow a user to view their own reviews, I found [this StackOverflow question](https://stackoverflow.com/questions/44693599/django-user-posts-to-be-filtered-from-all-posts-and-displayed-in-user-profile) useful, as it mentioned being able to filter the Reviews table by `author=request.user` and display the results. 

4/9/22:
During the course of this projects' development, my Mentor emphasised the importance of security and defensive programming against malicious users. As part of this, the [Django Admin Honeypot](https://django-admin-honeypot.readthedocs.io/en/latest/index.html) library was installed. This package provides a fake admin login page, the idea being that if an attacker knows that this project uses Django, they might navigate to the login page by appending `/admin` to the URL, as is convention for Django projects, and then try to break through the password defense to access the admin panel. From there, an attacker could cause terrible damage to the project. With this package installed and configured, the URL ending in `/admin` points to a decoy page whose form will not work, even if the correct credentials are supplied. The actual admin panel login page is located at the URL ending in `/beergate-admin`, where the correct superuse credentials may be supplied to access the admin panel. 

4/9/22:
To provide better security for the project, my Mentor provided several settings that could be added to the settings.py file:
`SECURE_BROWSER_XSS_FILTER = True`
`X_FRAME_OPTIONS`
`SECURE_SSL_REDIRECT`
`SECURE_HSTS_SECONDS`
`CSRF_COOKIE_SECURE`
`SESSION_COOKIE_SECURE`

Before adding these, I researched them. 
The `SECURE_BROWSER_XSS_FILTER = True` setting is deprecated per [this page](https://code.djangoproject.com/ticket/32678), so it was not added
The `X_FRAME_OPTIONS` setting already existed
The `SECURE_SSL_REDIRECT` redirects all HTTP requests to HTTPS requests. Per [this Cloudflare article](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/#:~:text=HTTPS%3A%20What%20are%20the%20differences,far%20more%20secure%20than%20HTTP.), HTTPS is a more secure request method, so adding this setting seemed like a good idea. 
The `SECURE_HSTS_SECONDS` setting initially caused some consternation, thanks to the warning that could temporarily break the project. Per the [Django documentation on this setting](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SECURE_HSTS_SECONDS), a low initial value of 60 seconds was used for testing purposes. 

The `CSRF_COOKIE_SECURE` marks the CSRF cookie as secure, so that it may only be sent over an HTTPS connection. This seems to have no downsides, so it added. 
The `SESSION_COOKIE_SECURE` setting marks session cookies as secure, so they may only be sent over an HTTPS connection. Django specifically recommends adding this setting, so I did so. 

When the `SECURE_SSL_REDIRECT` and `SECURE_HSTS_SECONDS` were added, I was unable to access the localhost development server. To resume development, I was forced to build a new workspace, install all dependencies again and reconstruct the env.py file. Hence, only the `CSRF_COOKIE_SECURE` and `SECURE_HSTS_SECONDS` settings were retained. 

5/9/22:
Styling the user_review and search_results pages proved difficult for mobile devices. I initially attempted to stack the images above the information about a beer review within each card. However, on smaller screen sizes the images became mis-aligned. After some thought, I removed the images for screen sizes of less than 576px, the smallest Bootstrap breakpoint. This has the added benefit of reducing the sizes of the cards on mobile devices, which makes scrolling through a large number of reviews easier, as such scrolling is typically done using the thumb. 

8/9/22:
My Mentor noted that the standard Bootstrap navbar design is quite muted and bland. He suggested using a bolder, more prominent design. To accomplish this, I changed the background colour to dark orange, with the intention of mimicking the colour of a pint of beer. I initially used white text to mimic the foamy head of a pint, but upon checking the colour contrast with [WebAIM](https://webaim.org/resources/contrastchecker/), I noted that white on orange provided insufficient colour contrast. To counter this, I switched to using black text with a increased font-size and font-weight. I also added a hover effect to the navbar button links to turn them white when moused over, so as to provide clear user feedback that they are about to a click a button. 

11/9/22:
The large number of commits made between 8/9/22 to 9/9/22 ultimately achieved nothing, except for some documentation regarding learning about how Django and Cloudinary work, and a minor fix to the AddReviewView that updated the name of the template being used. I considered deleting or reverting these commits but decided against this. Commit deletion is considered bad practice and commit reversion would achieve nothing, since the last commit made on 9/9/22 essentially restored the project to its last working state, except that the Review model's content field now uses a standard TextField instead of CK-editor's RichTextField or TinyMCE's HTMLField.  

## Ordering
11/9/22:
A good friend of mine, upon viewing the project, suggested implementing some sort of functionality for changing the ordering of the displayed Reviews. I considered that this could be a good idea, since by default the project orders Reviews by timestamp, with the newest appearing first. I considered that a user might want to order the Reviews by the highest number of upvotes, so that they can see particularly well written reviews. This mimics the way in which Facebook and Twitter posts are said to 'go viral', that is, when they achieve a lot of traction and are then seen by more and more users. I also considered that a user might want to order Reviews in reverse order, with the oldest displaying first. This might be because older beers that would have been reviewed when they were first created would quickly become next to invisible because they would be hidden behind so many pagination buttons. However, beers stay around for a long time, and age should not make a review any less valid. 

On the back of this, he also suggested that, as a person who does not drink beer and therefore is not particularly familiar with terminology, that the search bar would be of less use to him. Therefore, I added options to the dropdown menu that allow the user to broadly sort Reviews by beer type and colour. At time of writing I have implemented 7 sorting options - 3 for types and 4 for colours. The type sorting is for ales, stouts and lagers, and the colour sorting is for pale, golden, amber and dark beers. It is relatively simple to add additional sorting parameters. 

My friend also suggested modifying the data model so that a user can mark a beer as either a draught or bottled beer, since beers served in either form can vary considerably. 

11/9/22:
The AllAuth functions of password reset, password set and add email were not implemented because these require an email server. The password change function was kept. No links to the removed functions remain in the project, but the URLs were removed from user/urls.py as a precaution. The views and forms remain as a springboard for future work. For future reference, the removed URLs are:
`path('account/password/reset/', UserPasswordResetView.as_view(), name='account_reset_password'),`
`path('account/password/set/', UserPasswordSetView.as_view(), name='account_set_password'),`
`path('account/email/', UserAddEmailView.as_view(), name='account_email'),`
The necessary imports are:
`UserAddEmailView, UserPasswordSetView, UserPasswordResetView, UserPasswordResetFromKeyView`

12/9/22:
After successfully implememting the Summernote editor for the add_review form, I noted that it had a fixed size of 720px. This caused the editor to overflow horizontally when viewed on a device with a screen size of less than 720px. I tried various options before I turned to [the documentation](https://github.com/summernote/django-summernote) and the [Summernote website](https://summernote.org/deep-dive/#disable-drag-and-drop), where I thankfully noted that the Summernote editor could be extensively customised in the settings file by way of the SUMMERNOTE_CONFIG variable. Simply setting the width to be 100% was sufficient to make the editor responsive to screen size. At this point I noted that the editor ships as standard with many options. I decided to cut these down considerably because a large number of options causes the toolbar to become absurdly large in proportion to the editor field when viewed on smaller screen sizes, and limiting the number of options removes this. I also decided to remove the ability to upload pictures and videos, as I was concerned about how Cloudinary would handle these when I already had a CloudinaryField in the Review Model. If a user tries to upload an image or video, a new tab with it will open instead. To avoid damaging the user experience, the label for the editor has been modified to inform users of this. 

## Favicon

I decided to apply a pair of beer glasses as this app's favicon. Beer is the main theme of the app so this favicon seemed appropriate. The favicon was generated using the Clinking Beer Mugs emoji from the [Favicon.io](https://favicon.io/emoji-favicons/) favicon generator. 
 
# Local Clone / How you can use this code

BeerGate uses a large number of packages to enable all of its functionality. These are listed in the `requirements.txt` file, and hence can be installed with the terminal command:
`pip3 install -r requirements.txt`

You will also need a Cloudinary account to store and serve images and static files, and a Heroku account to host the app and provide the database. 

If developing a clone of BeerGate locally, you will need an `env.py` file to contain the local environment variables. These would be the CLOUDINARY_URL, SECRET_KEY, and DATABASE_URL. The CLOUDINARY_URL can be obtained from your Cloudinary account, whilst the DATABASE_URL is provided by Heroku when a postgres database is attached to the Heroku app. The SECRET_KEY is a password of your own making. These will need to be added to your Heroku app Config Vars in the settings tab. 

# Testing

## Manual User Story testing

### Admin user User Story testing

### Generic user User Story testing

### Unregistered user User Story testing

### Registered user User Story testing

## Other manual testing

What happens when a login attempt is made via the dummy admin sign-in page?

Are these attempts viewable in the real admin panel?

What happens when the tab duplication trick is used?

## Validation testing

### HTML Validation

#### Base template

#### Index template

#### Review template

#### Search Results template

#### User Reviews template

#### Add Review template

#### Update Review template

#### Delete Review template

#### Account Sign-in template

#### Account Sign-out template

#### Account Sign-up template

#### Account Password Change template

### CSS Validation

All custom styling is contained within static/css/styles.css

### JS Validation

There is no custom JS, though a JS file exists for future work. It is contained with static/js/script.js

### Python Validation

BeerGate's python files are contained within 3 directories - beergate, reviews and user

PEP8 Validator

#### Beergate settings.py

#### Beergate urls.py

#### Reviews admin.py

#### Reviews forms.py

#### Reviews models.py

#### Reviews urls.py

#### Reviews views.py

#### User forms.py

#### User views.py

#### User urls.py

## Automated testing

PyTest

# Technologies

Slack
<br>
Django
<br>
AllAuth
<br>
Github
<br>
Gitpod
<br>
Heroku
<br>
Cloudinary
<br>
CK Editor and TinyMCE were used initially, but then rejected
<br>
Django Summernote editor

# Other notes

Partway through the development of BeerGate, Heroku announced that it was suspended its free tier of Postgres database hosting at the end of November. Per instructions from Student Care (screenshot of email?), I continued to host BeerGate on Heroku. 

# Credits

In contrast to my previous projects, where I was able to write most of the code myself, Beergate owes its a lot of its development to many external articles, guides, tutorials and so on. Making sense of these was often difficult, as was applying the code and solutions they offered. 

Whilst I was not able to save every resource used, I credit the following people and resources for assisting BeerGate's development:

Firstly, the Code Institute Django Blog walkthrough project proved invaluable in the first stages of development, particularly with the deployment to Heroku and the use of Cloudinary. 

Gemma from Code Institute Tutor support, for helping to fix the issue with being unable to access the user_review.html page. This was the first major feature beyond the walkthrough project that I wanted to add, and her help in getting it working was a major boost to my confidence in my abilities.

Gemma also tried to fix the issue with the CK Editor and TinyMCE Rich Text Editors. Though unsuccessful, the tutoring process allowed me to realise that I was wasting time trying to get these working. From there, I used the django-summernote editor, which was implemented almost seemlessly and allowed development to continue. 

The [official Django documentation](https://docs.djangoproject.com/en/3.2/) proved very helpful generally, particularly the [model field reference page](https://docs.djangoproject.com/en/3.2/ref/models/fields/) for guidance on designing my models and field types. 

The [official Django AllAuth documentation](https://django-allauth.readthedocs.io/en/latest/index.html) was helpful in the implementation of the AllAuth templates, forms and views. AllAuth itself is clearly very powerful. 

The [Cloudinary documentation on image uploading](https://cloudinary.com/documentation/django_image_and_video_upload) proved helpful in writing the code to allow users to upload images when submitting beer review. 

[StackOverflow](https://stackoverflow.com/) proved very helpful generally. Given Django's widespread use and maturity, I was almost always able to find a question or an answer that matched my own issues. 

In particular, I credit the following question pages:
- [This question](https://stackoverflow.com/questions/21938028/how-can-i-get-a-favicon-to-show-up-in-my-django-app) helped apply BeerGate's favicon
- []() 
- []()


The [Codemy YouTube channel's Django walkthrough playlist](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) proved very useful, in particular for introducing the CreateView, UpdateView and DeleteView generic views.  

This [Medium article](https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56) provided invaluable guidance on how to apply widgets to AllAuth templates.Without this, the forms in BeerGate's AllAuth templates would look jarringly different to other forms. 

The idea of darkening off the main background image is not original and was taken from [bootstrap-experimentation](https://github.com/AdamBoley/bootstrap-experimentation), the repository set up to code along with the Code Institute Building With Bootstap videos. A different method had to be used to implement this, but the walkthrough videos gave the idea.

A custom scrollbar was applied with [this W3Schools page](https://www.w3schools.com/howto/howto_css_custom_scrollbar.asp) 

[Favicon.io](https://favicon.io/) was used to generate a favicon

[This Reddit post](https://www.reddit.com/r/django/comments/8jkh5t/updateview_creates_new_items_in_the_db_instead_of/), specifically the answer the questioner themselves added, provided the basis for providing the basis of the solution to automatically disapproving updated reviews

The official [django-summernote](https://github.com/summernote/django-summernote) documentation and [this article](https://djangocentral.com/integrating-summernote-in-django/) were collectively invaluable in implementing the summernote editor to both the admin panel and front-end form. Django Summernote itself should be credited for its ease of use and clarity of documentation. After the trials and travails encountered when working with the CK Editor and TinyMCE editors, this was very welcome. 

[This Summernote website page](https://summernote.org/deep-dive/#custom-toolbar-popover) was useful for customising the options available to the Summernote editors. 

[This article](https://learndjango.com/tutorials/django-search-tutorial) by noted Django export Will Vincent provided invaluable guidance on implementing a working search bar. 

Surprise me feature:
    - http://web.archive.org/web/20110802060451/http://bolddream.com/2010/01/22/getting-a-random-row-from-a-relational-database/
    - https://stackoverflow.com/questions/962619/how-to-pull-a-random-record-using-djangos-orm

