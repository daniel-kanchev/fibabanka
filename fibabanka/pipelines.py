from itemadapter import ItemAdapter
import sqlite3


class DatabasePipeline:
    # Database setup
    conn = sqlite3.connect('fibabanka.db')
    c = conn.cursor()

    def open_spider(self, spider):
        self.c.execute(""" CREATE TABLE IF NOT EXISTS articles 
        (title text, content text, year number) """)

    def process_item(self, item, spider):
        self.c.execute("""SELECT * FROM articles WHERE title = ? AND year = ?""",
                       (item.get('title'), item.get('year')))
        duplicate = self.c.fetchall()
        if len(duplicate):
            return item
        print(f"New entry added")

        # Insert values
        self.c.execute("INSERT INTO articles (title, content, year)"
                       " VALUES (?,?,?)", (item.get('title'), item.get('content'), item.get('year')))
        self.conn.commit()  # commit after every entry

        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
