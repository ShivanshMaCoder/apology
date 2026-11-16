
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
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">

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

body {
    min-height: 100vh;
}

.main-container {
    min-height: 850px;
    min-height: 100svh;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    position: relative;
    overflow: hidden;
    padding: clamp(16px, 4vw, 35px);
}

.card {
    width: min(100%, 650px);
    padding: clamp(25px, 5vw, 45px);
    background: rgba(255,255,255,0.85);
    border-radius: clamp(20px, 4vw, 30px);
    box-shadow: 0 15px 45px rgba(220, 50, 100, 0.2);
    z-index: 5;
    transition: all 0.4s ease;
}

.heart-icon {
    font-size: clamp(45px, 10vw, 65px);
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
    font-size: clamp(27px, 5.5vw, 35px);
    line-height: 1.4;
    transition: font-size 0.4s ease;
    overflow-wrap: break-word;
}

.subtitle {
    color: #8c5265;
    font-size: clamp(16px, 3.5vw, 18px);
    line-height: 1.6;
    margin-top: 15px;
    margin-bottom: 30px;
}

.buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: clamp(12px, 4vw, 25px);
    min-height: 90px;
    flex-wrap: wrap;
    width: 100%;
}

button {
    border: none;
    border-radius: 50px;
    cursor: pointer;
    font-size: clamp(17px, 4vw, 20px);
    font-weight: bold;
    padding: 15px clamp(22px, 5vw, 35px);
    transition: all 0.35s ease;
    font-family: Georgia, serif;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
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
    margin-top: 20px;
    animation: appear 1s ease;
}

.final-message h2 {
    font-size: clamp(24px, 5vw, 30px);
    margin: 15px 0;
}

.final-message p {
    overflow-wrap: break-word;
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
    will-change: transform, opacity;
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

/* iPhone and smaller mobile screens */
@media screen and (max-width: 480px) {

    .main-container {
        padding: 15px 12px;
        justify-content: center;
    }

    .card {
        width: 100%;
        padding: 28px 18px;
        border-radius: 24px;
    }

    h1 {
        font-size: clamp(25px, 7vw, 30px);
        line-height: 1.4;
    }

    .subtitle {
        font-size: 16px;
        margin-bottom: 20px;
    }

    .buttons {
        gap: 12px;
        min-height: 80px;
    }

    button {
        padding: 14px 25px;
        font-size: 17px;
    }

    .final-message {
        margin-top: 15px;
        font-size: 17px;
        line-height: 1.65;
    }

    .final-message p {
        font-size: 17px !important;
        line-height: 1.7 !important;
    }

    .final-message > div:first-child {
        font-size: 45px !important;
    }

    .final-message > div:nth-of-type(1) {
        font-size: 32px !important;
    }
}

/* Tablets and iPads */
@media screen and (min-width: 481px) and (max-width: 1024px) {

    .main-container {
        padding: 30px;
    }

    .card {
        width: min(90%, 650px);
        padding: 40px 35px;
    }

    h1 {
        font-size: 34px;
    }

    .final-message p {
        font-size: 20px;
    }
}

/* Small height screens */
@media screen and (max-height: 650px) {

    .main-container {
        justify-content: flex-start;
        padding-top: 20px;
        padding-bottom: 25px;
    }
}

/* Respect reduced motion preferences */
@media (prefers-reduced-motion: reduce) {
    .heart-icon {
        animation: none;
    }

    .card, button {
        transition: none;
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


// AUDIO PLAYBACK

function playSong(audio) {

    audio.pause();
    audio.currentTime = 0;

    const playPromise = audio.play();

    if (playPromise !== undefined) {

        playPromise.catch(error => {

            console.error("Audio playback error:", error);

            if (subtitle.style.display !== "none") {
                subtitle.innerText =
                    "The music couldn't play. Please try again. ❤️";
            }

        });

    }
}


// NO BUTTON

function sayNo() {

    if (accepted) return;

    noCount++;

    playSong(sorryAudio);

    // Increase apology text
    const textSize = Math.min(35 + noCount * 7, 77);

    apologyText.style.fontSize = textSize + "px";

    // Increase Yes button
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

    if (noCount >= 6) {

        noBtn.style.display = "none";

        subtitle.innerText =
            "Only one answer left... ❤️";

    }

}


// FLOATING HEARTS

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


// YES BUTTON

function sayYes() {

    if (accepted) return;

    accepted = true;

    // Stop Sorry
    sorryAudio.pause();
    sorryAudio.currentTime = 0;

    // Play Admiring You
    playSong(admiringAudio);

    // Change heading
    apologyText.innerHTML =
        "THANK YOU FOR GIVING ME ANOTHER CHANCE! ❤️";

    apologyText.style.fontSize =
        "clamp(25px, 5vw, 36px)";

    // Hide buttons and subtitle
    subtitle.style.display = "none";

    document.getElementById("buttons").style.display =
        "none";

    // Show final message
    document.getElementById("finalMessage").style.display =
        "block";

    // Update card
    document.getElementById("mainCard").style.background =
        "rgba(255,255,255,0.92)";

    // Heart celebration
    for (let i = 0; i < 80; i++) {

        setTimeout(createHeart, i * 80);

    }

    // Continuous hearts
    heartInterval = setInterval(function() {

        createHeart();

    }, 350);

}

</script>

</body>
</html>
"""

components.html(
    html_code,
    height=950,
    scrolling=True
)
