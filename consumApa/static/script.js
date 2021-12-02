            
function myFunction(x){
    //alert("Row index is: " + x.rowIndex)
    //document.querySelector("#demo").innerHTML = "You selected: " + x.rowIndex;
    document.getElementById("indexBuc").value = x.cells[0].innerHTML;
    document.getElementById("indexBaie").value = x.cells[1].innerHTML;
    document.getElementById("indexWC").value = x.cells[2].innerHTML;
}
    
var tb = document.querySelector('#table'),rIndex;

for(var i = 1; i < tb.rows.lenght; i++)
{
    tb.rows[i].onclick = function() {       
        rIndex=this.rowIndex; 
        console.log(rIndex);
        document.querySelector("#demo").innerHTML = "You selected: " + this.rowIndex;
        document.getElementById("indexBuc").value = this.cells[0].innerHTML;
        document.getElementById("indexBaie").value = this.cells[1].innerHTML;
        document.getElementById("indexWC").value = this.cells[2].innerHTML;
    }
}