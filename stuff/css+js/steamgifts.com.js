//Custom js to add keyboard shortcuts for steamgifts.com
//n for next page
//b for previous
window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
	type=e.target.getAttribute("type");
	tag=e.target.tagName.toLowerCase();
	if(type!='text'&&tag!='textarea'){
		switch(e.keyCode){
			case 66:
				window.location=document.querySelector('i[class="fa fa-angle-left"]').parentNode.href;
				break;
			case 78:
				window.location=document.querySelector('i[class="fa fa-angle-right"]').parentNode.href;
				break;
			default:
		}
	}
}