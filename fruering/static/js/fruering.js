function toggleVisible(elementId) {
    var element = document.getElementById(elementId);
    if (element.className.indexOf("w3-show") === -1){
        element.className += " w3-show";
    } else {
        element.className = element.className.replace(" w3-show", "");
    }
}

function toggleText(elementId, text1, text2) {
    var element = document.getElementById(elementId);
    if(element.textContent == text1)
        element.textContent = text2;
    else if (element.textContent == text2)
        element.textContent = text1;
}

function toggleBlogPostReadMore(postid){
    toggleVisible('post-' + postid);
    toggleText('moreButton-' + postid, 'Læs mere', 'Læs mindre')
}