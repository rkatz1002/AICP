var listaMedicamentos = ["a", "b", "c", "d"];

var medicamentoRetirado = document.getElementsByClassName("medicamento-retirado");
var procurarMedicamento = document.getElementsByClassName("procurar-medicamento");

console.log(medicamentoRetirado[0]);

procurarMedicamento[0].addEventListener('click', function(event){
    listaMedicamentos.forEach(function(medicamento){
        if(medicamentoRetirado[0].textContent == medicamento){
            
        }
        
    });

   
});