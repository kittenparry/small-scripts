//not working, can't tell why
window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
	type=e.target.getAttribute("type");
	tag=e.target.tagName.toLowerCase();
	if(type!='text'&&tag!='textarea'){
		switch(e.keyCode){
			case 66:
				window.location=document.querySelector('li[class="paginav-previous"]').lastChild.href;
				break;
			case 78:
				window.location=document.querySelector('li[class="paginav-next"]').lastChild.href;
				break;
			default:
		}
	}
}
