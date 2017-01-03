

function makeRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++){
        color += letters[Math.floor(Math.random() *16)];
    }
    return color;


}

function changeColor() {
    document.getElementById('box1').style.backgroundColor = makeRandomColor();
    document.getElementById('box2').style.backgroundColor = makeRandomColor();
    document.getElementById('box3').style.backgroundColor = makeRandomColor();
    document.getElementById('box4').style.backgroundColor = makeRandomColor();
    document.getElementById('box5').style.backgroundColor = makeRandomColor();
    document.getElementById('box6').style.backgroundColor = makeRandomColor();

}

changeColor();