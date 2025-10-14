from flask import Flask

app = Flask(__name__)

# 🎶 Online Happy Birthday tune
MUSIC_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# 🎈 Balloon colors
BALLOON_COLORS = ["#FF69B4", "#FF4500", "#FFD700", "#32CD32", "#1E90FF", "#BA55D3"]

base_head = f"""
<head>
    <title>Birthday Wishes</title>
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{
            margin:0; padding:0;
            font-family:'Roboto',sans-serif;
            overflow-x:hidden;
        }}
        h1 {{
            font-family:'Pacifico',cursive;
            color:#fff;
            text-shadow:2px 2px 8px rgba(0,0,0,0.3);
        }}
        p {{ font-size:20px; color:#fff; }}
        a {{
            display:inline-block;
            margin:15px;
            padding:12px 25px;
            font-size:18px;
            text-decoration:none;
            border-radius:30px;
            background:#fff;
            color:#ff4081;
            box-shadow:0px 4px 10px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }}
        a:hover {{ background:#ff4081;color:#fff; transform:scale(1.05); }}
        .card {{
            background: rgba(0,0,0,0.5);
            border-radius: 20px;
            padding: 30px;
            width: 500px;
            max-width:90%;
            position: fixed;
            bottom: 30px;
            left: 30px;
            text-align: center;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
            z-index:1;
        }}
        button {{
            margin-top: 20px;
            padding: 12px 25px;
            font-size: 20px;
            border: none;
            border-radius: 30px;
            background: #ff4081;
            color: white;
            cursor: pointer;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        }}
        button:hover {{ background:#e91e63; transform:scale(1.05); }}
        .balloon {{
            position:absolute;
            bottom:-100px;
            border-radius:50%;
            opacity:0.85;
        }}
        .balloon::after {{
            content: "";
            position: absolute;
            bottom: -40px;
            left: 50%;
            width: 2px;
            height: 40px;
            background: rgba(0,0,0,0.3);
            transform: translateX(-50%);
        }}
        canvas {{ position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:0; }}
        @keyframes rise {{
            0% {{ transform: translateY(0); }}
            100% {{ transform: translateY(-120vh); }}
        }}
    </style>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
    <script>
        function launchConfetti() {{
            setInterval(function(){{
                confetti({{ particleCount: 3, spread: 70, origin: {{y:0.6}} }});
            }}, 300);
        }}

        function createBalloons() {{
            const colors = {BALLOON_COLORS};
            for(let i=0;i<20;i++){{
                let balloon = document.createElement('div');
                balloon.className = 'balloon';
                balloon.style.background = colors[Math.floor(Math.random()*colors.length)];
                balloon.style.left = Math.random()*100 + '%';
                let sizeW = 40 + Math.random() * 30;
                let sizeH = 60 + Math.random() * 40;
                balloon.style.width = sizeW + 'px';
                balloon.style.height = sizeH + 'px';
                balloon.style.animation = 'rise ' + (10 + Math.random()*5) + 's linear infinite';
                document.body.appendChild(balloon);
            }}
        }}

        function playMusic() {{
            var audio = document.getElementById('music');
            audio.loop = true;
            audio.play();
            launchConfetti();
            createBalloons();
        }}

        document.addEventListener("click", function() {{
            let audio = document.getElementById("music");
            if (audio && audio.paused) {{ audio.play(); }}
        }}, {{ once: true }});
    </script>
</head>
"""

# --- First page ---
@app.route("/")
def home():
    return f"""
    <html>
        {base_head}
        <body style="background:#ff4081; display:flex; justify-content:center; align-items:center; height:100vh;">
            <div style="text-align:center;">
                <h1 style="font-size:60px;">🎂 Happy Birthday, Alex! 🎂</h1>
                <a href="/wish1">➡ Next</a>
            </div>
        </body>
    </html>
    """

# --- Second page ---
def wish_page_img(title, message, next_url=None):
    left_img_html = '<img src="https://wallpapers.com/images/hd/sad-person-pictures-3006-x-2214-2bnso9uiwlhrikrx.jpg" alt="Left" style="position:absolute; top:5px; left:8px; width:100px; opacity:0.6; filter: brightness(200%); border-radius:10px;">'
    right_img_html = '<img src="https://wallpapers.com/images/hd/sad-person-pictures-3006-x-2214-2bnso9uiwlhrikrx.jpg" alt="Right" style="position:absolute; top:5px; right:8px; width:100px; opacity:0.6; filter: brightness(200%); border-radius:10px;">'
    next_button_html = f'<a href="{next_url}">➡ Next</a>' if next_url else ''

    return f"""
    <html>
        {base_head}
        <body style="
            background: url('https://asset.gecdesigns.com/img/wallpapers/birthday-wishes-with-a-delicious-birthday-cake-background-sr17052504-cover.webp') no-repeat center center fixed;
            background-size: 2000px 1400px;
            margin:0; padding:0;
        ">
            <div class="card">
                {left_img_html}
                {right_img_html}
                <h1 style="font-size:36px;">{title}</h1>
                <p style="font-size:20px;">{message}</p>
                <a href="/">⬅ Back</a><br>
                {next_button_html}<br>
                <button onclick="playMusic()">🎶 Play Birthday Surprise!</button>
                <audio id="music">
                    <source src="{MUSIC_URL}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
        </body>
    </html>
    """

@app.route("/wish1")
def wish1():
    return wish_page_img("🎉🎂 Happy Birthday, Alex! 🎂🎉",
                         "May your special day be filled with joy and laughter! 🥳",
                         next_url="/wish2")

@app.route("/wish2")
def wish2():
    return wish_page_img("🌟 Happy Birthday, Alex! 🌟",
                         "Wishing you endless happiness and success today and always! 🎁",
                         next_url="/wish3")

# --- Third page with background video ---
# --- Third page with updated background video ---
@app.route("/wish3")
def wish3():
    left_img_html = '<img src="https://wallpapers.com/images/hd/sad-person-pictures-3006-x-2214-2bnso9uiwlhrikrx.jpg" alt="Left" style="position:absolute; top:5px; left:8px; width:100px; opacity:0.6; filter: brightness(200%); border-radius:10px;">'
    right_img_html = '<img src="https://wallpapers.com/images/hd/sad-person-pictures-3006-x-2214-2bnso9uiwlhrikrx.jpg" alt="Right" style="position:absolute; top:5px; right:8px; width:100px; opacity:0.6; filter: brightness(200%); border-radius:10px;">'

    return f"""
    <html>
        {base_head}
        <body style="margin:0; padding:0; overflow:hidden;">
            <!-- Background video -->
            <video autoplay muted loop id="background-video" style="position:fixed; top:0; left:0; width:100%; height:100%; object-fit:cover; z-index:-1;">
                <source src="https://resource.flexclip.com/templates/video/720p/happy-birthday-pure-text-animation.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>

            <div class="card">
                {left_img_html}
                {right_img_html}
                <h1 style="font-size:36px;">💖 Happy Birthday, Alex! 💖</h1>
                <p style="font-size:20px;">May your life be filled with love, health, and sweet surprises! 🎂✨</p>
                <a href="/wish2">⬅ Back</a><br>
                <button onclick="playMusic()">🎶 Play Birthday Surprise!</button>
                <audio id="music">
                    <source src="{MUSIC_URL}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
