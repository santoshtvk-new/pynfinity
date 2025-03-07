//var short_names = ["🖐 <span>S</span>antoshtvk", "🍴 <span>A</span>dventures", "💻 <span>N</span>ovice?", "🚀 <span>T</span>ests", "🤝 <span>U</span>nite?"]
//
//var long_names = ["🖐 <span>H</span>i, I'm ... !", "🍴 <span>E</span>xperiments", "💻 <span>L</span>et's Learn Together", "🚀 <span>L</span>ot's of Challenges", "🤝 <span>O</span>k, Time to Meet Now?"]

//const axiosRequest = require('axios');

//santoshtvk
//adventures
//novice to hero
//testing
//unite
//
//function menu_resizing() {
//    let width = screen.width;
//    //$("#topmargin").text(width);
//    if (width < 1200 && width > 768) {
//        $("#h").html(short_names[0]);
//        $("#e").html(short_names[1]);
//        $("#l").html(short_names[2]);
//        $("#ll").html(short_names[3]);
//        $("#o").html(short_names[4]);
//    }
//    else {
//        $("#h").html(long_names[0]);
//        $("#e").html(long_names[1]);
//        $("#l").html(long_names[2]);
//        $("#ll").html(long_names[3]);
//        $("#o").html(long_names[4]);
//    }
//}
//menu_resizing()
//window.addEventListener("resize", menu_resizing);


localStorage.setItem('author', 'guest');
async function jokeout() {

    let url = "https://official-joke-api.appspot.com/jokes/programming/random"

    const response = await fetch(url, {
        method: "GET"
    });

    if (!response.ok) {
        $("#title_word").html("Jokes on the way!");
        $("#explaination").html("Pay your Smile as a Tax Meanwhile 😊");
        return
    }

    const data = await response.json();
    res = data[0];
    console.log(res);

    if (res.setup) {
        $("#joke_word").html(res.setup);
        $("#jokeexplaination").html(res.punchline + ' 😁😂');
    }
}

async function findout() {
    
    let url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + String($("#search_word").val());

    const response = await fetch(url, {
        method: "GET"
    });

    if (!response.ok) {
        $("#search_word").val("welcome");
        findout();
        return
    }

    const data = await response.json();
    res = data[0];
    console.log(res);

    if (res.word) {
        $("#title_word").html(res.word);
        dyna_option = '<ol>';

        for (let i = 0; i < res.meanings.length; i++) {
            dyna_option += '<li><ol><strong>' + res.meanings[i].partOfSpeech + '</strong>&nbsp;';

            for (let j = 0; j < 1; j++) {
                //res.meanings[i].definitions.length
                dyna_option += "<li>" + res.meanings[i].definitions[j].definition + '</li>';
            }
            dyna_option += '</ol></li>';
        }

        dyna_option += '</ol>';

        for (let k = 0; k < res.phonetics.length; k++) {
            if (res.phonetics[k].audio && res.phonetics[k].audio.length > 5) {
                let default_phonetic_path = res.phonetics[k].audio;
                $("#phonetics").attr("src", default_phonetic_path);
                $("#title_word").html($("#title_word").html() + " 🔊");
                break
            }
        }
        $("#explaination").html(dyna_option);
    }
}
function playphonetics() {
    var audio = document.getElementById("phonetics");
    audio.play();
}

findout();
jokeout();