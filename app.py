import os
import requests
import pymongo
import logging
from bs4 import BeautifulSoup as bs
from flask import Flask, render_template, request
logging.basicConfig(filename='image_scrapper_log', level=logging.INFO)
app = Flask(__name__)
@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/review', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            
            query = request.form['content'].replace(' ', '')
            save_dir='images/'
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)

            headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/140.0.0.0 Safari/537.36"
    }
            response=requests.get(f'https://www.google.com/search?q={query}&sca_esv=efcd8d53741a0bb1&rlz=1C1ONGR_enIN1095IN1095&udm=2&biw=1163&bih=501&sxsrf=AE3TifNVuRlxT3EnXc3gul_xaNGwSrKuzA%3A1759634639245&ei=z-ThaJXQDo6bseMPl4GfoQc&ved=0ahUKEwjV8-zsjYyQAxWOTWwGHZfAJ3QQ4dUDCBE&uact=5&oq=mimit&gs_lp=Egtnd3Mtd2l6LWltZyIFbWltaXQyBxAjGCcYyQIyBRAAGIAEMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgoQABiABBhDGIoFMgUQABiABDIFEAAYgAQyBxAAGIAEGAoyBRAAGIAEMgUQABiABEiUMlCmGVi6K3ABeACQAQCYAbkDoAG3C6oBCTAuNS4xLjAuMbgBA8gBAPgBAZgCBaAC2gWYAwCIBgGSBwUxLjMuMaAHuC6yBwUwLjMuMbgHzAXCBwUyLTMuMsgHJg&sclient=gws-wiz-img')
            soup=bs(response.content,'html.parser')
            images=soup.find_all('img')
            del images[0]

            img_data = []
            for i in images:
                url=i['src']
                data=requests.get(url).content
                with open(os.path.join(save_dir,f'{query}_{images.index(i)}.jpg'),'wb') as f:
                    f.write(data)
                img_data.append({'Index': images.index(i), 'Image':data})
                    
           

            
            return "Images saved successfully"
                    

        except Exception as e:
            logging.exception("Error occurred")
            return f"Something went wrong: {e}"
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')