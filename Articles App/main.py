from flask import Flask, jsonify, request
from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import output
from content_based_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-article")
def get_movie():
    article_data = {
        "title": all_articles[12],
        "url": all_articles[11],
        "timestamp": all_articles[1] or "N/A",
        "id":all_articles[0],
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_movie():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not-liked-article", methods=["POST"])
def not_liked_movie():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-articles")
def popular_movies():
    articles_data = []
    for movie in output:
        _d = {
            "title": all_articles[12],
            "url": all_articles[11],
            "timestamp": all_articles[1] or "N/A",
            "id":all_articles[0],
        }
        articles_data.append(_d)
    return jsonify({
        "data": articles_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_articles in liked_articles:
        output = get_recommendations(liked_articles[12])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    articles_data = []
    for recommended in all_recommended:
        _d = {
            "title": all_articles[12],
            "url": all_articles[11],
            "timestamp": all_articles[1] or "N/A",
            "id":all_articles[0],
        }
        articles_data.append(_d)
    return jsonify({
        "data": articles_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()