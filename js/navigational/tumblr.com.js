window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
	type=e.target.getAttribute("type");
	tag=e.target.tagName.toLowerCase();
	if(type!='text'&&tag!='textarea'){
		switch(e.keyCode){
			case 66:
				window.location=document.getElementById("previous_page_link").href;
				break;
			case 78:
				window.location=document.getElementById("next_page_link").href;
				break;
			default:
		}
	}
}
window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
	type=e.target.getAttribute("type");
	tag=e.target.tagName.toLowerCase();
	if(type!='text'&&tag!='textarea'){
		switch(e.keyCode){
			case 66:
				window.location=document.querySelector('a[id="previous_page_link"]').href;
				break;
			case 78:
				window.location=document.querySelector('a[id="next_page_link"]').href;
				break;
			default:
		}
	}
}
//neither works for some reason
