"""
    Created by cala at 2019-10-29
"""

# ViewModel
# 裁剪 修饰 合并

class BookViewModel:
    def __init__(self, book):
        # cut book data from app.spider model
        self.title = book['title']
        self.author = ','.join(book['author'])
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.pages = book['pages']

class BookCollection:
    def __init__(self):
        # books: cut data list
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, panda_book, keyword):
        self.total = panda_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in panda_book.books]

class _BookViewModel:
    # consider that app.spider model returns single book or a list of books
    # app.view_models returns a dictionary with the view of single one or collection as a list
    @classmethod
    def package_single(cls, data, keyword):
        rst = {
            'books':[],
            'total':0,
            'keyword':''
        }
        if data:
            rst['total'] = 1
            rst['books'] = [cls.__cut_book_data(data)]
        return rst


    @classmethod
    def package_collection(cls, data, keyword):
        rst = {
            'books':[],
            'total':0,
            'keyword':''
        }
        if data:
            rst['total'] = data['total']
            rst['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return rst


    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'author': ','.join(data['author']),
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }

        return book


