import mysql.connector
from db.obj.article import Article, ArticleAbstract


class TrendsDB:

    @staticmethod
    def __get_database():
        database = mysql.connector.connect(
            host="localhost",
            user="admin",
            passwd="pass",
            database="trends_database"
        )
        return database

    def get_article(self, article_id):
        if not isinstance(article_id, int):
            raise TypeError("Invalid article ID.")

        database = self.__get_database()
        cursor = database.cursor()
        cursor.execute()

        cursor.execute('SELECT title, author, body, date, time_to_read FROM articles WHERE id=%d', article_id)
        article_data = cursor.fetchone()

        cursor.close()
        database.close()

        if article_data is None:
            raise FileNotFoundError("Article not found.")
        else:
            article_obj = Article(article_id, article_data)
            return article_obj

    def get_article_abstract(self, article_id):
        if not isinstance(article_id, int):
            raise TypeError("Invalid article ID.")

        database = self.__get_database()
        cursor = database.cursor()
        cursor.execute()

        cursor.execute('SELECT title, abstract, time_to_read FROM articles WHERE id=%d', article_id)
        article_data = cursor.fetchone()

        cursor.close()
        database.close()

        if article_data is None:
            raise FileNotFoundError("Article not found.")
        else:
            article_abstract_obj = ArticleAbstract(article_id, article_data)
            return article_abstract_obj
