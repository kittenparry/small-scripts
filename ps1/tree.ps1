#Creates a tree for archive/downloads folders in each drive
$al =":\Archive\"
$dl =":\Downloads\"
$d = @('D', 'E', 'F', 'G', 'H', 'I', 'J')
FOR ($i=0;$i-lt$d.Length;$i++){
	$lo = ""
	$lo = $d[$i] + $al
	CD $lo
	powershell -command "tree /f > tree.txt"
	$lo = $d[$i] + $dl
	CD $lo
	powershell -command "tree /f > tree.txt"
}