import datetime

from django.core.files import File

from trends.db.admin import article_admin
from trends.db.article import Article


confirmation = input("This will delete all database entries and reset it to the default test database. Are you sure? "
                     "(Y/N)")
if confirmation.lower() != "y":
    exit(0)

Article.objects.all().delete()

with open('./article_html/1.html', 'w') as f:
    file = File(f)
    file.write("<h1>Test article header</h1>")

article_admin.create_article("Test Article Title",
                             "John Smith",
                             "Test Article",
                             "./article_html/1.html",
                             datetime.datetime.strptime("2019-09-29", "%Y-%m-%d").date(),
                             20,
                             "")

with open('./article_html/2.html', 'w') as f:
    file = File(f)
    file.write("<p>poyo</p>")

article_admin.create_article("Another Test Article Title",
                             "Kirb",
                             "Another Test Article",
                             "./article_html/2.html",
                             datetime.datetime.strptime("2019-09-22", "%Y-%m-%d").date(),
                             10,
                             "https://upload.wikimedia.org/wikipedia/en/5/5c/Kirby.png")

with open('./article_html/3.html', 'w') as f:
    file = File(f)
    file.write('<a href="google.com">Google link</h1>')

article_admin.create_article("Skynet",
                             "Skynet",
                             "This test was written by an AI",
                             "./article_html/3.html",
                             datetime.datetime.strptime("1997-08-04", "%Y-%m-%d").date(),
                             9999,
                             "https://upload.wikimedia.org/wikipedia/en/b/b9/Terminator-2-judgement-day.jpg")
