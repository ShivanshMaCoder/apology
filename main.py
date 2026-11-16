
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Apology ❤️",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
    font-family: Georgia, serif;
    overflow-x: hidden;
    background: linear-gradient(
        135deg,
        #ffe0e9,
        #ffc2d1,
        #fff0f5
    );
}

.main-container {
    min-height: 850px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    position: relative;
    overflow: hidden;
    padding: 25px 15px;
}

.card {
    width: 95%;
    max-width: 650px;
    padding: 45px 25px;
    background: rgba(255,255,255,0.82);
    border-radius: 30px;
    box-shadow: 0 15px 45px rgba(220, 50, 100, 0.2);
    z-index: 5;
    transition: all 0.4s ease;
}

.heart-icon {
    font-size: 65px;
    animation: heartbeat 1.2s infinite;
}

@keyframes heartbeat {
    0%, 100% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.2);
    }
}

h1 {
    color: #d6336c;
    font-size: 35px;
    line-height: 1.4;
    transition: font-size 0.4s ease;
    overflow-wrap: break-word;
}

.subtitle {
    color: #8c5265;
    font-size: 18px;
    margin-top: 15px;
    margin-bottom: 35px;
}

.buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 25px;
    min-height: 100px;
    flex-wrap: wrap;
}

button {
    border: none;
    border-radius: 50px;
    cursor: pointer;
    font-size: 20px;
    font-weight: bold;
    padding: 15px 35px;
    transition: all 0.35s ease;
    font-family: Georgia, serif;
}

#yesBtn {
    background: linear-gradient(
        135deg,
        #ff477e,
        #e6005c
    );
    color: white;
    box-shadow: 0 8px 20px rgba(230, 0, 92, 0.25);
    z-index: 10;
}

#yesBtn:hover {
    filter: brightness(1.08);
    transform: scale(1.04);
}

#noBtn {
    background: #eeeeee;
    color: #555;
}

.final-message {
    display: none;
    color: #d6336c;
    font-size: 20px;
    line-height: 1.5;
    margin-top: 25px;
    animation: appear 1s ease;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.heart {
    position: fixed;
    bottom: -50px;
    pointer-events: none;
    z-index: 100;
    animation: floatUp linear forwards;
}

@keyframes floatUp {
    0% {
        transform: translateY(0) rotate(0deg) scale(0.5);
        opacity: 1;
    }
    100% {
        transform: translateY(-110vh) rotate(360deg) scale(1.5);
        opacity: 0;
    }
}

.small-note {
    margin-top: 25px;
    color: #b36b83;
    font-size: 13px;
}

@media(max-width: 500px) {
    .card {
        padding: 35px 15px;
    }

    h1 {
        font-size: 28px;
    }

    .buttons {
        gap: 12px;
    }

    .final-message p {
        font-size: 17px !important;
    }
}
</style>
</head>

<body>

<div class="main-container">

    <div class="card" id="mainCard">

        <div class="heart-icon">❤️</div>

        <h1 id="apologyText">
            I am Sorry Aastha!
            <br>
            Please Forgive Me!
        </h1>

        <p class="subtitle" id="subtitle">
            I know I may have made mistakes,
            but you mean a lot to me.
            🥺
        </p>

        <div class="buttons" id="buttons">

            <button id="yesBtn" onclick="sayYes()">
                Yes ❤️
            </button>

            <button id="noBtn" onclick="sayNo()">
                No 🥺
            </button>

        </div>

        <div class="final-message" id="finalMessage">

            <div style="font-size: 55px; margin-bottom: 20px;">
                🤍🌸🤍
            </div>

            <h2 style="color: #d6336c;">
                Thank You, Aastha!
            </h2>

            <p style="
                color: #8c5265;
                font-size: 21px;
                line-height: 1.8;
                font-family: Georgia, serif;
            ">
                I know sometimes words aren't enough,
                but I genuinely want you to know that
                I'm sorry.

                <br><br>

                I hope this little gesture brings a
                smile to your face.

                <br><br>

                You are special, and I hope we can leave
                the unpleasant moments behind.
            </p>

            <div style="font-size: 35px; margin-top: 20px;">
                🤍🌷🤍
            </div>

            <p style="
                font-size: 19px;
                color: #d6336c;
                font-style: italic;
                margin-top: 15px;
            ">
                I know you like Lilies :)
            </p>


        </div>


    </div>

</div>

