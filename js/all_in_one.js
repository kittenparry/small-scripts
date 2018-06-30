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
				pornolab_net(f);
				rarbg_to(f);
				reddit_com(f);
				steamgifts_com(f);
				break;
			case 78:
				nhentai_net(t);
				pornbay_org(t);
				pornolab_net(t);
				rarbg_to(t);
				reddit_com(t);
				steamgifts_com(t);
				break;
			default:
		}
	}
}
//true = n, false = b
//nhentai.net
function nhentai_net(n){
	if(n){
		window.location=document.querySelector('a[class="next"]').href;
	}else{
		window.location=document.querySelector('a[class="previous"]').href;
	}
}
//pornobay.org
function pornbay_org(n){
	if(n){
		window.location=document.querySelector('a[class="pager pager_next"]').href;
	}else{
		window.location=document.querySelector('a[class="pager pager_prev"]').href;
	}
}
//pornolab.net
function pornolab_net(n){
	patt = /start/g;
	winlo = window.location.href;
	wlos = winlo.split('=').reverse();
	if(wlos[1].match(patt) == "start"){
		bo_page = true;
	}else{
		bo_page = false;
	}
	if(bo_page){
		if(n){
			wlos[0] = parseInt(wlos[0]) + 50;
			window.location = wlos.reverse().join('=');
		}else{
			wlos[0] = parseInt(wlos[0]) - 50;
			window.location = wlos.reverse().join('=');
		}
	}else{
		if(n){
			window.location = winlo + "&start=50";
		}
	}
}
//rarbg.to
function rarbg_to(n){
	if(n){
		window.location=document.querySelector('a[title="next page"]').href;
	}else{
		window.location=document.querySelector('a[title="previous page"]').href;
	}
}
//reddit.com
function reddit_com(n){
	if(n){
		window.location=document.querySelector('a[rel="nofollow next"]').href;
	}else{
		window.location=document.querySelector('a[rel="nofollow prev"]').href;
	}
}
//steamgifts.com
function steamgifts_com(n){
	if(n){
		window.location=document.querySelector('i[class="fa fa-angle-right"]').parentNode.href;
	}else{
		window.location=document.querySelector('i[class="fa fa-angle-left"]').parentNode.href;
	}
}