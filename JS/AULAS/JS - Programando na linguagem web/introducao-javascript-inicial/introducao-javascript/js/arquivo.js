pacientes = document.querySelectorAll(".paciente");
titulo = document.querySelector(".titulo");
titulo.addEventListener("click", function(){console.log("HAHAHAH")})
for(var i = 0; i < pacientes.length; i++){

    var peso = pacientes[i].querySelector(".info-peso");
    var altura = pacientes[i].querySelector(".info-altura");
    var imc = pacientes[i].querySelector(".info-imc");

    console.log(imc.textContent)
    if(peso.textContent < 0 || peso.textContent > 500){
        imc.textContent = "Peso Inválido";
        pacientes[i].classList.add("paciente-invalido");
        continue;
    }
    else if (altura.textContent <= 0 || altura.textContent >= 3.00) {
        imc.textContent = "Altura Inválida";
        pacientes[i].classList.add("paciente-invalido");
        continue;
    }
    imc.textContent = (peso.textContent / (altura.textContent * altura.textContent)).toFixed(2);
}

