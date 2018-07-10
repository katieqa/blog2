from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit.'

blogs = dict() #mapping blog_name to blog object

def menu():
    # show the user the available blogs
    # let the user make a choice
    # show the blog
    # exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def ask_create_blog():
    #ask new blog title and new name
    title = input('Please enter a title for the new blog: ')
    author = input('Please enter your name: ')

    blogs[title] = Blog(title, author)
    """
    if(title not in blogs):
        blogs[title] = Blog(title, author)
    else:
        print("Unable to create blog. Blog of that name already exists")
"""

def ask_read_blog():
    #ask for a blog title, print the posts
    blogtitle = input('Please enter the blog title that you wish to read: ')

    if(blogtitle in blogs):
        #blogs[blogtitle].
        print("Need a post reading method??")
    else:
       print("Unable to locate a blog by that name.")

def ask_create_post():
    #ask for blog title
    blogtitle = input('Please enter the blog title that you wish to post to: ')
    if(blogtitle in blogs):
        #ask for post title
        posttitle = input('Please enter the title for the new post: ')
        #ask for post content
        postcontent = input('Please enter the content for the new post: ')
        #create post and add to blog
        blogs[blogtitle].create_post(posttitle, postcontent)
    else:
        print("Unable to locate a blog by that name.")

    pass


def print_blogs():
    #print the available blogs

    print("Available Blogs:")
    for key, blog in blogs.items(): #provides tuples of keys and values ie [(blog_name, Blog), (blog_name, Blog)]
        print('- {}'.format(blog))

