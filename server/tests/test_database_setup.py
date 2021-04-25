import datetime

from django.core.files import File

from trends.db.admin import usermgmt
from trends import view_handlers
from trends.db.article import Article


# confirmation = input("This will delete all database entries and reset it to the default test database. Are you sure? "
#                      "(Y/N)")
# if confirmation.lower() != "y":
#     exit(0)

# Article.objects.all().delete()
#
# with open('./article_html/1.html', 'w') as f:
#     file = File(f)
#     file.write("<h1>Test article header</h1>")
#
# view_handlers.handle_article_new("Test Article Title",
#                                  "John Smith",
#                                  "Test Article",
#                                  "./article_html/1.html",
#                                  "2019-09-29",
#                                  20,
#                                  "",
#                                  ["Test", "Tag1"])
#
#
# with open('./article_html/2.html', 'w') as f:
#     file = File(f)
#     file.write("<p>poyo</p>")
#
# view_handlers.handle_article_new("Another Test Article Title",
#                                  "Kirb",
#                                  "Another Test Article",
#                                  "./article_html/2.html",
#                                  "2019-09-22",
#                                  10,
#                                  "",
#                                  ["Test", "Tag2"])
#
# with open('./article_html/3.html', 'w') as f:
#     file = File(f)
#     file.write('<a href="google.com">Google link</h1>')
#
# view_handlers.handle_article_new("Skynet",
#                                  "Skynet",
#                                  "This test was written by an AI",
#                                  "./article_html/3.html",
#                                  "1997-08-04",
#                                  9999,
#                                  "",
#                                  ["Test2", "Tag2"])
#
# usermgmt.create_user("Fek", "usyd", "Top", "Fek", "smh@email.com")
