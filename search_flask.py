from flask import Flask, render_template, request

app = Flask(__name__)

resources = [
    {"title": "Beach 1",
        "magnet": "magnet:?xt=urn:btih:BRKLS2KMCZV7CLEMFUCRR33IZWL6OGWJ&dn=140111%20(720p).mp4&xl=7729699&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce"},
    {"title": "Beach 2",
        "magnet": "magnet:?xt=urn:btih:VO4DCE7RA2K76SSECYEXP5LBQFVJ2RI6&dn=158349%20(720p).mp4&xl=5896469&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce"},
    {"title": "Beach 3",
        "magnet": "magnet:?xt=urn:btih:T354K4R5AC5PUYG6M4X7FVTVRAW24EXW&dn=ocean_-_65560%20(540p).mp4&xl=4012553&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce"},
]


@app.route('/')
def index():
    return render_template('temp.html')


@app.route('/search/', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    matching_resources = []

    if keyword:
        matching_resources = [
            res for res in resources if keyword.lower() in res['title'].lower()]

    return render_template('search.html', keyword=keyword, resources=matching_resources)


if __name__ == '__main__':
    app.run()
