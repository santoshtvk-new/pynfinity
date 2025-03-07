let wordlist = ["abate", "aberrant", "abjure", "abscond", "abstain", "acumen", "admonish", "adulterate", "advocate", "aesthetic", "affectation", "aggrandize", "alacrity", "alleviate", "amalgamate", "ambiguous", "ambivalent", "ameliorate", "amenable", "anachronism", "analogous", "anoint", "anomaly", "antipathy", "antithetical", "apathy", "appease", "arbitrary", "arcane", "archaic", "arduous", "articulate", "artless", "ascetic", "assuage", "astonishment", "audacious", "austere", "avarice", "aver", "banal", "belie", "benign", "biased", "bolster", "bombastic", "brazen", "bucolic", "burgeon", "cacophony", "calumny", "candid", "canon", "capacity", "capricious", "castigate", "catalyst", "caustic", "censure", "chauvinist", "chicanery", "chronological", "coalesce", "cogent", "commensurate", "compelling", "comprehensive", "condone", "confound", "connoisseur", "consequential", "construe", "consumption", "contend", "contentious", "contrite", "convoluted", "copious", "cosmopolitan", "covet", "craft", "craven", "credence", "credulous", "decorum", "deference", "deflect", "deftness", "delineate", "demur", "denigrate", "deride", "derivative", "desiccate", "desultory", "detachment", "determinant", "diatribe", "didactic", "diffident", "dilettante", "dirge", "disabuse", "discern", "discrepancy", "disinterested", "disparage", "disparate", "dispassionate", "disregard", "dissemble", "disseminate", "dissonance", "diverge", "dogma", "dupe", "ebullient", "eccentric", "eclectic", "efficacy", "elegy", "elicit", "eloquence", "eminent", "empirical", "emulate", "enervate", "engender", "enhance", "entitlement", "ephemeral", "equable", "equivocate", "erroneous", "erudite", "eschew", "esoteric", "estimable", "eulogy", "exacerbate", "exacting", "exculpate", "exigent", "exonerate", "expatiate", "explicate", "exposition", "extraneous", "extrapolate", "facetious", "facilitate", "fallacious", "fastidious", "fluctuate", "foment", "forestall", "fortuitous", "frugal", "gainsay", "galvanize", "garrulous", "gauche", "germane", "glib", "gregarious", "guile", "hackneyed", "harangue", "hedonism", "hierarchical", "homogenous", "hyperbole", "iconoclast", "ideological", "imminent", "immutable", "impair", "impediment", "imperturbable", "implacable", "implicit", "imprudence", "impudent", "inadvertent", "Inchoate", "inconclusive", "indebted", "indefatigable", "indolent", "infer", "ingenuous", "inimical", "Innocuous", "inscrutable", "insipid", "insular", "intensive", "intermediary", "intimate", "intractable", "intransigent", "intrepid", "inveterate", "invulnerable", "irascible", "irresolute", "laconic", "laud", "laudable", "litigation", "loquacious", "lucid", "luminous", "magnanimity", "maladroit", "malign", "malleable", "maverick", "mendacity", "mercurial", "meticulous", "misanthrope", "mitigate", "modest", "mollify", "monotony", "mundane", "munificent", "naïve", "nascent", "neglect", "nonplussed", "notoriety", "nuance", "obdurate", "obscure", "obsequious", "obstinate", "obviate", "occlude", "occult", "offset", "olfactory", "omniscience", "onerous", "opaque", "opportunism", "opprobrium", "oscillate", "ostentatious", "outstrip", "overshadow", "painstaking", "partial", "partisan", "patent", "paucity", "pedantic", "pedestrian", "perfidy", "perfunctory", "peripheral", "permeate", "perseverance", "peruse", "pervasive", "phenomena", "phlegmatic", "pith", "placate", "plastic", "platitude", "plausible", "plethora", "plummet", "polarize", "polemical", "pragmatic", "precarious", "preceded", "precipitate", "precursor", "prescient", "presumptuous", "prevail", "prevaricate", "pristine", "probity", "prodigal", "prodigious", "profligate", "proliferate", "propitiate", "propriety", "prospective", "qualification", "quotidian", "rationalize", "reconcile", "recondite", "refute", "relentless", "relevant", "reproach", "repudiate", "rescind", "respectively", "reticent", "reverent", "rhetoric", "salubrious", "sanction", "satiate", "secular", "sediment", "sedulous", "simultaneous", "solicitous", "soporific", "sparse", "specious", "sporadic", "spurious", "stolid", "subjective", "substantiate", "subversive", "sufficient", "superbly", "supine", "supplant", "sycophant", "synthesize", "tacit", "taciturn", "temperance", "tenuous", "timorous", "tirade", "torpor", "tortuous", "tractable", "transient", "ubiquitous", "unadorned", "undermine", "underscore", "untenable", "vacillate", "venality", "venerate", "veracity", "verbose", "vexation", "volatile", "whimsical", "zeal"]

