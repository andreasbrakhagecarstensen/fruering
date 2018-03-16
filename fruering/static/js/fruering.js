function toggleSmallNav() {
    var smallNav = document.getElementById("small-nav");
    if (smallNav.className.indexOf("w3-show") === -1){
        smallNav.className += " w3-show";
    } else {
        smallNav.className = smallNav.className.replace(" w3-show", "");
    }
}