from models import Repository, Image
from flask import Flask, render_template, url_for
import random
import requests
import json

allImages = [
  "2016 base on 9b9t.png",
  "5 year coin csgo.jpg",
  "another pic of nevin.cc.png",
  "beating the end dragon on nevin.cc.png",
  "constantiam house.png",
  "coolbase.png",
  "cool farm on 9b9t.png",
  "franeks old base.png",
  "gta 4 1.jpg",
  "gta 4 2.jpg",
  "gta 5 beach 2.jpg",
  "gta 5 beach 3.jpg",
  "gta 5 beach.jpg",
  "gta beach overlooking the city.jpg",
  "gta bridge.jpg",
  "gta city 2.jpg",
  "gta city 3.jpg",
  "gta city 4.jpg",
  "gta city 5.jpg",
  "gta city 6.jpg",
  "gta city 7.jpg",
  "gta city dusk.jpg",
  "gta city evening.jpg",
  "gta city from car.jpg",
  "gta city.jpg",
  "gta diner.jpg",
  "gta from yacht.jpg",
  "gta hotel.jpg",
  "gta lake.jpg",
  "gta naturalvision.jpg",
  "gta vice city cars in alley.jpg",
  "hq steam screenshot.jpg",
  "nevin.cc enderman farm.png",
  "nevin.cc enderman got into chicken farm.png",
  "nevin.cc hole in the ground 2.png",
  "nevin.cc hole in the ground.png",
  "nevin.cc inventory.png",
  "nevin.cc mob grinder.png",
  "nevin.cc playerlist.png",
  "nevin.cc secret mob grinder.png",
  "nevin.cc topdown view.png",
  "nevin.cc view from my apartment.png",
  "new nevin.cc hole in the ground.png",
  "OG riggedcoinflip minecraft account.png",
  "old nevin.cc server.png",
  "perhaps boat.jpg",
  "rich in gmod darkrp.jpg",
  "world border on 9b9t queue map.png",]

app = Flask(__name__)

if (__name__) == "__main__":
    app.run(host='0.0.0.0')

@app.route("/")
def index():
    randomImage = random.choice(allImages)
    return render_template("index.html", imageDescription=randomImage[:-4], imageSrc=url_for('static', filename="images/" + randomImage), previewImage=url_for("static", filename="images/" + "preview-" + randomImage), title="Index")

@app.route("/repositories")
def repositories():
    request = requests.get("https://repositories.nevin.cc")
    repositories = json.loads(request.text)
    totalRepositories = []
    randomImage = random.choice(allImages)
    for repository in repositories:
        totalRepositories.append(Repository(repository["name"], repository["description"], repository["language"], repository["html_url"], repository["stargazers_count"], ("https://raw.githubusercontent.com/Nevin1901/" + repository["name"] + "/" + repository["default_branch"] + "/images/1.png")))
    return render_template("repositories.html", repositories=totalRepositories, imageDescription=randomImage[:-4], imageSrc=url_for('static', filename="images/" + randomImage), previewImage=url_for("static", filename="images/" + "preview-" + randomImage), title="Repositories" )

@app.route("/images")
def images():
    allImageUrls = []
    randomImage = random.choice(allImages)
    for image in allImages:
        allImageUrls.append(Image(url_for("static", filename="images/" + image), image[:-4]))

    return render_template("images.html", images=allImageUrls, imageSrc=url_for('static', filename="images/" + randomImage), previewImage=url_for("static", filename="images/" + "preview-" + randomImage), imageDescription=randomImage[:-4])