const randomElement = wordlist[Math.floor(Math.random() * wordlist.length)];
$("#search_word").val(randomElement);

google.charts.load('current', { 'packages': ['corechart', 'timeline'] });
google.charts.setOnLoadCallback(drawexps);
google.charts.setOnLoadCallback(drawskills);

function date_diff_in_years(a, b){
    const date1 = new Date(a);
    const date2 = new Date(b);
    const diffTime = Math.abs(date2.getTime() - date1.getTime());
    const diffY = (diffTime / (1000 * 60 * 60 * 24 * 365)).toFixed(2);
    console.log(diffY + " ----------------------years");
    return parseFloat(diffY);
}

function cur_date(){
    const today = new Date();
    const dd = String(today.getDate()).padStart(2, '0');
    const mm = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!
    const yyyy = today.getFullYear();

    const formattedDate = mm + '/' + dd + '/' + yyyy;
    console.log(formattedDate); // Output: mm/dd/yyyy
    d = new Date(formattedDate)
    return d;
}

function drawexps() {

    var container = document.getElementById('expchart');
    var chart = new google.visualization.Timeline(container);
    var dataTable = new google.visualization.DataTable();
    dataTable.addColumn({ type: 'string', id: 'Position' });
    dataTable.addColumn({ type: 'string', id: 'Name' });
    dataTable.addColumn({ type: 'date', id: 'Start' });
    dataTable.addColumn({ type: 'date', id: 'End' });
    dataTable.addRows([
        [ 'Executive Engineer', 'Misc', new Date(2014, 07, 1),  new Date(2015, 10, 9) ],
      [ 'Executive Engineer', 'Galada Power Pvt Ltd',new Date(2015, 10, 9),  new Date(2016, 7, 20) ],
      [ 'Software Engineer', 'Defence DRDL-RCI',    new Date(2016, 7, 25),  new Date(2019, 6, 1) ],
      [ 'Software Engineer', 'VotaryTech [Client-Qualcomm]', new Date(2019, 6, 4),   new Date(2021, 4, 22) ],
      [ 'Automation Engineer', 'Signant Health',      new Date(2021, 4, 26),  new Date(2023, 12, 1) ],
      [ 'Automation Engineer', 'S&P Global',          new Date(2024, 1, 5),   new Date() ]]);

      var options = {
            timeline: { groupByRowLabel: true }
        };

    chart.draw(dataTable, options);
}

function drawskills() {
    var data = google.visualization.arrayToDataTable([
        ['Skills', 'Rated-Myself (0-10)'],
        ['Python', 9],
        ['SQL', 8],
        ['Linux Shell', 7],
        ['Git', 8.5],
        ['Jenkins/Docker CI-CD', 6],
        ['C++', 5],
        ['Embedded Systems', 7.5],
        ['Android App development', 4],
        ['Machine Learning', 6]
    ]);

    var options = { 'title': 'Skills',
                    vAxis: {title: 'Rated-Myself (0-10)'},
                    };
                    //isStacked: true
    var chart = new google.visualization.AreaChart(document.getElementById('skchart'));
    chart.draw(data, options);
}

