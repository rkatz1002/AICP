var listaMedicamentos = ["a", "b", "c", "d"];

var medicamentoRetirado = document.getElementsByClassName("medicamento-retirado");
var procurarMedicamento = document.getElementsByClassName("procurar-medicamento");

console.log(medicamentoRetirado.textContent);

procurarMedicamento[0].addEventListener('click', function(event){
    listaMedicamentos.forEach(function(medicamento){
        if(medicamentoRetirado[0].textContent == medicamento){
            
        }
        
    });
});

quantidade_id = document.getElementById("quantidade");
quantidade = quantidade.value;

submeter_id = document.getElementById("submeter");

submeter_id.addEventListener("click",function(event){
    
});

alert(quantidade.value)