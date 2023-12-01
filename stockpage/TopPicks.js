document.addEventListener('DOMContentLoaded', function() {
    const nameList = document.getElementById('stockList');
    const fr = new FileReader();

    fr.onload=function(){ 
        alert("here");
        document.getElementById('output').textContent=fr.result; 
    } 
})
  