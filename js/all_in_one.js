//All .js files combined into one
//Needs testing, I don't know if it works
window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
	f = false;
	t = true;
	type=e.target.getAttribute("type");
	tag=e.target.tagName.toLowerCase();
	if(type!='text'&&tag!='textarea'){
		switch(e.keyCode){
			case 66:
				nhentai_net(f);
				pornbay_org(f);
				//pornolab_net(f);
				rarbg_to(f);
				reddit_com(f);
				steamgifts_com(f);
				break;
			case 78:
				nhentai_net(t);
				pornbay_org(t);
				//pornolab_net(t);
				rarbg_to(t);
				reddit_com(t);
				steamgifts_com(t);
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
 * ...
 */
//var arrays
n = [
	document.querySelector('a[class="next"]').href,							//nhentai.net
	document.querySelector('a[class="pager pager_next"]').href,				//pornbay.org
	document.querySelector('a[title="next page"]').href,					//rarbg.to
	document.querySelector('a[rel="nofollow next"]').href,					//reddit.com
	document.querySelector('i[class="fa fa-angle-right"]').parentNode.href,	//steamgifts.com
]
b = [
	document.querySelector('a[class="previous"]').href,						//nhentai.net
	document.querySelector('a[class="pager pager_prev"]').href,				//pornbay.org
	document.querySelector('a[title="previous page"]').href,				//rarbg.to
	document.querySelector('a[rel="nofollow prev"]').href,					//reddit.com
	document.querySelector('i[class="fa fa-angle-left"]').parentNode.href,	//steamgifts.com
]
//true = n, false = b
//nhentai.net
function nhentai_net(p){
	if(p){
		if(n[0])
			window.location = n[0];
	}else{
		if(b[0])
			window.location = b[0];
	}
}
//pornobay.org
function pornbay_org(p){
	if(p){
		if(n[1])
			window.location = n[1];
	}else{
		if(b[1])
			window.location = b[1];
	}
}
//pornolab.net
function pornolab_net(p){
	patt = /start/g;
	winlo = window.location.href;
	wlos = winlo.split('=').reverse();
	if(wlos[1].match(patt) == "start"){
		bo_page = true;
	}else{
		bo_page = false;
	}
	if(bo_page){
		if(p){
			wlos[0] = parseInt(wlos[0]) + 50;
			window.location = wlos.reverse().join('=');
		}else{
			wlos[0] = parseInt(wlos[0]) - 50;
			window.location = wlos.reverse().join('=');
		}
	}else{
		if(p){
			window.location = winlo + "&start=50";
		}
	}
}
//rarbg.to
function rarbg_to(p){
	if(p){
		if(n[2])
			window.location = n[2];
	}else{
		if(b[2])
			window.location = b[2];
	}
}
//reddit.com
function reddit_com(p){
	if(p){
		if(n[3])
			window.location = n[3];
	}else{
		if(b[3])
			window.location = b[3];
	}
}
//steamgifts.com
function steamgifts_com(p){
	if(p){
		if(n[4])
			window.location = n[4];
	}else{
		if(b[4])
			window.location = b[4];
	}
}