<audio id="sorryAudio" preload="none">
    <source src="/app/static/sorry.mp3" type="audio/mpeg">
</audio>

<audio id="admiringAudio" preload="none">
    <source src="/app/static/admiring_you.mp3" type="audio/mpeg">
</audio>

<script>

let noCount = 0;
let accepted = false;
let heartInterval = null;

const yesBtn = document.getElementById("yesBtn");
const noBtn = document.getElementById("noBtn");
const apologyText = document.getElementById("apologyText");
const subtitle = document.getElementById("subtitle");

const sorryAudio = document.getElementById("sorryAudio");
const admiringAudio = document.getElementById("admiringAudio");


// AUDIO PLAYBACK FUNCTION

function playSong(audio) {

    audio.pause();
    audio.currentTime = 0;

    const playPromise = audio.play();

    if (playPromise !== undefined) {

        playPromise.catch(error => {

            console.error("Audio playback error:", error);

            subtitle.innerText =
                "The music couldn't play. Please try again. ❤️";

        });

    }
}


// NO BUTTON FUNCTION

function sayNo() {

    if (accepted) return;

    noCount++;

    // Play Sorry once per click
    playSong(sorryAudio);

    // Increase apology text size
    const textSize = Math.min(35 + noCount * 7, 77);

    apologyText.style.fontSize = textSize + "px";

    // Increase Yes button size
    const yesSize = Math.min(20 + noCount * 8, 65);

    yesBtn.style.fontSize = yesSize + "px";

    const yesPadding = Math.min(15 + noCount * 5, 55);

    yesBtn.style.padding =
        yesPadding + "px " +
        (yesPadding * 1.8) + "px";

    // Shrink No button
    const noScale = Math.max(1 - noCount * 0.17, 0);

    noBtn.style.transform = "scale(" + noScale + ")";
    noBtn.style.opacity = noScale;

    noBtn.style.pointerEvents =
        noScale <= 0.05 ? "none" : "auto";

    // Update messages
    const messages = [
        "Please reconsider? 🥺",
        "I'll try to make things better! ❤️",
        "One more chance, please? 💗",
        "Look how much the Yes button loves you! 🥹",
        "Okay, I am not giving up! ❤️",
        "Only one answer left... ❤️"
    ];

    subtitle.innerText =
        messages[Math.min(noCount - 1, messages.length - 1)];

    // Remove No after six clicks
    if (noCount >= 6) {

        noBtn.style.display = "none";

        subtitle.innerText =
            "Only one answer left... ❤️";

    }

}


// HEART ANIMATION FUNCTION

function createHeart() {

    const heart = document.createElement("div");

    heart.className = "heart";

    const hearts = [
        "❤️",
        "💗",
        "💕",
        "💖",
        "💘",
        "💝",
        "🥰"
    ];

    heart.innerText =
        hearts[Math.floor(Math.random() * hearts.length)];

    heart.style.left = Math.random() * 100 + "vw";

    heart.style.fontSize =
        (20 + Math.random() * 40) + "px";

    heart.style.animationDuration =
        (3 + Math.random() * 4) + "s";

    document.body.appendChild(heart);

    setTimeout(function() {
        heart.remove();
    }, 7500);

}


// YES BUTTON FUNCTION

function sayYes() {

    if (accepted) return;

    accepted = true;

    // Stop Sorry song
    sorryAudio.pause();
    sorryAudio.currentTime = 0;

    // Play Admiring You
    playSong(admiringAudio);

    // Update heading
    apologyText.innerHTML =
        "THANK YOU FOR GIVING ME ANOTHER CHANCE! ❤️";

    apologyText.style.fontSize = "36px";

    // Hide subtitle and buttons
    subtitle.style.display = "none";

    document.getElementById("buttons").style.display =
        "none";

    // Display final message
    document.getElementById("finalMessage").style.display =
        "block";

    // Hide small note
    const smallNote =
        document.getElementById("smallNote");

    if (smallNote) {
        smallNote.style.display = "none";
    }

    // Update card appearance
    document.getElementById("mainCard").style.background =
        "rgba(255,255,255,0.92)";

    // Initial heart celebration
    for (let i = 0; i < 80; i++) {

        setTimeout(createHeart, i * 80);

    }

    // Continuous floating hearts
    heartInterval = setInterval(function() {

        createHeart();

    }, 250);

}

</script>

</body>
</html>
"""

components.html(
    html_code,
    height=880,
    scrolling=False
)
