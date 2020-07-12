const playBtn = document.querySelector('#previewBtn')
const player = document.querySelector('.video')

playBtn.addEventListener('click', function(e){
    console.log('Clicked') 

    // check if div has no current iframe

    if(player.childElementCount == 0){
               
        const iframe = document.createElement("iframe");
 
        iframe.setAttribute( "frameborder", "0" );
        iframe.setAttribute( "allowfullscreen", "" );
        iframe.setAttribute( "width", "560" );
        iframe.setAttribute( "height", "315" );
        iframe.setAttribute( "src", "https://www.youtube.com/embed/"+ player.dataset.embed); 
                
        player.appendChild( iframe );
        player.classList.remove('d-none')
    }
           
});   