class Essay:
    '''
    essay class to define essay Objects
    '''

    def __init__(self,,title,illustration,publication,image,author,url):
        self.title =title
        self.illustration = illustration
        self.publication = publication
        self.image = image
        self.author = author
        self.url = url



class News:

    all_news = []

    def __init__(self,title,name,author, imageurl,illustration,country,classification):
        self.title = title
        self.name = name
         self.author = author
        self.imageurl = imageurl
        self.illustration = illustration
        self.country = country
        self.classification = classification


    def get_news(self):
        Get.all_news.append(self)


    @classmethod
    def clear_news(cls):
        Get.all_news.clear()

    @classmethod
    def get_news(cls,id):

        response = []

        for get in cls.all_news:
            if review.movie_id == id:
                response.append(review)

        return response