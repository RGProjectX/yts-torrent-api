'''
Script Developed By : RGProjectX
Github : https://github.com/RGProjectX/yts-torrent-scrapper
Telegram : https://telegram.dog/RGProjectX
ATTENTION : This Script Is Only For Educational Purpose. 
            I'm Not Responsible For Your Downloads Of Illegal Contents.
            Please Abide By The Laws Of Your Country.
'''
import requests
from bs4 import BeautifulSoup
from flask import Flask , request , jsonify , redirect


app = Flask(__name__)

@app.route('/')
def home():
		return redirect("https://github.com/RGProjectX")


def get_page(url):
		return BeautifulSoup(requests.get(url).text, 'html.parser')

@app.route('/yts/')
def search_yts():
	query = request.args.get('q')
	results = []
	url = f'https://yts.mx/ajax/search?query={query}'
	response = requests.get(url).json()
	try:
		for movie in response['data']:
			try:
				html = get_page(movie['url'])
				soup = html.find_all('a', class_='avatar-thumb')
				crew = [[x.img['alt'].replace('Picture', '').strip(), x['href']] for x in soup]
				entry = \
				{
					"title": movie['title'],
					"year": movie['year'],
					"director": crew.pop(0),
					"cast": crew,
					"subtitles": 'https://yifysubtitles.org/movie-imdb/' + html.find('a', title='IMDb Rating')['href'].split('title/')[-1],
					"related_movies": [[x['title'], x['href']] for x in html.find('div', id='movie-related').find_all('a')],
					"synopsis": html.select('#synopsis > p.hidden-sm.hidden-md.hidden-lg')[0].text.strip(),
					"categories": [x.strip() for x in html.select("#movie-info > div.hidden-xs > h2:nth-child(3)")[0].text.split('/')],
					"link": movie['url'],
					'imdb': html.find('a', title='IMDb Rating')['href'],
					"trailer": ["N/A" if "https://www.youtube.com/watch?v=" + html.find('a', id='playTrailer')['href'].split('?')[0].split('/')[-1].strip() == "https://www.youtube.com/watch?v=" else "https://www.youtube.com/watch?v=" + html.find('a', id='playTrailer')['href'].split('?')[0].split('/')[-1].strip()][0],
					"rating": html.find('span', itemprop='ratingValue').text + '/10',
					"image": {
						"thumbnail": movie['img'],
						"poster": html.find('img', class_='img-responsive')['src']
					},
					"qualities":
					[[x.find('span').text + '.' + x.find('p', class_='quality-size').text, 
					x.find('p', class_='quality-size').find_next('p', class_='quality-size').text,
					x.find('a', class_="magnet-download download-torrent magnet")['href']] 
					for x in html.find_all('div', class_='modal-torrent')]
				}
				results.append(entry)
			except:
				continue


	except:
		results = {'status': "Error Loading API",'possible_error':{'web_block':'Website Has Been Blocked','name_error':'Please Check Movie Name'}}
		results = sorted(results, key=lambda entry: entry['rating'],reverse=True)
	dictionary = {"data" : crew}

	return dictionary
	
if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000, use_reloader=True, threaded=True)
