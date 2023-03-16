
function ranSong(json){
    console.log("Random Song");
    
    postSong().then((data) => {
        var rand = Math.floor(Math.random()*82)
        console.log(rand);
        console.log(data.items[rand].track.name);
        var x = data.items[rand].track.name;
        // var y = data.items[rand].name;
        document.getElementById("songname").innerHTML = x;

    });
};

async function postSong() {

    const response = await fetch('https://spotify23.p.rapidapi.com/playlist_tracks/?id=0K89GnCiPehWpnp9InmB3O&offset=0&limit=100', {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        headers: {
            'X-RapidAPI-Key': 'f2ef3fe080mshb4fe39d9d1cce58p1b2592jsne54e43046c9c',
		    'X-RapidAPI-Host': 'spotify23.p.rapidapi.com'
        },
    });
    console.log(response);
    return response.json(); // parses JSON response into native JavaScript objects
}


async function postArtist() {
    const response = await fetch('https://spotify23.p.rapidapi.com/artists/?ids=2w9zwq3AktTeYYMuhMjju8', {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        headers: {
            'X-RapidAPI-Key': 'f2ef3fe080mshb4fe39d9d1cce58p1b2592jsne54e43046c9c',
            'X-RapidAPI-Host': 'spotify23.p.rapidapi.com'
        },
    });
    console.log(response);
    return response.json(); // parses JSON response into native JavaScript objects
}

document.getElementById('loginbutton').onclick = function() {
    location.href = "/login"
}

document.getElementById("signoutbutton").onclick = function() {
    location.href = "/signout"
}