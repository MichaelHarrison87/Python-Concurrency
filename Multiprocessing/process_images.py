import concurrent.futures
import time
from PIL import Image, ImageFilter

images = ['photo-1493976040374-85c8e12f0c0e.jpg',
             'photo-1504198453319-5ce911bafcde.jpg',
             'photo-1507143550189-fed454f93097.jpg']

t0 = time.perf_counter()


size = (1200, 1200)

def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed')
    
with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, images)
    
print(f'Finished in {time.perf_counter() - t0} seconds')