import requests

class imageDownloader():
    def downladImageUrl(self, filename : str, url : str):
        data = requests.get(url)
        status_code = data.status_code
        content = data.content
        
        if status_code == 200:
            f = open(filename,'wb')
            f.write(content)
            f.close()
        else:
            print("An api call error occured! Error:", status_code)
        
