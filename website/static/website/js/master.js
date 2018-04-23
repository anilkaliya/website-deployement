var header=document.querySelectorAll("h1")
function changeheadercolor(){
  colorinput=getrandomcolor()
  header.style.color=colorinput;
}
setInterval("chnageheadercolor()",500);

function getrandomcolor(){
  var letters="0123456789ABCDEF";
  var color="#";
  for(var i=0;i<6;i++){
  color+=letters[Math.floor(Math.random()*16)]:
}
return color;
}
