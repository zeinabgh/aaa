import sqlite3

class ScraperDB():
    def __init__(self):
        self.connection = sqlite3.connect('scraper-db.db')
    def insertNew(self, contains):
        try:
            self.connection.execute(
            '''INSERT INTO news (title, link, description, body) VALUES (:n_title, :n_link, :n_desc, :n_body)''',
                {"n_title" : contains[0], "n_link" : str(contains[1]), "n_desc": str(contains[2]), "n_body" : str(contains[3])})
            self.connection.commit()
            return "Done"
        except:
            return "This new is stored before"
