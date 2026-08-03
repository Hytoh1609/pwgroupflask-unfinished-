from Flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

notes = []
@app.route("/new_note")
def new_note():
    if request.method == "POST":
        date = request.form.get("date")
        venue = request.form.get("venue")
        meeting_notes = request.form.get("meetingnotes")
        actions_to_take = request.form.get("actionstotake")

        with open("NOTES.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerows([date, venue, meetingnotes, actiosntotake])
            
    return render_template("new_note.html") 




@app.route("/notes")
def notes():
    datas = []
    with open("NOTES.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row:
                datas.append(row)

    return render_template("notes.html", datas=datas)

        




@app.route("/weather")
def weather():
    if request.method == "POST":
        search = request.form.get("keyword")

        response = request.get("https://api-open.data.gov.sg/v2/real-time/api/two-hr-forecast")

        if response.status_code == 200:
            data.response.json()    w
            forecasts = data.get("data", ())).get("items", [])[0].get("forecasts", [])

            for item in forecasts:
                print(f"Area: {item['area']} | Forecast: {item['forecast']}")

    return render_template("weather.html"

if __name__ == "__main__":
    app.run(port=7891)
