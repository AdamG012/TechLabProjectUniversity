class Article:
    def __init__(self, article_id=None, data=None):
        self.id = None
        self.title = None
        self.author = None
        self.body = None
        self.date = None
        self.time_to_read = None

        if article_id is not None and data is not None:
            self.id = article_id
            self.title = data[0]
            self.author = data[1]
            self.body = data[2]
            self.date = data[3]
            self.time_to_read = data[4]


class ArticleAbstract:
    def __init__(self, article_id=None, data=None):
        self.id = None
        self.title = None
        self.abstract = None
        self.time_to_read = None

        if article_id is not None and data is not None:
            self.id = article_id
            self.title = data[0]
            self.abstract = data[1]
            self.time_to_read = data[2]