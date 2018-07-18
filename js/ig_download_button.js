//Adds a download button to the right of the page that links to the full image on Instagram
//also keybind to 'D' key to do the same without a mouse
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//	SOMETHING'S CAUSING CONSTANT PAGE RELOADS
//	SUCKS UP A LOT OF MEMORY
//	DON'T USE UNTIL FIXED
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
	type=e.target.getAttribute("type");
	tag=e.target.tagName.toLowerCase();
	if(type!='text'&&tag!='textarea'){
		switch(e.keyCode){
			case 68: //D key
				window.location = document.querySelector("meta[property='og:image']").getAttribute('content');
				break;
			default:
		}
	}
}
//Create download button

//With Material Icons
//document.getElementsByTagName("head")[0].innerHTML += '<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">';
//test2 = '<a href="' + document.querySelector("meta[property='og:image']").getAttribute('content') + '" style="color:#7f8a94;"><div style="position:fixed; bottom:50%; right:0px; border-radius:15px 0px 0px 15px; background:#faf0e6; padding:5px; border:2px solid #7f8a94; border-right-style:none;"><i class="material-icons">arrow_downward</i></div></a>';

//Without Material Icons
test3 = '<a href="' + document.querySelector("meta[property='og:image']").getAttribute('content') + '" style="color:#7f8a94;"><div style="position:fixed; bottom:50%; right:0px; border-radius:15px 0px 0px 15px; background:#faf0e6; padding:13px; border:2px solid #7f8a94; border-right-style:none;"><i style="border:solid black; border-width:0 3px 3px 0; display:inline-block; padding:3px; transform:rotate(45deg); -webkit-transform:rotate(45deg);"></i></div></a>';
document.body.innerHTML += test3;
