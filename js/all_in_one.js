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
 * ...
 */
//vars
nhentai_net_n = document.querySelector('a[class="next"]').href;
nhentai_net_b = document.querySelector('a[class="previous"]').href;
pornbay_org_n = document.querySelector('a[class="pager pager_next"]').href;
pornbay_org_b = document.querySelector('a[class="pager pager_prev"]').href;
//pornolab_org_n
//pornolab_org_b
rarbg_to_n = document.querySelector('a[title="next page"]').href;
rarbg_to_b = document.querySelector('a[title="previous page"]').href;
reddit_com_n = document.querySelector('a[rel="nofollow next"]').href;
reddit_com_b = document.querySelector('a[rel="nofollow prev"]').href;
steamgifts_com_n = document.querySelector('i[class="fa fa-angle-right"]').parentNode.href;
steamgifts_com_b = document.querySelector('i[class="fa fa-angle-left"]').parentNode.href;
//true = n, false = b
//nhentai.net
function nhentai_net(n){
	if(n){
		if(nhentai_net_n)
			window.location = nhentai_net_n;
	}else{
		if(nhentai_net_b)
			window.location = nhentai_net_b;
	}
}
//pornobay.org
function pornbay_org(n){
	if(n){
		if(pornobay_org_n)
			window.location = pornbay_org_n;
	}else{
		if(pornobay_org_b)
			window.location = pornbay_org_b;
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
		if(rarbg_to_n)
			window.location = rarbg_to_n;
	}else{
		if(rarbg_to_b)
			window.location = rarbg_to_b;
	}
}
//reddit.com
function reddit_com(n){
	if(n){
		if(reddit_com_n)
			window.location = reddit_com_n;
	}else{
		if(reddit_com_b)
			window.location = reddit_com_b;
	}
}
//steamgifts.com
function steamgifts_com(n){
	if(n){
		if(steamgifts_com_n)
			window.location = steamgifts_com_n;
	}else{
		if(steamgifts_com_b)
			window.location = steamgifts_com_b;
	}
}