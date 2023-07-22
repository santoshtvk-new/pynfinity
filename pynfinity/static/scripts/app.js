var short_names = ["🖐 <span>S</span>antoshtvk", "🍴 <span>A</span>dventures", "💻 <span>N</span>ovice?", "🚀 <span>T</span>ests", "🤝 <span>U</span>nite?"]

var long_names = ["🖐 <span>H</span>i, I'm ... !", "🍴 <span>E</span>xperiments", "💻 <span>L</span>et's Learn Together", "🚀 <span>L</span>ot's of Challenges", "🤝 <span>O</span>k, Time to Meet Now?"]

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

