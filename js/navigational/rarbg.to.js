window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
	type=e.target.getAttribute("type");
	tag=e.target.tagName.toLowerCase();
	if(type!='text'&&tag!='textarea'){
		switch(e.keyCode){
			case 66:
				window.location=document.querySelector('a[title="previous page"]').href;
				break;
			case 78:
				window.location=document.querySelector('a[title="next page"]').href;
				break;
			default:
		}
	}
}
