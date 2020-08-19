## YTS/Yify-Torrent-API
- A Python Program Integrated With Flask To Provide An API Of Various Movies Along With Their _Synopsis_ And _Magnet Link_ From [**YTS/Yify Movies**](https://yts.mx)
- The _Raw Python Program_ Can Be Found Out At [**YTS/Yify Torrent Scrapper**](https://github.com/RGProjectX/yts-torrent-scrapper)

#### Key Features :
> The Script Use's Direct Source Of [**YTS/Yify Movies.**](https://yts.mx)

> The Performance Has Been Improved Drastically As Compared To [**YTS/Yify Torrent Scrapper.**](https://github.com/RGProjectX/yts-torrent-scrapper)

> The Flask Endpoints Returns ***JSON*** Based On IMDb Ratings Which Can Be Used For Any Projects.

#### Usage :

- The Flask Endpoint Accepts A Query In The Format `http://127.0.0.1:5000/yts?q={query}`

- The URL `http://127.0.0.1/yts/?q=Mission:%20Impossible` Returns A JSON
```
{
  "data": [
    {
      "cast": [
        [
          "Tom Cruise", 
          "https://www.imdb.com/name/nm0000129/"
        ], 
        [
          "Emilio Estevez", 
          "https://www.imdb.com/name/nm0000389/"
        ], 
        [
          "Jon Voight", 
          "https://www.imdb.com/name/nm0000685/"
        ], 
        [
          "Jean Reno", 
          "https://www.imdb.com/name/nm0000606/"
        ]
      ], 
      "categories": [
        "Action", 
        "Adventure", 
        "Thriller"
      ], 
      "director": [
        "Brian De Palma", 
        "https://www.imdb.com/name/nm0000361/"
      ], 
      "image": {
        "large": "https://img.yts.mx/assets/images/movies/Mission_Impossible_1996/medium-cover.jpg", 
        "small": "https://yts.mx/assets/images/movies/Mission_Impossible_1996/small-cover.jpg"
      }, 
      "imdbLink": "https://www.imdb.com/title/tt0117060/", 
      "imdbRating": "7.1/10", 
      "link": "https://yts.mx/movies/mission-impossible-1996", 
      "qualities": [
        [
          "720p.BluRay", 
          "647.80 MB", 
          "magnet:?xt=urn:btih:6AFA38D91051E01E150C85BB63C5C6833285D523&dn=Mission%3A+Impossible+%281996%29+%5B720p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337"
        ], 
        [
          "1080p.BluRay", 
          "1.68 GB", 
          "magnet:?xt=urn:btih:31E67A2201BC9644AD1299209A0D12BC6277E4B7&dn=Mission%3A+Impossible+%281996%29+%5B1080p%5D+%5BYTS.MX%5D&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fp4p.arenabg.ch%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337"
        ]
      ], 
      "related_movies": [
        [
          "Mission: Impossible - Ghost Protocol (2011)", 
          "https://yts.mx/movies/mission-impossible-ghost-protocol-2011"
        ], 
        [
          "Mission: Impossible II (2000)", 
          "https://yts.mx/movies/mission-impossible-ii-2000"
        ], 
        [
          "Mission: Impossible III (2006)", 
          "https://yts.mx/movies/mission-impossible-iii-2006"
        ], 
        [
          "Mission: Impossible - Rogue Nation (2015)", 
          "https://yts.mx/movies/mission-impossible-rogue-nation-2015"
        ]
      ], 
      "subtitles": "https://yifysubtitles.org/movie-imdb/tt0117060/", 
      "synopsis": "Based on the hit television series. Jim Phelps (Jon Voight) was sent to Prague for a mission to prevent the theft of classified material. His wife Claire (Emmanuelle B\u00e9art) and his trusted partner Ethan Hunt (Tom Cruise) were members of Phelps' team. Unfortunately, something went horribly wrong and the mission failed, leaving Ethan Hunt the seemingly lone survivor. After he reported the failed mission, Kittridge (Henry Czerny), the head of the agency, suspects Ethan of being the culprit for the failed mission. Now, Ethan uses unorthodox methods (which includes the aid of an arms dealer going by the name \"Max\" (Vanessa Redgrave)) to try to find who set him up and to clear his name.", 
      "title": "Mission: Impossible", 
      "trailer": "https://www.youtube.com/watch?v=vadCbBuUM0E", 
      "year": "1996"
    }
  ]
}
