window.addEventListener("keydown",checkKeyPressed,false);
function checkKeyPressed(e){
    type=e.target.getAttribute("type");
    if(type!='text'){
        switch(e.keyCode){
            case 66:
                check(false);
                break;
            case 78:
                check(true);
                break;
            default:
        }
    }
}
function check(op){ //op true = n, op false = b
	patt = /start/g;
	winlo = window.location.href;
	wlos = winlo.split('=').reverse();
	if(wlos[1].match(patt) == "start"){
		bo_page = true;
	}else{
		bo_page = false;
	}
	if(bo_page){
		if(op){
			wlos[0] = parseInt(wlos[0]) + 50;
			window.location = wlos.reverse().join('=');
		}else{
			wlos[0] = parseInt(wlos[0]) - 50;
			window.location = wlos.reverse().join('=');
		}
	}else{
		if(op){
			window.location = winlo + "&start=50";
		}
	}
}