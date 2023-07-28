var short_names = ["🖐 <span>S</span>antoshtvk", "🍴 <span>A</span>dventures", "💻 <span>N</span>ovice?", "🚀 <span>T</span>ests", "🤝 <span>U</span>nite?"]

var long_names = ["🖐 <span>H</span>i, I'm ... !", "🍴 <span>E</span>xperiments", "💻 <span>L</span>et's Learn Together", "🚀 <span>L</span>ot's of Challenges", "🤝 <span>O</span>k, Time to Meet Now?"]

//const axiosRequest = require('axios');

//santoshtvk
//adventures
//novice to hero
//testing
//unite

function menu_resizing() {
    let width = screen.width;
    $("#testsize").text(width);
    if (width < 1200 && width > 768) {
        $("#h").html(short_names[0]);
        $("#e").html(short_names[1]);
        $("#l").html(short_names[2]);
        $("#ll").html(short_names[3]);
        $("#o").html(short_names[4]);
    }
    else {
        $("#h").html(long_names[0]);
        $("#e").html(long_names[1]);
        $("#l").html(long_names[2]);
        $("#ll").html(long_names[3]);
        $("#o").html(long_names[4]);
    }
}


menu_resizing()
window.addEventListener("resize", menu_resizing);

function findout2() {
    let urll = "https://api.dictionaryapi.dev/api/v2/entries/en/" + String($("#search_word").val());
    let res = apiData(urll)

    console.log(res);
    if (res[0]) {
        res = res[1]
        console.log(res['word']);
        $("#title_word").html(res['word'] + " 🔊");
        dyna_option = '<ul>';

        for (let i = 0; i < res[0].meanings.length; i++) {
            dyna_option += '<li><ul><strong>' + res[0].meanings[i][partOfSpeech] + '</strong>&nbsp;';

            for (let j = 0; j < res[0].meanings[i][partOfSpeech][definitions].length; j++) {
                dyna_option += "<li>" + res[0].meanings[i][partOfSpeech][definitions][j] + '</li>';
            }
            dyna_option += '</ul></li>';
        }

        dyna_option += '</ul>';
        $("#explaination").html(dyna_option);
    }
    else {
        $("#explaination").html('<strong>' + res[1] +' or check our "Word of the day!"</strong>');
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