function gitclasses() {
    window.open("{{ url_for('gitcmds') }}", "_blank");
}

function copyToClipboard(elementId) {
    var commandCode = document.getElementById(elementId).textContent;
    var tempInput = document.createElement('textarea');
    tempInput.value = commandCode;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand('copy');
    document.body.removeChild(tempInput);
    alert("Copied to Clipboard " + commandCode);
}

function diff_years(dt2, dt1)
{
  var diff = (dt2.getTime() - dt1.getTime()) / 1000;
  diff /= (60 * 60 * 24);
  console.log(diff);
  return Math.abs(diff / 365.25).toFixed(2);
}

d1 = new Date(2014, 07, 1)
d2 = new Date()
$("#tot_exp").html(diff_years(d2, d1))

window.onload = () => {
            const api = new JitsiMeetExternalAPI("8x8.vc", {
              roomName: "vpaas-magic-cookie-274108d3aae44a759945a1a602cc50ee/SampleAppExperiencedCounsellorsKeyGenuinely",
              parentNode: document.querySelector('#jaas-container'),
							// Make sure to include a JWT if you intend to record,
							// make outbound calls or use any other premium features!
							// jwt: "eyJraWQiOiJ2cGFhcy1tYWdpYy1jb29raWUtMjc0MTA4ZDNhYWU0NGE3NTk5NDVhMWE2MDJjYzUwZWUvZjNjNTllLVNBTVBMRV9BUFAiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJqaXRzaSIsImlzcyI6ImNoYXQiLCJpYXQiOjE3MjcxNzI5NTQsImV4cCI6MTcyNzE4MDE1NCwibmJmIjoxNzI3MTcyOTQ5LCJzdWIiOiJ2cGFhcy1tYWdpYy1jb29raWUtMjc0MTA4ZDNhYWU0NGE3NTk5NDVhMWE2MDJjYzUwZWUiLCJjb250ZXh0Ijp7ImZlYXR1cmVzIjp7ImxpdmVzdHJlYW1pbmciOmZhbHNlLCJvdXRib3VuZC1jYWxsIjpmYWxzZSwic2lwLW91dGJvdW5kLWNhbGwiOmZhbHNlLCJ0cmFuc2NyaXB0aW9uIjpmYWxzZSwicmVjb3JkaW5nIjpmYWxzZX0sInVzZXIiOnsiaGlkZGVuLWZyb20tcmVjb3JkZXIiOmZhbHNlLCJtb2RlcmF0b3IiOnRydWUsIm5hbWUiOiJUZXN0IFVzZXIiLCJpZCI6Imdvb2dsZS1vYXV0aDJ8MTExNDM4OTI5NDc4ODUwMjE2MTc1IiwiYXZhdGFyIjoiIiwiZW1haWwiOiJ0ZXN0LnVzZXJAY29tcGFueS5jb20ifX0sInJvb20iOiIqIn0.sNSS48jMXwW0vkZJ4BbL1nXesdB2rExkBr3S-XyWhfWqD0_Xqla7VRbL9qvz7RY9XpGFPCEa0UnKUA7BjI938YmV9qQilLKxw69I1Yk1KBIhGeJBf9WAE6vrRtdSG99JR8kHAUmh0sujEFIDB5_NW54TaQAAntbSjR_es_3iXb74dNxtlQIz8Az9He_hfcs_6vl9vu9j82OHJfMXJgBPcaalZ5W6gSFoW4eXoYIL_AOBiz14FEsXqc-8-b9PdteVdMwp29NeoriSzf1Eyl-6R6NOvWGemIAmaJkTpxolgySGQ0NLWnlKKp7Rrcq9eioy1Mn6fIXaErt8kjno-YXc0w"
            });
          }

$("#jaas-container").css('pointer-events','none');

$(document).ready(function() {
    var storedInput = localStorage.getItem('author');
    if (storedInput=='santoshtvk') {
        $("#jaas-container").css('pointer-events','');
    }
});

