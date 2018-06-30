//All .js files combined into one
//Needs testing, I don't know if it works
window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
	type=e.target.getAttribute("type");
	tag=e.target.tagName.toLowerCase();
	if(type!='text'&&tag!='textarea'){
		switch(e.keyCode){
			case 66:
				pag(false);
				break;
			case 78:
				pag(true);
				break;
			default:
		}
	}
}
/* notes without doing any testing whatsoever
 * maybe check if values are null first, then run the functions, if it isn't working that is
 * i think it does crash the program if the values are null, haven't tested this but tested a different one
 * i think pornolab.net's one would directly break the whole thing, commenting it out
 * it doesn't break if i try to make an array from the values, does it?
 * i think i can even crop more repetition by turning the whole thing into one function
 * ...
 */
//var arrays, wl
n = [
	document.querySelector('a[class="next"]').href,							//nhentai.net
	document.querySelector('a[class="pager pager_next"]').href,				//pornbay.org
	document.querySelector('a[title="next page"]').href,					//rarbg.to
	document.querySelector('a[rel="nofollow next"]').href,					//reddit.com
	document.querySelector('i[class="fa fa-angle-right"]').parentNode.href,	//steamgifts.com
];
b = [
	document.querySelector('a[class="previous"]').href,						//nhentai.net
	document.querySelector('a[class="pager pager_prev"]').href,				//pornbay.org
	document.querySelector('a[title="previous page"]').href,				//rarbg.to
	document.querySelector('a[rel="nofollow prev"]').href,					//reddit.com
	document.querySelector('i[class="fa fa-angle-left"]').parentNode.href,	//steamgifts.com
];
wl = window.location;
//true = n, false = b
function pag(p){
	if(p){
		if(n[0])
			wl = n[0];
		if(n[1])
			wl = n[1];
		if(n[2])
			wl = n[2];
		if(n[3])
			wl = n[3];
		if(n[4])
			wl = n[4];
	}else{
		if(b[0])
			wl = b[0];
		if(b[1])
			wl = b[1];
		if(b[2])
			wl = b[2];
		if(b[3])
			wl = b[3];
		if(b[4])
			wl = b[4];
	}
}