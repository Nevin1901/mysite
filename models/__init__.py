class Repository:
    def __init__(self, title, description, language, url, stars, imagePath):
        self.title = title
        self.description = description
        self.language = language
        self.url = url
        self.stars = stars
        self.imagePath = imagePath

class Image:
    def __init__(self, imageUrl, imageDescription):
        self.imageUrl = imageUrl
        self.imageDescription = imageDescription
