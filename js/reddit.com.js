window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
	type=e.target.getAttribute("type");
	tag=e.target.tagName.toLowerCase();
	if(type!='text'&&tag!='textarea'){
		switch(e.keyCode){
			case 66:
				window.location=document.querySelector('a[rel="nofollow prev"]').href;
				break;
			case 78:
				window.location=document.querySelector('a[rel="nofollow next"]').href;
				break;
			/* disabled tests below
			case 82: //r
				//window.location=document.querySelector('a[class="random choice"]').href;
				window.location='https://www.reddit.com/r/random/';
				break;
			case 84: //t
				//window.location=document.querySelector('a[class="random choice"]').href;
				//window.location=$('a:contains("randnsfw")').attr('href');
				window.location='https://www.reddit.com/r/randnsfw/';
				break;
			case 85: //u
				$('.up:first').trigger('click');
				break;
			case 73: //i
				$('.upmod:first').trigger('click');
				break;
			case 49: //1
				$('.noncollapsed.comment .expand:eq(0)').not('.child .noncollapsed.comment .expand:eq(0)').trigger('click');
				break;
			case 50: //2
				//$('.comment.collapsed .expand:eq(-1)').trigger('click');
				break;
			*/
			default:
		}
	}
}
