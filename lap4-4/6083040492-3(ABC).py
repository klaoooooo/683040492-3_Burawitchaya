# Your code here
from abc import ABC,abstractclassmethod

class DigitalProduct(ABC):
  product_counter = 1000

  def __init__(self, title, price):
    self.title = title
    self.price = price
    DigitalProduct.product_counter += 1
    self.id = DigitalProduct.product_counter 
    

  @abstractclassmethod
  def cal_download_size(self):
    pass
  
  def gen_download_link(self):
    return f"domain.com/download/{self.id}"

  @abstractclassmethod
  def delivery_time(self):
    pass


class Ebook(DigitalProduct):
  def __init__(self, title, price, page, format):
      super().__init__(title, price)
      self.page = page
      self.format = format

  def cal_download_size(self):
      return self.page * 0.1
    
  def delivery_time(self):
      return 1 + (self.page / 100)
  
  def info(self):
    print(f"Title: {self.title}")
    print(f"Price: {self.price}")
    print(f"Page: {self.page}")
    print(f"Format: {self.format}")
    print(f"Download Size: {self.cal_download_size()} MB")
    print(f"Delivery Time: {self.delivery_time()} minute")
    print(f"Download Link: {self.gen_download_link()}")

class VideoGame(DigitalProduct):
   def __init__(self, title, price, genre,required_storage_space):
       super().__init__(title, price)
       self.genre = genre
       self.required_storage_space = required_storage_space

   def cal_download_size(self):
        return self.required_storage_space

   def delivery_time(self):
        return 5 + (2 * self.required_storage_space)

   def info(self):
    print(f"Title: {self.title}")
    print(f"Price: {self.price}")
    print(f"Genre: {self.genre}")
    print(f"Download Size: {self.cal_download_size()} GB")
    print(f"Delivery Time: {self.delivery_time()} minute")
    print(f"Download Link: {self.gen_download_link()}")


ebook1 = Ebook("kl", 500, 100, "PDF") 
ebook1.info()

print()
video1 = VideoGame("kkk", 1000, "moba", 300)
video1.info()