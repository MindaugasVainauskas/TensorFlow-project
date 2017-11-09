//Setting up image handling to load into canvas
function handleImage(imgPath){
    var canvas = document.getElementById('canvas');
    if (canvas.getContext){
        var ctx = canvas.getContext('2d');
        var image = new Image();

        image.onload = function(){
            ctx.drawImage(image, 0, 0)
            ctx.fillStyle = "rgba(200, 0, 0, 0.5)";
            ctx.fillRect(0, 0, 500, 500);
        };        
        image.src = imgPath;
    }
}