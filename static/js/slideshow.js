window.onload = function() {
    var index = 0;
    var img_list = ["url('../img/fjords.png')", "url('../img/california-rocks.jpg')", 
    "url('../img/mountain-river.jpg')", "url('../img/forest-sunset.jpg')"];
    slide();

    function slide() {
        var slides = document.getElementsByClassName("heroimg")[0];
        var dots = document.getElementsByClassName("dot");
        //for (var i = 0; i < img_list.length; i++) {
        slides.style.backgroundImage = img_list[index];
        dots[index].className = "dot active_dot";
        //}
        index++;
        if (index >= img_list.length) {
            index = 0;
        }
        /*if (index > slides.length) {index = 1}
        slides[index-1].style.display = "block";*/
        setTimeout(slide, 1800);
    }

    function current_slide(n) {
    	slide(index = n);
    }
}