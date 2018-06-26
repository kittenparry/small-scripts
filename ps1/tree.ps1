#Creates a tree for archive/downloads folders in each drive
#then copies them to the dated Google Drive folder

#SET paths, drive letters array
$al =":\Archive\"
$dl =":\Downloads\"
$d = @('D', 'E', 'F', 'G', 'H', 'I', 'J')
#SET cmd, fnames
$cmd = "TREE /F > "
$fna = "Archive-"
$fnd = "Downloads-"
$fne = "-tree.txt"
#SET Google Drive path, date
$g = "F:\Google Drive\Other\Trees\"
$dt = Get-Date -UFormat "%Y.%m.%d"
$gdl = $g + $dt
#COPY to Google Driver function
FUNCTION ctd($p){
	IF(Test-Path -Path $gdl){}ELSE{
		New-Item -ItemType directory -Path $gdl
	}
	Copy-Item -Path $p -Destination $gdl
}
FOR ($i=0;$i-lt$d.Length;$i++){
	#SET fnames, commands
	$fna1 = $fna + $d[$i] + $fne
	$fnd1 = $fnd + $d[$i] + $fne
	$cmda = $cmd + $fna1
	$cmdd = $cmd + $fnd1
	#SET paths, CD, TREE, COPY to Google Drive
	$lo = $d[$i] + $al
	CD $lo
	powershell -command $cmda
	ctd($lo + $fna1)
	$lo = $d[$i] + $dl
	CD $lo
	powershell -command $cmdd
	ctd($lo + $fnd1)
}