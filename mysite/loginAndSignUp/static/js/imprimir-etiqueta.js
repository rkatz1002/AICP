prescricoes = [["a", 2],["b",3],["c",7]]

var code=0;

prescricoes.array.forEach(prescricao => {
    n = prescricao[1];
    for(i=0;i<n;i++){
        code+=1;
    }
});